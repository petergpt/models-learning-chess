# Chess — GPT-6 Astra

A minimal autonomous learning experiment: persistent workspace, chess referee, fixed Stockfish opponents, append-only records, and an interactive replay/dashboard. The learner determines its own learning process.

## Start

Read `AGENTS.md` and `GOAL.md`. Run `./play start`, then submit UCI moves with `./play move e2e4`. No server, API key, or chess GUI is required to use the game interface. This folder does not itself run an LLM: the active GPT-6 Astra session is the learner. A session goal drives continuation; no separate background model process is installed.

## Fixed opponent

Stockfish **19**, official Linux x86-64 release, pinned by SHA-256. The main target is maximum skill 20 with strength limiting off and **1,000,000 nodes per move**. The other fixed settings are skill 0 and UCI Elo 1800. Two games per setting alternate the learner's color, then advance to the next setting. Every setting gets separate results; an easier-opponent win never counts as a maximum-strength win.

Stockfish uses one thread, 64 MiB hash and a fresh process each turn for consistent benchmark conditions, no pondering, opening books or tablebases. The one-thread setting is part of the chess opponent definition, not a host CPU limit. Engine node limits are reproducible work budgets; some nondeterminism, especially at weakened settings, remains. Full strength here means the strongest skill mode at this finite node budget.

Dependencies: vendored `chess==1.11.2` for legal rules/PGN and Stockfish 19 for the opponent. No pip installation or global packages are needed. Published archive hashes, source URLs and licenses are under `.arena/`. Stockfish and python-chess are GPL-licensed; retain their notices when redistributing.

## What is recorded

- `data/ledger.jsonl`: append-only, hash-chained events; starts, moves, FENs, SAN/UCI, color, opponent/configuration, timestamps, elapsed move time, failed moves, results, interruptions/errors, optional short comments and usage counters.
- `data/games/*.pgn.gz`: compressed completed game records. Active games can be reconstructed from the ledger.
- `data/snapshots/*.tar.gz`: content-addressed snapshots of `workspace/` at game start/end and activity notes. Identical content is stored once. These capture retained learning artifacts, not the model's weights.
- `data/dashboard.html`: refreshed after each command; animated board replay, move slider, game downloads, separate opponent scores and activity notes.
- `./play export`: creates a fresh, standalone dashboard in the parent workspace's `deliverables/`, suitable for a clickable T3 workspace link. It is a dated snapshot; export again to share newer results. The compact dashboard includes the last 100 games; originals are retained.

No screen video is recorded. Replay reconstructs the board from moves and timestamps, avoiding large video files. It does not capture browser activity, shell screens or private reasoning. The current conversation supplies additional tool/action context. Optional comments and workspace snapshots help explain activity. Unknown token usage is `null`/unavailable, never zero. Aggregate usage counters record their source and scope; per-move attribution is not inferred. Setup usage should be kept distinct from learning usage.

Recording plus learner workspace pauses at **2 GiB**, and commands also refuse writes below 2 GiB host free space. A workspace snapshot is limited to 32 MiB uncompressed. These are storage safeguards, not learning-token limits. Nothing deletes old games automatically. The model must not clean the historical ledger. The dashboard is regenerated in place; shareable exports are created only on explicit `export` calls, not after every move. Operator exports should be archived if they accumulate.

## Interpretation and limitations

Track wins/draws/losses and the last-50-game score separately for each opponent. Illegal-move forfeits count as losses; move-limit games remain visible as unfinished. All started games stay in the ledger. The dashboard now includes a provisional Bayesian engine-relative Elo estimate and 95% credible interval, recalculated after each completed nominally rated game. It uses skill 0 as a nominal 1320 anchor and the 1800 setting as a nominal 1800 anchor. Maximum-skill games remain in the score table but are excluded from Elo because their strength is uncalibrated. This is not an independently calibrated human FIDE/platform rating; sparse-data estimates are strongly prior-dependent.

