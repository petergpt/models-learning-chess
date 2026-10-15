# Benchmark 161 and trial 268

161 White nominal 1800: win by 43 Qa8#, 85 plies, one illegal submission (21 Bd4 blocked by own Ne5). Result seq 12881 at 2026-10-10T00:01:20.219006+00:00. Every move mentally selected using referee only.

Opening: e4 Nc6 d4 d5 Nc3 e6 Nf3 Bb4 Bd3 dxe4 Bxe4 Bd7 O-O Bxc3 bxc3 a6 Re1 Nf6 Bd3 O-O Bg5 Be8 Qe2 Ne7 Ne5 b5. 14 c4 bxc4 15 Bxc4 Qxd4 lost the d-pawn because c3 had been its defender; moving c3 removed that root. Rad1 attacked the queen, Qc5. Bxf6 Nd5 Bxd5 c6 Bxc6 Rc8 Bxe8 Rfxe8 gained minors through opponent decisions instead of the expected recaptures. Illegal Bf6d4 overlooked the knight on e5 in the bishop's path; corrected Bg5. Qxc2 Qxc2 Rxc2 traded queens; Rd2 f6 Rxc2 fxg5 traded an enemy rook for my bishop. Rc6 Rf8 Rxe6 Rf4 Rxa6 Rf8 removed both queenside/central enemy pawns. Nd7 Rd8 Rd6 g4 Re7 g5 Nf6+ Kf8 Ree6 Rxd6 Rxd6 removed the last enemy rook while keeping the knight and rook. Nxg4 and Rd1 kept the king away from the a-passer with the d-file barrier; a4-a5-a6-a7-a8=Q followed by Qe4+ Kf7 Rd7+ Kf8 Qa8# finished.

Positive limited evidence: did not lose a major piece to a pawn, defended attacked knight/rook on actual board, connected rooks before trading the last enemy rook, and used a passed pawn plus queen/rook mating net. Negative evidence: collateral pawn defender omission and an own-piece path error recurred. Several opponent decisions donated material; one 1800-setting win does not prove sustained transfer or an improved underlying method.

Verified totals: 161 scored, 46W 8D 107L. Full strength 0/0/54; skill0 38/4/12; nominal1800 8/4/41. Provisional engine-relative Elo 1570 [1450,1690], conditional 95% Bayesian credible interval, latest50 of107 rated; 54 maximum games excluded uncalibrated. Not FIDE/platform Elo, assumes nominal anchors/model and excludes systematic calibration error. Formal review remains game162.

## Learning trial 268

Weakness: a pawn break may remove an existing defender of another pawn/piece. Try Qe3 before committing to c4, supporting Pd4 and reacting to actual opponent threats. Observable transfer in next benchmark: a pawn move does not leave a major piece or central pawn newly undefended without recognizing the consequence. Keep separate any remembered repair from new-game evidence.

Practice141 maximum White from161ply26 after b5: Qe3 Nfd5 Qe4 f5 Qf3 h6. Three own moves, six plies, zero illegal submissions, stopped unfinished; resultseq1390 at2026-10-10T00:02:34.293499+00:00. Queen reacted to knight/pawn attacks, all material and Pd4 remained, but c4 was not played. Final h6 attacks Bg5 and is unresolved at the stopped horizon. This does not prove a sound pawn break, equality, or transfer; it only shows that the d-pawn can be retained over this short remembered line. Decision: retain current-board defender awareness, explicitly account for paths through occupied squares, and evaluate at162 before choosing next trial.
