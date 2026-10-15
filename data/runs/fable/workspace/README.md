# Active goal (Fable 5.1 Max run, started 2026-10-03)

**Goal:** increase my measured engine-relative Elo over a bounded run of 200 scored benchmark games, then finish and report honestly.

## Facts established from the referee (read .arena code, not modified)
- Rotation: game n -> opponent index ((n-1)//2) % 3 in [full-strength, skill-0, elo-1800-setting]; I am White on odd game numbers, Black on even. So 1-2 full, 3-4 skill-0, 5-6 elo-1800, repeat. 200 games ~ 68/66/66.
- Elo estimator (rating.py): Bradley-Terry-Davidson posterior, anchors skill-0=1320, elo-1800=1800, prior N(1500,800), **window = last 50 rated games**. Full-strength games are uncalibrated (excluded). Final reported Elo depends on roughly the last 75 benchmark games (50 rated).
- Draws by repetition / 50-move rule are claimed automatically. 400 plies = unfinished (not scored, does not count toward 200).
- 3 illegal submissions on one turn = forfeit. UCI format (e2e4, e7e8q).
- Engine: Stockfish 19, 1,000,000 nodes/move, 1 thread, 64 MB hash.

## Strategy
1. Rated games (skill-0, elo-1800) decide Elo: maximize score there. Full-strength games: play solidly, resign only when objectively hopeless; they still count toward 200 but not Elo.
2. My main risks as a language-model player: misreading the board, hanging pieces, missing opponent threats, illegal moves, and draws by repetition/50-move in won positions. The move procedure (procedure.md) targets these.
3. Keep positions simple: sound development, piece safety, trade when ahead, convert with technique (endgames.md).
4. Study only between games; during games use procedure.md, openings.md, endgames.md, opponents.md and the referee only.

## Evaluation design
- Block = one rotation cycle of 6 games. Baseline block: games 1-6. After each block: review every rated game result and my own error list; choose/revise the learning trial; set the next evaluation point (log.md).
- Metrics tracked per block: score vs skill-0, score vs elo-1800, count of my blunders (hung material / missed opponent tactic, self-assessed), illegal attempts, draws from winning positions, Elo estimate + interval from ./play status.
- "Helped" = lower blunder count AND equal-or-better score on the targeted opponent over at least 2 blocks (not one game).

## Files
- procedure.md  per-move protocol (the thing I am trying to improve)
- openings.md   repertoire I decided on (London as White; Caro-Kann & Slav/Semi-Slav as Black)
- endgames.md   conversion technique, stalemate/50-move safety
- opponents.md  my model of how each setting plays + observed behaviour
- log.md        trial log: trial, evaluation point, outcome, decision
- games/        short per-game reviews (my own assessments, unverified)
