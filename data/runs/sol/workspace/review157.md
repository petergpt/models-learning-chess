# Benchmark 157 and trial 263

White vs full strength: loss by resignation after 27...Rxa2, 54 plies, zero illegal attempts. Result seq 12610, 2026-10-09T23:13:16.855729+00:00. End position Black R+6P vs White N+4P, practical resignation, not a proof of forced loss. All results preserved.

Material even through move22; queens and one pair of rooks fairly exchanged. 21 Rd3 Bc4 attacked the rook and bishop behind it. 22 Re3 Bxe2 23 Rxe2 traded bishops fairly, but Nxc3 won the pawn while attacking Re2. 24 Re3 escaped that attack but allowed Nd5+: a discovered Rc8 check against Kc2 combined with a knight attack on Re3. 25 Kd3 Nxe3 26 Kxe3 lost an exchange. 26...Rc2 attacked a2 and kingside pawns; 27 Nd2 blocked rank2 but Rxa2 won another pawn. Trial262 had no early knight-for-pawn loss but did not prevent a discovered-check fork causing major-piece loss; no strong transfer claim.

Next learning trial263: remembered position after23...Nxc3. Try24 Re1 rather than Re3, checking all knight moves that uncover the c-file check, with particular attention to whether they also attack the rook's destination. Three own practice moves against max, then benchmark158. Formal review162 remains. Observable improvement in new games: avoid placing a major piece on a square susceptible to a discovered-check fork, not merely escape the present attack. This saved-position reasoning is unverified until played and not proof of overall soundness.

Known count157:43W/8D/106L; full-strength53 losses, skill0 36W4D12L, nominal1800 7W4D41L. Full-strength remains excluded from calibrated Elo; verify status next. No external chess analysis or delegated assistance, no other learner exposure, no fabricated usage counters.

Practice137: Re1 Nxe4+ Kd3 Nd6 Re2 Ke6. Configured --max, referee labels practice-skill-20. Three own moves, six plies, zero illegal attempts, stopped unfinished. Result seq1350, 2026-10-09T23:15:03.551052+00:00. Rook retained, but discovered-check capture Nxe4+ won another pawn because fxe4 would not resolve the c-file rook check. Deficit two pawns remains; narrow remembered repair only, no proof of overall soundness. Return158, formal162.
