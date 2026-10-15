# Final summary - Opus 5.5 chess experiment (200 scored benchmark games)

All 200 benchmark games are scored (no unfinished games). No further benchmarks will be started.
Source of the numbers below: `./play status` and `data/ledger.jsonl` (read-only), not my own notes.

## Measured result
| Opponent | W | D | L | Score |
|---|---|---|---|---|
| full strength (unrated) | 0 | 0 | 68 | 0% |
| skill 0 | 49 | 4 | 13 | 77% |
| 1800 setting | 23 | 6 | 37 | 39% |
| rated total (skill 0 + 1800) | 72 | 10 | 50 | 77/132 = 58% |

Referee Elo (provisional engine-relative scale, not human Elo): **1760 [1640, 1890] after 132 rated games**.
Peak: 1840 [1720, 1980] after 104 rated (after G156).
Game endings: 97 resignations, 93 checkmates, 8 threefold repetitions, 1 stalemate, 1 insufficient material.

## By phase (ledger)
| Games | full | skill 0 | 1800 | rated score | illegal attempts |
|---|---|---|---|---|---|
| 1-50 | 0-0-18 | 9-0-7 | 4-1-11 | 13.5/32 = 42% | 21 |
| 51-100 | 0-0-16 | 12-3-3 | 7-2-7 | 21.5/34 = 63% | 13 |
| 101-150 | 0-0-16 | 15-0-1 | 7-2-9 | 23/34 = 68% | 11 |
| 151-200 | 0-0-18 | 13-1-2 | 5-1-10 | 19/32 = 59% | 8 |

Elo trajectory at block checkpoints (rated games in brackets): about 1490-1560 for the first 56 [12-56];
1560 [60], 1610 [64], 1640 [68], 1660 [80], 1690 [84], 1760 [88-96], 1790 [100], 1840 [104, peak],
1810 [108], 1780 [112], 1740 [116], 1720 [120], 1730 [124], 1760 [128], 1760 [132, final].

## Changes tried (one trial per 6-game block, details in PLAN.md)
- T0-T1: baseline protocol and repertoire; then a line audit.
- T2: written safety table with escape squares for every enemy check (rated 0/4 to 3/4).
- T3: compact protocol under a self-imposed token budget (worse, 1/4); T7 dropped the budget for rated games.
- T4-T6: written LINES note and a slider PATH check (illegal moves fell), capture scan, three written lines.
- T8: `workspace/tools/mv` prints the referee board with rank labels and piece lists (pure rendering; no search or evaluation).
- T9-T13: square scans of destination and origin squares, discovery check, fixed order at check nodes
  (king captures first, en passant).
- T14-T15: enemy-diagonal and recapture scans: rated 8/8 over two blocks; Elo 1510 to 1610.
- T16-T25: per-move blunder block, written DEST (destination square) line, pawn path, blocker check: Elo 1640 to the 1840 peak.
- T26-T28: defender audit, from-square lines, alignment (Elo drifted back to 1740).
- T29-T32: a compact checklist (PATH, DEST, BOX, LEAF, LOOSE, OPEN-LINE, GUARD), each item added after the error
  that cost material in the previous block; repetition accepted against the 1800 setting when level or worse.

## Evidence of transfer or stagnation
- Transfer: the rated score rose from 42% (G1-50) to 63-68% (G51-150), Elo from about 1490 to 1760-1840,
  and illegal attempts fell from 21 per 50 games to 8. The gain came almost entirely against skill 0
  (9-0-7, then 15-0-1 and 13-1-2).
- Stagnation: against the 1800 setting the score never improved clearly (4-1-11, 7-2-7, 7-2-9, 5-1-10).
  Against full strength it was 0/68 throughout. After the G156 peak, seven more checklist trials did not raise
  the rating (1720-1760). The intervals overlap heavily, so neither the peak nor the later dip is a reliable
  difference. Each added checklist item fixed the error it targeted, but new error types kept appearing.
- These results measure the whole evolving agent with unrestricted thinking during play, not improvement at a
  fixed inference-token budget.

## Unresolved weaknesses
1. One-move tactical oversights in quiet positions:
   - lines opened by my own move;
   - x-ray recaptures (G197);
   - long bishop diagonals onto a landing square (G198);
   - knight forks of two rooks (G199).
2. King safety: discovered-check nets (G193) and my own king's flight squares in endgames (G197, ...g5#).
3. My own queen trapped on the rim (G194).
4. Legality/path errors on queen moves still happened (G181 x2, G196).
5. Openings against full strength: the Italian 5.d4 main line reached the same losing structure twice (G193, G199),
   and the Caro-Kann Advance lost both times.

## Record-keeping notes
- GAMES.md rows 2, 6, 8, 14, 18 and 20 wrote "0-1" for losses as Black; a correction note is appended there.
- Usage records come only from the session's own total_tokens counters (see `./play usage` entries).
