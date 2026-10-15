# Benchmark158 and trial264

Black vs full-strength loss by resignation after17 Qxg8+,33plies,0illegal attempts. Resultseq12645,2026-10-09T23:26:17.918428+00:00. OwnBlackQ,R,N,7P vsWhiteQ,2R,2N,B,6P: rook and two minors deficit offset by pawn (nominal10 points). Practical resignation, no forced-loss proof.

History: e4 c6 d4 d5 e5 Bf5 h4 h6 g4 Bh7 e6 fxe6 Bd3 Nf6 Bxh7 Rxh7 Qd3 Qa5+ Bd2 Qb6 Nc3 g6 Nf3 Bg7 Qxg6+ Kd8 g5 Rh8 Qxg7 Rg8 gxf6 exf6 Qxg8+.

Errors: after g6 I considered Rf7 as a response to Qxg6+, but then Bg7 blocked that rook route. King moved to d8 and castling was lost. QueenG6 attacked the unprotected Bg7, while g5 attacked Nf6 which protected Rh7. Rh8 did not save Bg7; Qxg7 took it. Rg8 attacked White's queen and was initially defended by Nf6. However gxf6 removed the defender AND rooted Qg7 with the new pawn on f6. I missed both changes when expecting the queen to be hanging, and after exf6, Qxg8+ captured the undefended rook. Direct changing-defender failure; trial263 did not prevent major-piece loss in new play. No illegal submissions, but legal choices can still be blunders.

Knowncount158:43W8D107L; fullstrength54losses, skill0 36W4D12L, nominal1800 7W4D41L. Elo unchanged by this excluded fullstrength game; verify status later. All records retained. No external/delegated/automated chess assistance.

Trial264: revisit saved position after16 gxf6 (ply31). Try Re8, putting the rook under Kd8's protection instead of assuming Nf6 still protects g8. Inspect both the moved pawn's new attacks and defenses. Three own practice moves at max, then benchmark159; formalreview162. Target observabletransfer: no major-piece hang caused by using a defender that was just captured or moved. Remembered repair is not soundness/transfer proof.

Practice138 failed: Re8 f7 Qxb2 Rb1 Qa3 fxe8=Q+ Kxe8 Qh8+. Extended from three to four own moves to finish the capture of the promoted queen. Eight plies, zero illegal attempts, stopped unfinished in check; seq1361,2026-10-09T23:29:13.005772+00:00. Queen retained and b2 captured, but rook lost for the promoting pawn despite being protected by the king. Defending a square alone is insufficient: escape squares, blockades and forcing pawn advances matter. This did not repair the major-piece-loss target. Practice remains excluded from measurement.

Trial265 revision before159: use development and earlier king safety instead of unnecessary queen excursions or pawn storms; before moving a major piece, recompute every actual defender after the latest opponent move, then inspect the immediate reply's checks/captures at the chosen destination. No claim that this procedure itself demonstrates learning. Benchmark159 next; formal162 remains. Observable target: no major-piece loss due to stale defenders or discovered-check forks in159-162; measure actual recurrence and Elo, not the length of thinking.
