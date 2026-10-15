# How the models actually did — independent review

Claude, 4 Oct 2026, ~22:00 UTC. Data: Astra 200/200 (complete), Opus 184, Sol 33, Sol · Long Context 16, Fable 15 (paused by the user).

Sources: every benchmark ledger, practice ledger, workspace note and snapshot (read-only), plus a new post-hoc Stockfish review of all 447 scored games (method in §3). Nothing was written to any learner folder, and nothing was sent to the learners. Elo throughout is the referee's engine-relative estimate with nominal anchors (skill 0 = 1320, 1800 setting = 1800), not a human rating.

## 1. The GPT assessment

**Where it is**
- Report: `deliverables/chess-learning-assessment-20261004-211004.{html,md,json}`.
- Generator: `.operator/learning-assessment/assess.py`.
- The prose, and the 3–4 "strategy changes" shown per model, are hand-written in `strategy-register.json`, reviewed at 20:50 UTC.

**What it gets right**
- Headline Elo numbers and direction: Astra 1680 → 1400, Opus 1510 → 1720.
- The ledger-integrity checks.
- Its cautious language about causality.
- The quoted failure examples (all ten check out).
- Treating Sol, Sol·LC and Fable as too early to call.

**Where it misleads or leaves things out**

1. **Astra's conditions differed from everyone else's.** Its instructions changed three times mid-run:
   - Game 30: learning trials became required.
   - Game 66: the practice tool was added.
   - Game 131: the 200-game endpoint was set.

   Games 1–30 were played under the original "beat max-strength Stockfish" goal with no learning requirement. That period is most of its "first 50 rated games" baseline. The report never mentions this.
2. **Its explanation for Astra is backwards.** The report says longer speculative branches and a growing checklist may have crowded out the board. The record shows Astra did the opposite:
   - It deliberately shortened its decisions (Trial 9: a 20-second clock and "one working candidate").
   - It cut its checklist from 4.4 KB to 0.36 KB.
   - Median time per move fell from 37 s to 13 s.
   - Tokens per game halved (about 285K → 140K by game 40; its counter stops at game 90).

   "Long speculative branches" is Astra's own self-diagnosis, repeated without checking it against the data.
3. **Opus: "+210" hides the shape, and the explanation is wrong.**
   - The gain was a step around game 55, followed by a plateau and a recent dip in results.
   - The report says the gain came from exploiting opponent mistakes, with little change in piece losses. Engine analysis says Opus's own blunder rate fell by about a third overall and by half against skill 0.
4. **The strategy evidence is cherry-picked and too small to mean anything.**
   - It covers 3 of Astra's 29 trials (all late) and 4 of Opus's 30.
   - The "before → after" scores use 8 rated games per side (for example "43.8% → 100%"). That is noise.
   - It misses the biggest changes:
     - Astra: the decision clock, the opening switch, the queen-trade preference.
     - Opus: the board-rendering tool at game 49, moving its effort to rated games (T7), and mandatory written checks with more time per move.
5. **It ignores comparability problems** (see §6): unequal context windows, Opus treating the harness token counter as a budget, status nudges interrupting moves, and session restarts.
6. **It has no measure of move quality.** The only behavioural signal is a crude material-loss proxy, reported as a lifetime total, which hides the trends below.

## 2. Results

| Model | Games | Current Elo (last 50 rated) | Elo by period (non-overlapping) | Trend |
|---|---:|---|---|---|
| GPT-6 Astra | 200, done | 1400 [1270–1520] | g1–60 **1720** → g61–120 1610 → g121–180 **1370** → g181–200 ~1510 (n=12) | −220 Elo per 100 games [−350, −90] |
| Claude Opus 5.5 | 184 | 1720 [1590–1850] | g1–54 **1470** → g55–162 **1750** → g163–184 1560 (n=14, wide) | +160 [+10, +310] overall; flat after g55 |
| GPT-6.1 Sol | 33 | 1570 [1380–1770] | its own checkpoints: 1870 @6 → 1700 @12 → 1650 @18 → 1630 @24 → 1560 @30 | too early |
| GPT-6.1 Sol · Long Context | 16 | 1610 [1340–1900] | — | too early |
| Claude Fable 5.1 | 15, paused | 1590 [1300–1890] | — | too early |

- **On equal footing (first 15 games), all five are indistinguishable:** Elo 1470–1720, each ±300.
- Over the first 30 games, Astra was best (1780), then Sol (1560), then Opus (1500).
- Every model scores about 0% against full strength. Astra drew 2 of 68.

**Astra by instruction phase**

| Phase | Elo | vs skill 0 | vs 1800 | Median s/move | Play min/game |
|---|---|---|---|---|---|
| A g1–30: original goal, no trials | 1780 [1590–1990] | 9/10 | 5/10 | 37 | 37 |
| B g31–66: trials required | 1650 [1480–1830] | 12/12 | 2/12 | 25 | 26 |
| C g67–132: practice tool | 1600 [1470–1730] | 17.5/22 | 6/22 | 22 | 24 |
| D g133–200: after endpoint | 1390 [1260–1520] | 13.5/22 | 2/22 | 13 | 13 |

