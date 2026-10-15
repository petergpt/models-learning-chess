#!/usr/bin/env python3
"""Read frozen chess ledgers; reproduce ratings and compare disjoint rotations.

No chess engine, model, live experiment, or original ledger is modified.
Run with: /home/peter/.local/bin/t3-job -- python3 <this-file>
"""
from __future__ import annotations

import collections
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
SNAPS = ROOT / "snapshots"
SLUGS = ["fable", "astra", "sol", "sol-long", "sol-long-max", "opus"]
ANCHORS = {"skill-0": 1320, "elo-1800-setting": 1800}
CELLS = [(o, c) for o in ["full-strength", "skill-0", "elo-1800-setting"] for c in ["white", "black"]]
RGRID = np.arange(-2500, 6501, 10, dtype=float)
DRAW = (np.arange(40) + .5) / 40
LOGNU = np.log(2 * DRAW / (1 - DRAW))
PRIOR = -.5 * ((RGRID - 1500) / 800) ** 2
LOGPROBS = []
for anchor in ANCHORS.values():
    margin = math.log(10) * (RGRID[:, None] - anchor) / 800
    den = np.logaddexp(np.logaddexp(margin, -margin), LOGNU[None, :])
    LOGPROBS.extend([-margin-den, LOGNU[None, :]-den, margin-den])
LOGPROBS = np.stack(LOGPROBS, axis=0)
POST_CACHE = {}
SEED = 20261015
N_PERM = 200_000
N_BOOT = 100_000
N_REFERENCE = 5_000


def counts_of(games):
    counts = [0] * 6
    for g in games:
        if g["opponent"] in ANCHORS:
            offset = 3 * list(ANCHORS).index(g["opponent"])
            counts[offset + {0: 0, .5: 1, 1: 2}[g["score"]]] += 1
    return tuple(counts)


def distribution(counts):
    if counts not in POST_CACHE:
        d = np.einsum("i,ijk->jk", np.array(counts), LOGPROBS, optimize=False)
        top = d.max(axis=1)
        lp = PRIOR + top + np.log(np.exp(d-top[:, None]).sum(axis=1)) - math.log(40)
        prob = np.exp(lp-lp.max())
        prob /= prob.sum()
        POST_CACHE[counts] = prob
    return POST_CACHE[counts]


def post(games):
    prob = distribution(counts_of(games))
    qs = np.searchsorted(np.cumsum(prob), [.025, .5, .975])
    return dict(estimate=int(RGRID[qs[1]]), lower=int(RGRID[qs[0]]), upper=int(RGRID[qs[2]]),
                grid_edge_mass=float(prob[:5].sum()+prob[-5:].sum()))


def posterior_difference(early, late):
    # P(late_rating - early_rating) from two independently fitted segment posteriors.
    pe, pl = distribution(counts_of(early)), distribution(counts_of(late))
    pd = np.convolve(pl, pe[::-1])
    dg = np.arange(-(len(RGRID)-1), len(RGRID)) * 10
    qs = np.searchsorted(np.cumsum(pd), [.025, .5, .975])
    return dict(median=int(dg[qs[1]]), lower=int(dg[qs[0]]), upper=int(dg[qs[2]]),
                probability_positive=float(pd[dg > 0].sum()),
                interval_type="95% equal-tail Bayesian posterior difference; conditional on nominal anchors and segment Davidson models")


def describe(games):
    scores = [g["score"] for g in games]
    return dict(n=len(scores), wins=scores.count(1), draws=scores.count(.5), losses=scores.count(0),
                points=sum(scores), score_rate=sum(scores)/len(scores) if scores else None,
                games=[g["game"] for g in games], rating=post(games) if any(g["opponent"] in ANCHORS for g in games) else None)


def bootstrap_difference(early_vectors, late_vectors, rng):
    """Within-phase bootstrap resampling entire six-game rotations."""
    ne, nl = len(early_vectors), len(late_vectors)
    de = early_vectors[rng.integers(ne, size=(N_BOOT, ne))].mean(axis=1)
    dl = late_vectors[rng.integers(nl, size=(N_BOOT, nl))].mean(axis=1)
    q = np.quantile(dl-de, [.025, .975])
    return dict(lower=float(q[0]), upper=float(q[1]), replicates=N_BOOT,
                interval_type="95% percentile bootstrap of within-phase complete rotation means; descriptive")


