#!/usr/bin/env python3
"""Read-only, repeatable assessment of adaptation in the chess experiments.

Uses recorded moves and authored notes. Never calls a chess engine or a learner.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import fcntl
import hashlib
import importlib.util
import json
import random
import statistics
import sys
import tarfile
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'Chess - GPT-6-Astra/.arena/vendor/chess-1.11.2'))
import chess

RUNS = {
    'astra': ('Chess - GPT-6-Astra', 'GPT-6 Astra'),
    'opus': ('Chess - Opus-5.5', 'Claude Opus 5.5'),
    'sol': ('Chess - GPT-6.1-Sol', 'GPT-6.1 Sol'),
    'sol-long-context': ('Chess - GPT-6.1-Sol - Long Context', 'GPT-6.1 Sol · 828K'),
    'fable': ('Chess - Fable-5.1', 'Claude Fable 5.1'),
}
OPPONENTS = ('full-strength', 'skill-0', 'elo-1800-setting')
RATED = OPPONENTS[1:]
VALUES = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
COLORS = {'astra': '#e8e7e1', 'opus': '#df9b7b', 'sol': '#a0bce6', 'sol-long-context': '#b2a3d9', 'fable': '#d9ba76'}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def read_ledger(path):
    """Caller holds the arena lock. Fail closed rather than silently skip records."""
    if not path.exists():
        return [], {'events': 0, 'head': None}
    events = []
    previous = '0' * 64
    for number, line in enumerate(path.read_text().splitlines(), 1):
        event = json.loads(line)
        saved = event['sha256']
        body = {k: v for k, v in event.items() if k != 'sha256'}
        if (event['previous'] != previous or event['seq'] != number
                or hashlib.sha256(canonical(body).encode()).hexdigest() != saved):
            raise ValueError(f'Ledger integrity failure: {path}, event {number}')
        previous = saved
        events.append(event)
    return events, {'events': len(events), 'head': previous if events else None,
                    'lastTimestamp': events[-1]['timestamp'] if events else None}


def group_games(events):
    games = {}
    for event in events:
        kind, number = event['kind'], event.get('game')
        if kind == 'start':
            if number in games:
                raise ValueError(f'Duplicate game {number}')
            games[number] = {'start': event, 'moves': [], 'illegal': [], 'end': None}
        elif number in games:
            game = games[number]
            if kind == 'move':
                game['moves'].append(event)
            elif kind == 'illegal':
                game['illegal'].append(event)
            elif kind == 'result':
                if game['end']:
                    raise ValueError(f'Duplicate result {number}')
                game['end'] = event
    return list(games.values())


def material(board, color):
    return sum(value * (len(board.pieces(piece, color)) - len(board.pieces(piece, not color)))
               for piece, value in VALUES.items())


def replay(game):
    """Mechanical features only. A material swing is not a best-move evaluation."""
    start = game['start']
    learner = start['color'] == 'white'
    board = chess.Board(start.get('initial_fen', chess.STARTING_FEN))
    balances = [material(board, learner)]
    captures, own, seconds, castles = [], [], [], []
    after_opponent = []
    for index, event in enumerate(game['moves']):
        move = chess.Move.from_uci(event['uci'])
        actor = 'model' if board.turn == learner else 'stockfish'
        if event['actor'] != actor or not board.is_legal(move):
            raise ValueError(f'Invalid accepted move/actor in game {start["game"]}, ply {index + 1}')
        if event['ply'] != index + 1:
            raise ValueError('Ply numbering mismatch')
        piece = board.piece_at(move.from_square)
        target = board.piece_at(move.to_square)
        if actor == 'model':
            own.append({'uci': event['uci'], 'san': event['san'], 'piece': piece.piece_type})
            if board.is_castling(move):
                castles.append(len(own))
            if isinstance(event.get('seconds'), (int, float)):
                seconds.append(event['seconds'])
        if actor != 'model' and target and target.color == learner and target.piece_type not in (chess.PAWN, chess.KING):
            captures.append({'index': index, 'ply': index + 1, 'piece': target.symbol().upper(),
                             'san': event['san'], 'uci': event['uci']})
        if event['san'] != board.san(move):
            raise ValueError('SAN mismatch')
        board.push(move)
        if event['fen'] != board.fen():
            raise ValueError('Recorded FEN mismatch')
        balances.append(material(board, learner))
        if actor != 'model' and index + 1 >= 20:
            after_opponent.append(balances[-1])
    losses = []
    for capture in captures:
        index = capture['index']
        if index == 0:  # no preceding learner move
            continue
        # Before learner move -> after opponent capture -> after next learner reply.
        # With no next reply, the short-horizon classification is unavailable.
        if index + 1 >= len(game['moves']):
            continue
        delta = balances[index + 2] - balances[index - 1]
        if delta <= -2:
            losses.append({k: v for k, v in capture.items() if k != 'index'} | {'materialChange': delta})
    end = game['end']
    if end and (end['plies'] != len(game['moves']) or end['illegal_attempts'] != len(game['illegal'])):
        raise ValueError('Result accounting mismatch')
    if end and end['score'] is not None:
        white_score = {'1-0': 1, '0-1': 0, '1/2-1/2': .5}[end['result']]
        if end['score'] != (white_score if learner else 1 - white_score):
            raise ValueError('Result perspective mismatch')
        outcome = board.outcome(claim_draw=True)
        if end['reason'] not in ('resignation', 'illegal_move_forfeit'):
            if not outcome or outcome.result() != end['result']:
                raise ValueError(f'Terminal result mismatch: {end["reason"]}')
    return {'ownMoves': len(own), 'seconds': seconds, 'illegal': len(game['illegal']),
            'shortLosses': losses, 'leadReached': any(x >= 3 for x in after_opponent),
            'castleBy10': bool(castles and castles[0] <= 10) if len(own) >= 10 else None,
            'queenMovesFirst10': sum(m['piece'] == chess.QUEEN for m in own[:10]),
            'firstMove': own[0]['san'] if own else None,
            'whiteFirstMove': game['moves'][0]['san'] if game['moves'] else None,
            'openingSignature': ' '.join(m['uci'] for m in own[:3]) if len(own) >= 3 else None,
            'finalMaterial': balances[-1]}


def tally(games):
    scores = [g['end']['score'] for g in games if g['end'] and g['end']['score'] is not None]
    return {'games': len(scores), 'wins': scores.count(1), 'draws': scores.count(.5),
            'losses': scores.count(0), 'points': sum(scores),
            'score': statistics.mean(scores) if scores else None}


def behavior(games):
    features = [g['features'] for g in games]
    own = sum(f['ownMoves'] for f in features)
    illegals = sum(f['illegal'] for f in features)
    losses = sum(len(f['shortLosses']) for f in features)
    leads = [g for g in games if g['features']['leadReached']]
    castle = [f['castleBy10'] for f in features if f['castleBy10'] is not None]
    seconds = [s for f in features for s in f['seconds']]
    return {'ownMoves': own, 'illegalAttempts': illegals,
            'illegalPer100': 100 * illegals / own if own else None,
            'shortLossCount': losses, 'shortLossPer100': 100 * losses / own if own else None,
            'gamesWithShortLoss': sum(bool(f['shortLosses']) for f in features),
            'leadGames': len(leads), 'leadWins': sum(g['end']['score'] == 1 for g in leads),
            'leadConversion': sum(g['end']['score'] == 1 for g in leads) / len(leads) if leads else None,
            'castleBy10': statistics.mean(castle) if castle else None, 'castleEligibleGames': len(castle),
            'medianMoveSeconds': statistics.median(seconds) if seconds else None}


def complete_rotations(games):
    """All six cells must be present, scored, and conform to the rotation."""
    grouped = collections.defaultdict(list)
    for game in games:
        grouped[(game['start']['game'] - 1) // 6].append(game)
    result = []
    expected = [(opponent, color) for opponent in OPPONENTS for color in ('white', 'black')]
    for number, group in sorted(grouped.items()):
        group.sort(key=lambda g: g['start']['game'])
        cells = [(g['start']['opponent']['id'], g['start']['color']) for g in group]
        if len(group) == 6 and cells == expected and all(g['end'] and g['end']['score'] is not None for g in group):
            result.append(group)
    return result


def quantile(sorted_values, p):
    index = p * (len(sorted_values) - 1)
    lo, hi = int(index), min(int(index) + 1, len(sorted_values) - 1)
    return sorted_values[lo] + (index - lo) * (sorted_values[hi] - sorted_values[lo])


def compare_blocks(early, late, seed=20261004):
    """Resample full rotation blocks, not individual moves or overlapping Elo points."""
    before = [g for block in early for g in block if g['start']['opponent']['id'] in RATED]
    after = [g for block in late for g in block if g['start']['opponent']['id'] in RATED]
    result = {'early': tally(before), 'late': tally(after),
              'earlyBehavior': behavior(before), 'lateBehavior': behavior(after),
              'earlyGames': [g['start']['game'] for g in before], 'lateGames': [g['start']['game'] for g in after],
              'rotationsPerWindow': len(early), 'delta': None, 'interval': None,
              'status': 'Too few games'}
    result['byOpponent'] = {op: {
        'early': tally([g for block in early for g in block if g['start']['opponent']['id'] == op]),
        'late': tally([g for block in late for g in block if g['start']['opponent']['id'] == op])}
        for op in OPPONENTS}
    if not before or not after:
        return result
    result['delta'] = result['late']['score'] - result['early']['score']
    if min(len(early), len(late)) >= 5:
        a = [tally([g for g in block if g['start']['opponent']['id'] in RATED])['score'] for block in early]
        b = [tally([g for g in block if g['start']['opponent']['id'] in RATED])['score'] for block in late]
        rng = random.Random(seed)
        samples = sorted(statistics.mean(rng.choices(b, k=len(b))) - statistics.mean(rng.choices(a, k=len(a)))
                         for _ in range(10000))
        interval = [quantile(samples, .025), quantile(samples, .975)]
        result['interval'] = interval
        result['status'] = ('Improved in matched windows' if interval[0] > 0 else
                            'Declined in matched windows' if interval[1] < 0 else 'No clear change')
    return result


def trends(games):
    blocks = complete_rotations(games)
    size = len(blocks) // 2
    primary = compare_blocks(blocks[:size], blocks[-size:] if size else [])
    recent_size = min(8, size)
    recent = compare_blocks(blocks[-2 * recent_size:-recent_size], blocks[-recent_size:]) if recent_size else None
    return {'primary': primary, 'recent': recent, 'completeRotations': len(blocks),
            'byOpponent': {op: tally([g for g in games if g['start']['opponent']['id'] == op]) for op in OPPONENTS}}


def source_at(folder, relative, text, marker=None):
    lines = text.splitlines()
    line = next((i for i, s in enumerate(lines, 1) if marker and marker in s), None)
    return {'path': str((folder / 'workspace' / relative).relative_to(ROOT)), 'line': line,
            'sha256': hashlib.sha256(text.encode()).hexdigest()}


def historical_notes(folder, games, filenames):
    """Only named regular note files; no archive extraction or helper execution."""
    cache, notes, versions = {}, {}, []
    previous = None
    for game in games:
        start = game['start']
        digest = start.get('snapshot')
        if not digest or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
            raise ValueError('Invalid workspace snapshot identifier')
        if digest not in cache:
            path = folder / 'data/snapshots' / (digest + '.tar.gz')
            values = {}
            with tarfile.open(path, 'r:gz') as archive:
                for name in filenames:
                    try:
                        entry = archive.getmember(name)
                    except KeyError:
                        continue
                    if not entry.isfile() or entry.size > 4 * 1024 * 1024:
                        raise ValueError('Unexpected note member')
                    values[name] = archive.extractfile(entry).read().decode()
            cache[digest] = values
        values = cache[digest]
        notes[start['game']] = values
        signature = hashlib.sha256(canonical({name: hashlib.sha256(value.encode()).hexdigest()
                                              for name, value in values.items()}).encode()).hexdigest()
        if signature != previous:
            versions.append({'game': start['game'], 'timestamp': start['timestamp'], 'snapshot': digest,
                             'noteWords': sum(len(v.split()) for v in values.values()),
                             'files': {n: hashlib.sha256(v.encode()).hexdigest() for n, v in values.items()}})
            previous = signature
    return notes, versions


def strategies(profile, folder, games, notes):
    """Human-curated meanings, automatic historical timing and fresh-game measurements."""
    result = []
    blocks = complete_rotations(games)
    for entry in profile['changes']:
        match = next(((number, texts[entry['file']]) for number, texts in sorted(notes.items())
                      if entry['file'] in texts and entry['marker'] in texts[entry['file']]), None)
        item = {k: v for k, v in entry.items() if k != 'marker'}
        item['verifiedBeforeGame'] = match[0] if match else None
        if match:
            number, text = match
            item['source'] = source_at(folder, entry['file'], text, entry['marker'])
            item['source']['snapshot'] = next(g['start']['snapshot'] for g in games if g['start']['game'] == number)
            before = [block for block in blocks if block[-1]['start']['game'] < number][-2:]
            after = [block for block in blocks if block[0]['start']['game'] >= number][:2]
            size = min(len(before), len(after))
            item['transfer'] = compare_blocks(before[-size:], after[:size]) if size else None
            item['retention'] = tally([g for block in [b for b in blocks if b[0]['start']['game'] >= number][2:4]
                                       for g in block if g['start']['opponent']['id'] in RATED])
        result.append(item)
    return result


def rating_data(folder, games, cache):
    spec = importlib.util.spec_from_file_location('assessment_rating', ROOT / 'Chess - GPT-6-Astra/.arena/rating.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    observations = [{'game': g['start']['game'], 'timestamp': g['end']['timestamp'],
                     'anchor': module.ANCHORS[g['start']['opponent']['id']], 'score': g['end']['score']}
                    for g in games if g['end'] and g['end']['score'] is not None and g['start']['opponent']['id'] in RATED]
    cached = (cache or {}).get('rating', {})
    # Never write to the learner's cache; ensure its signature matches this locked snapshot.
    completed = sum(bool(g['end']) and g['end']['score'] is not None for g in games)
    unfinished = sum(bool(g['end']) and g['end']['score'] is None for g in games)
    signature = hashlib.sha256(json.dumps([module.VERSION, observations, completed, unfinished], sort_keys=True).encode()).hexdigest()
    if (cache or {}).get('signature') == signature:
        rating = cached
    else:
        rating = module.estimate(games, cache_path=None)
    history = [{k: p[k] for k in ('game', 'estimate', 'lower', 'upper', 'rated_games')} for p in rating['history']]
    mature = [p for p in history if p['rated_games'] >= 20]
    peak = max(mature, key=lambda p: p['estimate']) if mature else None
    baseline = next((p for p in history if p['rated_games'] == 50), None)
    # The first and current 50-game windows must be disjoint for this headline change.
    change = rating['estimate'] - baseline['estimate'] if baseline and len(observations) >= 100 else None
    return {k: rating.get(k) for k in ('estimate', 'lower', 'upper', 'rated_games_total', 'window', 'interval_type')} | {
        'history': history, 'maturePeak': peak, 'baseline50': baseline, 'changeSinceBaseline50': change,
        'changeFromMaturePeak': rating['estimate'] - peak['estimate'] if peak else None}


def assess_run(key, profiles):
    name, label = RUNS[key]
    folder = ROOT / name
    with (folder / 'data/.lock').open('rb') as lock:
        fcntl.flock(lock, fcntl.LOCK_SH)
        events, integrity = read_ledger(folder / 'data/ledger.jsonl')
        practice_events, practice_integrity = read_ledger(folder / 'data/practice/ledger.jsonl')
        cache_path = folder / 'data/rating-cache.json'
        cache = json.loads(cache_path.read_text()) if cache_path.exists() else None
    games = group_games(events)
    practices = group_games(practice_events)
    for g in games:
        number = g['start']['game']
        expected_opponent = OPPONENTS[((number - 1) % 6) // 2]
        expected_color = 'white' if number % 2 else 'black'
        if (g['start']['opponent']['id'], g['start']['color'], g['start']['nodes_per_move']) != (expected_opponent, expected_color, 1_000_000):
            raise ValueError(f'Benchmark rotation/nodes changed: {key} game {number}')
        expected_options = {'Hash': 64, 'Threads': 1, 'UCI_LimitStrength': expected_opponent == 'elo-1800-setting'}
        if expected_opponent == 'elo-1800-setting':
            expected_options['UCI_Elo'] = 1800
        else:
            expected_options['Skill Level'] = 0 if expected_opponent == 'skill-0' else 20
        if g['start']['opponent']['options'] != expected_options:
            raise ValueError(f'Benchmark engine options changed: {key} game {number}')
        g['features'] = replay(g)
    for p in practices:
        replay(p)
    completed = [g for g in games if g['end'] and g['end']['score'] is not None]
    profile = profiles[key]
    notes, versions = historical_notes(folder, games, profile['noteFiles'])
    openings = collections.Counter(('white' if g['start']['color'] == 'white' else 'black vs ' + g['features']['whiteFirstMove'],
                                     g['features']['firstMove']) for g in completed)
    examples = [{'game': g['start']['game'], 'opponent': g['start']['opponent']['id'], **loss}
                for g in completed for loss in g['features']['shortLosses']]
    return {'id': key, 'label': label, 'color': COLORS[key], 'overall': tally(completed),
            'byColor': {c: tally([g for g in completed if g['start']['color'] == c]) for c in ('white', 'black')},
            'rating': rating_data(folder, games, cache), 'trend': trends(completed), 'behavior': behavior(completed),
            'practice': {'started': len(practices), 'scored': tally(practices),
                         'stopped': sum(bool(p['end']) and p['end']['score'] is None for p in practices),
                         'active': sum(not p['end'] for p in practices),
                         'origins': dict(collections.Counter(p['start'].get('source', {}).get('kind', 'unknown') for p in practices))},
            'openings': [{'side': side, 'move': move, 'games': count} for (side, move), count in openings.most_common()],
            'first12': tally([g for g in completed if g['start']['game'] <= 12 and g['start']['opponent']['id'] in RATED]),
            'strategyChanges': strategies(profile, folder, games, notes), 'noteVersions': versions,
            'shortLossExamples': examples, 'interpretation': profile['interpretation'],
            'diagnosisExamples': profile['examples'], 'integrity': {'benchmark': integrity, 'practice': practice_integrity,
                'acceptedBenchmarkPlies': sum(len(g['moves']) for g in games),
                'acceptedPracticePlies': sum(len(g['moves']) for g in practices), 'legalReplay': True},
            'activeGame': next((g['start']['game'] for g in games if not g['end']), None),
            'gameFeatures': [{'game': g['start']['game'], 'color': g['start']['color'],
                'opponent': g['start']['opponent']['id'], 'score': g['end']['score'],
                **{k: v for k, v in g['features'].items() if k != 'seconds'}} for g in completed]}


def pct(value):
    return '—' if value is None else f'{value:.1%}'


def markdown(data):
    lines = ['# How the models learn', '', f'Assessment captured {data["generatedAt"]}.', '',
             'Learning means adaptation of notes, decisions, repertoire and practice within the run; no model weights are updated.', '',
             '| Model | Scored games | Engine-relative Elo | Elo change |',
             '|---|---:|---:|---:|']
    for r in data['runs']:
        t, rat = r['trend']['primary'], r['rating']
        change = rat['changeSinceBaseline50']
        delta = f'{change:+d}' if change is not None else 'Early sample'
        lines.append(f'| {r["label"]} | {r["overall"]["games"]} | {rat["estimate"]} · {rat["lower"]}–{rat["upper"]} | {delta} |')
    lines += ['', 'Elo is the headline outcome. Change compares the first complete 50-rated-game estimate with the latest 50-rated-game estimate, and is shown only after 100 rated games so the windows do not overlap. Each estimate has its own credible interval; subtracting the medians does not provide a credible interval for the change.', '',
              'Supporting game-score analysis compares the first and last equal halves of complete six-game rotations; an unpaired middle rotation is omitted. Recent momentum compares adjacent windows of up to eight rotations. Opponent/color counts match and games do not overlap within a comparison. Each rated window has four games per rotation. Windows with fewer than five rotations are too small for a directional verdict. Intervals resample complete rotations and are exploratory, not causal tests.', '']
    for r in data['runs']:
        b, t = r['behavior'], r['trend']['primary']
        lines += [f'## {r["label"]}', '', r['interpretation']['observed'], '',
                  f'Possible explanation: {r["interpretation"]["hypothesis"]}', '',
                  f'What would strengthen the claim: {r["interpretation"]["nextEvidence"]}', '',
                  f'Accepted own moves: {b["ownMoves"]}; illegal submissions: {b["illegalAttempts"]} ({b["illegalPer100"]:.2f} per 100 accepted own moves).',
                  f'Short-horizon piece-loss events: {b["shortLossCount"]} ({b["shortLossPer100"]:.2f} per 100 own moves); won {b["leadWins"]}/{b["leadGames"]} games after reaching a +3 material lead after move 10.',
                  f'Practice: {r["practice"]["started"]} sessions; {r["practice"]["stopped"]} stopped/unfinished. Kept separate from benchmark outcomes.', '']
        baseline = r['rating']['baseline50']
        if r['rating']['changeSinceBaseline50'] is not None:
            lines.append(f'Elo baseline after 50 rated games: {baseline["estimate"]} ({baseline["lower"]}–{baseline["upper"]}); latest {r["rating"]["estimate"]} ({r["rating"]["lower"]}–{r["rating"]["upper"]}); median change {r["rating"]["changeSinceBaseline50"]:+d}.')
        lines.append(f'Supporting matched game scores: {pct(t["early"]["score"])} → {pct(t["late"]["score"])}. {t["status"]}.')
        if t['interval']:
            lines.append(f'Matched score change: {t["delta"]*100:+.1f} percentage points; exploratory 95% block-bootstrap interval {t["interval"][0]*100:+.1f} to {t["interval"][1]*100:+.1f}.')
        lines += ['', '| Opponent | Early matched score | Late matched score |', '|---|---:|---:|']
        for opponent, scores in t['byOpponent'].items():
            lines.append(f'| {opponent} | {pct(scores["early"]["score"])} ({scores["early"]["games"]} games) | {pct(scores["late"]["score"])} ({scores["late"]["games"]} games) |')
        lines += ['', '| Change declared | Verified before game | Fresh rated score before → after |', '|---|---:|---:|']
        for change in r['strategyChanges']:
            transfer = change.get('transfer')
            scores = f'{pct(transfer["early"]["score"])} → {pct(transfer["late"]["score"])}' if transfer else 'Not enough complete rotations'
            lines.append(f'| {change["title"]} | {change["verifiedBeforeGame"] or "Unverified"} | {scores} |')
        lines += ['', 'These are historical declarations, not proof the protocol was followed or that the change caused the result.', '', 'Authored failure examples:', '']
        for example in r['diagnosisExamples']:
            lines.append(f'- Game {example["game"]}: {example["summary"]} Source: `{example["source"]}`.')
        lines += ['', f'Ledger hashes, event numbering, accepted-move legality/FENs, results, colors and benchmark rotation were checked. Benchmark snapshot head: `{r["integrity"]["benchmark"]["head"]}`.', '']
    lines += ['## Interpretation rules', '', 'A strategy revision is an attempt. A changed move pattern is behavior. Better results in fresh, opponent-matched games are transfer evidence. Persistence across later blocks is retention. One uncontrolled run cannot identify why a particular intervention worked.', '',
              'Short-horizon piece losses include sacrifices and do not establish chess blunders. Material leads ignore king safety and positional compensation. Time between submissions includes pauses; it is not compute time. Elo is conditional on nominal Stockfish anchors; maximum-strength games are excluded. No private reasoning transcripts were read. All explanations are marked as observations or hypotheses.', '']
    return '\n'.join(lines)


def atomic_write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(value)
    temp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Fresh standalone HTML filename under deliverables/')
    args = parser.parse_args()
    profiles = json.loads((HERE / 'strategy-register.json').read_text())
    data = {'version': 1, 'generatedAt': dt.datetime.now(dt.timezone.utc).isoformat(),
            'annotationsReviewedAt': profiles.pop('reviewedAt'), 'runs': [assess_run(key, profiles) for key in RUNS]}
    data['sourceRevision'] = hashlib.sha256(canonical([r['integrity'] for r in data['runs']]).encode()).hexdigest()
    timestamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d-%H%M%S')
    output = args.output or ROOT / 'deliverables' / f'chess-learning-assessment-{timestamp}.html'
    if output.resolve().parent != (ROOT / 'deliverables').resolve():
        raise ValueError('HTML must be exported to workspace deliverables/')
    encoded = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    html = (HERE / 'template.html').read_text().replace('__ASSESSMENT_DATA__', encoded)
    atomic_write(output, html)
    atomic_write(HERE / 'latest.json', json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    atomic_write(output.with_suffix('.json'), json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    atomic_write(output.with_suffix('.md'), markdown(data))
    for r in data['runs']:
        rating = r['rating']
        change = rating['changeSinceBaseline50']
        delta = f'{change:+d} after the first 50 rated games' if change is not None else 'early sample'
        print(f'{r["label"]}: {r["overall"]["games"]} games; Elo {rating["estimate"]} ({rating["lower"]}–{rating["upper"]}); {delta}')
    print(output)


if __name__ == '__main__':
    main()