## 3. Move quality (new: post-hoc Stockfish review)

**Method**
- Every position of all 447 scored benchmark games was evaluated by Stockfish 19 at 200K nodes.
- ACPL: centipawn loss per move, capped at ±1000.
- Blunder: a move that drops the mover's winning chances by at least 30 percentage points (the Lichess convention).
- Tables use rated games only; full-strength games end too quickly by resignation.

| Rated games | Early | → | → | Late |
|---|---|---|---|---|
| Astra (phases A/B/C/D) | ACPL 45, blunders 1.65/100 | 52 / 1.84 | 60 / 2.62 | 64 / 2.82 |
| Opus (g1–60 / 61–120 / 121–184) | 63 / 3.06 | 56 / 1.98 | 49 / 1.95 | — |
| Sol (8-game blocks) | 38 / 2.4 | 49 / 2.7 | 54 / 3.7 | 54 / 4.7 |

- **Against skill 0, blunders per 100 moves:** Astra 1.2 → 2.8 → 3.7; Opus 3.5 → 2.4 → 1.8.
- **First 15 games (rated):**

  | Model | ACPL | Blunders per 100 |
  |---|---:|---:|
  | Sol | 48 | 2.7 |
  | Sol·LC | 54 | 2.6 |
  | Astra | 57 | 2.1 |
  | Opus | 65 | 3.5 |
  | Fable | 74 | 3.9 |

- **Converting winning positions** (rated games where the model reached +3 by engine eval):
  - Astra: 76% (g1–60) → 50% (g121–180).
  - Opus: 64% (g1–60) → 16/16 (g121–150) → 12/19 (g151–184).

**What this shows**
- Astra started as the best player by move quality and got steadily worse. The decline is sharpest against the weakest opponent.
- Opus started among the weakest and genuinely improved. Even at its best (ACPL ~48), it did not match Astra's first 30 games (45).
- **Opus's recent dip is not a decline in play.** Move quality in g151–184 equals g121–150 (ACPL 49.0 vs 48.2; blunders 1.92 vs 1.98). Only conversion dropped, so variance is the likely cause. Watch the remaining 16 games.
- **Sol's move quality is drifting worse**, the same early pattern as Astra (small sample).
- **Openings are not anyone's problem.** The first 12 moves average about 25–35 centipawns of loss and under 1 blunder per 100 moves for everyone. The damage is done after move 12.

## 4. What each model actually did

### GPT-6 Astra — complete; declined

**Learning loop**
- 29 trials, each a 6-game block with one new focus.
- Each was judged by "did the targeted error recur at all". With several errors per game, nearly every trial failed within a game or two and was *replaced*. Nothing accumulated.

**Practice**
- 51 sessions with 688 own moves, against 7,746 benchmark moves.
- Opponents: 27 at maximum strength, 22 at the 1800 setting, 2 at 1600.
- Positions: its own saved games, composed positions, and initial positions. 32 sessions were stopped early.
- About 12 h in total between games versus 59 h of play (games 31–200).

**Effort**
- Deliberately shortened (Trial 9 clock; checklist reduced to one paragraph).
- After about game 127 it played at 10–19 s per move without ever declaring it.
- After the endpoint, its learning periods shrank from 45 to 20, 12 and then 8 minutes.

**Other changes**
- Changed opening repertoire (T15: 1.d4/e3/Be2, ...e6/...d5).
- Added a "prefer safe queen trades" policy (T16, later dropped).

**Errors**
- Own-piece blockers, pawn-capture geometry, abandoned defenders and missed intermediate checks recur from game 1 to game 200.
- Losses to skill 0 went from 2 in its first 33 games against that opponent to 11 in the last 33.

**Self-report**
- Honest: "mixed locally and negative overall".
- It blames long speculative branches and never notes that its own time per move halved.
- Its activity notes stop after g72 and token logging after g90 (its goal tool got stuck on the obsolete objective).

**Likely why** (association, not proof): less deliberation per move, constant churn of focus, and drills rehearsing specific positions instead of building a habit.

### Claude Opus 5.5 — 184/200; improved, then plateaued

**Learning loop**
- Practice: a single 6-minute drill in the whole run.
- Between games (20 s–2 min): one line in GAMES.md and an entry in ERRORS.md.
- Every 6 games: a new trial in PLAN.md.

**Rules are cumulative**
- T10–T28 each equal the previous rules plus a new check, about 35 named checks in all.
- T29 cut them to four steps (PATH / DEST / BOX / LEAF), noting "the checklist has grown long and the misses are basic". T30 started adding again at once.

