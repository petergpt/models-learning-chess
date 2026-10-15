#!/usr/bin/env python3
"""Build compact chart data and source-cited measurement notes from audit JSON."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT/"measurement_results.json").read_text())
runs = data["runs"]
names = {"fable":"Fable", "astra":"Astra", "sol":"Sol", "sol-long":"Sol Long", "sol-long-max":"Sol Long Max", "opus":"Opus"}


def source(slug, name=".arena/rating.py", line=1, label=None):
    return f"[{label or name}](<{ROOT/'snapshots'/slug/name}:{line}>)"


def ci(d, scale=1, dp=1):
    return f"[{d['lower']*scale:.{dp}f}, {d['upper']*scale:.{dp}f}]"


out = [
    "Displayed Elo movement is a mixture of sample size, the last-50-game window, and observed chess performance. It is not, by itself, a measure of learning.",
    "",
    f"The frozen endpoint is {data['frozen_capture']}; {sum(r['scored_games'] for r in runs.values())} completed scored benchmark games, {sum(r['rated_games'] for r in runs.values())} rated. All {len(data['verified_files'])} snapshot files matched their manifest hashes. The vectorized rating calculation matched four independent scalar-reference cases and all {sum(r['cache_history_points_validated'] for r in runs.values())} cached history points (median and both credible limits). Originals and experiments were not modified; no model or chess engine was run.",
    "",
    "The displayed estimator uses nominal anchors1320/1800 and the most recent50 rated games. All full-strength games are excluded, including draws. Prior mean1500 is a reference prior, not an observed starting rating. Its95% intervals condition on nominal calibration and Davidson likelihood assumptions, and do not include anchor miscalibration. "+source("sol", line=13, label="Frozen rating definitions")+" "+source("sol", line=56, label="Outcome filtering")+" "+source("sol", line=77, label="Conditional uncertainty")+" "+source("sol", line=85, label="Rolling window"),
    "",
    "The main comparison uses equal, disjoint sets of complete six-game rotations. Each rotation contains all three opponents in both colors. For200-game runs this is games1–96 versus103–198, with64 rated games per phase. One middle rotation and the incomplete tail are omitted. P values permute complete rotations; Holm adjustment covers all six combined-rated run comparisons. Score intervals are95% within-phase rotation-bootstrap intervals; they are descriptive and not multiplicity-adjusted.",
    "",
    "| Run | Rated n/phase | Early score | Late score | Difference pp (95% bootstrap) | Raw p | Holm6 p |",
    "|---|---:|---:|---:|---:|---:|---:|",
]
for slug, r in runs.items():
    t = r["balanced"]["tests"]["combined-rated"]
    out.append(f"| {names[slug]} | {t['early']['n']} | {100*t['early']['score_rate']:.2f}% | {100*t['late']['score_rate']:.2f}% | {100*t['delta_score_rate']:+.2f} {ci(t['bootstrap_delta_interval'],100,2)} | {t['two_sided_p']:.6f} | {t['holm_p']:.6f} |")
out.extend([
    "",
    "Astra has evidence of observed deterioration under the six-game exchangeability assumption. Sol Long also deteriorates substantially, but its Holm-adjusted p=.0536 is just above .05. Sol, Max, and Fable have wide uncertainty about a time change; nonsignificance does not establish no learning. Opus's equal-half combined change is positive but uncertain.",
    "",
    "Opus's half-to-half gain is concentrated in skill0:65.625%→89.0625%; 1800 score is39.0625% in both halves. The skill0 comparison has raw p=.03646, Holm12 p=.36460 across the12 rated-opponent comparisons. This supports a descriptive specialization hypothesis, not a firm claim of general learning. Astra skill0 falls93.75%→62.5% (raw p=.00038; Holm12=.00456). Sol skill0 falls73.4375%→57.8125% while its1800 score rises10.9375%→21.875%; neither per-opponent trend is significant after adjustment.",
    "",
    "| Run | First50 score | Last50 score | First50 Elo | Last50 Elo | Posterior Elo difference95% interval | Standardized score difference pp (95% rotation-fragment bootstrap) |",
    "|---|---:|---:|---:|---:|---:|---:|",
])
for slug in ["astra", "sol", "opus"]:
    d = runs[slug]["disjoint_first50_last50"]
    out.append(f"| {names[slug]} | {100*d['early']['score_rate']:.1f}% | {100*d['late']['score_rate']:.1f}% | {d['early']['rating']['estimate']} | {d['late']['rating']['estimate']} | {d['rating_difference']['median']:+d} {ci(d['rating_difference'],1,0)} | {100*d['equal_cell_score_delta']:+.2f} {ci(d['equal_cell_score_delta_interval'],100,2)} |")
out.extend([
    "",
    "These50-game windows are disjoint but contain26/24 versus24/26 games against skill0/1800. Standardized score gives equal weight to all four rated opponent/color cells. Opus improves in the endpoint comparison, while the equal-half comparison is less decisive; the choice of temporal contrast matters. Bayesian rating-difference intervals use separate segment Davidson fits and should not be confused with the cluster permutation tests. Sol Long and Max do not have100 rated games and therefore cannot support a disjoint first50/last50 comparison.",
    "",
    "Initial peaks are particularly unreliable: Astra, Sol Long, and Opus reach2430 after just three rated wins (95% credible interval1660–3580); Sol reaches2210 after two rated wins (1370–3440). Later failure to sustain those near-perfect initial samples is enough to lower the rating without any change in ability. Shuffling complete rotations while holding every result fixed produces median early10-peak-to-final50 drops of590 Elo for Astra,630 for Sol,370 for Sol Long, and510 for Opus. This is an illustrative stationary reference, not a confirmatory p value. It does not remove Astra's or Long's independently observed score declines.",
    "",
    "Concrete arithmetic examples isolate the rolling-window mechanism:",
    "",
])
for slug, incoming_game in [("sol",102), ("opus",81)]:
    e = next(e for e in runs[slug]["mechanical_examples"] if e["incoming"]["game"] == incoming_game)
    incoming, outgoing = e["incoming"], e["outgoing"]
    out.append(f"- {names[slug]} game{incoming['game']} scores{incoming['score']} against {incoming['opponent']}; rating moves{e['before']['estimate']}→{e['after']['estimate']} because game{outgoing['game']} ({outgoing['opponent']}, score{outgoing['score']}) expires. "
               +source(slug,"data/ledger.jsonl",incoming["end_line"],"Incoming result")+" "+source(slug,"data/ledger.jsonl",outgoing["end_line"],"Expiring result"))
out.extend([
    "",
    "| Run | Final rolling50 Elo (95% credible interval) | Cumulative Elo (all rated games) |",
    "|---|---:|---:|",
])
for slug,r in runs.items():
    out.append(f"| {names[slug]} | {r['final_rolling']['estimate']} {ci(r['final_rolling'],1,0)} | {r['final_cumulative']['estimate']} {ci(r['final_cumulative'],1,0)} |")
out.extend([
    "",
    "Opus game186 ends by legal threefold repetition. Replacing only that draw with a loss changes final rolling Elo1760→1750; excluding the game leaves the median1760 whether or not the window is refilled. This single draw cannot explain Opus's +250 endpoint Elo change. This is arithmetic sensitivity with other games fixed, not a causal policy counterfactual. "+source("opus","data/ledger.jsonl",13808,"Game186 result"),
    "",
    "Serial dependence is a material limitation. Preserving pairs of consecutive rotations gives Astra raw p=.00886 and Long p=.02857; preserving four consecutive rotations gives .05714 and .33333 (only70 and6 possible allocations). These sensitivity p values are unadjusted. They reinforce the need to report observed deterioration separately from a causal claim or a universal significance statement. No full-strength wins occur:276 games produce0 wins,2 draws,274 losses; all are omitted from Elo. There is no evidence here of acquiring full-strength performance.",
    "",
    "All results are observational, exploratory, and conditional on their measurement assumptions. Generalization, causal learning, or absence of learning requires frozen-policy evaluations on held-out openings/positions/opponent settings, preferably with randomized intervention or ablation. Elo movements alone cannot determine those questions.",
    "",
    f"Reproduction: `/home/peter/.local/bin/t3-job -- python3 {ROOT/'analyze_measurement.py'}`. Machine-readable results: [measurement_results.json](<{ROOT/'measurement_results.json'}>). Per-game rolling and cumulative series: [measurement_chart_data.json](<{ROOT/'measurement_chart_data.json'}>).",
])
(ROOT/"measurement_conclusions.md").write_text("\n".join(out)+"\n")
chart = dict(frozen_capture=data["frozen_capture"], prior_reference=1500,
             rating_label="Nominal engine-relative Elo", no_data_value=None,
             note="Rolling and cumulative estimates describe observed results; cumulative is not itself a learning estimate.",
             runs={slug:dict(name=names[slug], scored_games=r["scored_games"], rated_games=r["rated_games"], history=r["per_game_history"],
                             balanced=r["balanced"], disjoint_first50_last50=r["disjoint_first50_last50"]) for slug,r in runs.items()})
(ROOT/"measurement_chart_data.json").write_text(json.dumps(chart,indent=2)+"\n")
print(f"Saved measurement_conclusions.md and measurement_chart_data.json; {sum(len(r['per_game_history']) for r in runs.values())} chart points")
