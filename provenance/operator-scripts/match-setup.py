#!/usr/bin/env python3
"""Freeze completed learner material and make real provider-native branches.

Never reads reasoning contents. Native history is copied only by provider fork APIs.
This prepares new sessions; it never starts or resumes the original players.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import os
import selectors
import shutil
import sqlite3
import subprocess
import tarfile
import time
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parent.parent
MATCH = ROOT / 'Matches' / 'Astra vs Opus - 30 games'
SETUP = MATCH / '.operator' / 'setup.json'
DB = Path('/home/peter/.t3/userdata/state.sqlite')
CODEX = '/home/peter/.local/opt/codex-t3-0.153.4/node_modules/.bin/codex'
NODE = '/home/peter/.local/opt/node-v24.19.0-linux-x64/bin/node'
CLAUDE_HISTORY = '/home/peter/.local/opt/t3-0.0.44-shadow-local/dist/claude-history-worker.mjs'
SOURCES = {
    'astra': {'folder': 'Chess - GPT-6-Astra', 'threadId': '965e6927-c288-4324-b3bb-a1b8b4a16495',
              'nativeId': '01a0ef25-69a0-7b31-b0f2-b8042b854a79',
              'nativePath': '/home/peter/.codex-t3/accounts/pro-vt/sessions/2026/09/29/rollout-2026-09-29T21-50-01-01a0ef25-69a0-7b31-b0f2-b8042b854a79.jsonl'},
    'opus': {'folder': 'Chess - Opus-5.5', 'threadId': 'bf1715ee-c265-45bb-9bcf-4b7b6beec6b7',
             'nativeId': '02b17840-e0cf-436c-a088-3a7d29464975',
             'nativePath': '/home/peter/.claude/projects/-home-peter-Chess-Learning-Chess---Opus-5-5/02b17840-e0cf-436c-a088-3a7d29464975.jsonl'},
}

def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def sha(path):
    with path.open('rb') as f: return hashlib.file_digest(f, 'sha256').hexdigest()
def save(value):
    SETUP.parent.mkdir(parents=True, exist_ok=True)
    tmp = SETUP.with_suffix('.tmp'); tmp.write_text(json.dumps(value, indent=2) + '\n'); tmp.replace(SETUP)
def api(path, value=None):
    token = json.loads((ROOT / '.operator/t3-session.json').read_text())['token']
    req = urllib.request.Request('http://127.0.0.1:3773' + path,
        data=json.dumps(value).encode() if value else None,
        headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)

class Rpc:
    def __init__(self):
        env = dict(os.environ, CODEX_HOME='/home/peter/.codex-t3/accounts/pro-vt')
        self.proc = subprocess.Popen([CODEX, 'app-server', '--stdio'], env=env,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, bufsize=1)
        self.seq = 0
        self.call('initialize', {'clientInfo': {'name': 'chess-match-operator', 'version': '1.0'},
            'capabilities': {'experimentalApi': True}})
        self.proc.stdin.write(json.dumps({'method': 'initialized'}) + '\n'); self.proc.stdin.flush()
    def call(self, method, params):
        self.seq += 1
        self.proc.stdin.write(json.dumps({'id': self.seq, 'method': method, 'params': params}) + '\n')
        self.proc.stdin.flush()
        deadline = time.monotonic() + 100
        with selectors.DefaultSelector() as poll:
            poll.register(self.proc.stdout, selectors.EVENT_READ)
            while time.monotonic() < deadline:
                if not poll.select(1): continue
                line = self.proc.stdout.readline()
                if not line: raise RuntimeError('Native app-server closed')
                value = json.loads(line)
                # Notifications and historical items are intentionally not inspected or logged.
                if value.get('id') != self.seq: continue
                if 'error' in value: raise RuntimeError('Native RPC failed: ' + method + ': ' + str(value['error'].get('message')))
                return value['result']
        raise TimeoutError(method)
    def close(self):
        self.proc.terminate()
        try: self.proc.wait(timeout=10)
        except subprocess.TimeoutExpired: self.proc.kill(); self.proc.wait()

def main():
    state = json.loads(SETUP.read_text()) if SETUP.exists() else {'createdAt': now(), 'players': {}, 'games': 30}
    for player, source in SOURCES.items():
        if player in state['players']: continue
        original = ROOT / source['folder']
        thread = api('/api/orchestration/threads/' + source['threadId'] + '?turnLimit=1')['thread']
        assert thread['latestTurn']['state'] == 'completed'
        assert thread['session']['status'] not in ('running', 'starting')
        results = [json.loads(l) for l in (original / 'data/ledger.jsonl').read_text().splitlines()
                   if json.loads(l).get('kind') == 'result' and json.loads(l).get('score') is not None]
        assert len(results) == 200, (player, len(results))
        folder = MATCH / ('GPT-6 Astra' if player == 'astra' else 'Claude Opus 5.5')
        folder.mkdir(parents=True, exist_ok=True)
        shutil.copytree(original / 'workspace', folder / 'workspace', dirs_exist_ok=False)
        manifest = {str(p.relative_to(original)): sha(p) for p in sorted((original / 'workspace').rglob('*')) if p.is_file()}
        archive = MATCH / '.operator' / 'checkpoints' / (player + '-after-200.tar.gz')
        archive.parent.mkdir(parents=True, exist_ok=True)
        with tarfile.open(archive, 'w:gz') as tar:
            for name in ['workspace', 'AGENTS.md', 'GOAL.md', 'data/ledger.jsonl']:
                tar.add(original / name, arcname=name)
        entry = {**source, 'originalFolder': str(original), 'folder': str(folder),
                 'threadId': str(uuid.uuid4()), 'sourceThreadId': source['threadId'],
                 'projectId': thread['projectId'], 'modelSelection': thread['modelSelection'],
                 'sourceNativeSha256': sha(Path(source['nativePath'])),
                 'sourceLedgerSha256': sha(original / 'data/ledger.jsonl'),
                 'sourceWorkspace': manifest, 'checkpointArchiveSha256': sha(archive),
                 'originalCompletedTurnId': thread['latestTurn']['turnId'], 'preparedAt': now()}
        # Save before forking so a subsequent stage can recover safely.
        state['players'][player] = entry; save(state)

    for player, entry in state['players'].items():
        if entry.get('forkNativeId'): continue
        if player == 'astra':
            rpc = Rpc()
            try:
                result = rpc.call('thread/fork', {'threadId': entry['nativeId'], 'model': 'gpt-6-astra',
                    'cwd': entry['folder'], 'sandbox': 'danger-full-access', 'approvalPolicy': 'never',
                    'excludeTurns': True, 'deferGoalContinuation': True,
                    'config': {'model_reasoning_effort': 'max'}})
                branch = result['thread']
                entry['forkNativeId'] = branch['id']; entry['forkNativePath'] = branch.get('path')
                entry['forkedFromId'] = branch.get('forkedFromId')
                assert branch['id'] != entry['nativeId']
                assert entry['forkedFromId'] == entry['nativeId'], entry['forkedFromId']
            finally: rpc.close()
        else:
            # SDK forkSession copies the native conversation without invoking the model.
            result = subprocess.run([NODE, CLAUDE_HISTORY, 'forkSession', entry['nativeId'],
                json.dumps({'dir': entry['originalFolder']})], check=True, capture_output=True, text=True, timeout=90)
            native = json.loads(result.stdout)['sessionId']
            assert native != entry['nativeId']
            source_path = Path(entry['nativePath']).with_name(native + '.jsonl')
            assert source_path.is_file()
            # Make the SDK-created branch discoverable at its new workspace. Opaque copy;
            # the original native file and all reasoning records remain unexamined.
            project_key = ''.join(c if c.isalnum() else '-' for c in entry['folder'])
            dest = Path('/home/peter/.claude/projects') / project_key / (native + '.jsonl')
            dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(source_path, dest)
            entry.update(forkNativeId=native, forkNativePath=str(dest), forkedFromId=entry['nativeId'],
                         sdkForkPath=str(source_path), forkOpaqueCopySha256=sha(dest))
        assert sha(Path(entry['nativePath'])) == entry['sourceNativeSha256'], 'Original native history changed'
        entry['forkedAt'] = now(); save(state)
        print(player, 'native branch created', entry['forkNativeId'])

    for player, entry in state['players'].items():
        if entry.get('threadCreated'): continue
        api('/api/orchestration/dispatch', {'type': 'thread.create', 'commandId': str(uuid.uuid4()),
            'threadId': entry['threadId'], 'projectId': entry['projectId'],
            'title': ('GPT-6 Astra' if player == 'astra' else 'Claude Opus 5.5') + ' — 30-game match',
            'modelSelection': entry['modelSelection'], 'runtimeMode': 'full-access', 'interactionMode': 'default',
            'branch': None, 'worktreePath': entry['folder'], 'createdAt': now()})
        entry['threadCreated'] = True; save(state)

    # T3 has no public native-fork adoption command. Seed only these never-started
    # threads with the exact stopped-binding shape used by its own history importer.
    # SQLite transactions leave every existing thread/provider binding untouched.
    with sqlite3.connect(DB, timeout=30) as conn:
        for player, entry in state['players'].items():
            existing = conn.execute('SELECT resume_cursor_json FROM provider_session_runtime WHERE thread_id=?', (entry['threadId'],)).fetchone()
            cursor = {'threadId': entry['forkNativeId']} if player == 'astra' else {'threadId': entry['threadId'], 'resume': entry['forkNativeId']}
            if existing:
                assert json.loads(existing[0]) == cursor, 'Unexpected existing match binding'
                continue
            provider = 'codex' if player == 'astra' else 'claudeAgent'
            conn.execute('INSERT INTO provider_session_runtime(thread_id,provider_name,provider_instance_id,adapter_key,runtime_mode,status,last_seen_at,resume_cursor_json,runtime_payload_json) VALUES(?,?,?,?,?,?,?,?,?)',
                (entry['threadId'], provider, entry['modelSelection']['instanceId'], provider,
                 'full-access', 'stopped', now(), json.dumps(cursor),
                 json.dumps({'cwd': entry['folder'], 'model': entry['modelSelection']['model'],
                             'modelSelection': entry['modelSelection']})))
    state['status'] = 'branched'; save(state)
    print('Both native branches bound to new T3 threads; originals unchanged.')

if __name__ == '__main__': main()
