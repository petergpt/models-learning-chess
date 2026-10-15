"""Check release boundaries with synthetic fixtures, without real experiment data."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('release_export', ROOT / 'tools/export_release.py')
export = importlib.util.module_from_spec(spec)
spec.loader.exec_module(export)


class ReleaseTests(unittest.TestCase):
    def test_credentials_are_removed_from_nested_tool_output_but_chess_tokens_survive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.operator').mkdir()
            secret = 'sk-' + 'Ab9x' * 12
            (root / '.operator/t3-session.json').write_text(json.dumps({'token': secret}))
            cleaner = export.Cleaner(root)
            cleaner.current = 'synthetic-tool-output'
            position = '30:102:abcdef0123456789abcdef01'
            payload = {'output': json.dumps({'positionToken': position, 'authorization': 'Bearer ' + secret}),
                       'note': 'Use basic board-reconstruction and literal recapture checks.'}
            result = cleaner.obj(payload, traces=True)
            nested = json.loads(result['output'])
            self.assertEqual(nested['positionToken'], position)
            self.assertEqual(result['note'], payload['note'])
            self.assertNotIn(secret, json.dumps(result))
            self.assertIn('[REDACTED:', nested['authorization'])
            parser_source = 'token_error(S.token, "Unexpected token: " + token_to_string(type, val) + ", expected: " + token_to_string(type, val));'
            self.assertEqual(cleaner.text(parser_source), parser_source)

    def test_exported_thinking_text_is_preserved_while_opaque_state_is_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            cleaner = export.Cleaner(Path(directory))
            value = {'type': 'thinking', 'thinking': 'Synthetic visible research text.',
                     'signature': 'opaque-signature', 'encrypted_content': 'opaque-content'}
            result = cleaner.obj(value, traces=True)
            self.assertEqual(result['thinking'], value['thinking'])
            self.assertIsNone(result['signature'])
            self.assertIsNone(result['encrypted_content'])

    def test_package_keeps_dataset_runs_and_excludes_new_local_runs_and_accounts(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / 'release'
            for name, content in [('README.md', 'Synthetic fixture'),
                                  ('data/runs/astra/ledger.jsonl', '{}\n'),
                                  ('provenance/runs/astra/arena/manifest.json', '{}\n'),
                                  ('runs/local/private.txt', 'local-only fixture'),
                                  ('.cache/download.txt', 'cache-only fixture'),
                                  ('.git/config', 'git-only fixture')]:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
            archive = base / 'fixture.zip'
            subprocess.run([sys.executable, '-I', str(ROOT / 'tools/package_release.py'),
                            '--root', str(root), '--output', str(archive)],
                           check=True, capture_output=True, text=True)
            with zipfile.ZipFile(archive) as package:
                names = set(package.namelist())
                self.assertIn('chess-learning/data/runs/astra/ledger.jsonl', names)
                self.assertIn('chess-learning/manifest.json', names)
                self.assertIn('chess-learning/provenance/runs/astra/arena/manifest.json', names)
                self.assertFalse(any('/runs/local/' in name or '/.cache/' in name or '/.git/' in name for name in names))


if __name__ == '__main__':
    unittest.main(verbosity=2)
