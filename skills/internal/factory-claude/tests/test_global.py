import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import factory
import dashboard


class GlobalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        self.root.mkdir()
        subprocess.run(['git','init',str(self.root)],capture_output=True,check=True)
        self.registry = Path(self.tmp.name) / 'projects.json'
        self.registry.write_text(json.dumps([str(self.root)]))
        self.jobs = self.root / '.git/factory-state/jobs'
        (self.jobs / 'job-1').mkdir(parents=True)
        self.job = dict(id='job-1',title='<script>unsafe</script>',stage='needs-human',round=1,
                        gate=None,attempts=[], reviews={})
        (self.jobs / 'job-1/job.json').write_text(json.dumps(self.job))
        self.key = next(iter(dashboard.projects(self.registry)))

    def test_snapshot_null_gate_and_malformed_other_job(self):
        (self.jobs / 'bad').mkdir()
        (self.jobs / 'bad/job.json').write_text('{')
        result = dashboard.snapshot(self.registry)
        self.assertEqual(len(result['jobs']),1)
        self.assertEqual(len(result['warnings']),1)
        self.assertIsNone(result['jobs'][0]['gate']['passed'])

    def test_artifact_traversal_and_symlink_refused(self):
        with self.assertRaises(ValueError):
            dashboard.artifact(self.registry,self.key,'..','config')
        (self.jobs / 'job-1/private.json').symlink_to(self.registry)
        with self.assertRaises(ValueError):
            dashboard.artifact(self.registry,self.key,'job-1','private.json')
        self.assertEqual(json.loads(dashboard.artifact(self.registry,self.key,'job-1','job.json')),self.job)

    def test_install_requires_checks_and_preserves_existing(self):
        config=Path(self.tmp.name)/'config.json';config.write_text('{}')
        with self.assertRaises(ValueError):factory.initialize(self.root,config)
        self.assertFalse((self.root/'factory').exists())
        config.write_text(json.dumps({'checks':[['python3','--version']]}))
        factory.initialize(self.root,config)
        self.assertTrue((self.root/'factory/runner.py').exists())
        with self.assertRaises(ValueError):factory.initialize(self.root,config)
        cfg=json.loads((self.root/'factory/config.json').read_text())
        self.assertEqual(cfg['roles']['security']['model'],'opus')

    def test_http_auth_and_no_git_serving(self):
        html=Path(self.tmp.name)/'dashboard.html';html.write_text('<h1>Factory</h1>')
        server=ThreadingHTTPServer(('127.0.0.1',0),dashboard.handler(self.registry,html,'test-token'))
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        self.addCleanup(server.server_close);self.addCleanup(server.shutdown)
        base='http://127.0.0.1:'+str(server.server_port)
        with self.assertRaises(HTTPError) as error:urlopen(base+'/api/jobs')
        self.assertEqual(error.exception.code,403)
        request=Request(base+'/api/jobs',headers={'X-Factory-Token':'test-token'})
        with urlopen(request) as response:self.assertEqual(len(json.load(response)['jobs']),1)
        with self.assertRaises(HTTPError) as error:urlopen(base+'/.git/config?token=test-token')
        self.assertEqual(error.exception.code,404)
        request=Request(base+'/api/jobs',headers={'X-Factory-Token':'test-token','Host':'evil.example'})
        with self.assertRaises(HTTPError) as error:urlopen(request)
        self.assertEqual(error.exception.code,403)


if __name__=='__main__':unittest.main()
