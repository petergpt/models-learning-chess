# Benchmark 156: evaluation and trial 262

Black vs nominal 1800: loss by resignation after 17 Nxe7+, 33 plies, zero illegal attempts. Result seq 12554, 2026-10-09T23:02:09.869707+00:00. Deficit at resignation: two minors plus two pawns; both pairs of rooks still present, queens fairly exchanged. Practical resignation, no proof of forced loss.

History: e4 c6 d3 d5 Qe2 e5 Nf3 Bd6 exd5 cxd5 Bf4 Nc6 Bxe5 Nxe5 d4 Be7 Nxe5 Nf6 Nc3 O-O g3 Bg4 Nxg4 Nxg4 Qxg4 f5 Qf3 Qa5 Qxd5+ Qxd5 Nxd5 Rfd8 Nxe7+.

Errors: e5 was pinned to Ke8 by Qe2 and not adequately defended against the complete exchange. After d4 attacked Ne5, I recognized the absolute pin and used Be7 rather than submitting an illegal knight retreat. This resolved legality but left the original pawn deficit. 11...Bg4 was defended by Nf6, but 12 Nxg4 Nxg4 13 Qxg4 left a minor deficit: I failed to include White's final queen capture. 14...Qa5 did not preserve Pd5, because Qxd5+ was supported by Nc3 and could lead to an equal queen exchange with a pawn won by White. 16...Rfd8 attacked Nd5 but left Be7 hanging to Nxe7+.

Evaluation at 156: trial 259 failed to prevent material loss at 154; trial 260 showed only a remembered knight-retention repair and no new pinned-piece submission at 155, yet 155 lost an exchange and queen; trial 261 repaired the remembered queen destination, and 156 had no direct major-piece hang, but repeated minor losses overwhelmed that narrow result. No convincing transfer or sustained improvement. Long speculative branches continue to miss direct captures on the latest board.

156 scored: 43W/8D/105L. Full strength 0/0/52; skill 0 36/4/12; nominal 1800 7/4/41. Provisional engine-relative Elo 1540 [1410,1660], conditional 95% credible interval, latest 50 of 104 rated games; 52 full-strength games excluded uncalibrated. These measurements do not establish human Elo.

Trial 262: revisit before 11...Bg4 in remembered 156. Try Be6, maintaining bishop safety and reinforcing d5 instead of offering Bg4 to the knight/queen exchange. Three own practice moves at nominal 1800, then benchmark 157. Next formal evaluation 162 (one complete fixed-rotation cycle). Target observable new-game behavior: no minor sacrificed for a pawn or lost to the final recapture, and no piece left directly capturable while attacking another target. Before each commitment focus on the actual moved piece's square and opponent captures, rather than adding longer hypothetical branches. Success in this saved position is not proof of transfer.

Practice 136: Be6 Qb5 Rb8 Qb3 Qc7 Bg2. Three own moves, six plies, zero illegal attempts, stopped unfinished. Result seq 1341, 2026-10-09T23:03:14.432623+00:00. The original pawn deficit remained, but no additional material loss in this remembered drill; both bishops and remaining knight retained, Qc7 guarded Be7 and Be6 guarded Pd5. This is limited remembered-position evidence only. Return benchmark 157, review 162.
