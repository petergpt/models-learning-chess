"""Read-only audit of the two Sol 828K runs. Never calls a learner or engine analysis."""
import bisect
import collections
import datetime as dt
import fcntl
import hashlib
import importlib.util
import json
import statistics
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/home/peter/Chess Learning')
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('readonly_features', ROOT / '.operator/learning-assessment/assess.py')
features = importlib.util.module_from_spec(spec)
spec.loader.exec_module(features)
spec = importlib.util.spec_from_file_location('readonly_rating', ROOT / 'Chess - GPT-6.1-Sol - Long Context - Max/.arena/rating.py')
rating = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rating)

RUNS = {
    'medium': ('Chess - GPT-6.1-Sol - Long Context', '/home/peter/.codex-t3/accounts/pro-vt/sessions/2026/10/04/rollout-2026-10-04T09-09-13-01a1062c-ad87-7810-a01f-7fb2815e2f3e.jsonl'),
    'max': ('Chess - GPT-6.1-Sol - Long Context - Max', '/home/peter/.codex-t3/accounts/pro-vt/sessions/2026/10/05/rollout-2026-10-05T21-49-43-01a10e0b-4ad1-75d2-9626-9c0df20c8bef.jsonl'),
    'standard-max': ('Chess - GPT-6.1-Sol', '/home/peter/.codex-t3/accounts/pro-vt/sessions/2026/10/03/rollout-2026-10-03T20-44-16-01a10382-a7c9-7a90-91bd-689af57a0ca1.jsonl'),
}


