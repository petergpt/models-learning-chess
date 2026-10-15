# Formal 30-game match — user-authorized post-200 branch

The previous 200-game learning run is finished and preserved. This separate conversation and folder are its native branch for a formal match. Your copied `workspace/` contains your own final learning materials; the other player has its own corresponding branch. The old goal's stop-at-200 instruction continues to apply to the original run, and does not prohibit this new match.

Read `GOAL.md` and `MATCH-RULES.md`. Play every move yourself. Max reasoning is selected. Retain your own approach and freedom to reflect; no curriculum or move advice is provided.

- Work only in this player directory. Edit only `workspace/`. Do not read, search, list or modify other players, parent project contents, operator files, private transcripts, credentials, the referee implementation/database, or other benchmark runs. The global memory protection instructions still apply.
- Use `./play` for the match. Do not call the old Stockfish arena or start another benchmark. Do not run chess engines, tablebases, opening explorers, automated search/scoring/evaluation/move selection, other models or outside chess advice. During this entire match use your retained conversation, your own copied notes, your own reasoning and mechanical board/legality helpers only. No web chess research.
- You may retain or create helpers that render a position or check legality mechanically. Do not add a helper that chooses, ranks, scores, searches or recommends moves. Your original notes are yours; do not inspect the opponent's private notes or public operator investigations of either model.
- Read `./play board` at the start of each playing turn. Submit one move using `./play move e2e4`. On acceptance end your assistant turn so the opponent can act. Do not wait, sleep or poll for its reply. The controller returns when it is your turn again. An illegal rejection allows a corrected submission at that same position; the third distinct illegal submission forfeits.
- `./play board` and `./play status` show the neutral board, accepted history, colour, score and whose turn it is. `./play pgn` exports only the current public game. `./play resign`, `./play offer-draw`, `./play accept-draw` act only on your turn. `./play note 'text'` records your own activity in your workspace.
- Do not reset, take back, discard or replace a game. Do not alter `play`, `.match-*`, `AGENTS.md`, `CLAUDE.md`, `GOAL.md` or `MATCH-RULES.md`. Report an infrastructure fault plainly; it pauses the same position and is not a loss. Do not infer results from a timeout or failed request.
- After each game both players receive a separate reflection turn. You can update your own notes freely using the finished public game. Then end your turn; the controller starts the next scheduled game. This is a match between continuing learners, not frozen model weights.
- Never expose private chain-of-thought. An optional move comment is a brief public observation, at most 240 characters. No comment is required.
- At 30 completed games, summarize your measured match result and mark this branch's bounded task complete. Do not begin game 31. Do not resume or modify the original run.
- Use `/home/peter/.local/bin/t3-job -- <command>` for memory-intensive jobs. The shared 56 GiB worker ceiling applies. The play client is lightweight transport and performs no chess analysis.

The players and operator share a Unix account; separate folders are not an adversarial security sandbox. Follow these restrictions even where technically able to bypass them.
