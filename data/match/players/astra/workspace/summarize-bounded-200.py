"""Read-only benchmark/practice accounting; no chess analysis or move selection."""
from pathlib import Path
from collections import Counter, defaultdict
import gzip
import json
import re

ROOT = Path(__file__).resolve().parent.parent

def read_ledger(relative):
    rows = [json.loads(line) for line in (ROOT / relative).read_text().splitlines() if line.strip()]
    previous = '0' * 64
    for index, row in enumerate(rows, 1):
        assert row['seq'] == index, (relative, index, 'sequence')
        assert row['previous'] == previous, (relative, index, 'previous link')
        previous = row['sha256']
    return rows

def tally(rows):
    scored = [r for r in rows if r['score'] is not None]
    counts = Counter(r['score'] for r in scored)
    return {'games': len(rows), 'scored': len(scored), 'wins': counts[1],
            'draws': counts[0.5], 'losses': counts[0],
            'unfinished': len(rows)-len(scored),
            'points': sum(r['score'] for r in scored),
            'score_percent': 100*sum(r['score'] for r in scored)/len(scored) if scored else None}

rows = read_ledger('data/ledger.jsonl')
starts = {r['game']: r for r in rows if r['kind'] == 'start'}
results = [dict(r) for r in rows if r['kind'] == 'result']
assert list(starts) == list(range(1, 201))
assert [r['game'] for r in results] == list(range(1, 201))
rotation = [('full-strength', 'white'), ('full-strength', 'black'),
            ('skill-0', 'white'), ('skill-0', 'black'),
            ('elo-1800-setting', 'white'), ('elo-1800-setting', 'black')]
settings = defaultdict(set)
for r in results:
    s = starts[r['game']]
    r['color'] = s['color']
    r['opponent'] = s['opponent']['id']
    assert (r['opponent'], r['color']) == rotation[(r['game']-1) % 6]
    assert s['nodes_per_move'] == 1000000
    settings[r['opponent']].add(json.dumps(s['opponent']['options'], sort_keys=True))
    r['own_moves'] = (r['plies']+1)//2 if r['color'] == 'white' else r['plies']//2
    with gzip.open(ROOT / f"data/games/{r['game']:06}.pgn.gz", 'rt') as f:
        pgn = f.read()
    headers = dict(re.findall(r'^\[(\w+) "(.*)"\]$', pgn, flags=re.M))
    assert int(headers['Round']) == r['game']
    assert headers['Result'] == r['result']
    assert headers['Termination'] == r['reason']
    assert headers['OpponentSetting'] == r['opponent']
assert all(len(v) == 1 for v in settings.values())
assert len(list((ROOT/'data/games').glob('*.pgn.gz'))) == 200
assert sum(r['illegal_attempts'] for r in results) == sum(r['kind']=='illegal' for r in rows)

status = json.loads((ROOT/'workspace/final-status-200.json').read_text())
assert status['active_game'] is None
opponents = {op: tally([r for r in results if r['opponent']==op]) for op, _ in rotation}
for s in status['stats']:
    t = opponents[s['opponent']]
    for key in ['wins', 'draws', 'losses', 'unfinished']:
        assert t[key] == s[key]
    assert t['scored'] == s['completed']

practice_rows = read_ledger('data/practice/ledger.jsonl')
practice_starts = {r['game']: r for r in practice_rows if r['kind']=='start'}
practice_results = [r for r in practice_rows if r['kind']=='result']
assert set(practice_starts) == {r['game'] for r in practice_results}
practice = tally(practice_results)
practice['illegal_attempts'] = sum(r['illegal_attempts'] for r in practice_results)
practice['source_kinds'] = dict(Counter(s['source']['kind'] for s in practice_starts.values()))
practice['opponents'] = dict(Counter(s['opponent']['id'] for s in practice_starts.values()))
practice['terminations'] = dict(Counter(r['reason'] for r in practice_results))

rated = [r for r in results if r['opponent'] != 'full-strength']
assert len(rated) == status['elo']['rated_games_total'] == 132
comparison = {}
for op in opponents:
    selected = [r for r in results if r['opponent'] == op]
    half = len(selected)//2
    comparison[op] = {'first_half': tally(selected[:half]), 'second_half': tally(selected[half:])}
trials = []
for p in sorted((ROOT/'workspace/trials').glob('*.md')):
    if p.name.startswith('move-check-before-'):
        continue
    match = re.search(r'-(\d+)\.md$', p.name)
    if match:
        trials.append({'number': int(match[1]), 'file': str(p.relative_to(ROOT)),
                       'title': p.read_text().splitlines()[0].lstrip('# ')})
trials.sort(key=lambda t:t['number'])
assert [t['number'] for t in trials] == list(range(1, 30))
summary = {
    'endpoint': '200 scored benchmark games; no further game started',
    'overall': tally(results), 'opponents': opponents,
    'by_color': {c:tally([r for r in results if r['color']==c]) for c in ['white','black']},
    'chronological_halves': {'1-100': tally(results[:100]), '101-200': tally(results[100:])},
    'equal_count_opponent_halves': comparison,
    'first_50_rated': tally(rated[:50]), 'last_50_rated': tally(rated[-50:]),
    'first_50_rated_game_span': [rated[0]['game'],rated[49]['game']],
    'last_50_rated_game_span': [rated[-50]['game'],rated[-1]['game']],
    'benchmark_plies': sum(r['plies'] for r in results),
    'benchmark_own_moves': sum(r['own_moves'] for r in results),
    'benchmark_illegal_attempts': sum(r['illegal_attempts'] for r in results),
    'benchmark_illegals_by_game': {r['game']:r['illegal_attempts'] for r in results if r['illegal_attempts']},
    'benchmark_terminations': dict(Counter(r['reason'] for r in results)),
    'final_8_games': [{k:r[k] for k in ['game','opponent','color','score','reason','plies','own_moves','illegal_attempts']} for r in results[-8:]],
    'final_8_tally': tally(results[-8:]),
    'trial_29_tally': tally(results[-2:]),
    'practice': practice, 'trial_count': len(trials), 'trials': trials,
    'milestones': [h for h in status['elo']['history'] if h['game'] in [30,42,60,76,96,120,150,180,198]],
    'final_elo': {k:v for k,v in status['elo'].items() if k != 'history'},
    'checks': {'benchmark_starts_and_results':200,'pgn_result_matches':200,
               'rotation_and_colors_match':True,'one_million_nodes_each_game':True,
               'opponent_options_constant_per_setting':True,'status_totals_match_ledger':True,
               'benchmark_and_practice_previous_links_and_sequences_match':True,
               'practice_all_closed':True,'active_benchmark':None,
               'cryptographic_event_hashes_recomputed':False},
    'first_benchmark_start': starts[1]['timestamp'],
    'final_benchmark_result': {k:results[-1][k] for k in ['timestamp','game','seq','sha256','snapshot']},
}
(ROOT/'workspace/final-summary-200.json').write_text(json.dumps(summary, indent=2)+'\n')
for key in ['overall','opponents','by_color','chronological_halves','equal_count_opponent_halves',
            'first_50_rated','last_50_rated','benchmark_plies','benchmark_own_moves',
            'benchmark_illegal_attempts','benchmark_illegals_by_game','benchmark_terminations',
            'practice','checks']:
    print(key, json.dumps(summary[key]))
