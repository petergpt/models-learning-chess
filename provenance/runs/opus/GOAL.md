# Goal

Increase your measured engine-relative Elo through improvements in how you play chess. The objective is stronger play, not merely estimating your existing strength, producing more notes, or completing more games.

Choose your own learning methods and use the persistent `workspace/`. There is no learning-token cap or prescribed chess curriculum. Use deliberate learning periods between measured games instead of treating the fixed opponent rotation as your entire learning strategy. You choose what to study or practise, how long to spend, and when to change an ineffective method.

After finishing any active measured game, choose a learning trial before automatically starting another benchmark block. State the weakness or skill you intend to improve, what you will try, and what observable result would suggest it helped. Revisit your own failed positions or undertake other permitted study and practice as you judge useful. Distinguish remembered positions from new examples, and your own unverified assessments from independently established facts. Do not treat a longer checklist as evidence of learning.

Use `./play practice` when opponent practice helps: you choose opponent strength, color, starting position, repetitions, and when to stop a drill. Practice is recorded separately and does not change benchmark Elo; easier practice wins alone are not evidence of improvement.

Return periodically to measured games in the existing fixed paired-color rotation to test whether practice transfers to new play. Choose and record a reasonable next evaluation point before a learning period; neither continuous benchmarking with no learning trial nor indefinite study with no evaluation fulfills this objective. Preserve all results, including losses. Track Elo and its uncertainty alongside recurrence of the errors you targeted. For benchmarks, keep the opponent settings, rating calculation, and fair-play rules fixed unless the user authorizes an operator change; a changed estimator or easier opponents is not learning progress.

The existing Elo estimate is provisional and engine-relative, not a human FIDE or platform rating. Seek sustained improvement across repeated evaluations; a single win, a temporary rating rise, or a memorized example does not establish that your method works. If a method fails, revise it on your own initiative and report that honestly. Maximum-strength games remain useful benchmark evidence, but the former requirement to beat maximum strength in two 100-game blocks is superseded by the user's clarified objective of increasing Elo.

Follow `AGENTS.md`. Every move must be your own decision. There is no model-token cap. Continue until the bounded experiment is finished; do not stop simply because learning is difficult. Report stagnation, resource limitations, or rule violations honestly. The user may stop or redirect the experiment at any time.


## Completion condition

This is a fresh, independent Opus 5.5 (Max) run. Complete 200 scored benchmark games, then stop and report what the measurements show. You choose learning and practice methods freely within `AGENTS.md`. Keep returning to the fixed benchmarks; choose your own reasonable evaluation points, and avoid indefinite study without evaluation. The run is complete at 200 scored games regardless of achieved Elo. Do not inspect any other learner’s work or the operator’s comparisons.
