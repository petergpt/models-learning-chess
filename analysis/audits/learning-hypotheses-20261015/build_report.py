#!/usr/bin/env python3
"""Assemble reviewed findings into a standalone report; never touches learners."""
from pathlib import Path
import datetime as dt
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DEST = ROOT / 'deliverables'
PREFIX = 'chess-learning-hypotheses-20261015-v4'


def read(relative):
    return json.loads((HERE / relative).read_text())


def summary_test(test):
    return {k: v for k, v in test.items() if k not in ('early', 'late')} | {
        phase: {k: v for k, v in test[phase].items() if k != 'games'} for phase in ('early', 'late')}


def main():
    measurement = read('measurement/measurement_results.json')
    transfer = read('transfer/results.json')
    quality = read('quality/quality-results.json')
    match = read('quality/head-to-head.json')
    fairplay = read('fairplay/assessment.json')
    integrity = read('source-verification.json')
    labels = {
        'astra': ('GPT-6 Astra', 'Mostly Max; standard context'),
        'opus': ('Claude Opus 5.5', 'Max; native large context'),
        'sol': ('GPT-6.1 Sol', 'Max; standard context'),
        'sol-long': ('Sol · long context', 'Medium; 828K setting'),
        'sol-long-max': ('Sol · long context', 'Max; 828K setting'),
        'fable': ('Claude Fable 5.1', 'Max; native large context'),
    }
    readings = {
        'astra': ('negative', 'Recorded decline', 'Lower fresh-game scores and worse cached middlegame safety; study did not retain the early level.'),
        'opus': ('positive', 'Narrow improvement', 'Gain concentrated against Skill 0. Stronger endpoint window; broad-half change remains uncertain.'),
        'sol': ('uncertain', 'No clear gain', 'Temporary recoveries were not retained. Early and late balanced results are similar.'),
        'sol-long': ('negative', 'Recorded decline', 'Large observed fall; fewer independent blocks make inference more sensitive to assumptions.'),
        'sol-long-max': ('uncertain', 'No clear gain', 'Some recovery from a poor start; 41 rated games do not establish sustained improvement.'),
        'fable': ('uncertain', 'Small sample', 'Some better behavior and results in a short middle period; only three rotations per comparison period.'),
    }
    practice_notes = {
        'astra': 'Four of five wins started +8 to +12 material; one win began from the normal position.',
        'opus': 'One 30-move saved-position drill; most adaptation was review and procedure changes.',
        'sol': '160/181 sessions had ≤4 own moves; 179/181 used saved benchmark positions.',
        'sol-long': '58/94 had ≤4 own moves. The only win replayed an already-won continuation.',
        'sol-long-max': '25/36 had ≤4 own moves; no scored practice wins.',
        'fable': 'Longer initial-position practice, but only four sessions.'
    }
    opp_labels = {'skill-0': 'Skill 0', 'elo-1800-setting': '1800 setting', 'full-strength': 'Full strength'}
    runs = []
    for slug in labels:
        r = measurement['runs'][slug]
        tr = transfer['runs'][slug]
        primary = r['balanced']['tests']['combined-rated']
        early_range, late_range = r['balanced']['early_game_range'], r['balanced']['late_game_range']
        by_game = {p['game']: p for p in r['per_game_history']}
        table = r['rated_game_table']
        history = []
        for index, observation in enumerate(table):
            p = by_game[observation['game']]
            old = table[index-50] if index >= 50 else None
            history.append({
                'game': observation['game'], 'ratedCount': p['rated_count'],
                **{k: p['rolling'][k] for k in ('estimate', 'lower', 'upper')},
                'opponent': opp_labels[observation['opponent']], 'score': observation['score'],
                'windowGames': min(index+1, 50),
                'outgoing': {'game': old['game'], 'score': old['score'], 'opponent': opp_labels[old['opponent']]} if old else None})
        cumulative = [{'game': p['game'], 'estimate': p['cumulative']['estimate']}
                      for p in r['per_game_history'] if p['cumulative'] and p.get('complete')]
        pr = tr['practice']
        before_after = r['disjoint_first50_last50']
        if before_after:
            chart_note = (f"Disjoint endpoint check: first 50 rated Elo {before_after['early']['rating']['estimate']} → "
                          f"last 50 {before_after['late']['rating']['estimate']}. This is a different temporal contrast "
                          f"from the balanced half-run comparison above. All-rated cumulative estimate at the endpoint: "
                          f"{r['final_cumulative']['estimate']}.")
        else:
            chart_note = ('There are fewer than 100 rated games, so two disjoint 50-game rating windows do not exist. '
                          'Before 51 rated results, rolling and cumulative estimates coincide. An active game contributes no result.')
        tone, verdict, interpretation = readings[slug]
        runs.append({
            'id': slug, 'label': labels[slug][0], 'configuration': labels[slug][1],
            'n': r['scored_games'], 'nRated': r['rated_games'], 'activeGames': r['active_games'],
            'rating': r['final_rolling'], 'cumulativeRating': r['final_cumulative'],
            'tone': tone, 'verdict': verdict, 'interpretation': interpretation,
            'comparison': {
                'early': primary['early']['score_rate'], 'late': primary['late']['score_rate'],
                'nPerPhase': primary['early']['n'],
                'range': f"Games {early_range[0]}–{early_range[1]} vs {late_range[0]}–{late_range[1]}",
                'ci': [primary['bootstrap_delta_interval']['lower'], primary['bootstrap_delta_interval']['upper']],
                'p': primary['two_sided_p'], 'holmP': primary['holm_p'],
                'opponents': [{'label': opp_labels[op], 'early': x['early']['score_rate'],
                               'late': x['late']['score_rate'], 'n': x['early']['n']}
                              for op, x in r['balanced']['tests'].items() if op in ('skill-0', 'elo-1800-setting')]},
            'history': history, 'cumulative': cumulative, 'chartNote': chart_note,
            'practice': {'sessions': pr['started'], 'scored': pr['scored']['games'], 'stopped': pr['stopped'],
                         'medianMoves': pr['ownMoveLengths']['median'], 'note': practice_notes[slug],
                         'origins': pr['origins'], 'wins': pr['scored']['wins'], 'atMost4OwnMoves': pr['atMost4OwnMoves']},
            'behavior': {'early': tr['matchedHalves']['early']['behavior'], 'late': tr['matchedHalves']['late']['behavior']},
            'tests': {key: summary_test(value) for key, value in r['balanced']['tests'].items()},
            'endpointComparison': before_after,
            'qualityCoverage': quality['runs'][slug]['cache_games_matched'],
            'qualityComparisons': quality['runs'][slug]['comparisons'],
            'mechanicalWindowShifts': r['mechanical_window_shifts'],
        })
    D = {
        'generatedAt': dt.datetime.now(dt.timezone.utc).isoformat(),
        'lead': 'The records show real changes in performance, extensive attempts to adapt, and some improvement specific to this benchmark. They do not demonstrate sustained, general chess learning across the models. Elo alone blends those effects with noisy early estimates and a moving result window.',
        'metadata': 'Frozen snapshot: 15 October 2026, 22:09 UTC · 807 scored benchmark games · six runs · separate 30-game transfer check',
        'verdicts': [
            {'title': 'Some changes are real', 'text': 'Astra’s later scores fell against the same opponent settings and colors. This survives removing the inflated opening Elo peak.'},
            {'title': 'Improvement is narrow', 'text': 'Opus’s gain concentrates against Skill 0. It did not carry its higher Stockfish rating into the match against Astra.'},
            {'title': 'Metric awareness is visible', 'text': 'Agents deliberately prioritized rated games and favorable draws. Reviewed records show legal optimization, without evidence that falsified results caused the rise.'},
        ],
        'runs': runs,
        'tableNote': 'Intervals describe late-minus-early score differences from 100,000 resamples of complete six-game rotations, conditional on independent rotations within each period. Tests are exploratory: Holm adjustment across six run-level comparisons gives Astra p=0.017, long-context Medium p=0.054; other runs p≥0.986. Longer serial dependence weakens these inferences. The small Fable and Max samples cannot establish absence of learning.',
        'hypotheses': [
            {
                'title': '1. Early Elo peaks made ordinary estimation look like unlearning', 'tone': 'positive', 'verdict': 'Supported, but incomplete',
                'prediction': 'Very high early ratings should be based on few results with wide uncertainty. The early peak should be a poor baseline for measuring decline.',
                'test': 'Recomputed all 531 cached rating-history points and inspected sample sizes, posterior intervals and disjoint 50-rated-game windows.',
                'result': 'Astra’s 2430 after only three rated games had a 1660–3580 interval. Its first complete 50-game window was 1680, followed by 1400 in the final 50. Standard Sol’s comparable values were 1460→1390, much smaller than its early-peak fall. The no-games state has no measured Elo; 1500 is the prior center.',
                'limit': 'This explains inflated visual declines. It does not explain away Astra’s lower later scores or the long-context Medium decline.',
                'source': 'measurement/measurement_results.json; measurement/analyze_measurement.py; frozen .arena/rating.py:14–18,65–70'
            },
            {
                'title': '2. Window turnover can move Elo opposite to the latest result', 'tone': 'positive', 'verdict': 'Mechanically verified',
                'prediction': 'After 50 rated games, removing an older result can outweigh the new result’s effect; a loss could raise Elo and a win lower it.',
                'test': 'Recomputed each incoming/outgoing rated result pair from the frozen ledgers, and compared rolling with all-results cumulative estimates.',
                'result': 'Sol game 102 lost to the 1800 setting but rose 1440→1450 when its game-28 Skill 0 loss expired. Opus game 81 won against Skill 0 but fell 1490→1480 when its game-5 win against the 1800 setting expired. Full-strength games never move this Elo. Practice results never enter it.',
                'limit': 'The rating remains internally consistent. A slope is a change in a moving performance estimate, rather than a direct measurement of acquired skill.',
                'source': 'measurement/measurement_results.json → mechanical_examples and mechanical_window_shifts; Sol ledger lines8159–8301; Opus game81/5'
            },
            {
                'title': '3. Astra’s decline reflects poorer fresh-game performance', 'tone': 'negative', 'verdict': 'Supported observationally',
                'prediction': 'Scores should fall with opponent and color held equal, and an independent quality measure should show deterioration beyond the opening.',
                'test': 'Compared games1–96 with103–198, 64 rated games per period, using whole-rotation permutation/bootstrap. Reused the separate 200k-node position cache with opponent/color controls and equal game weights.',
                'result': 'Rated score fell 62.5%→39.1% (−23.4pp; rotation-bootstrap95% −35.9 to−10.2pp). Primary p=.0029, Holm6=.0172. In cached near-balanced positions, ≥200cp move losses rose4.09%→6.86%; six-game-block difference interval+1.29 to+4.31pp. First12-move controls show no clear decline, suggesting the main problem lies later in play.',
                'limit': 'Longer 24-game clusters give unadjusted p=.057, with only70 allocations. The recorded decline is substantial; a universal significance claim under arbitrary serial dependence is unwarranted. This does not identify its cause or imply changed model weights.',
                'source': 'measurement_results.json → astra.balanced; quality/quality-results.json → astra.comparisons.bounded_halves'
            },
            {
                'title': '4. Opus improved at this opponent pool more than at general tactics', 'tone': 'uncertain', 'verdict': 'Positive, narrow evidence',
                'prediction': 'If adaptation is opponent-specific, gains should concentrate in one setting and may lack consistent move-quality or cross-opponent support.',
                'test': 'Compared equal complete-rotation halves, separate opponent results, disjoint endpoint rating windows, existing cached quality, and the later match.',
                'result': 'Skill0 score rose65.6%→89.1%; nominal1800 stayed39.1%→39.1%. Combined score rose52.3%→64.1%, but its95% difference interval includes zero (−5.5 to+29.7pp). First50/last50 rated Elo rose1510→1760, with conditional difference interval+80 to+430. Cached balanced-position errors fell5.21%→4.20%, but the block interval includes no change. Astra subsequently won the direct match.',
                'limit': 'These results support narrow adaptation and a better late benchmark window, not proof that nothing was learned. The Skill0 p=.036 is exploratory and becomes .365 after adjusting12 opponent comparisons; the larger gain in endpoint windows shows sensitivity to the time contrast.',
                'source': 'measurement_results.json → opus.balanced and disjoint_first50_last50; quality/quality-results.json; quality/head-to-head.json'
            },
            {
                'title': '5. Practice repaired remembered cases without reliable transfer', 'tone': 'negative', 'verdict': 'Strong evidence of a weak transfer test',
                'prediction': 'Many drills should be short, selected from known failures, or start from favorable positions; the same error classes should recur in new games.',
                'test': 'Replayed practice and benchmark ledgers, counted origins and lengths, checked initial material, dated strategy declarations in pre-game snapshots, and examined later recorded mistakes.',
                'result': 'Standard Sol had181 sessions, median3 own moves;179 began from saved benchmark positions, and160 ended within4 own moves. All3 practice wins began+13 to+24 material in already-won source games. Long-context Medium’s only practice win began+25 and exactly replayed a known three-ply mate. Later benchmark games still contained blocked recaptures and checking forks. Astra’s literal-recapture trial improved briefly, then returned to its prior score in the following block.',
                'limit': 'Short drills and remembered examples can teach useful components. Their existence, wins or legality checks cannot establish transfer. Mental study outside recorded practice is not fully measured, and the data do not prove that these drills caused stagnation.',
                'source': 'transfer/results.json → practice and notes.strategyChanges; transfer/findings.md; Sol workspace/final_report_200.md'
            },
            {
                'title': '6. The agents knowingly optimized the published metric', 'tone': 'uncertain', 'verdict': 'Verified legal score optimization',
                'prediction': 'Notes should distinguish rated from unrated games, allocate effort accordingly, or prefer a draw when it improves expected benchmark score.',
                'test': 'Checked pre-game note snapshots, authored plans and accepted ledger outcomes; recalculated the rating with Opus game186 changed from a draw to a loss.',
                'result': 'Opus explicitly gave rated opponents more effort than full strength, and accepted a claimable threefold in game186 for its expected-score value. Fable also described prioritizing the rated opponents. These are legal competitive choices under this objective. Replacing the Opus draw with a loss changes its final Elo only1760→1750; it cannot explain the roughly250-point endpoint gain.',
                'limit': 'This is evidence of benchmark awareness and potentially narrow specialization. It does not establish hidden intent, invented strength or cheating. A valid draw is a chess result.',
                'source': 'Opus workspace/PLAN.md:3–7,46–47,69–73,318–320; GAMES.md:190; Fable workspace/README.md:7,13; fairplay/assessment.json'
            },
            {
                'title': '7. Tampering or hidden tactical code produced the gains', 'tone': 'uncertain', 'verdict': 'Not found in reviewed evidence',
                'prediction': 'There should be altered protected code, dropped measured results, changed opponent strength, scored practice contamination, or executable chess assistance.',
                'test': 'Verified all frozen hashes/chains and benchmark schedules; current pinned files all match. Recovered419 Opus/Fable note archives; reviewed helper history. Used the prior7658-call Opus review and newly screened2126 Fable calls, including171 nonroutine executions.',
                'result': 'No changed opponent settings, engine-error losses, illegal-move forfeits or corrupted result accounting explain the trends. Opus helpers render FENs, retrieve its own positions, submit moves and enforce timing. Reviewed actions contain no tactical search or engine advice. A separate Fable deviation is access to its own Claude memory outside workspace; higher-priority harness authorization is unresolved, with no demonstrated external chess assistance.',
                'limit': 'Tool-call coverage is deepest for Opus and Fable, not all six models. Shared-account logs and hashes cannot rule out unrecorded activity. The conclusion is bounded absence of evidence, rather than proof of perfect compliance.',
                'source': 'source-verification.json; fairplay/assessment.json; fairplay/mechanical-audit.json; fairplay/opus-helper-versions.json'
            },
            {
                'title': '8. Context growth, forgetting or reduced computation caused regression', 'tone': 'uncertain', 'verdict': 'Plausible; causality unresolved',
                'prediction': 'Decline should track context pressure, compaction or less reasoning, and disappear when those factors are controlled.',
                'test': 'Compared retained structured usage/context metadata from the frozen Astra audit with matched results; checked specific late errors against recorded prompt lengths. Reviewed the earlier same-prefix Sol effort audit.',
                'result': 'Astra’s recorded reasoning tokens per own move fell about52%, from1072 to513. Mean prompt input rose only13%; late backward-pawn and blocked-line errors occurred around47K–90K tokens in a258K window. Compaction also occurred in its stronger early phase. The earlier15-game Sol comparison showed Max using more reasoning than Medium while playing worse, with very small samples.',
                'limit': 'Compute allocation, notes, positions and study methods changed together. A large journal is not the same as a full prompt, and a reasoning-effort label is not a fixed token budget. No randomized context or compute ablation was run.',
                'source': '.operator/audits/astra-context-20261008/review.json; astra-learning-20261008/review.json; deliverables/sol-828k-investigation-20261006-1701.md'
            },
            {
                'title': '9. Stockfish Elo should predict a general chess ranking', 'tone': 'negative', 'verdict': 'The ranking did not transfer',
                'prediction': 'If the benchmark gap generalized directly, Opus’s1760 versus Astra’s1400 should predict the stronger player across opponent pools.',
                'test': 'Independently replayed all3115 public moves and verified the separate30-game match, with15 games of each color and all results retained.',
                'result': 'Astra won24.5–5.5:22 wins,5 draws,3 losses. It scored13/15 as White and11.5/15 as Black. Both used declared Max reasoning, their post200 contexts and copied notes; both could adapt between games. The published benchmark ordering reversed in this matchup.',
                'limit': 'A scalar rating depends on opponent pool and conditions. Nontransitive styles, continued adaptation and different contexts can explain a reversal. This does not establish that Opus exploited a bug, or that Astra learned more during its original run.',
                'source': 'quality/head-to-head.json; quality/public-match-events.json; Matches/Astra vs Opus - 30 games/MATCH-RULES.md:3,5,9,11'
            },
        ],
        'examples': [
            {'run': 'Astra', 'game': 'Trial25 → games175–198', 'title': 'A temporary local recovery did not persist',
             'target': 'Replace broad safety prose with literal final recaptures and actual blockers.',
             'observed': 'The declaration existed before game175. Rated points over two rotations went2.5/8 before the change,5.5/8 just after, then2.5/8 in the following two rotations.',
             'meaning': 'A favorable block can be a real observation without identifying the cause or showing retention. Other interventions overlapped.',
             'source': 'transfer/results.json → astra.notes.strategyChanges (Literal recaptures); pre175 snapshot c6b00963…'},
            {'run': 'Standard Sol', 'game': 'games199–200', 'title': 'The target error returned after extensive practice',
             'target': 'Track checking knight forks and verify the current board before calculating.',
             'observed': 'Game199 still lost a rook to a checking knight fork. Game200 submitted a queen path blocked by its own knight. The finished run ended1390 Elo, with no sustained matched-score gain.',
             'meaning': 'These are recorded execution failures, not a diagnosis of the model’s hidden reasoning. Writing the correct rule did not ensure it was applied.',
             'source': 'Chess - GPT-6.1-Sol/workspace/final_report_200.md; workspace/review199.md; review200.md; frozen benchmark ledger'},
            {'run': 'Long-context Medium Sol', 'game': 'practice89', 'title': 'A practice win reproduced an already-won line',
             'target': 'Practice conversion and rook safety using a saved benchmark position.',
             'observed': 'The drill started+25 in material from benchmark94 and repeated the exact known three-ply continuation to mate. It was the run’s only scored practice win.',
             'sequence': 'Rh1 b4 Rxh3#',
             'meaning': 'This demonstrates replay of a remembered favorable ending. It offers little evidence about an unfamiliar defensive or tactical position.',
             'source': 'transfer/results.json → sol-long.practice.records (89); benchmark94 ply61; frozen practice ledger'},
            {'run': 'Opus', 'game': 'game190', 'title': 'A benchmark win can coexist with a major oversight',
             'target': 'Verify destination safety and actual recaptures.',
             'observed': 'Opus checked with an unprotected queen, which the opposing king immediately captured. Opus later won the game against Skill0.',
             'meaning': 'Winning may reflect resilience and use of the opponent’s later mistakes. A win alone does not establish accurate tactics; weak-opponent score and move quality can diverge.',
             'source': 'Chess - Opus-5.5/workspace/ERRORS.md:888; frozen game190 plies48–49; fairplay/case-verification.json'},
        ],
        'match': {
            'astraPoints': match['astra_points'], 'opusPoints': match['opus_points'],
            'result': 'Astra:22 wins,5 draws,3 losses. Each player had15 games with White and15 with Black. All30 games were scored.',
            'conditions': 'Separate post200 match,6–10 October2026. Standard start; untimed; legality-only referee; no Stockfish. Post-training contexts/notes retained; reflection allowed between games. Declared Max for both; equal inference-token budgets were not imposed.',
            'interpretation': 'The final Stockfish-based estimates were Opus 1760 and Astra 1400. Astra’s 81.7% score in their direct match demonstrates that the benchmark gap did not generalize to this opponent. It strengthens the case for evaluating novel opponents before calling an Elo rise general chess learning.',
            'rawSummary': {k: v for k, v in match.items() if k != 'games'},
        },
        'nextTests': [
            {'title': 'Compare early and late memory on the same unseen positions',
             'text': 'Freeze early and late note snapshots. Evaluate the same model with each snapshot on a blinded, unfamiliar position set, in randomized order and with an equal decision-token budget. Keep corrections out of later test items. This directly tests whether the learned memory helps.'},
            {'title': 'Separate context pressure from the decision procedure',
             'text': 'Compare full history, fresh context plus the same concise notes, and fresh context without notes. Match positions, compute and retrieval access. Measure board-state mistakes as well as outcomes. This distinguishes harmful context accumulation from unhelpful procedural advice.'},
            {'title': 'Test practice on new examples and delayed retention',
             'text': 'After a declared drill, test different positions that require the same skill, then repeat a separate held-out set later. Include the opponent’s strongest reply and score the complete tactic. A remembered repair should not count as its own transfer test.'},
            {'title': 'Use a hidden, varied opponent pool',
             'text': 'Run a separate evaluation across engines and playing styles, paired openings/colors, and replicated learning runs. Predeclare evaluation windows; keep the hold-out scores hidden during study. This tests general strength and reduces incentives to optimize one weak-opponent distribution.'},
        ],
        'scope': 'The audit freezes807 scored benchmark games and all367 recorded practice starts across six runs; two benchmark games remain active and unscored. It independently checks source hashes, ledger chains, fixed opponents/colors/nodes, and replays accepted moves. The separate30-game match is also legally replayed. No new engine analysis or learner games were run, and no comparative findings were sent to the learners.',
        'limits': 'This is an observational audit, not a randomized learning experiment. The task changes an agent’s notes, context and procedures; it is not weight training. One trajectory per configuration cannot establish a model-wide learning ability or the causal effect of a particular intervention. Elo is nominal and engine-relative, not a calibrated human rating. Retrospective explanations use authored notes and structured metadata, never hidden reasoning transcripts.',
        'methods': [
            measurement['methods']['primary'], measurement['methods']['test'],
            'Score differences use100,000 within-phase resamples of complete six-game rotations. These assume independent rotations within a phase.12- and24-game cluster permutation sensitivities are retained in the evidence; inference weakens with fewer clusters. Lack of a small p value does not prove absence of learning.',
            'First50/last50 rated comparisons are nonoverlapping only where at least100 rated games exist. The50-game boundaries have slightly different opponent/color counts, so an additional equal-cell standardized score comparison is supplied. Bayesian rating-difference intervals are calculated from segment posteriors, not inferred from whether two separate rating intervals overlap.',
            'The independently implemented vectorized Davidson posterior matches four scalar reference cases and all531 cached historical points. Its prior is Normal(1500,800); nominal anchors1320/1800; draw propensity integrated over40 bins; rating grid10 Elo. Full-strength games and practice are excluded.',
            'Astra is labelled mostly Max because structured runtime metadata records a brief Medium interval affecting11 accepted own moves in game84. Its late comparison period was Max; that brief interval does not establish the cause of its sustained decline.',
            'Stockfish documents its Elo control as calibrated at120 seconds+1 second per move against CCRL40/4. These experiments instead use1,000,000 nodes per reply and fresh engine processes. The displayed intervals assume the nominal anchors and exclude their calibration error. Weak settings deliberately choose randomized suboptimal moves.',
            'Independent quality corroboration reuses453 existing200k-node cached games: Astra200, Opus189, Sol33, long-context Medium16, Fable15, long-context Max0. Cache move lists/actors/colors match the frozen ledgers. It lacks per-evaluation depth, timestamp and engine fingerprint; results are finite-search estimates. Whole-game averages are confounded by already-won/lost positions, so balanced-position and first12-own-move controls are included. No claim about late Sol/Fable quality is made from those short-prefix caches.',
            'Short-horizon material-loss counts are mechanical proxies and can include sacrifices; they are not certified blunders. Castling and repertoire changes demonstrate changed behavior rather than stronger play. Material advantages ignore king safety and positional compensation.',
            'Fair-play coverage: fresh verification of419 Opus/Fable archives and their helper versions; the prior Opus native tool audit screened7658 calls and reviewed284 nonroutine calls. New Fable screening covers2126 calls, with171 nonroutine execution skeletons reviewed. No hidden thinking blocks, memory contents or unrelated sessions were read. A Fable own-memory location/access deviation has unresolved harness authorization and is reported separately from tactical assistance.',
        ],
        'sources': [
            {'label': 'Frozen source manifest and integrity checks', 'path': '.operator/audits/learning-hypotheses-20261015/measurement/snapshots/manifest.json; source-verification.json', 'note': 'Capture2026-10-15T22:09:24Z; hashes identify exact endpoint and source ledgers.'},
            {'label': 'Recomputed ratings, tests and all trajectories', 'path': '.operator/audits/learning-hypotheses-20261015/measurement/measurement_results.json; analyze_measurement.py; measurement_conclusions.md'},
            {'label': 'Practice, mechanical behavior and pre-game note chronology', 'path': '.operator/audits/learning-hypotheses-20261015/transfer/results.json; assess_transfer.py; findings.md'},
            {'label': 'Independent cached-quality and complete match verification', 'path': '.operator/audits/learning-hypotheses-20261015/quality/quality-results.json; head-to-head.json; audit_quality.py'},
            {'label': 'Fair-play findings and review coverage', 'path': '.operator/audits/learning-hypotheses-20261015/fairplay/assessment.json; audit_fairplay.py; verify_cases.py'},
            {'label': 'Prior structured context and effort audits', 'path': '.operator/audits/astra-context-20261008/review.json; astra-learning-20261008/review.json; deliverables/sol-828k-investigation-20261006-1701.md', 'note': 'Retained as secondary evidence with its original scope/date; hidden reasoning not inspected.'},
            {'label': 'Stockfish UCI documentation', 'url': 'https://official-stockfish.github.io/docs/stockfish-wiki/UCI-Protocol-and-Stockfish-Commands.html', 'note': 'Official source for Elo-control calibration and randomized weaker play; checked15October2026.'},
            {'label': 'Stockfish FAQ', 'url': 'https://official-stockfish.github.io/docs/stockfish-wiki/Stockfish-FAQ.html', 'note': 'Official source describing intentional suboptimal move selection at weak settings.'},
        ],
        'footnote': 'Read-only retrospective analysis · source data through10October2026 · report15October2026',
        'provenance': integrity,
        'measurementMethods': measurement['methods'], 'qualityMethods': quality['method'],
        'fairPlayAssessment': fairplay,
        'sensitivityGame186': measurement['runs']['opus']['opus_game186_rating_sensitivity'],
    }
    # Normalize compact numeric prose without altering source paths or data keys.
    def readable(value):
        import re
        return re.sub(r'(?<=[A-Za-z’])(?=\d)', ' ', value)

    for key in ('scope', 'limits', 'footnote'):
        D[key] = readable(D[key])
    D['methods'] = [readable(text) for text in D['methods']]
    for item in D['hypotheses']:
        for key in ('prediction', 'test', 'result', 'limit'):
            item[key] = readable(item[key])
    for item in D['examples']:
        for key in ('target', 'observed', 'meaning'):
            item[key] = readable(item[key])
    for key in ('result', 'conditions', 'interpretation'):
        D['match'][key] = readable(D['match'][key])
    assert sum(r['n'] for r in runs) == 807
    assert sum(r['practice']['sessions'] for r in runs) == 367
    assert sum(r['nRated'] for r in runs) == 531
    assert all(len(r['history']) == r['nRated'] for r in runs)
    serialized = json.dumps(D, ensure_ascii=False, separators=(',', ':'), allow_nan=False).replace('</', '<\\/')
    template = (HERE / 'report-template.html').read_text()
    assert template.count('__EVIDENCE__') == 1
    html = template.replace('__EVIDENCE__', serialized)
    DEST.mkdir(exist_ok=True)
    (DEST / (PREFIX + '.html')).write_text(html)
    (DEST / (PREFIX + '.json')).write_text(json.dumps(D, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
    (HERE / 'report-data.json').write_text(json.dumps(D, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
    print(json.dumps({'html': str(DEST / (PREFIX + '.html')), 'json': str(DEST / (PREFIX + '.json')),
                      'bytes': len(html.encode()), 'runs': len(runs), 'checks': 'counts and JSON finite values passed'}, indent=2))


if __name__ == '__main__':
    main()
