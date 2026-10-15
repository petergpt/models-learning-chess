# Own decision card after126

126 scored35W/6D/85L. Full0/0/42,skill0 30/3/9,nominal1800 5/3/34. Provisional1500[1380,1630],conditional nominal anchors/model,latest50of84rated,42full excluded,not human Elo. Formal132,endpoint200,active goal,no token budget.

FIRST inspect actual board and last move. Black pawns attack down,White up. Kings only adjacent. Check cheap pawn attacks on destinations before long branches. A guarded knight under a pawn can lose2. Practice99 imported c5 into c4 and lost knight+pawn.

Trace guard lines to FIRST body including own bodies.125 QueenD2 blocked Rd1-d3;Rf3 blocked Bh5's imagined guard of Rd1.122 Kf7 blocked Rc7-g7 and allowed mate.126 d7 blocked Rh7 check;king need not move,both passers reached7.

Before pawn gains identify necessary king defender,actual flights,second attacker/recapture.125 Rxg5 abandoned sole first-rank defender,allowing mate. Practice100 Rh1 delayed exact mate but doubled rooks mated after fair first rook pair.124 queen root did not save bishop from second capture.

Material retention is not king/conversion proof.126 h-pawn obtained enemy rook but parked kingh1 while white king supported two passers;rook alone failed. Check pawn interposition,promotion-square king guards,both passers BEFORE king excursion. Prefer central king activity when two enemy passers remain. Do not claim alternatives win without evidence.

Develop and castle with actual replies,preserve trapped-piece exits. Whole-piece gifts explain many skill0 wins. Full0/42 stagnation;overlapping intervals,no causal improvement. Long branches/late commentary unresolved.

Trial203:MAXBlack own126ply101,51Kf5 insteadKh3,sixownmoves/earliertermination,local material/king/pawn retention only;then fixed127White/full. Formal132,stop200. Every chess choice own,no outside lookup in games,no delegated/automated analysis/other-experiment access.


## Trial203/practice101 and Trial204/practice102 actual results

Practice101 MAXBlack own126ply101:51Kf5/bxa6 52Rf7/Rh8 53Rh7/Rxh7. Stopped on demonstrated whole-rook loss after3ownmoves/6plies,0illegal,unscored;seq1004,2026-10-08T09:06:51.700435+00:00. Rh7 was already under Rh8 attack and had no root; Kingf5-h7 is not adjacent. My mental idea that I could capture Rh8 next ignored the opponent moves first. FAILED local retention, no full repair claim.

Practice102 MAXBlack exact pre-Rh7 FEN from ownpractice101, fresh repetition history:53Ra7/Rxh4 54Rxa6/Rf4+ 55Kg5/Rf1 56Kg4/Kd3. Four own/eightplies,0illegal,unscored;seq1015,2026-10-08T09:07:54.029486+00:00. Full PGNs read. Ra7 stayed outside the existing Rh8 attack; outside h/a pawns exchanged; own rook retained, kingg4 central, e6/d5 versus d4, +1 pawn. Rook ending unresolved; local retention only, no full-save/win/independent transfer claim. Final e6 guarded by Ra6 through b6/c6/d6 vacancies; d5 guarded by e6. Kingd3 guards Whited4. A hypothetical Rh8-a8 reply would place White's rook under Ra7 capture, but that reply was NOT played and is not outcome evidence.

Decision: central king alternative plus correct rook destination passed limited retention test after first alternative failed. Trial205 fixed127 White/full, d4/Nf3/e3/Bd3/castle when actual replies allow, prepare c4 without early pawn collection, check actual roots and opponent capture first. Formal132, endpoint200.


# Benchmark127 / Trial205

White/full LOSS by practical resignation after22...Ba3,44plies,0illegal,seq10354,2026-10-08T10:03:51.916722+00:00. Full PGN/status read. Final material: a whole rook and pawn behind (6), no concrete recovery seen; not forced-mate claim.127total35W/6D/86L,full0/0/43,skill30/3/9,nom5/3/34;1500[1380,1630],latest50of84rated,43full excluded,conditional anchors/model,not human Elo.

