# Benchmark126 / Trial202

Black/nominal1800 LOSS by resignation after72Kxb8,143plies,0illegal. Seq10307,2026-10-08T09:01:04.118094+00:00. Full completed PGN/status read. White d7 could promote immediately and kingf3 could not stop it; practical resignation,no forced-mate claim.

Castled5. Two fair pawn pairs;11gxf6 preserved Be7's guard of Nc5,whereas Bxf6 would release it against Qc2. Rc8 added second guard;Ne4 opened c-file;f5 added pawn guard.23Nd4 changed candidateQb5 into cheap knight target;Bxd4/exd4 removed knight before Qb5/Qxb5/axb5. Fair pieces/rooks/queens simplified,local correctness insufficient.

e3 speculative:fxe3 released Whiteg3's pawn guard,permitting Rxg3+ and Rxe3. Rxh5 won pawn;b5 later fell. Rf6 protected e6/h6;Rf7 repaired b7 afterRb8;Kg5 protected h6 afterRh8 but did not guard e6(knight distance),so Re8 requiredRf6. One pawn ahead at47a5.

47h5/b4 48h4/b5 49Kg4/a6 50bxa6/Rg8+ 51Kh3/b6. Kh2/Kh1/Kg1/Kg2/Kxh1 supported promotion. Re7 guarded e6 until WhiteKe5 supportedRxe6 and attacked own rook;Rg7 saved rook. White tooke6/d5. h1Q/Re1+/Kg2/Rxh1/Kxh1 traded promoted pawn for enemy rook but left kingh1 distant from b6/d4 and WhiteKc6.

Kg2/d5/Kf3/b7 reached rook against two passers with king far away. Rg8/Kc7/Rg7+/Kb6/Rg8/Kc7/Rh8 allowedd6.69Rh7+ did NOT force king move:d7 interposed first body on seventh rank,both supported passers now7. Rh8/b8Q/Rxb8/Kxb8 removed one passer for my rook,leaving d7 immediate promotion. Long private king branches missed actual pawn interposition. Rook gain insufficient when king cannot contain two supported passers. No proven winning/drawing alternative asserted.

Trial203 predeclared:MAXBlack own126ply101,51Kf5 insteadKh3,sixownmoves/earliertermination. Retain central king/e6/rook roots,actual pawn attacks and first bodies. Known-position local test only;nextfixed127,formal132.


## Trial203/practice101 and Trial204/practice102 actual results

Practice101 MAXBlack own126ply101:51Kf5/bxa6 52Rf7/Rh8 53Rh7/Rxh7. Stopped on demonstrated whole-rook loss after3ownmoves/6plies,0illegal,unscored;seq1004,2026-10-08T09:06:51.700435+00:00. Rh7 was already under Rh8 attack and had no root; Kingf5-h7 is not adjacent. My mental idea that I could capture Rh8 next ignored the opponent moves first. FAILED local retention, no full repair claim.

Practice102 MAXBlack exact pre-Rh7 FEN from ownpractice101, fresh repetition history:53Ra7/Rxh4 54Rxa6/Rf4+ 55Kg5/Rf1 56Kg4/Kd3. Four own/eightplies,0illegal,unscored;seq1015,2026-10-08T09:07:54.029486+00:00. Full PGNs read. Ra7 stayed outside the existing Rh8 attack; outside h/a pawns exchanged; own rook retained, kingg4 central, e6/d5 versus d4, +1 pawn. Rook ending unresolved; local retention only, no full-save/win/independent transfer claim. Final e6 guarded by Ra6 through b6/c6/d6 vacancies; d5 guarded by e6. Kingd3 guards Whited4. A hypothetical Rh8-a8 reply would place White's rook under Ra7 capture, but that reply was NOT played and is not outcome evidence.

Decision: central king alternative plus correct rook destination passed limited retention test after first alternative failed. Trial205 fixed127 White/full, d4/Nf3/e3/Bd3/castle when actual replies allow, prepare c4 without early pawn collection, check actual roots and opponent capture first. Formal132, endpoint200.
