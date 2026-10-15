#!/usr/bin/env python3
"""Read-only operator audit of existing evaluations and a public head-to-head.

No engine is launched; no learner files or experiment state are written.
Run through t3-job. Outputs are written next to this saved script.
"""
from __future__ import annotations

import collections
import hashlib
import json
import math
from pathlib import Path
import sqlite3
import sys

import numpy as np

ROOT = Path('/home/peter/Chess Learning')
OUT = Path(__file__).resolve().parent
SNAP = OUT.parent / 'measurement/snapshots'
CACHE = ROOT / '.operator/claude-review/evals'
ALIASES = {'astra': 'astra', 'opus': 'opus', 'sol': 'sol',
           'sol-long': 'solLC', 'sol-long-max': 'sol-long-max', 'fable': 'fable'}
REPS = 6000
RNG = np.random.default_rng(20261015)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2, allow_nan=False) + '\n')


def score_proxy(cp):
    """Bounded logistic display proxy, NOT a calibrated win probability."""
    return 100 / (1 + math.exp(-0.00368208 * max(-1500, min(1500, cp))))


def pct(v):
    return 100 * sum(v) / len(v) if v else None


def mean(v):
    return sum(v) / len(v) if v else None


def summaries(moves, score):
    own = [m for m in moves if m['actor'] == 'model']
    first = own[:12]
    balanced = [m for m in own if abs(m['before']) <= 200]
    balanced_first = [m for m in first if abs(m['before']) <= 200]
    middle = own[12:30]
    balanced_middle = [m for m in middle if abs(m['before']) <= 200]
    # 200cp threshold remains interpretable for a balanced-to-mate move;
    # no average over the arbitrary +/-10000 mate encoding is reported.
    bad = lambda m: m['before'] - m['after'] >= 200
    proxy_drop = lambda m: max(0, score_proxy(m['before']) - score_proxy(m['after']))
    return {
        'score_pct': 100 * score,
        'own_moves': len(own),
        'first12_moves': len(first),
        'balanced_move_share_pct': 100 * len(balanced) / len(own),
        'balanced_first12_move_share_pct': 100 * len(balanced_first) / len(first),
        'winning_before_move_share_pct': pct([m['before'] >= 500 for m in own]),
        'losing_before_move_share_pct': pct([m['before'] <= -500 for m in own]),
        'decided_before_move_share_pct': pct([abs(m['before']) >= 1000 for m in own]),
        'legacy_clipped_acpl': mean([max(0, max(-1000, min(1000, m['before']))
                                           - max(-1000, min(1000, m['after']))) for m in own]),
        'proxy_loss_pp': mean([proxy_drop(m) for m in own]),
        'proxy_severe_loss_pct': pct([proxy_drop(m) >= 30 for m in own]),
        'first12_proxy_loss_pp': mean([proxy_drop(m) for m in first]),
        'first12_200cp_loss_pct': pct([bad(m) for m in first]),
        'balanced_200cp_loss_pct': pct([bad(m) for m in balanced]),
        'balanced_first12_200cp_loss_pct': pct([bad(m) for m in balanced_first]),
        'first12_any_balanced_200cp_loss_pct': 100 * any(bad(m) for m in balanced_first),
        'balanced_proxy_loss_pp': mean([proxy_drop(m) for m in balanced]),
        'balanced_first12_proxy_loss_pp': mean([proxy_drop(m) for m in balanced_first]),
        'middle13_30_balanced_200cp_loss_pct': pct([bad(m) for m in balanced_middle]),
        'middle13_30_balanced_proxy_loss_pp': mean([proxy_drop(m) for m in balanced_middle]),
        'best_pv_match_pct': pct([m['best'] == m['uci'] for m in own]),
    }


METRICS = [
    'score_pct', 'own_moves', 'first12_moves',
    'balanced_move_share_pct', 'balanced_first12_move_share_pct',
    'winning_before_move_share_pct', 'losing_before_move_share_pct', 'decided_before_move_share_pct',
    'legacy_clipped_acpl', 'proxy_loss_pp', 'proxy_severe_loss_pct',
    'first12_proxy_loss_pp', 'first12_200cp_loss_pct',
    'balanced_200cp_loss_pct', 'balanced_first12_200cp_loss_pct',
    'first12_any_balanced_200cp_loss_pct',
    'balanced_proxy_loss_pp', 'balanced_first12_proxy_loss_pp', 'best_pv_match_pct',
    'middle13_30_balanced_200cp_loss_pct', 'middle13_30_balanced_proxy_loss_pp',
]