def perm_test(early_vectors, late_vectors, rng):
    # Clusters are complete rotations. A vector here is the within-rotation
    # average score for a fixed, balanced set of opponent/color cells.
    values = np.concatenate((early_vectors, late_vectors))
    k, n = len(early_vectors), len(early_vectors)+len(late_vectors)
    actual = float(late_vectors.mean()-early_vectors.mean())
    total = values.sum()
    combinations = math.comb(n, k)
    threshold = abs(actual)-1e-12
    if combinations <= 200_000:
        stats = np.array([(total-values[list(ix)].sum())/(n-k)-values[list(ix)].sum()/k
                          for ix in itertools.combinations(range(n), k)])
        p = float((np.abs(stats) >= threshold).mean())
        method, count, se = "exact enumeration", len(stats), 0.
    else:
        # Independent uniform k-subsets from random ranks. Batched to bound RAM.
        extreme, count = 0, N_PERM
        for start in range(0, count, 5000):
            size = min(5000, count-start)
            ix = np.argpartition(rng.random((size, n)), k-1, axis=1)[:, :k]
            early_sum = values[ix].sum(axis=1)
            stats = (total-early_sum)/(n-k)-early_sum/k
            extreme += int((np.abs(stats) >= threshold).sum())
        p = (1+extreme)/(1+count)
        method, se = "Monte Carlo plus-one estimate", math.sqrt(p*(1-p)/count)
    return dict(delta_score_rate=actual, two_sided_p=p, method=method, permutations=count,
                possible_allocations=combinations, monte_carlo_standard_error=se,
                null="Selected complete six-game rotation vectors are exchangeable in time; no systematic early/late score shift")


def holm(items, source="two_sided_p", output="holm_p"):
    # items are mutable dicts, adjustment monotone in ordered p.
    order = sorted(items, key=lambda x: x[source])
    running = 0.
    for i, item in enumerate(order):
        running = max(running, min(1., (len(order)-i)*item[source]))
        item[output] = running


def window_comparison(early, late, label):
    return dict(label=label, early=describe(early), late=describe(late),
                raw_score_delta=describe(late)["score_rate"]-describe(early)["score_rate"],
                rating_difference=posterior_difference(early, late),
                by_opponent={o: dict(early=describe([g for g in early if g["opponent"] == o]),
                                     late=describe([g for g in late if g["opponent"] == o]))
                             for o in ANCHORS})


