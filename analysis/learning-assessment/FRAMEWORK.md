# Assessing how the chess agents learn

This framework measures **adaptation within a run**: changes in notes, repertoire, decision procedures and practice. The experiment does not update model weights. The operator observes all runs; the learners remain independent and receive no comparative findings or move advice.

It produces a reproducible assessment from the referee records and authored workspace notes, with an interactive HTML report, JSON evidence and a Markdown report.

## Questions and evidence

| Question | Evidence | What does not establish it |
|---|---|---|
| Is it trying something different? | A dated declaration in a workspace snapshot saved before a game; changes in repertoire and practice origins | More words, more tokens, a rising count of trials |
| Did its behavior change? | Observed openings, castling, legality, short-term material-loss patterns and conversion | Stating that it followed a checklist |
| Did the change transfer? | Fresh fixed-rotation benchmarks with the same opponent/color mix | A corrected remembered position, a favorable custom-position win |
| Did it retain the improvement? | Later fresh rotations preserve the outcome and behavioral change | One winning streak or one high Elo estimate |
| What is getting worse? | Repeated recorded failure patterns and matched deterioration | Comparing an early estimate from one win with a mature estimate |
| Why might this happen? | A declared mechanism, observed change, failures consistent with it, and alternative explanations | Treating an association as the causal effect of a study method |
| Is the improvement economical? | Behavior and outcomes alongside measured submission time; comparable scoped usage if available | Treating idle wall time as inference time or comparing incompatible token counters |

## Primary outcome: Elo

Use the referee's existing rolling 50-rated-game Elo as the headline measure, with its 95% credible interval. Once 100 rated games are available, compare the estimate after the first 50 with the latest 50. Those windows do not overlap. Before that point, show the current rating and uncertainty, and label the change as an early sample rather than compare a lucky first win with a later mature estimate.

The Elo calculation already conditions on nominal opponent strength. A change in its median is a descriptive difference; the two individual credible intervals do not themselves give a 95% credible interval for the difference. Preserve game-score and behavioral comparisons as supporting evidence explaining what underlies the rating change.

## Supporting outcome comparison: game score

1. Include only scored benchmark games. Keep started, unfinished and practice records in the evidence inventory.
2. Form complete six-game rotations: maximum strength White/Black, skill 0 White/Black, nominal 1800 White/Black.
3. Compare the first and last equal halves of complete rotations. Omit the middle rotation when the number is odd. This gives disjoint games with identical opponent and color counts.
4. Supporting game score is wins plus half of draws against the two nominally anchored opponents. Report each opponent separately. Maximum strength is separate and does not enter the existing Elo estimator.
5. Resample complete rotations independently within each window 10,000 times with a fixed seed. Report the percentile 95% interval for the score difference. Require at least five rotations in each window for a directional label. This sample threshold is a reporting convention, not a power guarantee.
6. Assess recent momentum using adjacent equal windows of up to eight complete rotations. Report both horizons: a model can improve overall and regress recently.
7. Between-model comparisons use the same benchmark range; the first 12 benchmark games provide a small common descriptive sample. Do not rank learning from unequal final Elo samples.

These intervals are exploratory. Blocks may remain correlated over time, agents keep changing their approach, and repeatedly refreshing the report is not a sequential significance test. The method does not remove opponent randomness or all differences in inference effort. At the 200-game endpoint, preserve the final report as a fixed assessment. Repeated runs are needed to generalize beyond one agent trajectory.

The dashboard's Elo is a rolling 50-rated-game Bayesian estimate with nominal Stockfish anchors of 1320 and 1800. It is engine-relative, not a human rating. Its credible interval excludes systematic anchor calibration error. Overlapping rolling windows and early wins can create apparent trends. Do not regress the rolling Elo points as independent observations. A peak is descriptive and selected after seeing the run.

## Strategy register and transfer

`strategy-register.json` contains the operator's reviewed interpretations and a selection of meaningful changes. Each entry supplies a source file and a literal declaration marker. The generator searches the **saved pre-game snapshots**, records the first benchmark before which that declaration existed, and stores the snapshot hash, note-content hash and source line.

