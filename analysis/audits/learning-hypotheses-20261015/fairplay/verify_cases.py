#!/usr/bin/env python3
"""Mechanical replay and fixed-rating sensitivity; no chess search/evaluation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tarfile

ROOT = Path('/home/peter/Chess Learning')
OUT = Path(__file__).resolve().parent
FROZEN = OUT.parent / 'measurement/snapshots'
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'Chess - Opus-5.5/.arena/vendor/chess-1.11.2'))
import chess

RUNS = {'opus': ROOT / 'Chess - Opus-5.5', 'fable': ROOT / 'Chess - Fable-5.1'}
report = {'method': 'Pure python-chess mechanical legality and repetition checks; pinned rating posterior on observed results only. No engine, position scoring or move selection.'}

for slug, run in RUNS.items():
    manifest_path = run / '.arena/manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    events = [json.loads(l) for l in (FROZEN / slug / 'data/ledger.jsonl').open()]
    starts = [e for e in events if e['kind'] == 'start']
    mismatches = [name for name, expected in manifest.items()
                  if hashlib.sha256((run / name).read_bytes()).hexdigest() != expected]
    out = {'pinnedFiles': len(manifest), 'pinnedFileMismatches': mismatches,
           'manifestSha256': manifest_hash, 'allStartsPinCurrentManifest': all(e['manifest_sha256'] == manifest_hash for e in starts),
           'agentsSha256': manifest.get('AGENTS.md'), 'agentsMtime': (run / 'AGENTS.md').stat().st_mtime,
           'initialMetricAwareness': []}
    first = starts[0]
    with tarfile.open(run / 'data/snapshots' / (first['snapshot'] + '.tar.gz'), 'r:gz') as archive:
        filename = 'PLAN.md' if slug == 'opus' else 'README.md'
        lines = archive.extractfile(filename).read().decode().splitlines()
        for n, line in enumerate(lines, 1):
            if any(x in line for x in ['rolling window', 'last 50 rated', 'Full-strength games', 'Rated games (']):
                out['initialMetricAwareness'].append({'firstGame': first['game'], 'timestamp': first['timestamp'],
                      'snapshot': first['snapshot'], 'file': filename, 'line': n, 'text': line})
    game = 186 if slug == 'opus' else 22
    ge = [e for e in events if e.get('game') == game]
    start = next(e for e in ge if e['kind'] == 'start')
    result = next(e for e in ge if e['kind'] == 'result')
    board = chess.Board(start.get('initial_fen', chess.STARTING_FEN))
    fens_match = True
    for event in ge:
        if event['kind'] == 'move':
            move = chess.Move.from_uci(event['uci'])
            if move not in board.legal_moves:
                raise ValueError(('illegal recorded move', slug, game, event['ply']))
            board.push(move)
            fens_match = fens_match and board.fen() == event['fen']
    out['repetitionCase'] = {'game': game, 'recordedResult': result,
         'recordedFensMatchReplay': fens_match,
         'canClaimThreefold': board.can_claim_threefold_repetition(),
         'finalPositionAlreadyRepeatedThrice': board.is_repetition(3),
         'resultWithClaimDrawTrue': board.result(claim_draw=True),
         'clarification': 'A legal threefold claim can be available before the third occurrence is played; the referee automatically claims available draws.'}
    if slug == 'opus':
        spec = importlib.util.spec_from_file_location('frozen_opus_rating', FROZEN / slug / '.arena/rating.py')
        rating = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rating)
        starts_by_game = {e['game']: e for e in starts}
        obs = [{'game': e['game'], 'anchor': rating.ANCHORS[starts_by_game[e['game']]['opponent']['id']], 'score': e['score']}
               for e in events if e['kind'] == 'result' and e.get('score') is not None
               and starts_by_game[e['game']]['opponent']['id'] in rating.ANCHORS][-50:]
        alt = [dict(e, score=0) if e['game'] == 186 else e for e in obs]
        out['game186RatingSensitivity'] = {
            'actualLast50': rating.posterior(obs),
            'replaceG186DrawWithLossSameOther49': rating.posterior(alt),
            'interpretation': 'This is a score sensitivity test, not evidence that continuing game 186 would have lost. One draw cannot by itself explain a roughly 250-Elo early-to-late increase.'}
    report[slug] = out

(OUT / 'case-verification.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
