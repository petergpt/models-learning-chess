# Own review after benchmark 112

Black versus skill0: loss by actual 29.Rxh5#, 57 plies, one illegal attempt. Result 2026-10-07T16:52:57.066673+00:00, sequence9057. Finished PGN and referee result read in full. Own reasoning only, no independent evaluation.

Trial173 tested the d4/d5 branch, not the e4/e5 branch. Castled5, completed all four minor developments10. White offered Bg5 on eight; hxg5 gained a whole bishop. g4 saved that pawn temporarily and blocked Qd1-h5 at the first body. The later g6 body blocked Bd3-h7 and supported Nh5. These were actual local guards, not proof of king safety.

One illegal 13...d5d4: d4 was still occupied by White's pawn. I had spent many private branches analyzing an impossible forward capture. Correct actual13...g6 followed. Selected-route checking failed again.

14...Nxe5/15.dxe5 fairly exchanged knights but created a pawn fork of Nf6 AND Bd6. I only answered the knight attack with Nh5. exd6/cxd6 cost a whole bishop for a pawn, and Qxg4 removed the former h-pawn. Material became equal. e5 uncovered Bd7's queen attack but removed the e6-d5 pawn guard; actual d4 was now legal and protected by e5. Bc6/Bxd5 and delayed exd5 fairly traded bishop/knight; Nxf4 won a pawn during the delay. Nxd3+/Qxd3 fairly exchanged the last minors. One pawn ahead, queens and two rooks each.

Rc8/Qb6 activated heavy pieces. White g5/h5 approached the king. My Rf8 placed an own body on f8; the claimed future Rf7 defense remained blocked by Pf7. gxh5/Rg6+/fxg6/Qxg6+ gave a whole enemy rook for the f-pawn, leaving an extra rook and pawn before the final move. I answered Kh8 while relying on my h5 pawn to block Rh1. Actual29.Rxh5# removed that last body: Rh5 checked Kh8, Qg6 covered G8/G7/H7, and Rf8 was an own flight blocker. At mate both sides had five pawns and a queen, but I had two rooks versus one: material advantage five did not matter.

My private analysis substituted imagined Qh6+ branches for the actual queen remaining on g6. I missed the simple rook capture of the shield. The h-file pattern from earlier losses recurred even against skill0. Early castling and narrow fair-exchange accounting did not repair later pawn forks or royal-flight/body checks. Trial173 failed piece-retention, path and king-safety targets. Huge speculative branches and severe commentary gaps remained; no process improvement claimed.

Observed after112: 30W/5D/77L. Full0/0/38, skill0 27/3/8, nominal1800 3/2/31. Current provisional nominal engine-relative1470 [1350,1590], 95% Bayesian equal-tail interval; latest50of74rated,38uncalibrated full games excluded. Anchors1320/1800, systematic calibration error excluded, not human Elo. Same estimate as formal108; no sustained transfer established. Formal114, endpoint200. No new usage counter recorded here.

## Trial174: finite king-defense replay

One Black/max practice from my own112ply51, after26.Rf6. Initial material one pawn ahead and otherwise equal, ownKg8/Qb6/Rc8/Rf8, WhiteKc1/Qd3/Rf6/Rh1. Own candidate26...Rfe8 clears f8 instead of capturing h5; adapt to the actual opponent. At most four own moves or natural completion. Target: retain a real legal king flight after checking captures, account for the current queen square and the first rook-file body, record material costs honestly. Stop unscored at the bound if still active. A surviving short replay is not a full save or measured transfer. Then fixed White/nominal1800 benchmark113; formal114 unchanged.

Practice86/Trial174 LOSS: Rfe8 hxg6 Kg7 Rxf7+ Kg8 Rh8+ Kxh8 Qh3+ Kg8 Qh7#. Five own moves/ten plies/zero illegal. One explicitly announced extension beyond four own moves answered Qh3+ and reached actual mate. Result2026-10-07T17:03:28.113916+00:00,sequence795; full practice PGN read. Excluded benchmark/Elo.

hxg6 and Rxf7 removed two own pawns; Kxh8 captured a whole enemy rook. Final material extraR5 minusPawn1, advantage four, yet actualQh7# was supported by WhitePg6 and Rf7. Rf7 controlled f8; Qh7 covered g7/h8. A king cannot take a pawn-supported queen. Empty f8 from Rfe8 was not a legal escape after Rxf7. The replay failed; the remembered position was not saved. Severe private branching/commentary gaps persisted. The four-move bound was extended once explicitly, not secretly claimed as the original bound.

Trial175 for fixedWhite/nominal1800 113: adaptive d4/c4 development and early legal castle, but before any central capture inspect every target attacked by the new pawn, and before opening a king file consider the actual shield capture and current queen/rook flight controls. Observe own whole losses, pawn costs, legal-route rejection and king survival. Own manual comparison of112/86 supplies this hypothesis; no external source or independent evaluation. Review113 outcome, formal114, endpoint200. A remembered defense failure and skill0 material gifts supply no strong transfer.
