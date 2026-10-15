# Chess — Opus 5.5 (Max)

Independent autonomous chess-learning run. Read `AGENTS.md` and `GOAL.md`, then use `./play`. Learning notes begin empty in `workspace/`; benchmark and practice records remain separate in `data/`.

The referee uses the same pinned Stockfish 19 release, 1,000,000 nodes per move, paired-color rotation, nominal strength anchors, rating estimator, practice interface, and fair-play conditions as the comparison protocol. The engine is an opponent only. There is no learning-token limit or prescribed curriculum. Stop after 200 scored benchmark games.

Do not inspect other experiments, shared comparisons, or other learners’ notes, records, or conversations. The operator owns `.arena/`, instructions, and measurement records.

Run `./play verify` to check installation and ledger integrity. GPL dependency notices are retained under `.arena/stockfish/` and `.arena/vendor/`.