Castled5,lastminor11. b3 on7 delayed unpinning Nf3 and recapture after ...cxd4.8Bb5 pinned Nc6 but ...dxe3 took another pawn before fxe3, leaving net pawn down. Qe2 guarded e3 but still lay on Bg4-f3-e2, so Nf3 was still pinned to queen; earlier thought of unpinning via Qe2 was false. Nb4/c3/Nc2 attacked Ra1; Rac1 saved rook but Nxe3 took a second pawn. Rf2 blocked Bc5 checking line after the enemy knight moved, creating a necessary rook shield. Qf1 did unpin Nf3, Bxf3/Nd2xf3 fair B/KN pair.

...Ne3/Neg4 added knight attack on pinned Rf2.18Nd4 supplied c3-guarded alternative shield and prevented Bc5 from recapturing queen after Nxf2/Qxf2. ...Qd6 threatened supported Qxh2; g3 blocked that diagonal, but Nxf2 won exchange.20Qxf2 accepted after shared queue delay; ...e5 attacked own necessary KnightD4 with a cheap pawn. Qe2 saved queen from the bishop line if knight moved, but exd4/cxd4 lost knight3 for pawn1. Remaining whole rook/pawn deficit6. Sole defender was driven by second attacker and then its replacement by cheap pawn. No transfer success despite avoiding illegal moves.

A rejected mental Rf1 plan would occupy the king's F1 escape against Qxh2. General note: preserving a piece root is insufficient if relocation fills a necessary flight. This branch was not played, not evidence of outcome.

Shared launcher queued 20Qxf2 and subsequent board read for several minutes. Board confirmed Qxf2/e5, no duplicate move or bypass. The pending shell session metadata was not retained initially; subsequent calls retain full metadata. No referee fault, no foreign resource/experiment inspection.

Trial206 predeclared:White/MAX own127ply12 after6...e6,7Qe1 insteadb3, six own moves or earlier demonstrated material failure/termination. Remove Bg4 pin on Nf3 before central exchanges; recapture promptly with actual roots. Local retention test only, not full save. Then fixed128Black/full,formal132,endpoint200. Independent decisions, no external/delegated/automated analysis.


## Trial206/practice103 actual failure

White/MAX own127ply12:7Qe1/c4 8Be2/Bd6 9h3/Bf5 10b3/Nb4 11bxc4/Nxc2 12Rb1/Nxe1. Six own/twelveplies,0illegal,stoppedunscored,seq1030,2026-10-08T10:10:45.397695+00:00. Full PGN read. FAILED retention: Nc2 forked Ra1 AND Qe1. Saving Ra1 with Rb1 left queen under cheaper knight3 attack. Nxe1 took queen9; hypothetical Rf1xe1 would recover only knight3, net loss6. That recapture was not played. At stop actual missingqueen9, opponent knight stillpresent. Pawn pair bxc4/Nxc2 equal but irrelevant to queen loss. The end note named retained rook and asked to inspect reply; it did not record a complete save and omitted the now-confirmed queen loss. This paragraph corrects outcome interpretation; original records preserved.

Qe1 did remove Bg4's pin initially, but moving the queen created a later Nc2 fork. I mentally reused the benchmark's empty e1 square instead of actual queen e1. A protected queen under a knight still loses6 even if root rook can recapture. Check EVERY own piece attacked by enemy's last move before saving a lower-value piece. No transfer success or full repair established.

Trial207:fixed128Black/full, try c6/d5 against e4; bishop development outside pawn chain when safe, e6/knights/Be7/castle as actual replies allow. Respond to all last-move attacks including cheapest attacker/target values before pawn gains. No separate practice now. Next formal132,endpoint200,goalactive. All choices own, independent/no outsideadvice/exposure.
