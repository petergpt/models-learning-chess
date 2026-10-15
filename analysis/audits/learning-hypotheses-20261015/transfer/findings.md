# Behavioral adaptation, remembered practice, and fresh transfer

The clearest distinction is between changing a procedure, repairing a remembered example, and becoming reliably better on new boards. There is substantial evidence of the first two. Astra and the three Sol runs do not show sustained improvement in the broader mechanical error measures examined here. That does not establish that nothing was learned: some narrow behaviors changed, and outcome statistics must be assessed separately.

## Frozen scope and checks

`assess_transfer.py` reads the common measurement manifest captured 2026-10-15T22:09:24 UTC, validates its file digests and the ledger hash chains, then mechanically replays every accepted move, SAN, FEN, and recorded terminal outcome. The endpoint sample is Astra 200, standard Sol 200, long-context Sol 99, maximum-effort long-context Sol 63, Opus 200, and Fable 45 scored benchmarks. Active next games are excluded from comparisons; their historical start snapshots may supply notes written after the preceding completed game. Every workspace archive used for chronology is verified against its recorded content digest. Only named authored note files are decoded. No engine, learner, new play, or private reasoning was invoked.

The short-horizon loss proxy counts a nonpawn piece captured by the opponent with at least two net material points still lost after the next learner reply. It includes sacrifices, excludes positional compensation, and misses terminal captures with no following learner reply. It is **not** an engine blunder rate. Rates and event counts are both retained in `results.json`.

## Hypothesis 1: remembered drills repair particular positions without reliable transfer

**Supported.** Practice is heavily selected and usually ends before an actual game result.

| Run | Practice sessions | Scored W/D/L | Stopped | Median own moves | At most four own moves | Recycled benchmark positions |
|---|---:|---|---:|---:|---:|---:|
| Astra | 51 | 5/2/12 | 32 | 12 | 1 | 21 |
| Sol | 181 | 3/0/17 | 161 | 3 | 160 | 179 |
| Long Sol | 94 | 1/0/11 | 82 | 4 | 58 | 89 |
| Long Sol, max | 36 | 0/0/5 | 31 | 4 | 25 | 32 |

Astra also used nine initial-position practices and 21 self-constructed positions. Its practice was more varied than Sol's; it should not be described as consisting entirely of tiny remembered drills. Most long-Sol practice used skill 5 (85/94), whereas the rated benchmark includes skill 0 and nominal 1800. Practice outcomes across these origins, initial advantages, and opponents cannot be pooled as an improvement estimate.

The apparently successful sessions are especially revealing:

- Standard Sol's three practice wins all start from positions in already-won benchmarks, with initial material advantages of **+14, +24, and +13**. They take two, two, and four own moves respectively.
- Long Sol's only practice win, practice 89, starts **+25** from its already-won benchmark 94 and exactly repeats the original three-ply finish **Rh1 b4 Rxh3#**. This verifies retention of that finish; it is not a fresh-position strength test.
- Four of Astra's five practice wins start **+8 to +12**. Its remaining practice win is a legitimate new initial-position session. In the two-rook conversion trial, it wins one constructed position and then loses both rooks to direct captures in the next preselected composition, according to its authored review.
- Sol's practice 127 meets its short no-mate/no-rook-loss/material targets, but its authored review identifies a still-pending checking fork at the stopping point. A favorable short horizon can conceal the next failure. This is a weakness of the surrogate criterion, not evidence that the author concealed it: the journal explicitly records the limitation.

These tests support a local-repair/generalization gap. They do not prove that remembered practice caused subsequent deterioration.

## Hypothesis 2: written rules changed, but execution failed on new boards

**Supported, with evidence of narrow adaptation.** The first and last equal halves of complete six-game rotations match the opponent and color mix. The middle rotation is omitted when necessary.

| Run | Compared benchmark windows | Illegal attempts per 100 own moves | Short-loss events per 100 own moves | Short-loss event counts |
|---|---|---|---|---|
| Astra | 1–96 vs 103–198 | 0.216 → 0.188 | 1.509 → 1.801 | 56 → 67 |
| Sol | 1–96 vs 103–198 | 0.460 → 0.567 | 1.947 → 2.070 | 72 → 73 |
| Long Sol | 1–48 vs 49–96 | 0.469 → 0.675 | 2.110 → 2.587 | 36 → 46 |
| Long Sol, max | 1–30 vs 31–60 | 0.263 → 0.098 | 1.489 → 2.155 | 17 → 22 |

These are descriptive rates, not significance claims about each mechanism. Max Sol demonstrates why a narrower improvement can coexist with poor chess: illegal requests fall from three to one across the matched halves while material losses increase. Astra castles by its tenth own move in **76.0% → 95.8%** of eligible games, a clear changed behavior that does not translate into lower material-loss rates or stronger overall results. In all four runs, most loss-proxy events occur after the fifteenth own move; satisfying an opening-only safety target does not establish middlegame competence.

