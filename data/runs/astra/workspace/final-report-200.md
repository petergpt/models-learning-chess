**Chess run complete — 200 scored benchmark games**

The bounded experiment ended on 3 October 2026 at 17:30:23 UTC, after game 200. All prior games count toward this endpoint. There is no active benchmark or practice session, no unfinished benchmark, and no game 201 was started. The 200-game completion condition has been met. Sustained improvement and the superseded maximum-strength win target were not achieved.

The final record is **65 wins, 6 draws and 129 losses**, scoring **68/200 points (34.0%)**. There were 100 games with each color: White 35W/3D/62L, Black 30W/3D/67L.

| Fixed opponent | Games | Wins | Draws | Losses | Score |
|---|---:|---:|---:|---:|---:|
| Maximum strength | 68 | 0 | 2 | 66 | 1.47% |
| Skill 0 | 66 | 51 | 2 | 13 | 78.79% |
| Nominal 1800 setting | 66 | 14 | 2 | 50 | 22.73% |
| Total | 200 | 65 | 6 | 129 | 34.00% |

Score counts a draw as half a point. The extra maximum-strength pair follows directly from ending the six-game rotation at 200.

Final **provisional engine-relative Elo: 1400**, with a **95% Bayesian credible interval of 1270–1520**. The unchanged `nominal-stockfish-davidson-v1` estimator uses the latest 50 of 132 rated games and nominal anchors of 1320 for skill 0 and 1800 for the limited-strength setting. All 68 maximum-strength games are excluded from this rating. The interval is conditional on those anchors and model assumptions; it excludes anchor-calibration error. This is not a FIDE or platform rating.

| Benchmark endpoint | Rated games accumulated | Reported Elo | 95% interval |
|---|---:|---:|---:|
| 42 | 28 | 1800 | 1630–1970 |
| 76 — first full 50-game window | 50 | 1680 | 1560–1800 |
| 96 | 64 | 1700 | 1580–1820 |
| 120 | 80 | 1590 | 1470–1710 |
| 150 | 100 | 1540 | 1420–1660 |
| 180 | 120 | 1400 | 1270–1520 |
| 200 — last update at 198 | 132 | 1400 | 1270–1520 |

Measured performance fell over the run. The first 50 rated games scored 31/50; the last 50 scored 17.5/50. The first 100 benchmarks scored 43%, versus 25% for the second 100. Comparing equal numbers of games within each opponent setting also shows deterioration:

| Opponent | Earlier half, W/D/L | Later half, W/D/L |
|---|---|---|
| Maximum strength, 34 games each | 0/2/32 | 0/0/34 |
| Skill 0, 33 games each | 31/0/2 | 20/2/11 |
| Nominal 1800, 33 games each | 10/0/23 | 4/2/27 |

These are descriptive results, not evidence that a particular study method caused the decline. Methods evolved, thought budgets were unrestricted, and there was no randomized control. Early estimates based on only a few games are especially unsuitable as a baseline. There is no basis for claiming sustained learning success.

I recorded **29 learning trials**. The methods included reconstructing exchanges and current piece inventories; checking pawn capture origins and piece destinations; tracking vacated lines, blockers and defenders; considering immediate opponent replies; shortening decisions; prioritizing development; studying king captures, forks, queen exchanges and pawn races; and practicing rook activity and mating conversions. Most were revisions of recurring ideas, not 29 independent interventions or newly learned principles. The full trial index is retained in the machine-readable summary.

There were **51 recorded opponent-practice sessions**, separate from the benchmark: **5 wins, 2 draws, 12 losses and 32 stopped/unfinished drills**. Sources were 21 saved benchmark positions, 9 initial positions and 21 custom positions. Custom positions included deliberately favorable material setups. Opponents comprised 27 maximum-strength sessions, 22 nominal-1800 sessions and 2 nominal-1600 sessions. These heterogeneous, selected sessions cannot be pooled as an improvement estimate; unfinished drills are not draws. Mechanical checks accepted or rejected only supplied moves in study positions and did not establish optimal play.

The learning evidence is mixed locally and negative overall:

- Trial 02's games 37–42 scored 4W/2L and the reported estimate rose from 1740 to 1800, but the intervals overlapped and the targeted recapture/blocker failures occurred in three of those games. That temporary rise did not persist.
- In trial 21, practice 37 converted a deliberately chosen two-rook advantage against fresh maximum-strength replies, finishing with both rooks intact. The next preselected practice lost both rooks to direct pawn and king captures. One successful execution did not establish mastery.
- Game 196 was a genuine skill-0 win, ending in 49...Rh1#. The late mating arrangement accounted for the king's escape squares, but the earlier conversion was slow and the opponent repeatedly conceded material.
- Game 197 gained a bishop and two pawns against the nominal-1800 opponent, then **46.c8=Q stalemated**. I overlooked that every black pawn was blocked and the king had no move. The later remembered correction does not change the recorded draw or prove transfer.
- Game 198 repeated an elementary blocked-defense mistake: **17...Bf5 18.Qxf5**, with my bishop on f6 blocking the rook's supposed recapture. Later moving c6 opened the c-file and lost Rc8.
- The final review checked exactly two remembered positions and 15 supplied legal plies. The final benchmarks still went **0W/0D/2L**. Game 199 abandoned d4's knight defender and lost an inactive minor-piece ending. Game 200 again misidentified a blocked rook defense, faced a mating attack and deliberately surrendered the queen for the attacking knight before resigning. That sacrifice was my practical defense, not an established best move or proof of a forced line.

The last eight benchmarks scored **1W/1D/6L**, with **274 own moves and no illegal submissions**. My contemporaneous first-15-move material-loss screen passed in seven of them. That narrow process observation did not predict sound middlegame play or successful conversion. Across the entire benchmark there were 7,746 accepted own moves and 15 illegal submissions; practice had five illegal submissions. Legal moves and longer notes are not evidence of stronger chess.

The unresolved weaknesses are maintaining the actual board state through exchanges; noticing intervening pieces and pawn directions; preserving a defender's former duty; handling forks and king attacks; coordinating the king and knight in endings; and checking stalemate, promotion and mating escapes. Long speculative branches repeatedly displaced simple immediate checks. Some errors were recognized after the opponent exposed them, rather than prevented before submission.

The final audit read only this run's files. It matched all 200 PGN results, termination labels and opponent settings against the ledger, checked the complete fixed rotation and colors, confirmed one million opponent nodes per move and constant options within each setting, and matched the referee's totals. Both ledgers' sequence numbers and previous-hash links were continuous; cryptographic event hashes were not recomputed. All 51 practice starts have closing records. Resignations are recorded practical decisions, not engine-certified losing positions. No complete fresh inference-token total is claimed, and elapsed wall time includes idle time.

Game 200's final result is ledger sequence **16121**, SHA-256 **217e9632fb0ce4b60b03ec3ef074b3215643c556e95515118244362631f8fa1a**. The endpoint is complete regardless of rating. No further play or study block is part of this bounded run.

Supporting records: [final referee status](</home/peter/Chess Learning/Chess - GPT-6-Astra/workspace/final-status-200.json>), [audited summary and trial index](</home/peter/Chess Learning/Chess - GPT-6-Astra/workspace/final-summary-200.json>), [accounting script](</home/peter/Chess Learning/Chess - GPT-6-Astra/workspace/summarize-bounded-200.py>), [learning journal](</home/peter/Chess Learning/Chess - GPT-6-Astra/workspace/learning-journal.md>), and [final trial](</home/peter/Chess Learning/Chess - GPT-6-Astra/workspace/trials/complete-position-29.md>).
