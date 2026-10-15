#!/usr/bin/env python3
"""Audit source preservation and native match settings, never reasoning contents."""
from pathlib import Path
import datetime as dt
import hashlib
import importlib.util
import json
import sqlite3
import subprocess
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
MATCH = ROOT / 'Matches/Astra vs Opus - 30 games'
SETUP = json.loads((MATCH / '.operator/setup.json').read_text())

def sha(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

def api(path):
    token = json.loads((ROOT / '.operator/t3-session.json').read_text())['token']
    req = urllib.request.Request('http://127.0.0.1:3773' + path,
                                 headers={'Authorization': 'Bearer ' + token})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)

def stamp(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))

report = {'checkedAt': dt.datetime.now(dt.timezone.utc).isoformat(), 'players': {}}
with sqlite3.connect('file:/home/peter/.t3/userdata/state.sqlite?mode=ro', uri=True) as db:
    for player, p in SETUP['players'].items():
        original = Path(p['originalFolder'])
        assert sha(Path(p['nativePath'])) == p['sourceNativeSha256'], player
        assert sha(original / 'data/ledger.jsonl') == p['sourceLedgerSha256'], player
        manifest = {str(f.relative_to(original)): sha(f) for f in sorted((original / 'workspace').rglob('*')) if f.is_file()}
        assert manifest == p['sourceWorkspace'], player
        archive = MATCH / '.operator/checkpoints' / (player + '-after-200.tar.gz')
        assert sha(archive) == p['checkpointArchiveSha256'], player
        with tarfile.open(archive) as tar:
            for name in ['AGENTS.md', 'GOAL.md']:
                assert hashlib.sha256(tar.extractfile(name).read()).hexdigest() == sha(original / name), (player, name)
        results = [json.loads(line) for line in (original / 'data/ledger.jsonl').read_text().splitlines()]
        assert sum(r.get('kind') == 'result' and r.get('score') is not None for r in results) == 200
        thread = api('/api/orchestration/threads/' + p['threadId'] + '?turnLimit=1')['thread']
        assert thread['modelSelection'] == p['modelSelection'], player
        native_metadata = []
        # Only inspect session/turn metadata. Do not access thinking, reasoning,
        # summaries, message content, tool outputs or encrypted reasoning fields.
        with Path(p['forkNativePath']).open() as history:
            for line in history:
                entry = json.loads(line)
                if player == 'astra' and entry.get('type') == 'turn_context':
                    payload = entry['payload']
                    if payload.get('cwd') == p['folder']:
                        native_metadata.append({k: payload.get(k) for k in ['model','effort','cwd','turn_id']})
                elif player == 'opus' and entry.get('type') == 'assistant':
                    if stamp(entry['timestamp']) < stamp(p['forkedAt']):
                        continue
                    native_metadata.append({
                        'model': (entry.get('message') or {}).get('model'),
                        **{k: entry.get(k) for k in ['effort','perTurnEffort','cwd','sessionId']}})
        assert native_metadata, player
        for meta in native_metadata:
            assert meta['model'] == p['modelSelection']['model'], (player, 'model')
            assert meta['effort'] == 'max', (player, 'effort')
            assert Path(meta['cwd']).is_relative_to(Path(p['folder'])), (player, 'folder')
            if player == 'opus':
                assert meta['perTurnEffort'] == 'max' and meta['sessionId'] == p['forkNativeId']
        runtime = db.execute('SELECT resume_cursor_json FROM provider_session_runtime WHERE thread_id=?', (p['threadId'],)).fetchone()
        assert runtime and p['forkNativeId'] in runtime[0], player
        report['players'][player] = {
            'originalNativeUnchanged': True, 'originalLedgerUnchanged': True,
            'originalWorkspaceUnchanged': True, 'originalInstructionsAndGoalUnchanged': True,
            'sourceGames': 200, 'workspaceFiles': len(manifest),
            'checkpointVerified': True, 'nativeForkBindingVerified': True,
            'verifiedNativeMetadataEntries': len(native_metadata), 'allNativeEffort': 'max',
            'model': p['modelSelection']['model'], 'latestTurnState': thread['latestTurn']['state']}

assert sha(MATCH / 'protocol.json') == SETUP['protocolSha256']
for relative, expected in SETUP.get('integrityFiles', {}).items():
    assert sha(ROOT / relative) == expected, relative
spec = importlib.util.spec_from_file_location('match_referee', ROOT / '.operator/match-referee.py')
referee = importlib.util.module_from_spec(spec)
spec.loader.exec_module(referee)
ref = referee.Referee()
report['referee'] = ref.verify()
public = ref.public()
report['match'] = {k: public.get(k) for k in ['status','score','currentGame','turn','eventSequence','ledgerHead','startedAt']}
report['match']['currentPly'] = public['games'][-1]['ply'] if public['games'] else None
controller = json.loads((MATCH / '.operator/controller.json').read_text())
report['controller'] = {k: controller.get(k) for k in ['status','game','dispatches','reason','lastInfrastructureError','updatedAt']}
assert controller['status'] in ('active','waiting','complete')
report['services'] = {}
for name in ['chess-match-referee.service','chess-match-controller.service','chess-live-dashboard.service','chess-cloudflare-feed.service']:
    active = subprocess.run(['systemctl','--user','is-active',name], capture_output=True, text=True).stdout.strip()
    report['services'][name] = active
    assert active == 'active', (name, active)
report['protocolVerified'] = True
report['integrityFilesVerified'] = len(SETUP.get('integrityFiles', {}))
output = MATCH / '.operator/launch-verification.json'
output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
