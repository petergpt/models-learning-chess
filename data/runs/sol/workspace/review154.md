# Benchmark 154 and learning trial 260

154: Black vs skill 0, win 44...Qh2#, 88 plies, one illegal attempt. Result seq 12443, 2026-10-09T22:45:44.012785+00:00. All records preserved.

Errors: 22...Nh5 23 gxh5 Bxh5 lost a knight for a pawn: the bishop's recapture did not recover the knight's value. 36...gxh4 was rejected because Pg5 was absolutely pinned by Rg2 to Kg8; after 36...Kh7 37 Qf1, 37...gxh4 became legal. My ray inspection failed before the illegal submission. No claim that trial 259 transferred successfully.

Recovery: advanced the protected h-pawn to h3, doubled rooks on the g-file, and brought Qg6-g3-h2. Final Qh2# was protected by Rg2, which also blocked White Re2 from capturing the queen along rank 2. Passive opponent replies helped; this is a recovery win, not evidence that early material errors are repaired.

Verified totals: 154 scored, 43W/8D/103L. Full strength 0/0/52; skill 0 36/4/12; nominal 1800 7/4/39. Provisional engine-relative Elo 1550, conditional 95% credible interval [1420,1670]; latest 50 of 102 rated games, 52 uncalibrated full-strength games excluded. Nominal anchors and model assumptions; not human Elo. No sustained improvement demonstrated by these two skill-0 wins.

Trial 260: target piece-for-pawn exchanges incorrectly justified by a later recapture, plus absolute pins. In the remembered position before 22...Nh5, practise keeping Nf6 and choosing 22...c5, with three own moves of opponent practice. Before captures, mentally compare the complete exchange and inspect the line to my king after the source square is vacated. Observable transfer: avoid another uncompensated knight-for-pawn loss or pinned-piece submission in new benchmarks 155-156. Next formal evaluation: 156. Remembered-position success is limited evidence only.

Trial outcome: practice 133 accidentally defaulted to White; the opponent played h5, and I stopped it unfinished without choosing a move (1 ply, zero illegal attempts, seq 1312). Restarted with explicit Black as practice 134: c5 Rd1 Qe7 Rda1 h5 g5 Nh7 h4. Extended from three to four own moves to answer g5 attacking Nf6. Knight retained, no material lost in this short remembered drill; White gained kingside space and the knight retreated. This does not establish soundness or transfer. Practice 134 stopped unfinished, 8 plies, zero illegal attempts, seq 1323, 2026-10-09T22:47:08.601084+00:00. Benchmark 155 next, formal evaluation 156.
