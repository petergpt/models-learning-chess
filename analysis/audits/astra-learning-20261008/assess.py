#!/usr/bin/env python3
"""Read-only analysis of Astra's original run; no engine or private reasoning."""
from __future__ import annotations
import collections
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import random
import re
import statistics
import sys
import tarfile
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/home/peter/Chess Learning')
FOLDER = ROOT / 'Chess - GPT-6-Astra'
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(FOLDER / '.arena/vendor/chess-1.11.2'))
import chess
import chess.pgn

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value

a = module('learning_assessment', ROOT / '.operator/learning-assessment/assess.py')
rating = module('astra_rating', FOLDER / '.arena/rating.py')
def digest(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()

events, chain = a.read_ledger(FOLDER / 'data/ledger.jsonl')
games = a.group_games(events)
assert [g['start']['game'] for g in games] == list(range(1,201))
assert all(g['end'] and g['end']['score'] is not None for g in games)
config = json.loads((FOLDER / '.arena/config.json').read_text())
manifest = json.loads((FOLDER / '.arena/manifest.json').read_text())
assert not [k for k,v in manifest.items() if digest(FOLDER / k) != v]
expected_manifest = games[0]['start']['manifest_sha256']
updates = []
for event in events:
    if event['kind'].endswith('update'):
        old = event.get('previous_manifest_sha256', event.get('previous_manifest'))
        if old:
            assert old == expected_manifest
        expected_manifest = event.get('new_manifest_sha256', event.get('manifest_sha256'))
        assert expected_manifest
        updates.append({k:v for k,v in event.items() if k not in ['sha256','previous']})
    if event['kind'] == 'start':
        assert event['manifest_sha256'] == expected_manifest
assert expected_manifest == digest(FOLDER / '.arena/manifest.json')

for game in games:
    start, end = game['start'], game['end']
    n = start['game']
    assert start['nodes_per_move'] == 1000000 == config['nodes_per_move']
    assert start['opponent'] == config['opponents'][((n-1)%6)//2]
    assert start['color'] == ('white' if n%2 else 'black')
    assert start['model'] == config['model'] == 'gpt-6-astra'
    game['features'] = a.replay(game)
    if end['reason'] == 'resignation':
        assert end['score'] == 0
    with gzip.open(FOLDER / f'data/games/{n:06d}.pgn.gz','rt') as handle:
        pgn = chess.pgn.read_game(handle)
    assert not pgn.errors and pgn.headers['Result'] == end['result']
    assert [m.uci() for m in pgn.mainline_moves()] == [m['uci'] for m in game['moves']]

practice_events, practice_chain = a.read_ledger(FOLDER / 'data/practice/ledger.jsonl')
practice = a.group_games(practice_events)
for game in practice:
    assert game['end']
    game['features'] = a.replay(game)

trends = a.trends(games)
blocks = a.complete_rotations(games)
early, late = blocks[:16], blocks[-16:]
rng = random.Random(20261008)
opponent_bootstrap = {}
for op in a.OPPONENTS:
    before = [a.tally([g for g in b if g['start']['opponent']['id']==op])['score'] for b in early]
    after = [a.tally([g for g in b if g['start']['opponent']['id']==op])['score'] for b in late]
    values = sorted(statistics.mean(rng.choices(after,k=16)) - statistics.mean(rng.choices(before,k=16)) for _ in range(10000))
    opponent_bootstrap[op] = {'delta': statistics.mean(after)-statistics.mean(before),
                              'bootstrap95': [a.quantile(values,.025),a.quantile(values,.975)]}
def by_op_behavior(selected):
    return {op:a.behavior([g for g in selected if g['start']['opponent']['id']==op]) for op in a.OPPONENTS}

quarters=[]
for lo in (1,51,101,151):
    selected=[g for g in games if lo<=g['start']['game']<lo+50]
    quarters.append({'games':[lo,lo+49], 'rated':a.tally([g for g in selected if g['start']['opponent']['id'] in a.RATED]),
                     'byOpponent':{op:a.tally([g for g in selected if g['start']['opponent']['id']==op]) for op in a.OPPONENTS},
                     'behavior':a.behavior(selected)})
obs=[{'game':g['start']['game'],'timestamp':g['end']['timestamp'],'anchor':rating.ANCHORS[g['start']['opponent']['id']], 'score':g['end']['score']}
     for g in games if g['start']['opponent']['id'] in rating.ANCHORS]
ratings = {'first3Rated':rating.posterior(obs[:3]), 'first50Rated':rating.posterior(obs[:50]),'last50Rated':rating.posterior(obs[-50:])}

# Read original native session only for settings and event timestamps.
# Never extract or analyse reasoning text or compaction summaries.
source = json.loads((ROOT/'Matches/Astra vs Opus - 30 games/.operator/setup.json').read_text())['players']['astra']
native = Path(source['nativePath'])
contexts, compactions=[],[]
event_types=collections.Counter()
for line in native.open():
    e=json.loads(line);event_types[e['type']]+=1
    p=e.get('payload',{})
    if e['type']=='turn_context':
        contexts.append({'timestamp':e['timestamp'],'model':p.get('model'),'effort':p.get('effort',p.get('reasoning_effort'))})
    elif e['type']=='compacted':compactions.append(e['timestamp'])
def when(value):
    return dt.datetime.fromisoformat(value.replace('Z','+00:00'))
medium_moves=[]
for game in games:
    for move in game['moves']:
        if move['actor']!='model':continue
        ctx=next((c for c in reversed(contexts) if when(c['timestamp'])<=when(move['timestamp'])),None)
        if ctx and ctx['effort']!='max':medium_moves.append({'game':game['start']['game'],'ply':move['ply'],'effort':ctx['effort']})

# Verify every retained workspace archive; retain note statistics and trial chronology only.
archives={}; note_names=['learning-journal.md','geometry-cards.md','move-check.md']
trial_paths=[str(Path(t['file']).relative_to('workspace')) for t in json.loads((FOLDER/'workspace/final-summary-200.json').read_text())['trials']]
snap_events=[e for e in events+practice_events if e.get('snapshot')]
for event in snap_events:
    key=event['snapshot']
    if key in archives:continue
    listing={};notes={};sizes={};trials_present=[]
    with tarfile.open(FOLDER/f'data/snapshots/{key}.tar.gz','r:gz') as archive:
        for entry in archive:
            assert entry.isfile() and not entry.issym() and entry.size<=32*1024**2
            value=archive.extractfile(entry).read();listing[entry.name]=hashlib.sha256(value).hexdigest()
            if entry.name in note_names:
                sizes[entry.name]={'bytes':len(value),'words':len(value.decode().split())}
            if entry.name in trial_paths:trials_present.append(entry.name)
    assert hashlib.sha256(a.canonical(listing).encode()).hexdigest()==key
    archives[key]={'noteSizes':sizes,'trialsPresent':trials_present}
trial_history=[]
for path in trial_paths:
    first=next((g['start']['game'] for g in games if path in archives[g['start']['snapshot']]['trialsPresent']),None)
    trial_history.append({'file':path,'presentBeforeBenchmark':first})
note_growth=[{'game':g['start']['game'],'sizes':archives[g['start']['snapshot']]['noteSizes']}
             for g in games if g['start']['game'] in (1,31,37,73,97,103,133,157,181,199,200)]
source_preserved={'native':digest(native)==source['sourceNativeSha256'],
                  'ledger':digest(FOLDER/'data/ledger.jsonl')==source['sourceLedgerSha256'],
                  'workspace':all(digest(FOLDER/k)==v for k,v in source['sourceWorkspace'].items())}
assert all(source_preserved.values())

summary=json.loads((FOLDER/'workspace/final-summary-200.json').read_text())
report={
    'assessedAt':dt.datetime.now(dt.timezone.utc).isoformat(),
    'scope':{'benchmarkGames':len(games),'acceptedMoves':sum(len(g['moves']) for g in games),'practiceSessions':len(practice),'hiddenReasoningAnalysedOrExported':False},
    'integrity':{'ledger':chain,'practiceLedger':practice_chain,'pinnedFilesVerified':len(manifest), 'pinnedMismatches':[],
                 'allPgnMoveListsAndResultsMatchLedger':True,'allAcceptedMovesSanFenAndOutcomesVerified':True,
                 'fixedOpponentsColorRotationAndNodesVerified':True,'documentedManifestUpdateChainVerified':True,
                 'documentedOperatorUpdates':updates,'snapshotArchivesVerified':len(archives),'snapshotHashesAllMatch':True,'originalSourcePreserved':source_preserved},
    'outcomes':{op:a.tally([g for g in games if g['start']['opponent']['id']==op]) for op in a.OPPONENTS},
    'quarters':quarters,'matchedEarlyLate':trends['primary'],'recentMatchedWindows':trends['recent'],'opponentBootstrap':opponent_bootstrap,
    'perOpponentBehavior':{'early':by_op_behavior([g for b in early for g in b]),'late':by_op_behavior([g for b in late for g in b])},
    'independentRating':ratings,
    'practice':{'countsBySource':dict(collections.Counter(g['start'].get('source',{}).get('kind') for g in practice)),
                'endings':dict(collections.Counter(g['end']['reason'] for g in practice)), 'scoredResults':a.tally(practice),'behavior':a.behavior(practice)},
    'trialHistory':trial_history,'noteGrowth':note_growth,
    'nativeMetadata':{'contextSettings':dict(collections.Counter(f"{c['model']}:{c['effort']}" for c in contexts)),
                      'nonMaxMoves':medium_moves,'compactions':len(compactions),
                      'compactionsDuringFirst96Games':sum(when(games[0]['start']['timestamp'])<=when(t)<=when(games[95]['end']['timestamp']) for t in compactions),
                      'compactionsDuringGames103To198':sum(when(games[102]['start']['timestamp'])<=when(t)<=when(games[197]['end']['timestamp']) for t in compactions),
                      'note':'Only configuration metadata and compaction timestamps were read; no private reasoning or compacted summaries were analysed.'},
    'limitations':['The learning methods changed sequentially; no randomised causal comparison.',
                   'Material-loss features are mechanical proxies, not engine evaluations of move quality.',
                   'Elapsed move time includes idle/tool delay and is not pure reasoning time.',
                   'Context compaction and note growth are possible contributors, not established causes.']
}
HERE.mkdir(parents=True,exist_ok=True)
(HERE/'assessment.json').write_text(json.dumps(report,indent=2)+'\n')
primary=trends['primary']
print(json.dumps({'scope':report['scope'],'integrity':{k:v for k,v in report['integrity'].items() if k!='documentedOperatorUpdates'},
 'ratings':ratings,'matched':{k:primary[k] for k in ['early','late','delta','interval','byOpponent','earlyBehavior','lateBehavior']},
 'opponentBootstrap':opponent_bootstrap,'quarters':quarters,'practice':report['practice'],'trialHistory':trial_history,'native':report['nativeMetadata']},indent=2))
