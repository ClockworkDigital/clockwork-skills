#!/usr/bin/env python3
"""Global launcher: preserve project runners and route from an explicit repository."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

HOME = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'factory'
ASSETS = Path(__file__).resolve().parents[1] / 'assets'


def repository(path):
    root = subprocess.check_output(['git', '-C', str(path), 'rev-parse', '--show-toplevel'], text=True).strip()
    rows = subprocess.check_output(['git', '-C', root, 'worktree', 'list', '--porcelain'], text=True).splitlines()
    return Path(next(row[9:] for row in rows if row.startswith('worktree '))).resolve()


def register(root):
    HOME.mkdir(parents=True, exist_ok=True)
    with (HOME / 'registry.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        path = HOME / 'projects.json'
        projects = json.loads(path.read_text()) if path.exists() else []
        if str(root) not in projects:
            projects.append(str(root))
            tmp = path.with_suffix('.tmp')
            tmp.write_text(json.dumps(projects, indent=2) + '\n')
            tmp.replace(path)


def initialize(root, config_path):
    if (root / 'factory').exists() or (root / '.agents/skills/factory').exists():
        raise ValueError('Factory already installed; existing files will not be replaced')
    defaults = json.loads((ASSETS / 'template/config.json').read_text())
    defaults.update(json.loads(Path(config_path).read_text()))
    if not defaults.get('checks'):
        raise ValueError('Configure real project checks before installation')
    for command in defaults.get('setup', []) + defaults['checks']:
        if not isinstance(command, list) or not command or not all(isinstance(s, str) and s for s in command):
            raise ValueError('Commands must be nonempty arrays of strings')
    shutil.copytree(ASSETS / 'template', root / 'factory', ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    (root / 'factory/config.json').write_text(json.dumps(defaults, indent=2) + '\n')
    (root / 'factory/README.md').write_text(
        '# Codex factory\n\nUse the global `$factory` skill or `python3 factory/runner.py --help`.\n'
        'Review config.json, commit and merge setup to the remote base before starting a job.\n'
        'One job per repository; three build rounds; human merging; no deployment.\n'
        'Run `python3 -m unittest discover -s factory/tests -v` to verify the runner.\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default='.')
    parser.add_argument('command', choices=['init', 'register', 'dashboard', 'status', 'issue', 'run', 'start', 'resume', 'rework', 'publish'])
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    root = repository(args.repo)
    if args.command == 'init':
        init = argparse.ArgumentParser()
        init.add_argument('--config', required=True)
        options = init.parse_args(args.args)
        initialize(root, options.config)
    elif not (root / 'factory/config.json').is_file():
        raise ValueError('No factory/config.json in ' + str(root) + '; install with init --config PATH first')
    register(root)
    if args.command == 'dashboard':
        from dashboard import serve
        p = argparse.ArgumentParser()
        p.add_argument('--port', type=int, default=8787)
        options = p.parse_args(args.args)
        serve(HOME / 'projects.json', ASSETS / 'dashboard.html', options.port)
    elif args.command in ('init', 'register'):
        print('Registered ' + str(root))
    else:
        runner = root / 'factory/runner.py'
        if not runner.is_file():
            raise ValueError('Repository runner missing: ' + str(runner))
        os.chdir(root)
        os.execv(sys.executable, [sys.executable, str(runner), args.command, *args.args])


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print('factory: ' + str(error), file=sys.stderr)
        sys.exit(1)