def disjoint_cell_bootstrap(early, late, rng):
    """Resample whole observed rotation fragments; standardize opponent/color."""
    phase_values = []
    for phase in [early, late]:
        rot_ids = sorted({(g["game"]-1)//6 for g in phase})
        sums = np.zeros((len(rot_ids), 4))
        nums = np.zeros((len(rot_ids), 4))
        rated_cells = [(o,c) for o in ANCHORS for c in ["white", "black"]]
        for g in phase:
            i = rot_ids.index((g["game"]-1)//6)
            j = rated_cells.index((g["opponent"],g["color"]))
            sums[i,j] += g["score"]
            nums[i,j] += 1
        ix = rng.integers(len(rot_ids), size=(N_BOOT, len(rot_ids)))
        ss, nn = sums[ix].sum(axis=1), nums[ix].sum(axis=1)
        valid = (nn > 0).all(axis=1)
        assert valid.all()
        phase_values.append((ss/nn).mean(axis=1))
    q = np.quantile(phase_values[1]-phase_values[0], [.025, .975])
    return dict(lower=float(q[0]), upper=float(q[1]), replicates=N_BOOT,
                interval_type="95% percentile within-phase bootstrap of observed rotation fragments; equal opponent/color cell weights")


def load_games(slug):
    games = {}
    path = SNAPS / slug / "data/ledger.jsonl"
    for line, text in enumerate(path.read_text().splitlines(), 1):
        row = json.loads(text)
        if row["kind"] == "start":
            games[row["game"]] = dict(game=row["game"], color=row["color"], opponent=row["opponent"]["id"],
                                      start_line=line, start_timestamp=row["timestamp"], snapshot=row.get("snapshot"),
                                      start_sha256=row["sha256"], end=None)
        elif row["kind"] == "result":
            g = games[row["game"]]
            g.update(end=row, score=row["score"], end_line=line, timestamp=row["timestamp"],
                     reason=row["reason"], result_sha256=row["sha256"])
    return games


def random_order_reference(rotations, actual_rated, rng):
    # Illustrative stationary reference: reshuffle complete rotations, keeping
    # their four rated results together, then compare early-10 maximum to final50.
    rated_rotations = [[g for g in r if g["opponent"] in ANCHORS] for r in rotations]
    actual_complete = [g for r in rated_rotations for g in r]
    if len(actual_complete) < 50:
        return None
    actual_early = max(post(actual_complete[:i])["estimate"] for i in range(1, min(10, len(actual_complete))+1))
    actual_final = post(actual_complete[-50:])["estimate"]
    observed = actual_early-actual_final
    drops = []
    for _ in range(N_REFERENCE):
        seq = [g for j in rng.permutation(len(rotations)) for g in rated_rotations[j]]
        early = max(post(seq[:i])["estimate"] for i in range(1, min(10, len(seq))+1))
        final = post(seq[-50:])["estimate"]
        drops.append(early-final)
    q = np.quantile(drops, [.025, .5, .975])
    return dict(early_rated_horizon=10, complete_rotation_games=len(actual_complete),
                observed_early_peak=actual_early, observed_final=actual_final, observed_drop=observed,
                reshuffled_drop_95_percent_range=[float(q[0]), float(q[2])], reshuffled_median_drop=float(q[1]),
                fraction_at_least_observed=float(np.mean(np.array(drops) >= observed)), permutations=N_REFERENCE,
                interpretation="Illustrative stationary random-order reference, not a confirmatory p value; early horizon chosen for interpreting visible initial peaks; correlations inside each rotation retained")


def analyze_run(slug, rng):
    by_game = load_games(slug)
    games = [g for g in by_game.values() if g["end"] and g["score"] is not None]
    rated = [g for g in games if g["opponent"] in ANCHORS]
    rotations = []
    for i in range(0, max(by_game), 6):
        rs = [by_game.get(j) for j in range(i+1, i+7)]
        if not all(g and g["end"] and g["score"] is not None for g in rs):
            continue
        assert [(g["opponent"], g["color"]) for g in rs] == CELLS
        rotations.append(rs)
    # Every plotted point uses only completed observations available at that game.
    chart, rated_so_far = [dict(game=0, rated_count=0, rolling=None, cumulative=None)], []
    for g in by_game.values():
        if g["end"] and g["score"] is not None and g["opponent"] in ANCHORS:
            rated_so_far.append(g)
        chart.append(dict(game=g["game"], timestamp=g.get("timestamp", g["start_timestamp"]),
                          complete=bool(g["end"]), rated_count=len(rated_so_far),
                          rolling=post(rated_so_far[-50:]) if rated_so_far else None,
                          cumulative=post(rated_so_far) if rated_so_far else None))
    cache = json.loads((SNAPS/slug/"data/rating-cache.json").read_text())["rating"]
    differences = []
    for p in cache["history"]:
        ours = next(x for x in chart if x["game"] == p["game"])["rolling"]
        if any(ours[k] != p[k] for k in ["estimate", "lower", "upper"]):
            differences.append(dict(game=p["game"], cache=p, recomputed=ours))
    assert not differences, (slug, differences)

    half = len(rotations)//2
    early_rot, late_rot = rotations[:half], rotations[-half:]
    early, late = [g for r in early_rot for g in r], [g for r in late_rot for g in r]
    balanced = dict(complete_rotations=len(rotations), rotations_each_phase=half,
                    early_game_range=[early[0]["game"], early[-1]["game"]],
                    late_game_range=[late[0]["game"], late[-1]["game"]],
                    omitted_middle_rotations=[r[0]["game"]//6+1 for r in rotations[half:len(rotations)-half]],
                    omitted_incomplete_rotation_games=[g["game"] for g in games if not any(g in r for r in rotations)],
                    tests={})
    for opponent in ["combined-rated", "full-strength", "skill-0", "elo-1800-setting"]:
        filt = lambda g: g["opponent"] in ANCHORS if opponent == "combined-rated" else g["opponent"] == opponent
        eg, lg = [g for g in early if filt(g)], [g for g in late if filt(g)]
        er = np.array([np.mean([g["score"] for g in r if filt(g)]) for r in early_rot])
        lr = np.array([np.mean([g["score"] for g in r if filt(g)]) for r in late_rot])
        test = perm_test(er, lr, rng)
        test.update(early=describe(eg), late=describe(lg), bootstrap_delta_interval=bootstrap_difference(er, lr, rng))
        if opponent == "combined-rated":
            test["serial_cluster_sensitivity"] = {}
            for block_rotations in [2, 4]:
                if half % block_rotations == 0:
                    larger = perm_test(er.reshape(-1, block_rotations).mean(axis=1),
                                       lr.reshape(-1, block_rotations).mean(axis=1),
                                       np.random.default_rng(SEED+2000+100*SLUGS.index(slug)+block_rotations))
                    larger["block_rotations"] = block_rotations
                    larger["games_per_cluster"] = 6*block_rotations
                    larger["note"] = "Exploratory unadjusted sensitivity to preserving longer consecutive dependence; assumes exchangeability of these larger clusters"
                    test["serial_cluster_sensitivity"][str(block_rotations)] = larger
        if opponent != "full-strength":
            test["rating_difference"] = posterior_difference(eg, lg)
        balanced["tests"][opponent] = test

    disjoint = window_comparison(rated[:50], rated[-50:], "First 50 vs last 50 rated games; disjoint, slight opponent-composition difference") if len(rated) >= 100 else None
    if disjoint:
        for phase_name, phase in [("early", rated[:50]), ("late", rated[-50:])]:
            cells = {(o, c): [g["score"] for g in phase if (g["opponent"], g["color"]) == (o,c)] for o in ANCHORS for c in ["white", "black"]}
            disjoint[phase_name]["equal_cell_score_rate"] = float(np.mean([np.mean(v) for v in cells.values()]))
            disjoint[phase_name]["cell_n"] = {f"{o}/{c}": len(v) for (o,c),v in cells.items()}
        disjoint["equal_cell_score_delta"] = disjoint["late"]["equal_cell_score_rate"]-disjoint["early"]["equal_cell_score_rate"]
        disjoint["equal_cell_score_delta_interval"] = disjoint_cell_bootstrap(
            rated[:50], rated[-50:], np.random.default_rng(SEED+1000+SLUGS.index(slug)))

    # All mechanical window changes retained, and a few concretely decomposed.
    shifts = []
    for i in range(50, len(rated)):
        prev = rated[i-50:i]
        new = rated[i-49:i+1]
        before, after = post(prev), post(new)
        shifts.append(dict(incoming=rated[i], outgoing=rated[i-50], before=before, after=after,
                           delta=after["estimate"]-before["estimate"]))
    candidates = []
    for condition in [lambda s:s["incoming"]["score"] == 0 and s["delta"] > 0,
                      lambda s:s["incoming"]["score"] == 1 and s["delta"] < 0,
                      lambda s:True]:
        eligible = sorted([s for s in shifts if condition(s)], key=lambda s:abs(s["delta"]), reverse=True)
        for s in eligible[:2]:
            if s not in candidates:
                candidates.append(s)
    for s in candidates:
        i = rated.index(s["incoming"])
        prev = rated[i-50:i]
        removed = post(prev[1:])["estimate"]
        added = post(prev+[rated[i]])["estimate"]
        before, after = s["before"]["estimate"], s["after"]["estimate"]
        s["shapley_elo_change"] = dict(outgoing_expiry=.5*((removed-before)+(after-added)),
                                        incoming_result=.5*((added-before)+(after-removed)),
                                        note="Average of add-first/remove-first decompositions; median-grid rounding in 10 Elo units")
    result = dict(slug=slug, started_games=len(by_game), scored_games=len(games), rated_games=len(rated),
                active_games=[g["game"] for g in by_game.values() if not g["end"]],
                cache_history_points_validated=len(cache["history"]), cache_rating_matches=True,
                final_rolling=post(rated[-50:]), final_cumulative=post(rated),
                by_opponent={o:describe([g for g in games if g["opponent"] == o]) for o in ["full-strength", *ANCHORS]},
                balanced=balanced, disjoint_first50_last50=disjoint,
                per_game_history=chart, rated_game_table=rated,
                mechanical_window_shifts=[dict(incoming_game=s["incoming"]["game"], incoming_score=s["incoming"]["score"], incoming_opponent=s["incoming"]["opponent"],
                                               outgoing_game=s["outgoing"]["game"], outgoing_score=s["outgoing"]["score"], outgoing_opponent=s["outgoing"]["opponent"],
                                               delta=s["delta"], before=s["before"]["estimate"], after=s["after"]["estimate"]) for s in shifts],
                mechanical_examples=candidates, stationary_random_order_reference=random_order_reference(rotations, rated, rng))
    if slug == "opus":
        actual50 = rated[-50:]
        target = next(g for g in actual50 if g["game"] == 186)
        assert target["score"] == .5
        as_loss = [dict(g, score=0) if g["game"] == 186 else g for g in actual50]
        no_refill = [g for g in actual50 if g["game"] != 186]
        refill = [g for g in rated if g["game"] != 186][-50:]
        result["opus_game186_rating_sensitivity"] = dict(
            actual=post(actual50), draw_replaced_by_loss=post(as_loss),
            game_excluded_without_refill=post(no_refill), game_excluded_with_window_refill=post(refill),
            actual_game=target, note="Arithmetic sensitivity, holding every other observed game fixed; not a simulated alternative policy or causal estimate")
    return result


def main():
    manifest = json.loads((SNAPS/"manifest.json").read_text())
    verification = []
    for slug in SLUGS:
        for name, meta in manifest["runs"][slug]["files"].items():
            actual = hashlib.sha256((SNAPS/slug/name).read_bytes()).hexdigest()
            assert actual == meta["sha256"], (slug, name, actual)
            verification.append(dict(slug=slug, file=name, sha256=actual))
    # Check against original scalar implementation, loaded without writing pycache.
    ns = {}
    exec(compile((SNAPS/"sol/.arena/rating.py").read_text(), "frozen-rating.py", "exec"), ns)
    validation_windows = [[], [dict(opponent="skill-0", score=1)],
                          [dict(opponent="skill-0", score=1),dict(opponent="skill-0", score=1),dict(opponent="elo-1800-setting", score=1)],
                          [dict(opponent="skill-0", score=0)]*15+[dict(opponent="elo-1800-setting", score=.5)]*10+[dict(opponent="elo-1800-setting", score=1)]*25]
    for gs in validation_windows:
        ref = ns["posterior"]([dict(anchor=ANCHORS[g["opponent"]], score=g["score"]) for g in gs])
        ours = post(gs)
        assert all(ref[k] == ours[k] for k in ["estimate", "lower", "upper"]), (ref, ours)
        assert abs(ref["grid_edge_mass"]-ours["grid_edge_mass"]) < 1e-12
    result = dict(frozen_capture=manifest["capturedAt"], seed=SEED, verified_files=verification,
                  rating_code_validation_cases=len(validation_windows),
                  methods=dict(rating="Frozen nominal-stockfish-davidson-v1: normal1500/sd800 prior; 50 most recent rated games; 1320/1800 nominal anchors; full-strength excluded; unknown draw propensity integrated over40 bins",
                               primary="Each run: first floor(R/2) vs last floor(R/2) complete six-game rotations; middle rotation omitted if odd; incomplete trailing rotations omitted. Preserves all opponent/color cells.",
                               test="Two-sided permutation of complete rotation vectors across phase labels; exact where <=200000 allocations, otherwise200000 uniform Monte Carlo draws and plus-one p. Holm across six run-level combined-rated tests.",
                               interval="Phase-specific cluster-bootstrap percentile score-difference intervals. Separate Bayesian rating-difference intervals are conditional on segment rating model; no CI-overlap rule used.",
                               limitations="Exploratory observational audit; permutation assumes exchangeable rotations under null and bootstrap assumes independent rotations within phase. Persistent serial dependence may invalidate those assumptions. No randomized training ablation or generalization test; do not infer causal learning or no learning from p values."), runs={})
    rng = np.random.default_rng(SEED)
    for slug in SLUGS:
        result["runs"][slug] = analyze_run(slug, rng)
        t = result["runs"][slug]["balanced"]["tests"]["combined-rated"]
        print(json.dumps(dict(slug=slug, early=t["early"]["score_rate"], late=t["late"]["score_rate"], delta=t["delta_score_rate"], p=t["two_sided_p"], final=result["runs"][slug]["final_rolling"])), flush=True)
        (ROOT/"measurement_results.partial.json").write_text(json.dumps(result, indent=2)+"\n")
    holm([r["balanced"]["tests"]["combined-rated"] for r in result["runs"].values()])
    holm([r["balanced"]["tests"][o] for r in result["runs"].values() for o in ["skill-0", "elo-1800-setting"]])
    result["posterior_count_vectors_cached"] = len(POST_CACHE)
    (ROOT/"measurement_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print("Saved measurement_results.json", flush=True)


if __name__ == "__main__":
    main()