def timestamp(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00')).timestamp()


def digest(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def independent_rating(games):
    """Independent direct-probability Davidson implementation, unlike log-margin code."""
    import numpy as np
    observations = [(rating.ANCHORS[g['start']['opponent']['id']], g['end']['score'])
                    for g in games if g['end'] and g['end']['score'] is not None
                    and g['start']['opponent']['id'] in rating.ANCHORS][-rating.WINDOW:]
    grid = np.array(list(rating.RATINGS), dtype=float)
    draws = np.array(rating.DRAW_PROBABILITIES)[None, :]
    nu = 2 * draws / (1 - draws)
    likelihood = np.ones((len(grid), len(rating.DRAW_PROBABILITIES)))
    for anchor, score in observations:
        strength = 10 ** ((grid[:, None] - anchor) / 400)
        draw_term = nu * np.sqrt(strength)
        denominator = strength + 1 + draw_term
        numerator = strength if score == 1 else draw_term if score == .5 else 1
        likelihood *= numerator / denominator
    density = likelihood.mean(axis=1) * np.exp(-.5 * ((grid - rating.PRIOR_MEAN) / rating.PRIOR_SD) ** 2)
    density /= density.sum()
    cumulative = np.cumsum(density)
    quantiles = [int(grid[np.searchsorted(cumulative, q)]) for q in (.5, .025, .975)]
    return dict(zip(('estimate', 'lower', 'upper'), quantiles))


def native_metadata(path):
    contexts, settings, usages, occupancy, compacted = [], [], [], [], []
    with path.open() as handle:
        for line in handle:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            payload = row.get('payload') or {}
            kind, at = row.get('type'), row.get('timestamp')
            if kind == 'turn_context':
                contexts.append({'at': at, 'effort': payload.get('effort'), 'model': payload.get('model'),
                                 'cwd': payload.get('cwd'), 'turnId': payload.get('turn_id'),
                                 'collaborationEffort': (payload.get('collaboration_mode', {}).get('settings') or {}).get('reasoning_effort')})
            elif kind == 'token_usage_record':
                usages.append({'at': at, 'responseId': payload.get('response_id'), 'usage': payload.get('usage') or {}})
            elif kind == 'event_msg' and payload.get('type') == 'thread_settings_applied':
                applied = payload.get('thread_settings') or {}
                settings.append({'at': at, 'effort': applied.get('reasoning_effort'), 'model': applied.get('model'),
                                 'collaborationEffort': (applied.get('collaboration_mode', {}).get('settings') or {}).get('reasoning_effort')})
            elif kind == 'event_msg' and payload.get('type') == 'token_count' and payload.get('info'):
                info = payload['info']
                occupancy.append({'at': at, 'input': (info.get('last_token_usage') or {}).get('input_tokens'),
                                  'window': info.get('model_context_window')})
            elif kind == 'compacted':
                compacted.append(at)
    return {'contexts': contexts, 'settings': settings, 'usage': usages, 'occupancy': occupancy,
            'compactionTimes': compacted}


def range_usage(games, native):
    start, end = timestamp(games[0]['start']['timestamp']), timestamp(games[-1]['end']['timestamp'])
    usage = [u for u in native['usage'] if start <= timestamp(u['at']) <= end]
    fields = ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens')
    return {'apiResponses': len(usage), **{field: sum(u['usage'].get(field, 0) for u in usage) for field in fields},
            'scope': 'All provider responses between first benchmark start and final result, including intervening practice and notes.'}


def move_usage(games, native):
    """Match the final completed provider response before a move, not all work for a move."""
    usage = sorted(native['usage'], key=lambda u: timestamp(u['at']))
    times = [timestamp(u['at']) for u in usage]
    matches, missing = [], 0
    for game in games:
        for event in game['moves']:
            if event['actor'] != 'model':
                continue
            at = timestamp(event['timestamp'])
            i = bisect.bisect_right(times, at)
            nearby = [(abs(at - times[j]), usage[j]) for j in range(max(0, i - 2), min(len(times), i + 2))
                      if abs(at - times[j]) <= 1.75]
            if not nearby:
                missing += 1
                continue
            delta, record = min(nearby, key=lambda pair: pair[0])
            matches.append({'game': game['start']['game'], 'ply': event['ply'], 'san': event['san'],
                            'reasoningTokens': record['usage'].get('reasoning_output_tokens', 0),
                            'inputTokens': record['usage'].get('input_tokens', 0),
                            'deltaSeconds': delta, 'seconds': event.get('seconds')})
    return {'matched': len(matches), 'unmatched': missing,
            'medianReasoningTokens': statistics.median(x['reasoningTokens'] for x in matches) if matches else None,
            'meanReasoningTokens': statistics.mean(x['reasoningTokens'] for x in matches) if matches else None,
            'longestResponseTokens': max((x['reasoningTokens'] for x in matches), default=None),
            'matches': matches,
            'scope': 'Usage for the final completed provider response near each move; excludes earlier work for that decision.'}


def main():
    audit = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'runs': {}, 'equalRange': 15,
             'method': 'Read-only hashes, legal move replay, actual metadata, independent Elo calculation; no engine position analysis.'}
    for key, (name, log_name) in RUNS.items():
        folder = ROOT / name
        with (folder / 'data/.lock').open('rb') as lock:
            fcntl.flock(lock, fcntl.LOCK_SH)
            events, integrity = features.read_ledger(folder / 'data/ledger.jsonl')
            practice_events, practice_integrity = features.read_ledger(folder / 'data/practice/ledger.jsonl')
            cache = json.loads((folder / 'data/rating-cache.json').read_text())
        games, practices = features.group_games(events), features.group_games(practice_events)
        config = json.loads((folder / '.arena/config.json').read_text())
        for game in games:
            n = game['start']['game']
            assert game['start']['opponent'] == config['opponents'][((n - 1) // 2) % 3]
            assert game['start']['color'] == ('white' if n % 2 else 'black')
            assert game['start']['nodes_per_move'] == 1000000
            game['features'] = features.replay(game)
        for game in practices:
            features.replay(game)
        manifest = json.loads((folder / '.arena/manifest.json').read_text())
        actual = {path: digest(folder / path) for path in manifest}
        assert actual == manifest, f'Manifest mismatch in {key}'
        completed = [g for g in games if g['end'] and g['end']['score'] is not None]
        native = native_metadata(Path(log_name))
        expected = 'medium' if key == 'medium' else 'max'
        assert all(c['effort'] == expected and c['collaborationEffort'] == expected for c in native['contexts'])
        assert all(c['model'] == 'gpt-6.1-sol' and c['cwd'] == str(folder) for c in native['contexts'])
        result = {'folder': str(folder), 'manifestFilesChecked': len(manifest), 'manifest': actual,
                  'integrity': integrity, 'practiceIntegrity': practice_integrity,
                  'completed': len(completed), 'acceptedPlies': sum(len(g['moves']) for g in games),
                  'engineErrors': sum(e['kind'] == 'engine_error' for e in events),
                  'forfeits': sum(g['end']['reason'] == 'illegal_move_forfeit' for g in completed),
                  'actualEfforts': dict(collections.Counter(c['effort'] for c in native['contexts'])),
                  'appliedSettings': native['settings'], 'compactions': native['compactionTimes'],
                  'latestOccupancy': native['occupancy'][-1], 'currentRating': cache['rating'],
                  'practiceSessions': len(practices), 'practiceOwnMoves': sum(sum(e['actor'] == 'model' for e in g['moves']) for g in practices),
                  'ranges': {}}
        for cutoff in (6, 10, 12, 15, len(completed)):
            selected = [g for g in completed if g['start']['game'] <= cutoff]
            if not selected:
                continue
            independent = independent_rating(selected)
            observations = [{'anchor': rating.ANCHORS[g['start']['opponent']['id']], 'score': g['end']['score']}
                            for g in selected if g['start']['opponent']['id'] in rating.ANCHORS][-50:]
            actual_rating = rating.posterior(observations)
            assert all(independent[k] == actual_rating[k] for k in independent)
            cached_points = [p for p in cache['rating']['history'] if p['game'] <= cutoff]
            assert not cached_points or all(cached_points[-1][k] == independent[k] for k in independent)
            counts = {op: features.tally([g for g in selected if g['start']['opponent']['id'] == op]) for op in features.OPPONENTS}
            result['ranges'][str(cutoff)] = {'tally': features.tally(selected), 'byOpponent': counts,
                                            'rating': independent, 'ratedGames': len(observations),
                                            'behavior': features.behavior(selected), 'tokens': range_usage(selected, native)}
        matched = [g for g in completed if g['start']['game'] <= 15]
        result['matchedMoveUsage'] = move_usage(matched, native)
        first_result = timestamp(completed[0]['end']['timestamp'])
        before_first_result = [u for u in native['occupancy'] if timestamp(u['at']) <= first_result]
        result['firstGameInputTokenRange'] = [min(u['input'] for u in before_first_result), max(u['input'] for u in before_first_result)]
        result['matchedGames'] = [{'game': g['start']['game'], 'opponent': g['start']['opponent']['id'], 'color': g['start']['color'],
                                 'score': g['end']['score'], 'reason': g['end']['reason'], 'plies': len(g['moves']),
                                 'finalMaterial': g['features']['finalMaterial'], 'illegal': g['features']['illegal'],
                                 'lastMoves': ' '.join(e['san'] for e in g['moves'][-8:]),
                                 'shortLosses': g['features']['shortLosses'], 'fen': g['moves'][-1]['fen']}
                                for g in matched]
        audit['runs'][key] = result
        print(json.dumps({'run': key, 'completed': result['completed'], 'efforts': result['actualEfforts'],
                          'manifestFilesChecked': result['manifestFilesChecked'], 'engineErrors': result['engineErrors'],
                          'forfeits': result['forfeits'], 'first15': result['ranges']['15'],
                          'medianFinalResponseReasoning': result['matchedMoveUsage']['medianReasoningTokens'],
                          'meanFinalResponseReasoning': result['matchedMoveUsage']['meanReasoningTokens'],
                          'matchedMoves': result['matchedMoveUsage']['matched'],
                          'firstGameInputTokenRange': result['firstGameInputTokenRange'],
                          'latestOccupancy': result['latestOccupancy']}))
    medium, maximum = audit['runs']['medium'], audit['runs']['max']
    audit['identicalMeasurementFiles'] = [key for key, value in medium['manifest'].items()
                                        if value == maximum['manifest'].get(key)]
    assert all(key in audit['identicalMeasurementFiles'] for key in ('.arena/arena.py', '.arena/config.json', '.arena/rating.py', '.arena/stockfish/stockfish/stockfish-linux-x86-64-universal'))
    (HERE / 'audit.json').write_text(json.dumps(audit, indent=2) + '\n')


if __name__ == '__main__':
    main()