def aggregate(rows):
    return {
        'games': len(rows),
        'own_moves': sum(r['counts']['own'] for r in rows),
        'first12_moves': sum(r['counts']['first12'] for r in rows),
        'balanced_moves': sum(r['counts']['balanced'] for r in rows),
        'balanced_first12_moves': sum(r['counts']['balanced_first12'] for r in rows),
        'first12_short_games': [r['game'] for r in rows if r['counts']['first12'] < 12],
        'metrics_game_weighted': {k: mean([r['metrics'][k] for r in rows
                                          if r['metrics'][k] is not None]) for k in METRICS},
        'opponent_color_counts': dict(collections.Counter(r['label'] for r in rows)),
    }


def compare(rows, early_end, late_start):
    early = [r for r in rows if r['game'] <= early_end]
    late = [r for r in rows if r['game'] >= late_start]
    es = collections.defaultdict(list)
    ls = collections.defaultdict(list)
    for r in early:
        es[r['stratum']].append(r)
    for r in late:
        ls[r['stratum']].append(r)
    common = sorted(set(es) & set(ls))
    result = {'early_game_numbers': [r['game'] for r in early],
              'late_game_numbers': [r['game'] for r in late],
              'raw_early': aggregate(early), 'raw_late': aggregate(late),
              'matched_strata': [], 'matched_game_numbers': {'early': [], 'late': []},
              'metrics': {}}
    total = sum(len(es[s]) + len(ls[s]) for s in common)
    if not total:
        result['status'] = 'No overlapping opponent/color/config strata'
        return result
    for s in common:
        result['matched_strata'].append({'key': json.loads(s), 'early_n': len(es[s]),
                                         'late_n': len(ls[s]),
                                         'pooled_game_weight': (len(es[s])+len(ls[s]))/total})
        for group, data in [('early', es), ('late', ls)]:
            result['matched_game_numbers'][group].extend(r['game'] for r in data[s])
    minimum_cell = min(min(len(es[s]),len(ls[s])) for s in common)
    result['bootstrap_diagnostics'] = {
        'minimum_games_in_one_period_stratum': minimum_cell,
        'singleton_period_strata': sum(len(es[s])==1 or len(ls[s])==1 for s in common),
        'interpretation': ('Tiny cells: resampling can produce artificially narrow or zero-width intervals; descriptive only.'
                           if minimum_cell < 5 else
                           'Game-cluster intervals describe sampling variation conditional on these periods/configurations; serial dependence remains unmodeled.')}
    for k in METRICS:
        # Resample games, preserving all within-game move dependence. Fixed pooled
        # opponent/color/config weights standardize both halves to the same mix.
        eligible = []
        for s in common:
            a = np.asarray([r['metrics'][k] for r in es[s] if r['metrics'][k] is not None], dtype=float)
            b = np.asarray([r['metrics'][k] for r in ls[s] if r['metrics'][k] is not None], dtype=float)
            if len(a) and len(b):
                eligible.append((s, a, b))
        if not eligible:
            continue
        denom = sum(len(a)+len(b) for _, a, b in eligible)
        estimate_a = estimate_b = 0.
        boots_a = np.zeros(REPS)
        boots_b = np.zeros(REPS)
        for s, a, b in eligible:
            w = (len(a)+len(b)) / denom
            estimate_a += w * a.mean()
            estimate_b += w * b.mean()
            boots_a += w * a[RNG.integers(0, len(a), (REPS, len(a)))].mean(axis=1)
            boots_b += w * b[RNG.integers(0, len(b), (REPS, len(b)))].mean(axis=1)
        result['metrics'][k] = {
            'early': float(estimate_a), 'late': float(estimate_b),
            'late_minus_early': float(estimate_b-estimate_a),
            'early_ci95': np.quantile(boots_a, [.025, .975]).tolist(),
            'late_ci95': np.quantile(boots_b, [.025, .975]).tolist(),
            'delta_ci95': np.quantile(boots_b-boots_a, [.025, .975]).tolist(),
            'early_games': sum(len(a) for _, a, _ in eligible),
            'late_games': sum(len(b) for _, _, b in eligible),
        }
        if min(len(early),len(late)) >= 35:
            # Sensitivity to dependence across nearby games: resample fixed
            # six-game blocks, then reapply the same opponent/color weights.
            weights = np.asarray([(len(a)+len(b))/denom for _,a,b in eligible])
            block_estimates = []
            for data in [es,ls]:
                block_ids = sorted({(r['game']-1)//6 for s,_,_ in eligible for r in data[s]})
                lookup = {b:i for i,b in enumerate(block_ids)}
                sums = np.zeros((len(block_ids),len(eligible)))
                ns = np.zeros_like(sums)
                for j,(s,_,_) in enumerate(eligible):
                    for r in data[s]:
                        v=r['metrics'][k]
                        if v is not None:
                            i=lookup[(r['game']-1)//6]
                            sums[i,j] += v
                            ns[i,j] += 1
                ids = RNG.integers(0,len(block_ids),(REPS,len(block_ids)))
                bsums = sums[ids].sum(axis=1)
                bn = ns[ids].sum(axis=1)
                estimates = np.full(REPS,np.nan)
                valid = (bn > 0).all(axis=1)
                estimates[valid] = (bsums[valid]/bn[valid]*weights).sum(axis=1)
                block_estimates.append(estimates)
            delta = block_estimates[1]-block_estimates[0]
            valid_delta = delta[np.isfinite(delta)]
            result['metrics'][k]['six_game_block_delta_ci95'] = np.quantile(valid_delta,[.025,.975]).tolist()
            result['metrics'][k]['six_game_block_valid_replicates'] = len(valid_delta)
    return result


def audit_cache():
    run_output = {}
    all_rows = {}
    for slug, alias in ALIASES.items():
        source = SNAP / slug / 'data/ledger.jsonl'
        games = {}
        for line in source.read_text().splitlines():
            e = json.loads(line)
            n, kind = e.get('game'), e['kind']
            if kind == 'start':
                assert n not in games
                games[n] = {'start': e, 'moves': [], 'end': None}
            elif n in games and kind == 'move':
                games[n]['moves'].append(e)
            elif n in games and kind == 'result':
                games[n]['end'] = e
        rows, provenance, excluded = [], [], []
        for path in sorted(CACHE.glob(alias + '-*.json')):
            d = json.loads(path.read_text())
            n = d['game']
            g = games.get(n)
            if not g or not g['end'] or g['end'].get('score') is None:
                excluded.append({'file': path.name, 'reason': 'no completed frozen game'})
                continue
            raw = g['moves']
            err = []
            if [m['uci'] for m in d['moves']] != [m['uci'] for m in raw]:
                err.append('different move sequence')
            if [(m['actor'] == 'model') for m in d['moves']] != [(m['actor'] == 'model') for m in raw]:
                err.append('different actor sequence')
            if d['learnerWhite'] != (g['start']['color'] == 'white'):
                err.append('different learner color')
            if d['run'] != alias:
                err.append('different run alias')
            if g['start'].get('initial_fen') not in (None,'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
                err.append('cache lacks initial FEN for a nonstandard game')
            if any(a['after'] != -b['before'] for a,b in zip(d['moves'],d['moves'][1:])):
                err.append('discontinuous cached perspective/evaluation')
            if err:
                excluded.append({'file': path.name, 'reason': err})
                continue
            start = g['start']
            own = [m for m in d['moves'] if m['actor'] == 'model']
            row = {'game': n, 'opponent': start['opponent']['id'],
                   'color': start['color'], 'score': g['end']['score'],
                   'end_reason': g['end']['reason'],
                   'started': start['timestamp'], 'ended': g['end']['timestamp'],
                   'label': start['opponent']['id'] + '|' + start['color'],
                   'stratum': json.dumps({'opponent': start['opponent'],
                                          'color': start['color'],
                                          'nodes_per_move': start['nodes_per_move']}, sort_keys=True),
                   'counts': {'own': len(own), 'first12': len(own[:12]),
                              'balanced': sum(abs(m['before']) <= 200 for m in own),
                              'balanced_first12': sum(abs(m['before']) <= 200 for m in own[:12])},
                   'metrics': summaries(d['moves'], g['end']['score'])}
            rows.append(row)
            provenance.append({'file': path.name, 'sha256': sha(path),
                               'game': n, 'fields': sorted(d),
                               'moves': len(d['moves'])})
        completed = sorted(n for n,g in games.items() if g['end'] and g['end'].get('score') is not None)
        cached = sorted(r['game'] for r in rows)
        info = {'frozen_ledger_sha256': sha(source),
                'completed_games': len(completed), 'cache_games_matched': len(rows),
                'cache_game_numbers': cached,
                'completed_without_cache': sorted(set(completed)-set(cached)),
                'excluded_cache_files': excluded,
                'cache_files': provenance, 'all_cached': aggregate(rows), 'comparisons': {}}
        if rows:
            maximum = max(cached)
            early_end = maximum // 2
            for label, subset in [('all_halves', rows),
                                  ('bounded_halves', [r for r in rows if r['opponent'] != 'full-strength'])]:
                info['comparisons'][label] = compare(subset, early_end, early_end+1)
            third = maximum // 3
            info['comparisons']['bounded_first_last_third'] = compare(
                [r for r in rows if r['opponent'] != 'full-strength'], third, maximum-third+1)
            info['cache_ended_at'] = max(r['ended'] for r in rows)
        run_output[slug] = info
        all_rows[slug] = rows
    dump('game-quality.json', all_rows)
    return run_output


def public_match():
    folder = ROOT / 'Matches/Astra vs Opus - 30 games'
    source = folder / '.referee/match.sqlite'
    db = sqlite3.connect('file:' + str(source) + '?mode=ro', uri=True)
    db.row_factory = sqlite3.Row
    # Query only public games/moves/results and event count metadata. Never read
    # actions/requests or either player's match notes/native conversation.
    db.execute('BEGIN')
    rows = [dict(x) for x in db.execute('SELECT id,white,black,started,ended,result,reason,moves FROM games ORDER BY id')]
    counts = dict(db.execute('SELECT kind,count(*) FROM events GROUP BY kind'))
    illegal_public = [dict(x) for x in db.execute(
        "SELECT seq,at,game,actor,payload FROM events WHERE kind='illegal_submission' ORDER BY seq")]
    head = dict(db.execute('SELECT seq,at,kind,game,hash FROM events ORDER BY seq DESC LIMIT 1').fetchone())
    public_events = [dict(x) for x in db.execute("SELECT seq,at,kind,game,actor,payload,previous,hash FROM events WHERE kind IN ('game_started','move','game_ended') ORDER BY seq")]
    db.rollback()
    db.close()
    sys.path.insert(0, str(folder / '.referee/vendor'))
    import chess
    bycolor = collections.defaultdict(list)
    scores = []
    move_digest = hashlib.sha256()
    for r in rows:
        moves = json.loads(r.pop('moves'))
        board = chess.Board()
        for m in moves:
            actor = r['white'] if board.turn else r['black']
            assert m['actor'] == actor
            move = chess.Move.from_uci(m['uci'])
            assert move in board.legal_moves
            assert board.san(move) == m['san']
            board.push(move)
        r['plies'] = len(moves)
        r['final_fen'] = board.fen()
        r['all_moves_replayed_legally'] = True
        s_white = {'1-0': 1., '1/2-1/2': .5, '0-1': 0.}[r['result']]
        s = s_white if r['white'] == 'astra' else 1-s_white
        r['astra_score'] = s
        scores.append(s)
        bycolor['white' if r['white']=='astra' else 'black'].append(s)
        move_digest.update(json.dumps(moves, sort_keys=True).encode())
    # Game resampling describes this match's score variation; adaptation breaks
    # iid sampling, so do not claim this is a universal player-strength interval.
    a = np.asarray(scores)
    bs = a[RNG.integers(0, len(a), (REPS, len(a)))].mean(axis=1)
    protocol_path = folder / 'protocol.json'
    setup_path = folder / '.operator/setup.json'
    verification_path = folder / '.operator/launch-verification.json'
    protocol = json.loads(protocol_path.read_text())
    setup = json.loads(setup_path.read_text())
    verification = json.loads(verification_path.read_text())
    result = {
        'sources': {'database': str(source.relative_to(ROOT)), 'read_mode': 'SQLite mode=ro, single read transaction',
                    'public_moves_sha256': move_digest.hexdigest(), 'last_event': head,
                    'protocol_sha256': sha(protocol_path),
                    'rules_sha256': sha(folder/'MATCH-RULES.md'),
                    'setup_sha256': sha(setup_path), 'launch_verification_sha256': sha(verification_path)},
        'games': rows, 'completed_games': len(rows),
        'astra_points': sum(scores), 'opus_points': len(scores)-sum(scores),
        'astra_wins': scores.count(1.), 'draws': scores.count(.5), 'astra_losses': scores.count(0.),
        'astra_by_color': {k: {'games': len(v), 'points': sum(v), 'wins':v.count(1.),'draws':v.count(.5),'losses':v.count(0.)} for k,v in bycolor.items()},
        'astra_first15_points': sum(scores[:15]), 'astra_last15_points': sum(scores[15:]),
        'astra_score_fraction': float(a.mean()),
        'descriptive_game_bootstrap_score_ci95': np.quantile(bs,[.025,.975]).tolist(),
        'public_event_kind_counts': counts,
        'illegal_submissions_by_actor': dict(collections.Counter(x['actor'] for x in illegal_public)),
        'protocol_conditions': {k: protocol[k] for k in ['reasoning','context','learning','assistance','tools','timeControl','position','rating','isolation']},
        'declared_config': {k: {'model_selection':v['modelSelection'], 'runtime_evidence':v.get('runtimeEvidence')} for k,v in setup['players'].items()},
        'existing_effort_verification': {'checked_at':verification['checkedAt'],
            'players':{k:{x:v[x] for x in ['allNativeEffort','model','sourceGames','verifiedNativeMetadataEntries']} for k,v in verification['players'].items()},
            'note':'Existing verification was at game 25, not an independently repeated audit of all 30 native sessions.'},
        'limits': ['Not a frozen-policy transfer evaluation: carried-over post-200 conversations/workspaces and between-game adaptation were permitted.',
                   'Both declared Max effort; provider architectures/context differ and Max effort is not identical compute.',
                   'Astra beating Opus despite lower nominal Stockfish Elo challenges transitive general-strength interpretation, but cannot establish benchmark exploitation or learning causally.',
                   'No pretraining/before-200 head-to-head baseline; opponent-style/nontransitive effects remain plausible.',
                   'Only public move/result data and operator configuration were read; no private match notes or conversation contents were inspected.']}
    dump('public-match-events.json',public_events)
    dump('head-to-head.json', result)
    return result


def main():
    runs = audit_cache()
    match = public_match()
    output = {
        'analysis': 'Existing cache quality controls, no new chess engine analysis',
        'method': {
            'cache_source': str(CACHE.relative_to(ROOT)),
            'existing_review_script_sha256': sha(ROOT/'.operator/claude-review/engine_review.py'),
            'cache_claimed_nodes': 200000,
            'cache_claimed_engine': 'Stockfish 19 according to review script; cache lacks engine binary digest/version/depth/date and nodes fields.',
            'cache_match_validation': 'Exact whole-game UCI list, actor list, and learner color against frozen Oct15 ledgers.',
            'periods': 'Primary split at floor(last cached game number / 2); sensitivity compares first and last third. No uncached late games are assessed.',
            'strata': 'Exact opponent id/options, color, and nodes_per_move; only strata present in both periods.',
            'weights': 'Pooled game counts in overlapping strata, fixed for both periods; within stratum each game has equal weight.',
            'uncertainty': f'{REPS} stratified game bootstrap replicates; moves never treated as independent observations; six-game block sensitivity for comparisons with at least 35 games per period; seed 20261015.',
            'balanced': 'Before-move cached eval between -200 and +200cp inclusive, from mover perspective.',
            'first12': 'First 12 actual own moves of each game, including all shorter games with their actual opportunities. Count short games explicitly.',
            'severe_cp_loss': 'Before-after >=200cp on a single model move; balanced controls avoid arbitrary mate averages and lost-position saturation.',
            'proxy': '100/(1+exp(-0.00368208*clip(cp,-1500,1500))); a bounded display proxy, not calibrated win probability.',
            'legacy_acpl': 'Positive loss after clipping before and after separately to +/-1000cp; descriptive saturation-sensitive comparator only.',
            'limits': ['Posthoc observational comparisons are not randomized interventions.',
                       'Game clustering allows within-game dependence, not shared opening/serial dependence across games; intervals can be optimistic.',
                       'Balanced positions remain selected by previous play; first12 and any-error-per-game controls reduce but do not eliminate survivorship.',
                       '200k-node fixed-position cache is noisy, single-PV best-match is not a count of uniquely correct moves.',
                       'Existing analysis script does not clear the transposition table between games/positions; cached values can depend on earlier engine state.',
                       'Many metrics and periods examined; no multiplicity-corrected causal significance claims.',
                       'Small-prefix caches cannot test the completed runs: Sol33/200, Sol-long16/99, Fable15/45, Sol-long-max0/63.']},
        'runs': runs,
        'head_to_head_summary': {k: match[k] for k in ['astra_points','opus_points','astra_wins','draws','astra_losses','astra_by_color']},
    }
    dump('quality-results.json', output)
    # Concise log for parent, with full audit trail saved to JSON.
    for slug, r in runs.items():
        print(slug, f"coverage={r['cache_games_matched']}/{r['completed_games']}", flush=True)
        c = r['comparisons'].get('bounded_halves',{}).get('metrics',{})
        for k in ['legacy_clipped_acpl','first12_proxy_loss_pp','balanced_first12_200cp_loss_pct',
                  'first12_any_balanced_200cp_loss_pct','balanced_200cp_loss_pct']:
            if k in c:
                x=c[k]
                print(k, f"{x['early']:.3f} -> {x['late']:.3f}; delta={x['late_minus_early']:.3f}; CI={x['delta_ci95']}")
    print('public match',match['astra_points'],match['opus_points'],match['astra_by_color'])


if __name__ == '__main__':
    main()