For each verified declaration, compare up to two complete rotations immediately before and after it, using equal window sizes. Report the next two rotations separately as a retention check. Do not issue a directional statistical verdict for these small local windows. Changes can overlap, including opening changes, budget changes and new safety rules. The local comparison is an association, not a controlled intervention estimate.

The count of changed note bundles includes game logging and edits; it is not a count of learned concepts. Source snapshots establish that text existed, not that the model executed every step. Qualitative interpretations have an explicit review date. Numeric refreshes do not automatically review new prose or explain a new trend.

## Observable behavior

| Metric | Exact definition | Interpretation limit |
|---|---|---|
| Illegal submissions | Number per 100 accepted learner moves | Legal play can still be weak |
| Short-horizon non-pawn losses | The opponent captures a learner minor/rook/queen immediately after a learner move; material balance from before that move to after the next learner reply falls by at least 2 | Includes sacrifices; ignores positional compensation and later recovery; unavailable if there is no next learner reply; not an engine-certified blunder |
| Material-lead conversion | Win rate in games reaching +3 in P=1, N/B=3, R=5, Q=9 after ply 20, measured after opponent replies | Material is not a winning-position evaluation; selected subset differs between models |
| Castling by move 10 | Fraction of games with at least 10 learner moves where castling occurred by its tenth move | Style marker, not a universal measure of quality |
| Repertoire | First own move, conditional on color and White's first move; first three own UCI moves retained per game | Opponent variation can change continuations without intentional exploration |
| Submission time | Median referee-reported time between accepted learner submissions | Includes interruptions and idle time; not compute time |

Mechanical features use python-chess only to replay and inspect recorded positions. No engine, tablebase, best-move search or automated move recommendations are used. Practice results and origins are inventoried separately; unfinished drills do not become draws.

## Error taxonomy for reviewed game evidence

| Class | Example | Evidence available |
|---|---|---|
| Board and geometry | Wrong square, blocked slider, wrong movement shape | Legality rejection is mechanical; root cause needs reviewed notes |
| Defender and blocker tracking | Sole defender moved, own piece blocks recapture, pinned defender | Authored diagnosis plus the played continuation; tactical severity unverified without separate evaluation |
| Forcing replies | Missed check, fork, discovered attack or intermediate move | Played sequence plus reviewed diagnosis |
| King safety | Imagined flight square, overlooked back-rank net | Terminal mate is mechanical; preventability is a reviewed claim |
| Conversion | Stalemate, repetition, unsafe promotion, giving back a lead | Terminal result and material trajectory, with selected-position limits |
| Opening and planning | Repertoire revision, development or pawn-break choice | Behavior can be observed; opening quality is not inferred from its name |
| Execution and economy | Scan skipped, superficial answer, long calculation | Authored process account and measured submission time; no private reasoning inspection |

Use `review-record.schema.json` for future reviewed assessments. Every explanation has an evidence level, supporting references, alternative explanations and a proposed discriminating observation. Leave unknowns unknown; do not produce an opaque combined “learning score.”

## Refresh and output

Run from the project root:

```sh
/home/peter/.local/bin/t3-job -- python3 .operator/learning-assessment/assess.py
```

Each run creates a fresh timestamped HTML, JSON and Markdown file in `deliverables/`, and updates `.operator/learning-assessment/latest.json`. Deliver the new HTML with an absolute workspace file link so T3 generates its asset URL. No redeployment is involved.

The generator holds each arena's shared lock only while reading its ledger, practice ledger and rating cache. It verifies ledger hashes and sequence numbers, accepted move legality/SAN/FENs, scored result perspective and terminal positions, rotation, colors, engine options and nodes per move. It reads immutable archived note members without extracting archives or running learner helpers. It never writes to a learner's folder. A detected inconsistency stops generation rather than silently discarding data.

Run verification:

```sh
/home/peter/.local/bin/t3-job -- python3 -m unittest discover -s .operator/learning-assessment/tests -v
```

## What would allow a stronger “why” claim?

For a future experiment, compare replicated runs with fixed opponent settings, game counts and decision budgets. Predeclare a strategy change and a targeted observable; hold the method stable for a complete evaluation block and a retention block. Randomize or counterbalance the treatment across independent runs. A context-window experiment needs repeated standard/large-context pairs at equal game counts. Do not alter the ongoing learners' freedom to choose their approaches just to simplify this retrospective analysis.