The model's underlying weights are unchanged; its workspace and behavior may evolve. Learning and playing have no enforced model-token cap in v1; time and any available usage are recorded. More thinking can be part of an observed gain. Benchmark games are from the normal initial position. Progress against this fixed engine is the measured objective; transfer to other opponents is untested.

Integrity checks enforce the pinned files through the normal interface, but same-account access is not a hardened anti-cheating sandbox. All observed inputs, records and rules should be audited before making strong scientific claims. Changing the protocol requires a new version/experiment, not relabeling old games.

## Verification

`./play verify` checks pinned installation hashes and the ledger chain. `.arena/test_arena.py` exercises legal play, persistence, black-to-move starts, illegal forfeits, resignations, PGN replay, checksums, result statistics and UI export using an isolated temporary directory. Test moves are synthetic and never enter the measured ledger.

## Provisional rating method (measurement update, 29 September 2026)

`rating.py` uses a Bradley–Terry–Davidson win/draw/loss likelihood. For rating difference Δ, let q = 10^(Δ/800). Win, loss and draw probabilities are proportional to q, 1/q and ν. The rating prior is Normal(1500, 800²). The equal-strength draw probability has a Uniform(0,1) prior (ν = 2d/(1-d)), numerically integrated over 40 midpoint bins. Rating is evaluated on a 10-point grid from −2500 to 6500; the posterior median and equal-tail 95% interval are displayed. The grid-edge mass is retained for diagnostics. The latest 50 completed games with nominal anchors are used; all earlier game records remain intact. No rating is displayed before the first qualifying result. Draws contribute through the draw likelihood; illegal-move forfeits count as losses; unfinished games are excluded and stay visible. Color effects and changing strength within the window are not modeled.

The 95% band is a **Bayesian credible interval conditional on the stated model and nominal anchors**, not a calibrated frequentist confidence interval. It does not include systematic error in Stockfish's nominal ratings at our one-million-node budget. Early results, especially all wins or all losses, can be strongly influenced by the broad prior. Independent opponent calibration remains future work.

The estimate and its history are cached in `data/rating-cache.json`; this derived file can be reconstructed from the immutable ledger. Each historical estimate uses only earlier results. The dashboard shows the latest 200 rating checkpoints. This observer-only update did not change the learner's goal, instructions, game rules, opponent settings, or past results. Previous recorder files and manifest were preserved in `.arena/operator-revisions/20260929-rating-v1/`; the installation change is recorded in the ledger.

Sources: [Stockfish strength settings](https://official-stockfish.github.io/docs/stockfish-wiki/Stockfish-FAQ.html), the installed Stockfish 19 `src/search.h` and `wiki/UCI-Protocol-and-Stockfish-Commands.md` (nominal 1320 lower anchor; original time-control calibration differs from this experiment), and [Davidson's model for ties](https://doi.org/10.1080/01621459.1970.10481082).

Validation: 9 statistical tests plus all 11 existing referee integration tests; desktop and mobile checks of the estimate, interval, chart, board and horizontal layout.

## Selectable opponent practice (1 October 2026)

The learner may choose Stockfish skill 0–20 or nominal Elo 1320–3190, either color, a custom FEN, or a recorded benchmark position through `./play practice`. See `AGENTS.md` for the commands. All practice remains in a separate hash-chained ledger and compressed PGNs under `data/practice/`; it contributes neither to benchmark scores nor Elo and does not advance the fixed benchmark rotation. Explicitly ending a drill records it as unfinished, without discarding its history. Finish any active benchmark before practice and finish or end practice before the next benchmark. Engine analysis and move advice remain prohibited.

The user authorized opponent and position freedom for practice while retaining periodic fixed benchmarks of learning transfer. The goal remains increasing measured Elo. Installation and both ledger chains are checked by `./play verify`. Validation: all 28 referee, rating, and practice tests passed using disposable records, including actual engine strength controls, custom-position PGN replay, retry after engine failure, and benchmark/rating isolation.
