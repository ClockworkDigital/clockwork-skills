"""Read-only loopback dashboard. Never serves repository/Git directories."""
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import subprocess
from urllib.parse import parse_qs, urlsplit

LIMIT = 2 * 1024 * 1024


def projects(registry):
    result = {}
    for name in json.loads(registry.read_text()) if registry.exists() else []:
        path = Path(name).resolve()
        key = hashlib.sha256(str(path).encode()).hexdigest()[:16]
        result[key] = path
    return result


def jobs_path(root):
    common = subprocess.check_output(['git', '-C', str(root), 'rev-parse', '--git-common-dir'], text=True, stderr=subprocess.DEVNULL, timeout=5).strip()
    return (root / common).resolve() / 'factory-state/jobs'


def read_text(path):
    if path.stat().st_size > LIMIT:
        raise ValueError('Artifact exceeds 2 MiB; inspect it locally')
    return path.read_text(errors='replace')


def snapshot(registry):
    repos, jobs, warnings = [], [], []
    for key, root in projects(registry).items():
        repos.append(dict(id=key, name=root.name, path=str(root)))
        try:
            folder = jobs_path(root)
            for file in sorted(folder.glob('*/job.json')):
                try:
                    if file.is_symlink() or file.parent.is_symlink():
                        raise ValueError('Symlinked job excluded')
                    data = json.loads(read_text(file))
                    if not isinstance(data, dict) or data.get('id') != file.parent.name:
                        raise ValueError('Invalid job identity')
                    # Avoid returning config/environment/request contents on the board.
                    visible = {k: data.get(k) for k in ('id','title','stage','round','issue','branch','pr','updated_at','error','intake','reviews','attempts')}
                    visible['gate'] = {k: (data.get('gate') or {}).get(k) for k in ('passed','commit')}
                    visible['repo'] = key
                    visible['files'] = [p.name for p in sorted(file.parent.iterdir())
                                        if p.is_file() and not p.is_symlink() and p.suffix in {'.json','.jsonl','.log','.md','.txt'}]
                    jobs.append(visible)
                except (OSError, ValueError, TypeError) as error:
                    warnings.append(root.name + '/' + file.parent.name + ': ' + str(error))
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            warnings.append(root.name + ': ' + str(error))
    return dict(projects=repos, jobs=jobs, warnings=warnings)


def artifact(registry, repo, job, name):
    roots = projects(registry)
    if repo not in roots or not job or not name or any(x in {'.','..'} or '/' in x or '\\' in x for x in (job,name)):
        raise ValueError('Invalid artifact path')
    folder = jobs_path(roots[repo])
    path = folder / job / name
    if path.is_symlink() or path.parent.is_symlink() or not path.resolve().is_relative_to(folder.resolve()):
        raise ValueError('Artifact must remain inside its job directory')
    if path.suffix not in {'.json','.jsonl','.log','.md','.txt'}:
        raise ValueError('Unsupported artifact')
    return read_text(path)


def handler(registry, html, token):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass  # Never log the URL token or private artifact text.

        def reply(self, code, body, content_type):
            data = body.encode()
            self.send_response(code)
            self.send_header('Content-Type', content_type + '; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            url = urlsplit(self.path)
            query = parse_qs(url.query)
            host = self.headers.get('Host', '')
            if host not in {'127.0.0.1:' + str(self.server.server_port), 'localhost:' + str(self.server.server_port)}:
                return self.reply(403, 'Invalid host', 'text/plain')
            supplied = self.headers.get('X-Factory-Token') or query.get('token', [''])[0]
            if not secrets.compare_digest(supplied, token):
                return self.reply(403, 'Open the dashboard URL printed by the launcher.', 'text/plain')
            try:
                if url.path in {'/', '/dashboard.html'}:
                    return self.reply(200, html.read_text(), 'text/html')
                if url.path == '/api/jobs':
                    return self.reply(200, json.dumps(snapshot(registry)), 'application/json')
                if url.path == '/api/artifact':
                    values = [query.get(k, [''])[0] for k in ('repo','job','name')]
                    return self.reply(200, artifact(registry, *values), 'text/plain')
                return self.reply(404, 'Not found', 'text/plain')
            except (OSError, ValueError, subprocess.SubprocessError) as error:
                return self.reply(400, str(error), 'text/plain')
    return Handler


def serve(registry, html, port):
    token = secrets.token_urlsafe(32)
    server = ThreadingHTTPServer(('127.0.0.1', port), handler(registry, html, token))
    print('Factory dashboard: http://127.0.0.1:' + str(server.server_port) + '/?token=' + token, flush=True)
    print('Read-only saved state; Ctrl-C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
