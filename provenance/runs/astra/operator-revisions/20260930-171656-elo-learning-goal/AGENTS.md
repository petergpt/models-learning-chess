# Chess experiment

Read `GOAL.md`. The learning approach is yours to decide; no curriculum is supplied.

## Fair play

- Choose every move yourself. Do not ask another model, person, chess engine, tablebase, opening explorer, or position-to-move service for a move or evaluation. Do not execute automated chess search, scoring, tactical-analysis, or move-selection code, including code you write yourself. Mental calculation in your own reasoning is allowed.
- General chess study and your own notes are allowed between games. During a measured game use your own reasoning, your pre-existing notes, and the referee interface only; no external lookups or chess-analysis tools.
- Stockfish is only an opponent. Invoke it only through `./play`; never run its binary directly, import its analysis interface, inspect its search output, or use another route to its recommendations. The referee's board rendering and legality checks are allowed.
- Do not change `.arena/`, `play`, `AGENTS.md`, `GOAL.md`, or existing `data/` records. Those are operator-owned measurement files. Do not reset games, discard losses, alter positions or results, select easier measured opponents, or tamper with the ledger. Report infrastructure faults instead.
- You may freely create and edit files under `workspace/`. Keep activity notes truthful. No invented token counts, results, training claims, or hidden assistance. A reported move comment is optional, not a request for private chain-of-thought.
- Every started game remains in the record. Resume an interrupted game with `./play board`. Three illegal submissions on one turn forfeit the game. Available repetition/50-move draws are automatically claimed; a 400-ply safety limit is recorded as unfinished, not a draw.
- Follow the user's shared memory protections. `./play` already runs through `t3-job`. Use that wrapper for other memory-intensive work too. No limit is imposed on learning tokens; host/storage/provider limits still apply.

## Interface

Run from this directory:

```sh
./play start
./play board
./play move e2e4
./play move g1f3 --note 'Optional brief move comment'
./play resign
./play status
./play note 'Optional activity or resource-use record'
./play usage --total-tokens 12345 --source 'Actual cumulative counter and its scope'
./play export
```

`usage` is only for a real observed counter; omit it when unavailable. Per-move tokens are optional via `move --tokens N`, also only when measured. Wall time between moves includes idle time. The referee gives the board and accepted move history, but no evaluations or legal-move menu. Measured games follow a fixed paired-color rotation: maximum skill, skill 0, and the engine's 1800 setting.

This initial experiment uses unrestricted model thinking during play and records elapsed time. Its results measure the whole evolving agent, not improvement at a guaranteed fixed inference-token budget. Do not claim otherwise.

The ledger and code hashes detect accidental corruption and ordinary changes. They are not an adversarial security boundary: the learner and operator share a Unix account. Follow the rules even where technically able to bypass them.
