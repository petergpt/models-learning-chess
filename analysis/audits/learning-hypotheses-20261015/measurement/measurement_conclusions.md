Displayed Elo movement is a mixture of sample size, the last-50-game window, and observed chess performance. It is not, by itself, a measure of learning.

The frozen endpoint is 2026-10-15T22:09:24.019665+00:00; 807 completed scored benchmark games, 531 rated. All 36 snapshot files matched their manifest hashes. The vectorized rating calculation matched four independent scalar-reference cases and all 531 cached history points (median and both credible limits). Originals and experiments were not modified; no model or chess engine was run.

The displayed estimator uses nominal anchors1320/1800 and the most recent50 rated games. All full-strength games are excluded, including draws. Prior mean1500 is a reference prior, not an observed starting rating. Its95% intervals condition on nominal calibration and Davidson likelihood assumptions, and do not include anchor miscalibration. [Frozen rating definitions](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/sol/.arena/rating.py:13>) [Outcome filtering](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/sol/.arena/rating.py:56>) [Conditional uncertainty](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/sol/.arena/rating.py:77>) [Rolling window](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/sol/.arena/rating.py:85>)

The main comparison uses equal, disjoint sets of complete six-game rotations. Each rotation contains all three opponents in both colors. For200-game runs this is games1–96 versus103–198, with64 rated games per phase. One middle rotation and the incomplete tail are omitted. P values permute complete rotations; Holm adjustment covers all six combined-rated run comparisons. Score intervals are95% within-phase rotation-bootstrap intervals; they are descriptive and not multiplicity-adjusted.

| Run | Rated n/phase | Early score | Late score | Difference pp (95% bootstrap) | Raw p | Holm6 p |
|---|---:|---:|---:|---:|---:|---:|
| Fable | 12 | 50.00% | 66.67% | +16.67 [-16.67, 50.00] | 0.700000 | 1.000000 |
| Astra | 64 | 62.50% | 39.06% | -23.44 [-35.94, -10.16] | 0.002870 | 0.017220 |
| Sol | 64 | 42.19% | 39.84% | -2.34 [-17.97, 13.28] | 0.851456 | 1.000000 |
| Sol Long | 32 | 50.00% | 18.75% | -31.25 [-50.00, -14.06] | 0.010723 | 0.053613 |
| Sol Long Max | 20 | 25.00% | 30.00% | +5.00 [-10.00, 20.00] | 0.682540 | 1.000000 |
| Opus | 64 | 52.34% | 64.06% | +11.72 [-5.47, 29.69] | 0.246424 | 0.985695 |

Astra has evidence of observed deterioration under the six-game exchangeability assumption. Sol Long also deteriorates substantially, but its Holm-adjusted p=.0536 is just above .05. Sol, Max, and Fable have wide uncertainty about a time change; nonsignificance does not establish no learning. Opus's equal-half combined change is positive but uncertain.

Opus's half-to-half gain is concentrated in skill0:65.625%→89.0625%; 1800 score is39.0625% in both halves. The skill0 comparison has raw p=.03646, Holm12 p=.36460 across the12 rated-opponent comparisons. This supports a descriptive specialization hypothesis, not a firm claim of general learning. Astra skill0 falls93.75%→62.5% (raw p=.00038; Holm12=.00456). Sol skill0 falls73.4375%→57.8125% while its1800 score rises10.9375%→21.875%; neither per-opponent trend is significant after adjustment.

| Run | First50 score | Last50 score | First50 Elo | Last50 Elo | Posterior Elo difference95% interval | Standardized score difference pp (95% rotation-fragment bootstrap) |
|---|---:|---:|---:|---:|---:|---:|
| Astra | 62.0% | 35.0% | 1680 | 1400 | -280 [-450, -100] | -24.76 [-40.06, -9.13] |
| Sol | 42.0% | 34.0% | 1460 | 1390 | -70 [-240, 110] | -5.93 [-23.70, 12.10] |
| Opus | 47.0% | 67.0% | 1510 | 1760 | +250 [80, 430] | +21.47 [3.85, 40.06] |

