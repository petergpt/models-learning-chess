The independent bounded experiment finished on 10 October 2026 at exactly **200 scored benchmark games: 51 wins, 8 draws, 141 losses**. All 200 started benchmarks completed, with zero unfinished benchmarks and no active game. No benchmark 201 was started. The objective of increasing measured strength was not demonstrated; the authorized completion condition was met regardless of rating.

The final referee estimate is **1390 provisional engine-relative Elo**, with a **conditional 95% Bayesian equal-tail credible interval of 1270–1520**. It uses the latest 50 of 132 rated games. The 68 maximum-strength games remain in the results but are excluded from this estimator as uncalibrated. Nominal anchors are skill 0 at 1320 and the engine's 1800 setting at 1800. These controls are not certified human ratings. The interval assumes those anchors and the operator's model, excludes systematic calibration error, and is not FIDE or platform Elo. Games 199–200 were maximum-strength losses; the final estimate therefore remains the estimate after game 198.

| Fixed opponent | Scored games | Wins | Draws | Losses | Score |
|---|---:|---:|---:|---:|---:|
| Maximum strength | 68 | 0 | 0 | 68 | 0.0% |
| Skill 0 | 66 | 42 | 4 | 20 | 66.7% |
| Nominal 1800 setting | 66 | 9 | 4 | 53 | 16.7% |
| All benchmarks | 200 | 51 | 8 | 141 | 27.5% |

Score counts a draw as half a point. Every loss was retained. The fixed paired-color rotation and estimator were unchanged. Practice status separately reports 181 started sessions: 20 completed and 161 stopped or unfinished, with no active practice. None enters benchmark results or Elo. Many were deliberately short replays of remembered positions, not independent new examples.

Measured history gives no sustained improvement:

| Benchmark checkpoint | Estimated Elo | Conditional 95% interval |
|---|---:|---|
| 6 | 1870 | 1410–2460 |
| 24 | 1630 | 1410–1860 |
| 60 | 1500 | 1370–1640 |
| 100 | 1440 | 1320–1560 |
| 120 | 1530 | 1400–1650 |
| 138 | 1560 | 1440–1680 |
| 162 | 1580 | 1460–1710 |
| 180 | 1490 | 1370–1620 |
| 192 | 1440 | 1310–1560 |
| 200 | 1390 | 1270–1520 |

There was no rating at the empty starting state. The six-game estimate used only four rated observations, so its large early value is not a reliable baseline for claiming a precise decline. Later temporary rises, including 1580 at game 162, were followed by weaker measured results. Rolling windows change composition, and intervals overlap; this is not a controlled causal comparison. The last eight benchmarks were all losses. No maximum-strength win or draw was achieved in 68 attempts. The honest outcome is repeated tactical failure and no demonstrated sustained improvement, with a late rating decline from the temporary higher checkpoints.

Methods tried included ordinary center control, development and castling; adapting opening choices from my existing knowledge; mentally counting complete capture exchanges through the final recapture; tracking pawn attacks, knight geometry, pins and bishop rays; checking the origin square for released defenders and opened lines; keeping king escapes available; and practising rook coordination, passed-pawn support, promotion races and conversion. Persistent decision notes were repeatedly revised after failures. Learning periods used mental reconstruction and recorded opponent drills from my own failed positions, followed by the fixed benchmarks at declared evaluation points. No automated chess search, scoring, tactical analysis or move-selection code was used, and no moves or evaluations were requested from another model, person, engine, tablebase or opening service.

Some local changes worked in particular positions. Short remembered drills sometimes preserved a piece or avoided the immediate recorded mate, and some favorable endings were converted. Game 200 used Nfd7 after e5 and avoided game 198's early Ne4–Ng5 knight trap. These are narrow observations, not evidence of reliable general transfer. Other proposed repairs failed even in the remembered drill: practice 178 opened a bishop ray and lost the rook; practice 180's Ng6+ sequence ended with Qxg6 hxg6 and a lost queen. Stopped drills commonly left a new threat unanswered. Several benchmark wins benefited from opponent material gifts, and earlier blunders could coexist with eventual wins. More notes, longer calculation and memorized corrections did not establish stronger measured play.

The unresolved weaknesses are concrete and recurrent:

- Current-board accuracy deteriorates during long hypothetical calculation. Direct pawn attacks, occupied squares and simple movement geometry were still missed. Game 200's Qd7-d4 submission ignored the knight on d6 and was rejected.
- Exchange calculations still omit a final defender or king recapture, or treat a secondary rook as protected when only the first rook is guarded. Bishop rays and queen exchange traps repeatedly caused major losses.
- Checking forks and discovered checks still displace defenders. Game 199's Nc3-e2+ fork won the c1 rook despite the focused checking-fork trial.
- King escape analysis remains unreliable. Game 198 ended in Rg3# after the g-pawn reached g2; the white king supported the checking rook and the knight covered both h-file escapes. Game 200 ended in Qf8# after Qxe6 removed the f7 blocker. A tempting capture or near-promotion repeatedly diverted attention from an immediate mate.
- Isolated pawns, competing passers and rook endings remain difficult to coordinate. Promotion threats were sometimes assessed before verifying the defender's checks and capture sequence. Early material retention did not guarantee a playable ending.

Records and limitations: final totals and rating were verified through ./play status; practice counts through ./play practice status; the final mate through my own saved game-200 PGN. The final status is saved as workspace/final_measurement_200.json, and game-specific reviews remain in workspace/. Operator measurement files and existing records were not edited. Opponent play used ./play and its shared memory wrapper. Temporary admission delays earlier in the run were recorded, not treated as chess progress. Thinking was unrestricted and varied over the run; this measures the evolving agent and its notes, not strength at a guaranteed fixed inference-token budget. No new token counts or per-move usage are inferred here.

One boundary incident is recorded in review162.md: ./play export unexpectedly printed a shared-deliverables path with another model label. Only that printed path was seen; the artifact was not opened, comparison material was not read, and further export calls were avoided. No website was altered or published, and no other learner's material was imported.

The experiment is complete at the prescribed endpoint. All benchmark and practice outcomes remain preserved. The measurement supports an honest final rating and a failed demonstration of sustained learning, not a claim that the tested methods improved Elo.
