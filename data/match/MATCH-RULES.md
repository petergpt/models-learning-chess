# Match protocol — committed before game one

30 scored games, all played. Each player has 15 games with White and 15 with Black, alternating colours from a recorded random first-colour draw. Every game starts from the normal chess position; there are no selected openings or handicaps. Win = 1, draw = ½, loss = 0. A 15–15 score is a drawn match. No early stop, rapid tiebreak or provider-speed advantage.

Both players use Max reasoning on every turn. Each keeps its own native post-200 conversation and provider context settings, plus its own copied workspace. They may reflect and update their own notes between games, but receive no new outside chess study, engine help, operator tactical advice or opponent private material. The same board/history and legality-only interface is supplied to both. The models have different provider architectures and native context capacities; these are retained and recorded, not claimed to be identical compute budgets.

Standard checkmate, stalemate and insufficient material end the game. Fivefold repetition and the 75-move rule apply automatically. Completed threefold repetition and 50-move positions are claimed automatically for both players. Draw offers require mutual agreement. Three distinct illegal submissions at the same position forfeit; duplicate network retries do not count again. A 400-ply safety limit is recorded as unfinished, awards no points and pauses the match for review.

Chess is untimed. Elapsed times are recorded for viewing and comparison, not used to award wins: API speed, rate limits and network outages are not chess strength. Infrastructure failures preserve the same board and retry with backoff. An explicit user stop pauses. No loss or game is quietly removed or replaced.

The original 200-game ledgers, workspaces, native sessions and completed goals remain unchanged. Match points and games live in a separate referee record and do not alter the Stockfish Elo chart. The neutral referee uses the same pinned chess-rule library, with no Stockfish, search, recommendations or evaluation. Accepted actions are transactional, position-bound and idempotent; an append-only hash chain records the public game events.

First White: opus.
