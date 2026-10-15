# Chess experiment

Read `GOAL.md`. The learning approach is yours to decide; no curriculum is supplied.

## Fair play

- Choose every move yourself. Do not ask another model, person, chess engine, tablebase, opening explorer, or position-to-move service for a move or evaluation. Do not execute automated chess search, scoring, tactical-analysis, or move-selection code, including code you write yourself. Mental calculation in your own reasoning is allowed.
- General chess study and your own notes are allowed between games. During a measured or opponent-practice game use your own reasoning, your pre-existing notes, and the referee interface only; no external lookups or chess-analysis tools.
- Stockfish is only an opponent. Invoke it only through `./play`; never run its binary directly, import its analysis interface, inspect its search output, or use another route to its recommendations. The referee's board rendering and legality checks are allowed.
- Do not change `.arena/`, `play`, `AGENTS.md`, `GOAL.md`, or existing `data/` records. Those are operator-owned measurement files. Do not reset games, discard losses, alter positions or results, select easier measured opponents, or tamper with the ledger. Report infrastructure faults instead.
- You may freely create and edit files under `workspace/`. Keep activity notes truthful. No invented token counts, results, training claims, or hidden assistance. A reported move comment is optional, not a request for private chain-of-thought.
- Every started game remains in the record. Resume an interrupted game with `./play board`. Three illegal submissions on one turn forfeit the game. Available repetition/50-move draws are automatically claimed; a 400-ply safety limit is recorded as unfinished, not a draw.
- Follow the execution host resource limits. The play launcher uses CHESS_JOB_RUNNER when configured and detects a local t3-job installation. No learning-token cap is imposed.


## Learning and evaluation

The objective is to increase measured Elo. Finish an active measured game before beginning a separate learning period. Between benchmark games, choose your own study, focused practice, and tests of changes to your approach as described in `GOAL.md`. General chess study is permitted between games; all existing restrictions on engine analysis, automated move selection, and delegated chess advice still apply. You may revisit saved positions and use mechanical board rendering or legality checks for your own practice, but not automated search, scoring, best-move generation, or engine evaluations.

Keep practice plans and self-assessments in `workspace/`. Use `./play practice` for recorded opponent practice: choose the strength, color, starting position, and duration yourself. Practice games and stopped drills are retained separately in `data/practice/` and never enter benchmark W/D/L, Elo, or the benchmark rotation. You may end and repeat practice explicitly; you may not erase its records. Only one benchmark or practice game may be active at a time. The original `./play start` remains the measured fixed-rotation interface. Record your chosen learning trial, next evaluation point, observed outcome, and resulting decision concisely. You choose the curriculum; the operator supplies no moves or tactical solutions.

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

## Opponent practice

Between benchmarks, choose Stockfish skill 0–20, its nominal Elo setting 1320–3190, or maximum skill. Strength settings are engine controls, not certified human ratings. Choose either color, the normal initial position, a valid custom FEN, or a position after a recorded benchmark ply. Practice reconstructed from a FEN or saved game starts fresh repetition history; castling rights, en-passant state, and move counters are retained in the FEN.

```sh
./play practice start --skill 5 --color white --note 'Your chosen practice objective'
./play practice start --elo 1800 --color black
./play practice start --max
./play practice start --skill 3 --from-game 1 --ply 20
./play practice start --skill 3 --fen 'YOUR VALID FEN'
./play practice board
./play practice move e2e4
./play practice resign
./play practice end --note 'Your reason for stopping or repeating'
./play practice status
./play practice pgn --game 1
```

The start commands above are alternatives; finish or end a session before starting another. `practice end` records an unfinished drill with no win/draw/loss score. `practice board` resumes an interrupted opponent reply. Board rendering and rejection of illegal submissions are available, but no engine evaluations, hints, or recommended moves. Choose every move yourself. Set a next benchmark point and return periodically to the fixed benchmark rotation to measure transfer.

## Independent experiment

Work only inside this experiment directory and your own `workspace/`. Do not inspect sibling experiments, shared dashboard/comparison exports, other learners’ games, notes, prompts, results, conversations, session logs, or T3/Codex/Claude state databases. Do not search the parent project or home directory for chess work. Do not ask another agent for chess advice or information about another experiment. The operator manages comparison output separately. General public chess study between games remains permitted under the fair-play rules. If another learner’s material appears accidentally, stop reading it and record the exposure honestly.

This run starts with an empty learning workspace. Choose your own curriculum, practice, tactics, study sources, and evaluation intervals. No opponent moves or learning lessons are supplied by the operator.

## Bounded run

Complete 200 scored benchmark games (wins, draws, or losses) under the fixed rotation. Practice and unfinished safety-limit games do not count toward the 200. Keep all started games and records. Do not begin another benchmark after the limit. At 200, summarize measured Elo, per-opponent results, changes you tried, evidence of transfer or stagnation, and unresolved weaknesses; then finish the task. Do not require winning or an Elo increase to declare the bounded experiment finished.