The failure recurrence is concrete:

- Astra's historical pawn-geometry trial is present before benchmark **163**. It nevertheless requests a backward White pawn capture in **173**. Slider-path illegal requests rise **2 → 5** across matched halves, and **198** loses a bishop after a rook's imagined recapture is blocked by its own bishop. **197** promotes to a queen and stalemates. These are fresh execution failures after extensive corresponding study.
- Standard Sol's blocked slider requests recur **5 → 7**. Its late authored reviews distinguish local opening repairs from broader failure: **199** misses a checking knight fork; in **200**, its queen leaves f7 to capture on e6 and White immediately plays **Qf8#**. The recorded move line and mate are mechanically verified.
- Long Sol's **95** moves its king away from a bishop's defense and loses the bishop to **Rxh4**. In **96**, it retreats a rook onto the opponent's rook file and loses it to **Rxc8**, despite its remembered defender and destination drills. The same game includes a queen request through its own pawn.
- Max Sol's immediate-check and short-calculation trials recur throughout its notes. Benchmark **61** ends **Qd4 Nh2#** after addressing a different anticipated queen mate. Benchmark **63** ends **Qg1 Rxg1#**. Lower illegal counts have not resolved king safety.

Historical declarations are dated from immutable benchmark-start snapshots. Small pre/post examples are included in `results.json` but cannot identify intervention effects. For example, Astra's literal-recapture change is present before **175**: the next two full rotations score **5.5/8 rated points**, then the following two score **2.5/8**. That is a temporary positive patch, followed by weaker retention; the nearby interventions and small samples prevent attribution to one rule.

## Hypothesis 3: context growth or compaction caused the decline

**Plausible contributor; not established.** This section uses the existing structured Astra context audit as secondary evidence, with source hashes saved in `context-secondary.json`; it does not re-read hidden reasoning or summaries.

Astra's journal grows to roughly **101,000 words**, but disk note length is not prompt length. Across the same matched rated periods, mean actual input increases only **105,157 → 118,627 tokens** (12.8%); responses above 90% of its 258,400-token window are **2.0% → 4.2%**. The active checklist shrinks from **719 words** before game 31 to **58** before 199. Detected journal-reading commands decline sharply. Therefore “the whole enormous journal was repeatedly stuffed into context” is not supported by the measured reads.

Compaction occurs **41 times early and 22 late**. The screened first five accepted benchmark moves after compaction show **1/135** early and **0/70** late short-loss events, versus **38/2606** and **48/2770** elsewhere in rated games. There is no observed immediate error spike in this narrow proxy; sparse counts and game-stage confounding make this inconclusive. Important late errors also occur with substantial headroom: the backward pawn request in 173 follows a **46,523-token** input; the stalemate in 197 follows **78,908**; the blocked imagined recapture in 198 follows **90,379**. Context saturation is not necessary for these failures.

Structured reasoning-use metadata also changes: Astra's recorded reasoning tokens per accepted own move fall about **1072 → 513** across matched rated periods. This is another possible confound, not a causal explanation. Summary quality and attention cannot be inferred from lengths and timestamps.

The older Sol metadata audit covers earlier endpoints only and shows **different reasoning settings** between the original 828K medium-effort run and the standard max-effort run. Consequently, differences between those runs do not isolate context-window size. No controlled context-reset experiment was performed here.

## Hypothesis 4: this is benchmark exploitation or reward hacking

**No affirmative evidence of score manipulation from this subaudit.** Selected short drills can make a *practice-success narrative* misleading, but they are explicitly stopped/unscored, retained, and separate from the rated benchmark. Several authors explicitly acknowledge the horizon's limits and opponent gifts. Calling that deliberate reward hacking would exceed the evidence.

Specializing against a fixed weak opponent remains possible: learning to exploit its recurring mistakes can raise results without broad chess improvement. It can also be legitimate task learning. The present data lack held-out opponents, unseen opening families, repeated runs, or reset-context controls to distinguish those explanations. The parent measurement audit addresses rating mechanics, fixed rotation, excluded games, and score trends.

## Positive comparison and limits

The same mechanical screen does not declare every run incapable of learning. Opus's illegal-request rate falls **0.928 → 0.567**, while its short-loss rate is essentially flat **1.321 → 1.314** and it reaches a +3 material lead in **37 → 48** matched games. Fable's small matched sample shows both lower illegal requests **0.982 → 0.158** and fewer loss-proxy events **2.384 → 1.420**. These are possible behavioral improvements; neither one uncontrolled run nor this proxy identifies their cause or proves generalized chess learning.

Reproducible outputs: `assess_transfer.py`, `evidence_supplement.py`, `results.json`, per-run JSON, `supplement.json`, `context-secondary.json`, hash-pinned authored copies, and historical note copies. The retrospective cannot assess weight learning, optimal move quality, counterfactual saved games, or causal effects of individual procedures.