These50-game windows are disjoint but contain26/24 versus24/26 games against skill0/1800. Standardized score gives equal weight to all four rated opponent/color cells. Opus improves in the endpoint comparison, while the equal-half comparison is less decisive; the choice of temporal contrast matters. Bayesian rating-difference intervals use separate segment Davidson fits and should not be confused with the cluster permutation tests. Sol Long and Max do not have100 rated games and therefore cannot support a disjoint first50/last50 comparison.

Initial peaks are particularly unreliable: Astra, Sol Long, and Opus reach2430 after just three rated wins (95% credible interval1660–3580); Sol reaches2210 after two rated wins (1370–3440). Later failure to sustain those near-perfect initial samples is enough to lower the rating without any change in ability. Shuffling complete rotations while holding every result fixed produces median early10-peak-to-final50 drops of590 Elo for Astra,630 for Sol,370 for Sol Long, and510 for Opus. This is an illustrative stationary reference, not a confirmatory p value. It does not remove Astra's or Long's independently observed score declines.

Concrete arithmetic examples isolate the rolling-window mechanism:

- Sol game102 scores0 against elo-1800-setting; rating moves1440→1450 because game28 (skill-0, score0) expires. [Incoming result](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/sol/data/ledger.jsonl:8301>) [Expiring result](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/sol/data/ledger.jsonl:2301>)
- Opus game81 scores1 against skill-0; rating moves1490→1480 because game5 (elo-1800-setting, score1) expires. [Incoming result](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/opus/data/ledger.jsonl:6267>) [Expiring result](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/opus/data/ledger.jsonl:304>)

| Run | Final rolling50 Elo (95% credible interval) | Cumulative Elo (all rated games) |
|---|---:|---:|
| Fable | 1590 [1430, 1750] | 1590 [1430, 1750] |
| Astra | 1400 [1270, 1520] | 1570 [1490, 1640] |
| Sol | 1390 [1270, 1520] | 1470 [1390, 1540] |
| Sol Long | 1330 [1190, 1450] | 1370 [1260, 1480] |
| Sol Long Max | 1280 [1120, 1420] | 1280 [1120, 1420] |
| Opus | 1760 [1640, 1890] | 1650 [1580, 1730] |

Opus game186 ends by legal threefold repetition. Replacing only that draw with a loss changes final rolling Elo1760→1750; excluding the game leaves the median1760 whether or not the window is refilled. This single draw cannot explain Opus's +250 endpoint Elo change. This is arithmetic sensitivity with other games fixed, not a causal policy counterfactual. [Game186 result](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/snapshots/opus/data/ledger.jsonl:13808>)

Serial dependence is a material limitation. Preserving pairs of consecutive rotations gives Astra raw p=.00886 and Long p=.02857; preserving four consecutive rotations gives .05714 and .33333 (only70 and6 possible allocations). These sensitivity p values are unadjusted. They reinforce the need to report observed deterioration separately from a causal claim or a universal significance statement. No full-strength wins occur:276 games produce0 wins,2 draws,274 losses; all are omitted from Elo. There is no evidence here of acquiring full-strength performance.

All results are observational, exploratory, and conditional on their measurement assumptions. Generalization, causal learning, or absence of learning requires frozen-policy evaluations on held-out openings/positions/opponent settings, preferably with randomized intervention or ablation. Elo movements alone cannot determine those questions.

Reproduction: `/home/peter/.local/bin/t3-job -- python3 /home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/analyze_measurement.py`. Machine-readable results: [measurement_results.json](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/measurement_results.json>). Per-game rolling and cumulative series: [measurement_chart_data.json](</home/peter/Chess Learning/.operator/audits/learning-hypotheses-20261015/measurement/measurement_chart_data.json>).
