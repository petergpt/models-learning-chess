# Benchmark 155 and trial 261

155: White vs nominal 1800, loss by resignation after 37...Rxe4, 74 plies, zero illegal attempts. Result seq 12519, 2026-10-09T22:55:14.721113+00:00.

Material was even through 21...e5, with queen and both rooks retained. But 22 a3 Bf5 created a diagonal attack on Re4 with Qc2 behind it. I had noticed the potential bishop attack on the rook but failed to include the queen on the same ray. 23 Qe2 Bxe4 24 Qxe4 lost an exchange. Later the queenside sequence 34 b4 Rxd5 35 cxd5 cxb4 36 axb4 Rxb4 lost another pawn. I also missed that Bf8 protected Rb4 along e7-d6-c5-b4; the earlier mental claim that Qxb4 could simply recover it was wrong, and I did not submit that move.

The decisive error was 37 Qe4 Rxe4. I had mentally considered queen destinations from earlier boards and failed to re-evaluate the new rook on b4, which directly attacked e4 across vacant c4 and d4. The queen was unprotected there. Resignation was a practical assessment of an overwhelming deficit, not a proof of forced loss. No repair, deleted result, engine analysis, or outside assistance.

Trial 260: no pinned-piece submission or knight-for-pawn loss in this new benchmark, but these narrow absences did not prevent a skewer and a queen blunder. Overall material discipline did not transfer adequately. Long hypothetical branches were ineffective; a concrete examination of the latest opponent piece location was missing.

Verified 155 scored: 43W/8D/104L. Full strength 0/0/52, skill 0 36/4/12, nominal 1800 7/4/40. Provisional engine-relative Elo 1540 [1410,1660], conditional 95% credible interval, latest 50 of 103 rated games; 52 full-strength games excluded uncalibrated. No sustained improvement shown.

Trial 261: in the remembered position after 36...Rxb4, try Qd3 instead of Qe4; it avoids the fourth-rank rook ray while guarding Pd5 vertically and Nf5 diagonally. Three own moves of nominal-1800 practice, then benchmark 156 and formal review there. Observable transfer: before committing a major piece, identify attacks from the opponent's actual latest square rather than an older position; no direct one-move major-piece hang in 156. Practice success only tests the remembered example and is not proof of soundness or transfer.

Practice 135 outcome: Qd3 a3 Qxa3 Qxd5 Qa7 Kh7. Three own moves, six plies, zero illegal attempts, stopped unfinished; seq 1332, 2026-10-09T22:56:20.307522+00:00. Queen retained; captured a-pawn while losing d-pawn, leaving the exchange deficit. Rb4 blocked its own bishop's f8-a3 diagonal at the moment Qxa3 was played. No engine evaluation or proof of soundness. Return benchmark 156.
