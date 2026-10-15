# Data guide

This release preserves the six learning trajectories and the separate Astra–Opus match at their recorded endpoints. Benchmark, practice, and match records have separate `mode` values.

| File | Format and purpose |
|---|---|
| `data/index.json` | Run names, configurations, counts, and deployment link |
| `data/games.csv`, `data/games.jsonl` | One row per game or practice start; 1,206 rows |
| `data/moves.jsonl.gz` | One row per accepted ply; includes UCI, SAN, FEN, actor, timestamp, and recorded usage when available |
| `data/all-games.pgn.gz`, `data/pgn/` | Every game/session as PGN, including stopped and active records |
| `data/runs/<run>/ledger.jsonl.gz` | Benchmark event ledger, including notes, failed moves, results, and protocol updates |
| `data/runs/<run>/practice/ledger.jsonl.gz` | Separate practice ledger |
| `data/runs/<run>/workspace/` | Final learner files |
| `data/runs/<run>/snapshots/` | Content-addressed historical workspace archives |
| `data/snapshots.jsonl.gz` | Snapshot member names and content hashes; maps source IDs to public IDs |
| `data/traces/<run>/events.jsonl.gz` | Exported messages, tool activity, returned reasoning/thinking text, usage, compactions, and runtime metadata |
| `data/traces/index.json` | Trace counts, source checksums, and branch ancestry |
| `data/match/` | Match event ledger, protocol, controller history, starting checkpoints, and players’ notes |

`game_id` joins games and moves, for example `astra/benchmark/000001`. `game_number` is local to its run and mode. `ply` counts individual moves from that session’s starting position. For practice, check `initial_fen` rather than assuming the normal initial position.

`status=scored` identifies a finished scored game; `stopped` identifies an explicitly ended, unscored drill; `active` identifies an unfinished game. Practice results never enter benchmark Elo. A match row uses `white`, `black`, and `result`; its `score` is null because there is no single designated learner. Missing usage values are unknown, not zero. Elapsed time includes pauses and infrastructure delays.

The trace `record` preserves native event structure inside a portable wrapper containing `run_id`, `source_sequence`, `timestamp`, and `kind`. These are research exports, not resumable provider session files. Repeated event representations can appear. The two match traces inherit learning history: use branch ancestry and timestamps to avoid counting that history twice. Provider-returned reasoning/thinking text and summaries are retained; encrypted/signature fields and provider base-instruction state are removed.

`provenance/redactions.json` lists credential substitutions and omitted runtime fields by file and category, without exposing their values. `provenance/ledger-provenance.json` distinguishes original and public chain heads. A redacted snapshot gets a new content address; any changed ledger chain is recomputed. Original experiment files remain untouched.

Folder labels and dashboard selectors are not complete settings histories. Use the exported native turn-context records and settings audit, including documented effort changes. The runs have different context capacities, durations, stopping points, and inference budgets. Historical analysis reports are dated observations and may describe an earlier prefix of a run.

Installed Claude Code/Codex implementations, account directories, authentication files, native resume files, installed dependency trees, and the native Stockfish executable are excluded. The portable setup downloads its chess dependencies separately. The frozen website retains its browser engine and the upstream source/build archive that accompanies it.