**What coincided with the jump (g55–72)**
- A board-rendering wrapper (g49) that prints a labelled board and piece lists. Pure display, allowed.
- "Square scans" (T9: walk the rays out from the target square) and origin scans (T10).
- Later, mandatory written checks (T12–13), with rising time per rated move:
  - 1800 games: 11 → 23 s median.
  - Skill 0: 10 → 14 s.
- About 60% more tokens per game (60K → ~100K).

**Repertoire:** stable in rated games (1.e4; Caro-Kann).

**Resource behaviour**
- It read the referee code and knew the final Elo comes from roughly games 125–200.
- It treated the harness's "15M tokens left" counter as a budget, although the goal says there is no cap. It played full-strength games fast and resigned them at about −3.

**Errors**
- By its own record, one-move material losses never reached zero except in T14.
- Errors after games 151–184 are the same family as everyone's: discovered lines, pins, loose pieces.

### GPT-6.1 Sol — 33 games; no improvement so far

**Learning loop**
- After *every* game it picks the decisive error and tests one alternative move from that position for 2–4 moves against skill 5. That is 23 sessions with a median of 2 own moves. Many of the alternatives also lost.
- It then goes straight back to benchmarks.

**Openings:** frequent switches.
- White: 1.e4 → 1.d4 → 1.e4.
- Black: ...e5 → ...Nf6 → French → Caro-Kann → ...e5.

**Effort and self-report**
- The slowest player: about 36 s per move and 40 min per game.
- It repeatedly writes that very long speculative calculation coexisted with missing one-move threats, and that its intended compact review "was not achieved".
- The most candid self-reporter. It has never claimed progress.

### GPT-6.1 Sol · Long Context — 16 games

- Same model with an 828K context window, and the same per-game loop with roughly 10-ply drills (8 sessions, 36 own moves).
- At game 12 it changed approach on its own: it dropped drills ("repeated drill success has not supplied fresh transfer") in favour of a short safety pass on the actual board. Only 4 games have been played since.
- It is indistinguishable from Sol at the same point. Nothing can be said about a context-window effect yet.

### Claude Fable 5.1 — 15 games, paused

**Setup:** the most structured start.
- Read the referee code.
- Fixed repertoire (London; Caro-Kann).
- A written A–D scan before every move.
- 3 full practice games (1 win, 2 losses).

**Patching:** it patches the procedure after almost every loss. It is already at v2.8, which is long.

**Move quality:** the worst early of the five (rated ACPL 74, 3.9 blunders per 100), yet its Elo of ~1590 matches the others.

**Status nudges:** at least two moves were played straight after a harness "say what you're doing" nudge without its usual check. One cost the queen in game 7. It added a rule to re-read the board after any nudge.

## 5. Cross-model picture

- **Same diagnosis everywhere.** All five decided they fail at tracking the board in the middlegame: moved defenders, blocked lines, pawn-capture geometry and intermediate checks. Not openings or strategy. The engine data agrees.
- **Same response everywhere.** All five wrote rules and checklists. None did any real outside study. Practice was a minor activity for all of them; the main "learning" is reviewing their own benchmark games.
- **The two long runs differ in a telling way:**
  - Opus kept and stacked its rules and spent more time per move as the run went on.
  - Astra replaced its focus every block, shrank its checklist and spent less time per move.
  - Opus improved and Astra declined. With one run each, this is suggestive, not proof.
- **Self-reports are honest but not always right.** No model inflated its results. Astra's self-diagnosis does not match its own data.
- **Elo is noisy at these sample sizes.** Twenty to forty rated games give ±200 Elo. The move-quality numbers are far more stable and catch changes earlier.

## 6. Comparability issues and recommended fixes

- **Mark change points on every chart.** Show Astra's phase boundaries (g30, g66, g131) and Opus's interruptions (operator resumes during games 77 and 130). Never compare Astra's first-50 baseline with another run without that caveat.
- **Context windows are unequal:** Astra and Sol 258K, Sol·LC 828K, Opus and Fable 1M. This confounds any GPT-versus-Claude comparison.
- **Opus treats the harness token counter as a budget.** That counter is shown to the Claude agents only. It shaped Opus's strategy: compact play, fast full-strength games, early resignations.
- **Status nudges can trigger rushed moves.** Fable documents a queen lost this way.
- **Changes to the assessment itself:**
  - Add engine-based move quality per block.
  - Report non-overlapping Elo windows plus a drift slope instead of first-50 versus last-50.
  - Replace the cherry-picked strategy entries with full trial timelines.
  - Drop the 8-game before/after percentages.

## Files

**Scripts and per-game engine evaluations** are in `.operator/claude-review/`:

| File | What it does |
|---|---|
| `engine_review.py` | Evaluates games; results cached in `evals/` |
| `quality.py`, `quality2.py`, `quality3.py` | Move-quality tables |
| `blocks.py`, `drift.py` | Elo windows and the drift slope |
| `table.py` | Per-game table |

To refresh as the runs progress, run `t3-job -- python3 engine_review.py 8`. It only analyses new games.
