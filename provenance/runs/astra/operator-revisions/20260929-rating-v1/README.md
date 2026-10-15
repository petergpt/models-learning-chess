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

Track wins/draws/losses and the last-50-game score separately for each opponent. Illegal-move forfeits count as losses; move-limit games remain visible as unfinished. All started games stay in the ledger. This setup has no independently calibrated human Elo scale. The engine's `UCI_Elo` setting is a configuration label, not a measured human rating for the learner. Do not convert sparse results or all-loss runs into a precise rating. Independent rating calibration can be added later without rewriting historical results.

The model's underlying weights are unchanged; its workspace and behavior may evolve. Learning and playing have no enforced model-token cap in v1; time and any available usage are recorded. More thinking can be part of an observed gain. Games are from the normal initial position. Progress against this fixed engine is the measured objective; transfer to other opponents is untested.

Integrity checks enforce the pinned files through the normal interface, but same-account access is not a hardened anti-cheating sandbox. All observed inputs, records and rules should be audited before making strong scientific claims. Changing the protocol requires a new version/experiment, not relabeling old games.

## Verification

`./play verify` checks pinned installation hashes and the ledger chain. `.arena/test_arena.py` exercises legal play, persistence, black-to-move starts, illegal forfeits, resignations, PGN replay, checksums, result statistics and UI export using an isolated temporary directory. Test moves are synthetic and never enter the measured ledger.
