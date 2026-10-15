# Match vs Astra - 30 games (my own notes)

## Facts
- 30 games, colours alternate; first White is me: I am White in odd games (G1, G3, ...), Black in even games.
- Each playing turn: `./play board` first, then ONE `./play move <uci>`; once accepted, end the turn (no waiting/polling).
- UCI: e2e4; castling e1g1/e1c1/e8g8/e8c8; promotion e7e8q. Three distinct illegal submissions at one position forfeit.
- `./play offer-draw` / `accept-draw` / `resign` act only on my turn. Threefold and 50-move are auto-claimed for both.
- 400-ply safety limit = unfinished, no points: when winning, convert directly (trade pieces, push passers, mate).
- Pure rendering helper: `python3 workspace/tools/fen2board.py '<FEN>'` (labelled board + piece lists).
- Move comments are public (max 240 chars) and optional; keep them to brief observations or omit them.

## Opponent
- Astra is another post-200 learning model, not an engine. Expect loose pieces, missed tactics, maybe illegal tries.
  Assume a level roughly like mine until the games show otherwise.

## Policy (differs from the engine run)
- Do not resign early: the opponent can blunder back or fail to convert. Resign only when totally hopeless.
- Draws: offer or accept only when my position is worse, or in a dead-level ending. Avoid repetition when better.
- Solid openings I know, every piece defended, punish loose enemy pieces, simplify when ahead.

## Openings
- White 1.e4.
  - 1...e5 2.Nf3 Nc6 3.Bc4: vs 3...Bc5 play 4.c3 Nf6 5.d3, then O-O, Re1, h3, Nbd2-f1-g3, a4, and d4 when ready.
    vs 3...Nf6 play 4.d3. (G193/G199: 5.d4 led to an early queen trade and ...Nf4/...Bb7 pressure on g2/f3.)
    Match line: 6.O-O d6 7.b4 Bb6 8.a4 a6 9.a5 Ba7 10.h3 d5 11.exd5 Nxd5 12.Qb3 Be6 13.Bg5 (G5 13...Qd6 15.Ne4!).
    v 13...Qd7 14.Re1 f6: G7/G9 15.Bd2 16.Na3 was slow and d3 fell after ...Bf7/...Nf4 (G9); try 15.Bh4 + Nbd2.
    PREFERRED (G11, good position until a blunder): 6.O-O d6 7.Bb3 Be6 8.Nbd2 d5 9.exd5 Nxd5 10.Re1 Bd6 11.Nc4!
    (hits Bd6/e5) f6 12.Nxd6 Qxd6 13.d4 exd4 14.Nxd4 Nxd4 15.Qxd4 c5 16.Qe4 with the bishop pair and Q+R on e6.
    G13 16...Rae8 17.Bd2 Bf7 18.Qd3 Qc6 19.Qg3 Bg6 20.Qf3 c4! (cuts Bb3; 21.Bd1 passive) = . Improve: 16...Rae8 17.h3
    (luft first; the e-file back rank was a theme all game) and meet ...c4 with Ba4/Bc2 ideas; avoid 29.a4?-style levers
    that give Black's queenside majority a passed a-pawn.
    (17.h3 checked at the board in G15: 17...Bf7 hits Qe4 down the e-file and Re1 is loose - so 17.Bd2 again.)
    G15: 17.Bd2 Bf7 18.Qd3 Qc6 19.Bc4! (stops ...c4; better than 19.Qg3) Nb6 20.Bb5 Rxe1+ 21.Rxe1 Qd5 22.Qxd5 Bxd5
    23.Re7 Rf7 24.Re8+ Rf8 25.Rxf8+ Kxf8 26.a3 = bishop pair v B+N. Then 28...Nc4 29.Bxc4?! Bxc4+ gave an opposite
    bishop ending that only Black could win (active king, ...c5-c4/...b5 majority). Keep the pair: 29.Bc1.
    G17 (draw): same moves to 28...Nc4 29.Bc1! a6 30.Ba4 b5 31.Bc2 g6 32.f3 f5 33.b3 Ne5 34.Bf4 (pin) Ke6 35.Ke2
    c4 36.b4 Kf6 37.Ke3? g5! - my king on e3 blocked the f4-d2 retreat, so 38.Bxe5+ was forced (Bg3? f4+ forks).
    Same-coloured bishops, every pawn locked: draw. Keep the king off the bishop's retreat line (37.h3 or 37.Kd2),
    and open the position for the bishops earlier (a4 v b5, or h3+g4 before Black's ...f5/...g5 gains space).
    G19 (draw): 18.Qf3 (new) Qc6 19.Rad1 c4 20.Bc2 b5 21.Qh3! Bg6 (forced: Qxh7+ ideas) 22.Bxg6 hxg6 (doubled g-pawns)
    23.Qg4 f5 24.Qf3 Re6 25.Rxe6 Qxe6 26.Bg5 (opens the d-file v Nd5) Nf6 27.Bxf6 Rxf6 28.Qd5 Qxd5 29.Rxd5 a6 = R ending
    with my better structure. Play h3 (luft) early in this line: with no luft, Rxd5?? Qe1# and Rd8?? Rxd8 Bxd8 Qe1#
    were mates all middlegame and limited my rook.
    G21 (loss): 21.Qh3 g6 (not ...Bg6) 22.Bh6 Rxe1+ 23.Rxe1 Re8 24.Rxe8+ Bxe8 25.Qf3 Bf7 26.h3 Qd6 27.Be4 f5 28.Bc2
    a5 29.Qd1?! b4 30.Qd4 Qf6 31.Qxf6?! Nxf6 32.Bd2 b3! 33.axb3 cxb3 = Black's a/b pawns cramped my a2-b2-c3 and
    later broke with ...a4-a3. Improve: stop the majority before it reaches the 4th rank (29.a3, or cxb4 when ...b4
    comes), keep queens until it is fixed, and v ...b3 hitting Bc2 consider Bb1 (keeps a2) instead of axb3 cxb3.
    G23 (loss): G15 line to 19.Bc4, then 19...Rxe1+ 20.Rxe1 Re8 21.Bb5 Rxe1+ 22.Bxe1 Qe6 (hits loose Be1) 23.Bd2 a6
    24.Bc4 b5 25.Bxd5 (25.Be2?? illegal - my Qd3 blocked c4-e2; Bb3? c4 forks Q+B; Ba2 gets buried by ...c4) Qxd5
    26.Qxd5 Bxd5 = OCB ending where only Black can play (my light pawn g2 a target). Better: keep both rook pairs
    (no 21.Bb5 trade), or retreat 21.Bb3/Bf1 early so ...a6/...b5 do not gain space with tempo.
    G25 SLOW LINE (very good for me until a one-move blunder): 6.O-O d6 7.h3 Be6 8.Bb3 d5 9.Nbd2 Re8 10.Re1 Bd6
    11.Nf1 h6 12.Ng3 Qd7 13.Qe2 Rad8 14.Be3 dxe4 15.dxe4 Bxb3 16.axb3 a6 17.Qc2! (guards b3 AND e4 - with Be3 on e3
    the queen on e2 does NOT see e4; 17.Nf5?? Nxe4 would drop a pawn) Qe6 18.Nf5 Bf8 19.Rad1 Ne7 20.N3h4 Kh7
    21.Nxe7 Bxe7 22.Nf5 Bf8 23.f3 g6 24.Ng3 Nd7 25.c4 (blocks Qe6-b3) Bc5 26.Nf1 b6 27.Bxc5 Nxc5 28.Ne3 Qc6 29.Nd5
    Kg7 30.Qc3! (pins e5 to Kg7) Nd7 31.b4 Nf6 32.Rd2 Nxd5 33.exd5! (opens e-file, pin again) Qf6 34.Rde2 (3 v 2 on
    e5) c6 35.Rxe5 +1, then 40.Re7+ 41.Qe6+ Qxe6 42.dxe6 = R ending +1 with e6 passer. Repeat it.
    G27: identical to 28.Ne3, then 28...c6! (stops Nd5) 29.b4 Nd7 30.Qa4 Ra8 31.Rd2 b5 32.Qb3 Nb6 33.c5?? Qxb3 - my
    c4 pawn was the only blocker on e6-d5-c4-b3 between the queens. Level at move 32; play 33.Red1/Kh2, not c5.
    G29: same to 29...Nd7, then 30.Qc3 Nf6 31.Qa3 Qc8 32.Rd3 Rxd3 33.Qxd3 Rd8 34.Qc3 Qe6 35.c5?! b5 36.Rd1 Rxd1+
    37.Nxd1 = Q+N each. But c4-c5 gave up d4 for good (no c-pawn to cover it) and ...b5/...c6/...g6/...h5 took every
    square from my knight; Black's knight sat on f4/d4. Keep c3/c4 covering d4; do not close with c5 v ...b5.
  - 1...c5 2.c3. 1...e6 2.d4 d5 3.Nd2 or 3.e5. 1...c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2.
  - 1...d5 2.exd5 Qxd5 3.Nc3. 1...Nf6 2.e5 Nd5 3.d4. 1...d6 / ...g6: classical d4, Nc3, Nf3, Be2, O-O.
- Black:
  - vs 1.e4 Caro-Kann 1...c6 2...d5. Advance: ...Bf5, ...e6, ...c5, ...Nc6; vs 4.h4 ...h5. Do not park the queen on a6.
    G24 Classical (good for me until move 42): 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3
    10.Qxd3 e6 11.Bd2 Ngf6 12.O-O-O Be7 13.Ne4 Nxe4 14.Qxe4 Nf6 15.Qe2 Qd5 16.Kb1 O-O (not O-O-O: Ne5-xf7 forks)
    17.c4 Qe4+ 18.Qxe4 Nxe4 = with a strong Ne4; then ...Rfd8, ...Bf6, ...Bxe5, ...Rxd1+, ...b6, ...f5 gave me the play.
    G26: same to 15...Qd5, then 16.c4 (before Kb1) Qe4 17.Qxe4 Nxe4 18.Be3 Bf6 19.Nd2 Nd6 20.c5 Nf5 21.Ne4 Ke7
    22.g4 Nxe3 23.fxe3 Rhd8 24.Nd6 b6 25.Rhe1 bxc5 26.dxc5 Rab8 27.b3 Rb4 (hits g4) 28.e4 = active for me (castling
    was not needed: the king on e7 was fine). Then 28...Bd4?? 29.a3! (see lessons). Keep 28...Rb6/...Rd7 instead.
    G28: same to 27...Rb4, then 28.Nc4 Rb5 29.Rxd8 Kxd8 30.Nd6 Rxc5+ (+1) 31.Nc4 Ke7 ... 38...Rxa2 39.Rxc5 = R+B+5
    v R+N+4. Third good ending from this line. In it keep my king central (f7/g7/h6 need it), not on a6/b5.
  - vs 1.d4 QGD: ...d5, ...e6, ...Nf6, ...Be7, ...O-O, later ...c5 or ...c6.
    Match line (G12, level): Tartakower to 10.Rc1 dxc4 11.Bxc4 c5 12.Qe2 cxd4! 13.Nxd4 Nd5 14.Bxe7 Qxe7 15.Nxd5 exd5
    16.Bb3 Nf6 17.Rfd1 Rac8 18.Rxc8 Rxc8 19.h3 Ne4 20.Bc2 Qe5 21.Bxe4 dxe4 22.Qb5 Qxb5 23.Nxb5 Ba6 24.Nd6 Rc2
    25.Nxe4 Rxb2 = (B v N, 5 v 5). Better than 12...a6 (G8/G10 gave White e4-e5 attacks). The ending needs care (G12).
    G14: 14.Bxd5 exd5 15.Bxe7 Qxe7 16.Rfd1 Nf6 (guard d5) 17.Qf3 Rfd8 (third guard) 18.h3 Ne4 19.Nxe4 dxe4 20.Qg3 = but
    then Qg3/g4 + Nf5 aimed at g7 (Qxg7#) and my Bb7 + e4 were loose. Keep a defender near g7 (...Kh8/...Qf6) and
    the bishop protected; after the queen trade 25...Ba6! (+...Bd3 for e4) was the safe square, not 25...Bc8?.
    Lasker (G16, good): 4.Nf3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 c5
    12.O-O Nc6 13.Re1 Qd6 (queen off the e-file: e4 dxe4 Bxe4 then Bh7+ would hit Qe7) 14.e4 dxe4 15.Bxe4 cxd4
    16.cxd4 Nb4 17.a3 Nd5 18.Bxd5 Qxd5 19.Re5 Qd6 20.Qb3 Qb6 21.Qxb6 axb6 = (IQP v doubled b-pawns). Not ...Be6
    while my knight is on c6: d4-d5 forks. After 22.d5 Rd8 23.Nd2? f6! 24.Re4? Rxd5 I was a pawn up.
    G18 same to 21...axb6, then 22.Rb5 Ra6 23.Ne5 Rd8 (d4 loose) 24.Rb4 Be6 25.a4 Bd5 26.Nd3 Kf8 27.Nf4 Bc6 28.Ne2
    b5! (White's back rank: axb5? Rxa1+ and mate) 29.Nc3 bxa4 30.Rd1 Ra5 31.f3 a3 32.Ne4 a2 33.Ra1 Bd5 = Black better
    (+1, a2 pawn ties Ra1). The Lasker ending is good for me; the losses came from my own later errors.
    G20 same to 24...Be6, then 25.Kf1 Bd5 26.g3 Kf8 27.Ke2 Ke7 28.Ke3 f6 29.Ng6+ Kd6 30.Nf4 Bc6 31.d5 Bd7! (31...Bxd5?
    32.Nxd5 Kxd5 33.Rd1+ skewers Rd8) 32.Kd4 Rc8 33.Rc4 Rc5! 34.Rxc5 bxc5+ 35.Kc4 b5+ 36.Kb3 g5 37.Nh5 Kxd5 (+1,
    connected b/c passers) 38.Rd1+ Ke6 39.Re1+ Kf7 (traps Nh5) 40.f3 Kg6 41.g4 c4+ 42.Kb2 Rd6 43.Re2 Rd3 44.Rf2 Bc6 -
    winning. Then 45.f4 gxf4?? 46.Nxf4+ forked Kg6 and Rd3 (exchange lost, game lost). 45...Rd2/Rd8 first kept +1.
    G22 same to 32...Rc8, then 33.h4 (new) Rc2! 34.Rf1 b5 35.Rb3 Ra4+ 36.Ke3 = active for me. Then 36...Bf5?? took
    the only guard off b5 (37.Rxb5), and after 37...Rxa3+ 38.Kd4 Ra4+ 39.Ke3 Kc7?? 40.d6+! opened the 5th rank
    (Rb5 x Bf5): a piece lost. Keep Bd7 on d7 while it guards b5; keep my king off c7/e7 while d5-d6+ can discover.
  - vs 1.c4 ...Nf6 with ...e5 or ...e6/...d5. vs 1.Nf3 ...d5, ...Nf6.

## Checklist before every move (T32, written briefly)
0. RAY SCAN (mandatory, LAST step before every submission, above all for QUEEN moves): on the rendered board,
   walk all 8 rays outward from the destination square to the first piece (rank, file, both diagonals) and
   look at the 8 knight squares and the enemy pawn squares. Any enemy Q/R on a straight ray or Q/B on a diagonal
   ray = the square is attacked. Then compare value and defenders. G10 Qxb2?? (ray north: Qb6) and G11 Qe8+??
   (ray south-west: d7 empty, Qc6) both lost the queen at once; the scan would have shown each in one line.
   ENEMY KING SQUARES (G25 43.Rh7?? Kxh7, a +1 rook ending thrown away): the enemy king attacks all 8 squares
   around it. Before any move, ask "is my landing square NEXT TO the enemy king, and is my piece protected there?"
   I had calculated ...h5 e7 lines from h7 and never looked at the king on g8 one square away.
   MY QUEEN'S RAYS (G27 33.c5?? Qxb3, queen lost for nothing): before ANY move, walk the 8 rays from MY QUEEN (and
   king/rooks) to the first piece. If the first piece is my own pawn/piece and the NEXT one is an enemy Q/R/B, that
   unit is a shield - moving it (even a pawn push "with tempo") hangs whatever is behind it.
   PAWN SCAN (part of step 0, for EVERY piece move, rook/king included): name each enemy pawn that touches the
   destination diagonally. CAPTURES TOO (G24, threw away +2): 42...Rxb4+?? 43.axb4 - the target pawn b4 was guarded
   by the a3 pawn diagonally behind it. Before taking any pawn, look at the two squares diagonally BEHIND it
   (for a white pawn on b4: a3 and c3; for a black pawn on b5: a6 and c6). An enemy pawn on my 2nd rank (a2 v b1) captures onto my 1st rank AND PROMOTES: G13
   48.Rb1?? axb1=Q ended a level ending in one move although I had written "a2 attacks b1" several times before.
   EN PASSANT: before any two-square pawn push, look at both squares beside the landing square: an enemy pawn there
   takes en passant (G15 52.b4?? cxb3 e.p. - the c4 pawn got a passed b3 pawn next to my 1st rank).
   DOUBLE STEP: the square in between must be empty of MY pieces too (G16 32...g5 was illegal: my Kg6 stood on g6).
   PIN SCAN: list every enemy rook/queen/bishop line through my king. A pawn or piece standing alone between that
   piece and my king is PINNED and protects nothing. G16: Re7 + Kh7 pinned g7, so f6 (guarded only by g7) was really
   unguarded: 29.Ne8 then 30.Nxf6+! won it back with check. Before ANY king move, scan its new lines this way.
   PIN + PAWN (G29 45.Ng4? hxg3+ 46.Kxg3 f5!): a piece pinned to my king that an enemy PAWN can attack is lost
   (pawn takes piece; protection does not help). Before blocking a line to my king, or recapturing with the king
   onto such a line, ask which enemy pawn can hit the blocker next.
1. OPP: what does the opponent's last move attack or threaten; what did it stop guarding?
2. PATH: every square a slider crosses (queen moves too), done before writing the command - MY OWN pieces block too
   (G17 38.Bd2 was illegal: my Ke3 stood on f4-e3-d2; G23 25.Be2 was illegal: my Qd3 stood on c4-d3-e2). Before a KING move, check that it does not block the retreat
   line of my own piece that a pawn can attack next (G17 37.Ke3? g5! left Bf4 only Bxe5 or Bg3? f4+).
3. DEST: every enemy rank/file/diagonal (long ones too) and knight jump onto the landing square; my defenders;
   pieces lined up behind a capturer (x-ray). Enemy rook facing my rook on an open line: is mine protected?
   When counting captures on any target, add batteries behind (Q behind R on a rank, Q behind B) on BOTH sides (G6).
   Before capturing a PAWN, trace its defenders along the WHOLE file/rank/diagonal, not only adjacent squares: G10
   46...Qxb2?? - b2 was guarded by Qb6 four squares up the open b-file (b3-b5 empty); queen lost, game over.
4. BOX: flights of my king (also in endgames and when it is advanced) and safe squares of any rim piece, my queen too.
   MATE SCAN (every move once my king is boxed): list EVERY enemy check after my move; for each, test each flight
   square with the PAWN SCAN (an enemy pawn on d6 covers c7 AND e7), knights, the enemy king, and MY OWN pieces
   standing on flight squares. G18 64...Rd2?? 65.Rb8#: Kd8, c7/e7 covered by the d6 pawn, d7 by Ke6+Ne5, e8 blocked
   by my own bishop. I had even looked at Rb8+ and "answered" Kc7 - illegal because of the d6 pawn.
   Is my king on a line with an enemy R/Q/B with only ONE enemy unit between (a discovered-check battery)? Step off (G7).
5. LEAF: at the end of each line, all opponent checks and captures, including discovered checks and knight forks.
   KNIGHT RECAPTURE FORK (G20, threw away a won ending): when I capture a pawn that an enemy knight can recapture,
   or when a knight checks me, write the 8 squares the knight attacks FROM ITS NEW SQUARE. 45...gxf4?? 46.Nxf4+ hit
   Kg6 and my Rd3 at once. A rook guarded only by a pawn is still lost for a knight (the exchange).
   Captures WITH CHECK first (even "sacrifices" like Qxf8+): follow them 2 more plies for pins/skewers on my king's line.
   PAWN PUSH WITH CHECK = DISCOVERED ATTACK (G22): before a king move, list enemy pawn pushes that would give check
   on the new square and the line each push OPENS (39...Kc7?? 40.d6+ opened b5-f5: Rb5 took my Bf5).
   Include DISCOVERED checks: a pawn push/promotion that unblocks a rook onto my king (G7 57.Rxa1?? c1=Q+ via Rb2).
   ENDGAME KING MOVES v a knight: for each king square, list every knight check that CAPTURES a pawn (G12 38.Nf5+
   Ke6?? 39.Nxg7+ and 41.Nxh6 lost two pawns; 38...Kf8 kept g7). Also check which PAWNS guard a square before
   assuming a recapture there (G12 64...Bxf7 65.Nxf7: e6 guarded f7, so ...Kxf7 was impossible).
   If my line relies on a follow-up AFTER an enemy capture ("Rxd2 Qd1+"), redraw the board after that capture: the
   capturing piece now guards new squares, often the one I wanted (G8 31.Rxd2 guarded d1, so Qd1+ was impossible).
   SAME ERROR AGAIN in G14: 27...Bb7?? planned 28.Nxb7 Rxd8 - but a knight landing on b7 guards d8 (a5, c5, d6,
   d8). Rule: for every capture in my line, write the 8 knight squares / the lines of the capturing piece FROM ITS
   NEW SQUARE before I count the next capture.
6. LOOSE: my undefended pieces after the move; for each enemy check or capture, everything that piece then attacks.
   CHECK + LOOSE PIECE (G21): an enemy bishop check that also hits my loose bishop (40...Bc4+ v Ke2 and Bb5) forces
   a trade on THEIR square; then do the knight-recapture fork scan (41.Bxc4 Nxc4 hit Be3 AND b2). I had even listed
   "...Bc4+ ideas" before the move and still played 40.Be3. Before moving a bishop to a rim square, list enemy checks
   that would attack it there.
   Loose PAWNS too: list enemy queen checks; a check that lands on a loose pawn's file/diagonal wins it with tempo
   (G8 Qc7-d7 left a5 loose: 50.Qa8+ Kg7 51.Qxa5).
7. SELF-BLOCK: does the moving unit land BETWEEN one of my defenders and what it defends? G18 42...Rc4 blocked Bd5-a2
   (43.Raxa2) and 46...Re6 blocked Bd5-f7 (47.Rxf7) - two pawns lost to the same error in one game.
   OPEN-LINE / GUARD: what line the moving unit (or a recapture I rely on) stops blocking; which squares next to my
   king it stops guarding. LAST GUARD (G22 36...Bf5?? 37.Rxb5): name every unit the moving piece defends now; if it
   is the ONLY defender of anything attacked, the move drops it. GUARD UNDER ATTACK (G26 28...Bd4?? 29.a3!): if my new
   piece is defended ONLY by a unit that the opponent can hit with a pawn/tempo (Rb4 v a2-a3), I lose one of the two.
   THE KING TOO (G23 29.Ke2?? Bxg2: Kf1 was g2's only
   guard against the enemy bishop) - in endings the king is usually the last guard of its pawns. Also the opponent's last move: which lines did ITS moved piece open onto my pieces (G5)?
   And which of MY squares/pawns the moved piece stopped guarding (Qe7 left e6: Bxg6 fxg6 Nxe6+ fork, G6).
8. RACE (endgames with passers on both wings): give each of my pieces ONE job (knight v the rook pawn from in front,
   king v the enemy king's raid), then count moves to queen for both sides incl. squares my knight must reach (G9).
   BIND: before moving the piece that keeps the enemy rook passive (G19 Ke5 shut the rook out of d6/e6/f6), count
   the race that follows once that rook is free (39.Kf4 let ...Re6-e2, ...Rxb2, ...Rg3 x c3/h3).
   SPLIT PASSERS (G21): two passed pawns one file apart (a + c) plus my king do NOT run by themselves: a lone enemy
   king between them (Kc5 covers b4/b5/b6/c4/d4/d5/d6) holds them while its knight eats the other wing. Count the
   knight raid (pawns it takes + moves to queen) against my plan, and keep my far-side pawns where the knight
   cannot reach them; a pawn safe only because enemy pawns block the knight's squares (h4 v f5/g6) dies when they move.
9. EDGE KING v R+K (my king next to my rook pawn): a king on the rim with the enemy king two files away is a mate
   pattern. G19: K h6 + P h7 v enemy K f6 = ...Rh1#; K h8 + P h7 v enemy K g6 = ...Ra8#. Shuttle g7/f7 instead.
   G28: my K a6 + own pawn a5 v enemy K reaching c6 + a rook on the 8th rank = Ra8#. Each tempo spent escaping
   the net cost material. With rooks on, keep my king off the rim unless the enemy king is far away.
10. BISHOP SQUARES (G28): count my bishop's safe squares after the opponent's best reply. If a rook on my back
   rank and a pawn take them all (Bg7: f8/h8 on the rank, f6 hit by e5), it falls to the next double attack.

## Match log
| G | colour | result | opening | key moment |
|---|---|---|---|---|
| 1 | W | 1-0 (Black resigned, ply 135) | Italian 4.c3 Nf6 5.d3, b4-a4-b5, Nbd2-f1-g3, Be3 | 21...Kh8? left f7 guarded only by Qd7: 22.Bxf7! (Qxf7 loses Q to Qb3 battery), 23.Be6 hit Q, 24.Qb6 forced Q trade, +1. c4 stopped ...d5 fork of Rb6/Re3. Nxh6 (+2), Rxd4 (+3), Rxg6. Won with Rg7/f6/g5 self-protecting chain, Ke4 + d5 boxing the king, Re6 (protected by d5) cutting it off, f7, g6, Re8. |
| 2 | B | 1/2 (threefold, ply 111) | QGD Lasker 6...h6 7.Bh4 Ne4, ...Nxc3, ...dxc4, ...Nd7, ...e5; Q trade 16.Qd4 | Equal R ending; 26...g5/27...gxf4 left White three isolated pawns but 30.Rg3 hit my loose Rg7 (had to retreat). 45...Rc1?! put my rook on my king's file: 46.Rc3+ forced the rook trade. K+P a4/b5 v a5/b6 held by shuttling Ke6/Kd6 (d5 gate covered, c5 by the b6 pawn). |
| 3 | W | 1-0 (Black resigned, ply 121) | Italian as in G1 to move 20; 20...Bh7 21...Bxf5 22...d5? | 23.Bxd5! Nxd5 24.Qxd5 (+1; 24...Nb4 25.Qxd7). 25.Qxe6 Rxe6 26.Rg3! pinned g7 (threats Rxg7+, Nxh6+): ...Rg6 Rxg6 fxg6 doubled g-pawns. 29.Nc4, 30.Rb6 pinned Nc6 to Ke6, 31.Rb5 overloaded Nc6 (a5/e5); 32.Kf1/33.Ke2 guarded d3 before 34.Nxa5 (R ending +2). 39.Rb6+ 40.Re6 left Kc5 no moves, won e5; Rf7 on the 7th won b7/g7; 53.Rc8+ cut the king to the b-file; 55.Rc7 (protected by d6), 56.e5, Kd4-d5-e6-e7 escorted d7. |
| 4 | B | 1-0 (I resigned as Black after 33.Kd3, ply 65) | Slav 4...dxc4 5.a4 Bf5 6.e3 e6 7.Bxc4 Bb4 8.O-O O-O 9.Qe2 Nbd7 10.e4 Bg6 11.Bd3 Bh5 12.e5 Nd5 13.Nxd5 cxd5 14.Qe3 Be7 | Level after 16...hxg6. 18...Nb6? 19.b3 20.a5 left the knight no retreat (d7/c8 blocked by my own Qd7/Rc8): 20...Na8. White tripled on the c-file (Rc2, Rc1, Qc3-c5) against my Nc7 blocker pinned to Rc8; my queen shuffled (Qd8-e7-d8). 27.Qd6 Nb5?? 28.Qxf8+! Kxf8 29.Rxc8 pinned Qd8 to Kf8 on the 8th rank: lost a rook. I only checked 28.Rxc8/Qxd8 and missed the capture with check on f8 (d6-f8 diagonal opened when my queen left e7). |
| 5 | W | 1/2 (threefold, ply 120) | Italian; Astra varied 8...a6 9.a5 Ba7 10.h3 d5 11.exd5 Nxd5 | 12.Qb3 (Bc4+Qb3 pin on Nd5 to Qe6), 13.Bg5, 15.Ne4! (Qd6 had only d7: d8/e7 hit by Bg5, c5 by b4/Ne4), 18.Nxe6 bishop pair, 19.b5/20.Qxb5/21.a6 passed pawn locking Ba7, 22.d4, 24.Bxd5 Rxd5 25.dxe5 Rxe5: I had planned Nxe5 winning the exchange, but Rd5-e5 opened the b3-e6 diagonal (Qe6 hit Qb3), so 26.Qxe6 = level. Black's ...c5/...b4-b3-b2 majority and ...Rb6xa6 traded my a6 for b2; locked same-colour bishop ending (my c4/e4/g4-type light pawns immune) drew by repetition. |
| 6 | B | 1/2 (threefold, ply 100) | QGD Tartakower 6...h6 7.Bh4 b6 8.Bd3 Bb7 9.O-O Nbd7 10.Rc1 c5 11.cxd5 Nxd5 12.Bxe7 Qxe7 13.e4 Nxc3 14.bxc3 (hanging c3/d4) | White attacked: 16.e5 17.Bb1 18.Qd2 19.h4 20.Ng5 21.f4; I held with ...g6, ...Kg7, ...h5, 20...Ba6 (denied d3/e2), 21...cxd4 22...Qb4 (Q-trade offer). 23.Qf2 declined and threatened Bxg6 fxg6 Nxe6+ (K+Rd8 fork, Qe7 gone): 23...Ne7. 26...Qa4 (a2 + loose Rd1), 29...Rc2 30.Rd2 Rxd2 (Qf2 x-ray behind Rd2), 32...Qb4! (protected by Nd5; every decline lost material) forced the queen trade. N ending: 34...Nd3 forced g3, 38...f6 freed my king, 43...Nf5 tied Kf3 to g3, but my K could not guard both a5/b6 and g6/h5 against the knight: repetition. |
| 7 | W | 0-1 (I resigned at ply 118, mate in 1 everywhere) | Italian as G5 to 12...Be6; Astra varied 13.Bg5 Qd7 14.Re1 f6 15.Bd2 Rad8 16.Na3 Nf4? | 17.Bxf4! won a piece (17...Bxc4 18.Qxc4+, f7 empty so the c4-g8 diagonal checked). After Q and B trades I had R+2N v R+N but loose pawns (a5,b4,c3,d3,e3): ...Rxd3, ...e4/...Nxc3+, ...Rxb4 left R+N v R (knight for two pawns). Black's K+R escorted a passed c-pawn (c5-c4-c3-c2) and ...b5! (49.axb6 Rxb6) left its a-pawn free; my Rc1/Ne1/Ke2 were tied. 51.g4! fxg4 52.hxg4 gave my e-pawn a fair race, but after 56.e7 a1=Q I played 57.Rxa1?? c1=Q+ (discovered check by Rb2 on Ke2), so I could not take the second queen: 58.Kf1 Qf4+ 59.Kg1 Qg3+. 57.Rxc2+! (c2 covered by Ne1) 58.Nxc2 hitting a1, then e8=Q, kept a won game. |
| 8 | B | 1-0 (I resigned, ply 119) | QGD Tartakower as G6 to 10.Rc1, then 10...dxc4 11.Bxc4 c5 12.Qe2 a6 13.Rfd1 b5 14.Bd3 c4 15.Bb1 Qc7 16.e4 b4 17.e5 bxc3 18.exf6 Nxf6 19.Rxc3 Bd5 20.Ne5 Ne4! 21.Bxe4 Bxh4 22.Bxd5 exd5 = | Held Qh5/Rh3 pressure (...Qe7, ...Bg5, ...Rac8), got a passed c-pawn (25.b3 Rac8 26.bxc4 dxc4). 30...Qa4?? planned 31.Rxd2 Qd1+ but the rook on d2 guarded d1: lost a piece. 31...c3! 32...c2 33...c1=Q+ won it back (R+Q v Q+N, +1); 36...Qe6 covered h6/g4 under the Rg3 pin; 38...Qd6 blockade pinned Rg3 to Kh2, 40...Rxg3+. Then my queen left the a5 guard: 50.Qa8+ Kg7 51.Qxa5 made a4 passed; Q+N with passers on a6/d6 (Qb6 supporting both, Qc7 trade threat) beat my blockading Qd7 + rook: 56.a7 57.Qb8 58.Qb7+ 59.d7 60.Ne6. |
| 9 | W | 0-1 (I resigned, ply 116) | Italian as G7 to 16.Na3; Astra improved 16...Bf7! 17.Nc2 Rfe8 18.Ne3 Nf4 | d3 hit by Nf4 + Qd7/Rd8 battery, guarded only by Bc4: 19.Bxf7+ 20.Qxf7+ 21.Nc4 Nxd3 (-1). Trades to N ending; 36.Nxa6 37.Nxc7 levelled (N+b4,c3,g2,h3 v N+a4,f6,g7,h7). Then 38.Kc2? 39.Nd5+ 40.Ne3: my king went after the a-pawn, the knight to the kingside; ...a3-a2 + ...Nc4 (covering b2, a2 covering b1) tied my Na1 AND king while ...Kf4-g3xg2, ...Kxh4 ate my kingside. After 48.Kxa2 Black's king + three passers v my knight: ...Kg4! ...h4-h3 (Kg4 covered g3, Ne5 covered f3/g4) trapped my knight on h2; ...Nd7 stopped b6. |
| 10 | B | 1-0 (I resigned, ply 93) | QGD Tartakower as G8 to 19.Rxc3 Bd5 20.Ne5; I varied 20...Rac8 (20...Ne4 21.Bxe4 Bxh4 22.Bxh7+ wins a pawn) | White attacked: 21.Rh3 22.f4 23.f5 25.Bg3 26.Ng4 27.Qxg4 28.Be5 30.e6 31.Rg3. Held with 24...Rc7, 25...Bd6 (blocked g3-c7), 26...Nxg4, 27...Kh8 (unpinned g7), 28...Bxe5, 29...Rf8, 30...Bxe6 (+1), 31...Qb6+ 32...g5 (blocked Qxg7#), 34...f6, 39...Kg6, 40...Re6, 44...Rf7, 45...Qe2 (double attack Rf1/b2). Then 46...Qxb2?? 47.Qxb2: b2 was defended by Qb6 down the b-file. |
| 11 | W | 0-1 (I resigned, ply 48) | Italian 4.c3 Nf6 5.d3 O-O 6.O-O d6 7.Bb3 Be6 8.Nbd2 d5 9.exd5 Nxd5 10.Re1 Bd6 11.Nc4 f6 12.Nxd6 Qxd6 13.d4 exd4 14.Nxd4 Nxd4 15.Qxd4 c5 | Good: bishop pair (11.Nc4), 16.Qe4 (Q+R on e6), 18.Qd3 (x-ray on the loose Qd6 froze Nd5: any knight move lost the queen), 19.Rad1, 20.Bxf7+! (zwischenzug v ...Qxg2#, Ne3 supporting) 21.Rxe3 22.Qxe3 = with my better pawns. Then 24.Qe8+?? Qxe8: e8 was covered by Qc6 via d7. |
| 12 | B | 1-0 (I resigned, ply 129) | QGD Tartakower as G8 to 11...c5 12.Qe2, then 12...cxd4 13.Nxd4 Nd5 14.Bxe7 Qxe7 15.Nxd5 exd5 ... 22.Qb5 Qxb5 23.Nxb5 Ba6 24.Nd6 Rc2 25.Nxe4 Rxb2 26.Rd2 Rxd2 27.Nxd2 = | Level B (light) v N ending, 5 v 5. White centralised (Kh2-g3-f4, e4, Nd4, f4, e5+) while my bishop roamed (Bd3-b1-a2-c4). 38.Nf5+ Ke6?? 39.Nxg7+ 40.Nf5+ 41.Nxh6: two pawns lost to knight checks (38...Kf8 held g7). 44...Bxh3 won one back, but ...b4 axb4 axb4 left b4 to Kxb4. Then e5/f6/g5 + N v f7 + B: I set up Kf8/Ke8 + Bf5, but 60.g6! fxg6 61.Nxg6 Kf7 62.Nh8+! (N guards f7) 63.e6 64.f7+ broke through. |
| 14 | B | 1-0 (I resigned, ply 77) | QGD Tartakower 12...cxd4 as G12, then 14.Bxd5 exd5 15.Bxe7 Qxe7 16.Rfd1 Nf6 17.Qf3 Rfd8 18.h3 Ne4 19.Nxe4 dxe4 = | 20.Qg3 Rd7 21.Nf5 (Qxg7# threat) Rxd1+ 22.Rxd1 Qf6 23.Qg4 Qg5 24.Qxg5 hxg5 25.Rd7 Bc8?! 26.Rd8+ Kh7 27.Nd6! (c8 hit twice, f7/e4 too) Bb7?? 28.Nxb7 Rxd8 29.Nxd8: the knight on b7 guarded d8 - a piece down. N ending lost (Nc6, Kf1-e2-f3, f3 break, b3/a4 fixing my king raid). Also 36...Kb3 was illegal (a2 pawn). |
| 13 | W | 0-1 (I resigned, ply 96) | Italian G11 line to 16.Qe4 Rae8 17.Bd2 Bf7 18.Qd3 Qc6 19.Qg3 Bg6 20.Qf3 c4 21.Bd1 = | 21...Rxe1+ 22...Re8 threatened Rxe1# (no luft): 23.Bd2, 24.h3. Black's Be4 + f5 + Nd5 dominated; 29.a4?! b5xa4 lever led to 30.axb5 Qxb5 31.b4 a4 and the a-pawn reached a2, tying Ba1 for good. Good defence: Bc1-b2-a1, 37.Qe3/39.Rc1, 40.Qxd3 (c3 was effectively guarded once), 41.c4 42.Rd1 43.c5 44.c6 47.b5 = (48.b6 would have kept a level B v N ending). 48.Rb1?? axb1=Q. |
| 15 | W | 0-1 (I resigned, ply 104) | Italian G11 line; 17.Bd2 Bf7 18.Qd3 Qc6 19.Bc4! Nb6 20.Bb5 Rxe1+ 21.Rxe1 Qd5 22.Qxd5 Bxd5 23.Re7 ... 25.Rxf8+ Kxf8 = | 29.Bxc4?! entered an opposite-coloured bishop (OCB) ending, level material. I put every pawn on dark squares (a3,b2,c3 / f4,g3,h4; fine), but g3 could only be guarded by my bishop from e1/f2. Black fixed my queenside (...c4, ...b5, ...a6), then ...Kd5-e4 (47.Kd2? gave up e2/f3), ...Kf3-g2-f1: the king on f1 attacked both e1 and f2, and 51...Be2! took d1 from my king - zugzwang (my bishop was boxed in by its own c3/g3). 52.b4?? cxb3 e.p. made it immediate. |
| 16 | B | 1-0 (I resigned, ply 93) | QGD Lasker 7...Ne4 (4.Nf3 order) to 21.Qxb6 axb6 =, then 22.d5 Rd8 23.Nd2? f6! 24.Re4? Rxd5 (+1) | A pawn up but passive (Rb8 tied to b7, Bc8 blocking my back rank) v Nc4-d6, Re7, Rae1. 28...Kh7? put my king behind g7 on the 7th rank: Re7 pinned g7, 29.Ne8 30.Nxf6+! (f6 guarded only by the pinned pawn) =. Then rook lifts Re3-g3+/b3 hit my king and b6; 36.Rg3+ left no square that kept g7 (Kh7 = two-rook mate, Kh5 = Rh3#): 37.Rexg7 (-1), 44.Rf6+ 45.Rxh6 (-2). Illegal try 32...g5 (own king on g6). |
| 17 | W | 1/2 (agreement, ply 92) | Italian G15 line with 29.Bc1! (kept the bishop pair) | 30.Ba4 31.Bc2 32.f3 33.b3 34.Bf4 pin, but 37.Ke3? g5! cut the bishop's retreat (Bd2 blocked by my king - one illegal try), 38.Bxe5+ forced. Same-coloured bishops: 39.g4 f4+ locked the kingside, 41.h3 stopped ...h5 tricks, Bc2 + Ke2/Kf2 covered b3/d3/f3; v ...a5 I kept b4 (not bxa5+) and recaptured axb4 (not cxb4, which gives a passed c-pawn). My offer at move 42 was declined; Astra's at move 47 accepted. |
| 19 | W | 1/2 (insufficient material, ply 142) | Italian G17 line, 18.Qf3 Qc6 19.Rad1 c4 20.Bc2 b5 21.Qh3 Bg6 22.Bxg6 hxg6 ... 28.Qd5 Qxd5 29.Rxd5 | R ending, Black's doubled g-pawns. Good: 30.Kf1 (no luft), 31.Rd7+ (7th rank), 35.Ra7 tied the rook to a6, 36.Ke5 shut it out of d6/e6/f6, 37.h3 removed the g4 pawn, 41.f4 (pawn next to my king), 42.Rxa6, 45.Rxb5 (+1), 48.Kxg6 50.Kxf5 = R+a4/f4/h3 v R+c4. But 39.Kf4?! freed ...Re6-e2xb2 and ...Rg3 won c3, and ...Kd5-e4-d3 + c-pawn cost my rook (59.Rxc1). Pins Rb3/Rb2 on the c-pawn gained tempi. K+3P v R: h6-h7 with Kg7/Kf7 shuttle (avoided Kh6? ...Kf6 & Rh1#), then a5-a6-a7 kept Black's king busy and 70.h8=Q forced the rook trade before Black could win a7 with the rook still on. |
| 20 | B | 1-0 (I resigned, ply 115) | QGD Lasker as G16/G18 to 24...Be6; 25.Kf1 Bd5 26.g3 Kf8 27.Ke2 Ke7 28.Ke3 f6 | Good: 31...Bd7 (not Bxd5? Rd1+ skewer), 33...Rc5 34.Rxc5 bxc5+ (undoubled, passed c-pawn), 35...b5+, 36...g5 37...Kxd5 (+1), 39...Kf7/40...Kg6 trapped Nh5, 41...c4+ 42...Rd6-d3 44...Bc6 v f3 - winning. 45.f4 gxf4?? 46.Nxf4+ forked Kg6/Rd3 (47.Nxd3 cxd3). R+3 v B+4: Be4/Bf5 guarded d3 and a8, but 56.Rd6 Kxh4 57.Rxd3 (Bxd3 Kxd3 is a lost K+P: outside a-pawn) and 58.Rd4 pinned Be4 to Kh4 - resigned. |
| 30 | B | 0-1 (WIN - Astra resigned, ply 102) | Caro-Kann Classical as G26/G28 to 29...Kxd8; 30.Rd1+ Ke7 31.Nd6 Rxc5+ (+1) 32.Kb1 Rd5! 33.Rxd5 exd5 | 30...Ke7 (not Kc8/Ke8: Nd6+ forks), 32...Rd5 (blocked the d-file so Nd6 lost its rook guard; e4 would have dropped the knight), 33...exd5 (c6+d5 took b5/c4/e4 from the knight, queenside majority), 34...Ke6 35...c5 36...Ke5 37...a5 (stopped b4), 38...Ke6 (waiting: Bf6 regained d4), 39...d4! protected passer, 40...Ke5 41...Kf4 (hit Ng3+g4) 42...Kxe4 (+2), 43...d3 44...Ke3 45...Ke2 46...Bc3 (guarded a5 and d2) 47...d2 48.Nxd2 Bxd2 (B+4 v 4), 50...Bb4 (a5/Bb4 protect each other, b-pawn frozen), 51...Kxg4 - resigned. |
| 29 | W | 0-1 (I resigned, ply 116) | Italian G25/G27 line to 29...Nd7; 30.Qc3 Nf6 31.Qa3 Qc8 32.Rd3 Rxd3 33.Qxd3 Rd8 34.Qc3 Qe6 35.c5?! b5 36.Rd1 Rxd1+ 37.Nxd1 | Level Q+N v Q+N to move 44, but 35.c5 handed Black d4 and left my knight no squares. 37...Nh5-f4, 39...h5, 41.g3 Ne6 42.Kg2 Nd4 (f3 weak), 44...h4 45.Ng4? hxg3+ 46.Kxg3 f5!: Qg5 pinned Ng4 to Kg3 on the g-file and a pawn hit it - the knight was lost (49...fxg4). Illegal try 47.Qd7+ (Nd4 blocked the d-file). Then 55...Nxf3! (protected by Qb3 on the 3rd rank), 56...Nd4+ discovered check, 57...Qd5+, 58...e4 - resigned. |
| 28 | B | 1-0 (I resigned, ply 125) | Caro-Kann Classical as G26 to 27...Rb4; 28.Nc4 Rb5 29.Rxd8 Kxd8 30.Nd6 Rxc5+ (+1) 31.Nc4 Ke7 | Good to move 42 (+1, R+B v R+N, 38...Rxa2). Then my king walked to the queenside (43...Kc6 45...Kb5 46...Ka6, 47...Ba7 passive) while White's rook went for my kingside: 49.Rg8 51.Rxg7 (=). 52...f5+ 53.gxf5 exf5+ 54.Kd5 gave White's king d5 with tempo and a free e5 passer. My bishop was tied to h6 (fixed by h5) and my Ka6 stood in a mating net (Kc6 + Ra8#): 55.Rh8 Bg7 56.Rg8 Rg2 57.Nd6! (threat Kc6) forced 57...Kb6, and 58.Nxf5 hit g7 twice - bishop lost (f8/h8 on the rook's rank, f6 hit by e5). 61.Kd6 offered a poisoned knight (61...Rxf5 62.e7! Rf6+ 63.Kd7 queens). Resigned. |
| 27 | W | 0-1 (I resigned, ply 66) | Italian G25 line to 28.Ne3, then 28...c6 29.b4 Nd7 30.Qa4 Ra8 31.Rd2 b5 32.Qb3 Nb6 | Level and comfortable (Q+2R+N each, 7 v 7). 33.c5?? (meant to kick Nb6 and gain d6) opened e6-d5-c4-b3: 33...Qxb3 won my queen; nothing recaptures on b3. Resigned. |
| 26 | B | 1-0 (I resigned, ply 93) | Caro-Kann Classical as G24 to 15...Qd5, then 16.c4 Qe4 17.Qxe4 Nxe4 18.Be3 Bf6 19.Nd2 Nd6 20.c5 Nf5 21.Ne4 Ke7 22.g4 Nxe3 23.fxe3 Rhd8 24.Nd6 b6 25.Rhe1 bxc5 26.dxc5 Rab8 27.b3 Rb4 28.e4 | Good to move 28 (active rooks, b2/g4 targets). 28...Bd4?? 29.a3! - Rb4 was the bishop's only guard and a pawn hit it: 29...Bxc5 30.axb4 Bxd6 31.e5 Bxb4 32.Re4 Rxd1+ = B+2P v R. 33...c5 34...a5 (a5/Bb4/c5 chain), 35...f6 37...gxf6, 39...e5 - every pawn on a dark square but then NO safe non-king moves: 42.Kg6 43.Kxh6, 44.g5! fxg5 45.Kxg5 46.h6+ 47.Rf2+ (Kg8 Kg6 & Rf8#, else h8=Q). Resigned. |
| 25 | W | 0-1 (I resigned, ply 86) | Italian 7.h3 Be6 8.Bb3 d5 9.Nbd2 Re8 10.Re1 Bd6 11.Nf1 h6 12.Ng3 Qd7 13.Qe2 Rad8 14.Be3 dxe4 15.dxe4 Bxb3 16.axb3 a6 17.Qc2 | Good: 17.Qc2 (b3+e4; caught that Be3 blocked Qe2-e4 before 17.Nf5??), Nf5 outpost twice, 21.Nxe7 v ...g6 plans, 23.f3, 25.c4, 27.Bxc5 28.Ne3 29.Nd5, 30.Qc3! pin on e5 v Kg7, 33.exd5 (e-file + pin), 34.Rde2 35.Rxe5 (+1), 38.Qd4/39.Qe4 (g6 pinned, e1/b4/d5 covered), 40.Re7+ 41.Qe6+ Qxe6 42.dxe6 = R ending +1. Then 43.Rh7?? Kxh7: h7 was next to Kg8. Resigned. |
| 24 | B | 1-0 (I resigned, ply 85) | Caro-Kann Classical 3.Nc3 dxe4 ... 12.O-O-O Be7 13.Ne4 Nxe4 14.Qxe4 Nf6 15.Qe2 Qd5 16.Kb1 O-O 17.c4 Qe4+ 18.Qxe4 Nxe4 | Good: 21...Bxe5 22...Rxd1+ (h5 lost its rook guard), 26...f5 (v Rd4 x Ne4) 27.exf6 Nxf6, 28...Nxg4, 29...Kf7! (hit Re6 while Ng4 hit e3), 30...Nf6, 32...Ng4 (rook overloaded), 33...Nxe3+ 34...Rd4 (fork c4/f4), 35...Rxc4+, 37...Rc5 (v h5), 39...Rc2 40...Ra2 41...Rb2 = +1, rook ending winning. Then 42...Rxb4+?? 43.axb4: the a3 pawn guarded b4. Resigned. |
| 23 | W | 0-1 (I resigned, ply 90) | Italian G15 line to 19.Bc4; 19...Rxe1+ 20.Rxe1 Re8 21.Bb5 Rxe1+ 22.Bxe1 Qe6 23.Bd2 a6 24.Bc4 b5 25.Bxd5 Qxd5 26.Qxd5 Bxd5 27.a3 = OCB | Illegal try 25.Be2 (own Qd3 in the way). 28.Kf1 Ke6 29.Ke2?? Bxg2 (Kf1 was the only guard). Defended -1: 30.Be3 c4 31.h4 Kf5 32.f3 g5 33.Bf2 gxh4 34.Bxh4 h5 35.Ke3 (v ...Kf4) 36.Bg3 37.f4+ (stopped ...f5-f4+ fork) 38.Bf2 39.Be1 40.Kf2 41.Bd2 42.Kg1 (v ...h2) Kg3 43.Be1+ Kxf4 (-2: passed f- and h-pawns, black king to d3-c2 v b2). Resigned. |
| 22 | B | 1-0 (I resigned, ply 115) | QGD Lasker as G20 to 32...Rc8; 33.h4 Rc2 34.Rf1 b5 35.Rb3 Ra4+ 36.Ke3 | Good to move 36 (active rooks, White's king boxed). 36...Bf5?? left b5 with no guard (37.Rxb5); 37...Rxa3+ regained it, but 39...Kc7?? allowed 40.d6+! uncovering Rb5 on my Bf5 (41.Rxf5, N for P). Fought with checks (Ra3+/Rd2+/Rc2 threatening Rc4#), 45...Rxd3 traded a rook pair, then R+4P v R+N+3P: Rd7/Rc7 tied to b7, king tied to g7/f6; 51.h5, 53.Ng6, 56.f4, 57.Kh4, 58.g4 prepared g5 - resigned. |
| 21 | W | 0-1 (I resigned, ply 114) | Italian G19 line to 20...b5 21.Qh3, then 21...g6 22.Bh6 Rxe1+ 23.Rxe1 Re8 24.Rxe8+ Bxe8 ... 31.Qxf6 Nxf6 32.Bd2 b3 33.axb3 cxb3 | 2B v B+N, Black's a/b pawns advanced and its king came to d6. 39.Bb5 (hit a4) Nb6 40.Be3? Bc4+! 41.Bxc4 Nxc4 forked Be3/b2; 42.Bc1 a3! 43.bxa3 b2 44.Bxb2 Nxb2 = 5 pawns v N+3. 46.Kc2/47.Kb3 kept a3/c3; Ka4 answered ...Na5+ while the pawn stood on a3. But 48.h4/50.f3 then 51...f4! fixed g2 (g3/g4 allow ...fxg3, e.p. too) and opened f5: ...Nf5-xh4/...Ne3+xg2. Black's Kc5 alone held my a/c passers; my king had to stop the h-pawn while Black's king took the queenside. Resigned. |
| 18 | B | 1-0 (checkmated, ply 129) | QGD Lasker as G16 to 21...axb6; 22.Rb5 Ra6 23.Ne5 Rd8 24.Rb4 Be6 25.a4 Bd5 ... 28...b5! 29...bxa4 32...a2 (+1) | Good: 28...b5 used White's back rank, a2 pawn tied Ra1, 34...Ra7/38...Kc7-39...b6 kept everything guarded. Then 42...Rc4? blocked my Bd5-a2 guard (43.Raxa2 =), 46...Re6? blocked Bd5-f7 (47.Rxf7, -1). Long defence: 52...Rc7, 54...Rc6 tying Ne4/Rd2 to d6, 56...Rb6 pinning d6 to Kf6, 58...b3, 60...Rc2 61...Rxg2 (=), 62...Re2+ 63...b2. Then 64...Rd2?? 65.Rb8# (d6 pawn covered c7/e7, Ke6+Ne5 d7, own Be8 on e8). |

## Lessons from the match so far
- G1: when the opponent's king leaves the f7 defender and only the queen guards f7, check Bxf7 with a Qb3 battery behind.
- G1 near-miss: 58.Re8?? would have lost the rook to ...Re2+ (my king on the e-file between). Before putting a rook on the
  same file/rank as my king, list enemy rook checks that drive the king off that line (skewer).
- G1: pushing f7 too early frees the enemy king to e7 (the pawn blocks my rook's 7th-rank control). Cut the king off
  first (rook on a file protected by a pawn, e.g. Re6 with d5), then push.
- G1: the referee auto-claims threefold. Count repeats; change the pawn structure (d4) to reset when needed.
- G2: a rook on the same file/rank as my own king can be forced off by an enemy rook check (46.Rc3+ forced Rxc3).
  Check this before every rook move in the endgame (same family as the G1 skewer check).
- G2: when an enemy rook lands on my rook's file (30.Rg3 v Rg7), is my rook protected? If not, it is simply hanging.
- G2 K+P with blocked pawns: list the squares the enemy king needs to attack my weak pawn (c6/d6 for b6), then keep the
  gate squares (d5; c5 was covered by b6) under my king and shuttle between two squares that both cover the gate.
  Worked out: ...Kd7 v Kd5 and ...Kc7 v Ke6 (Black to move) lose to zugzwang.
- G3: Italian v ...d5 break: with Bc4 + Qb3 on the a2-g8/b3-d5 lines and Nf5, Bxd5 Nxd5 Qxd5 wins a pawn; check the
  enemy queen on the d-file behind (24...Nb4? 25.Qxd7).
- G3: rook lift Rg3 + Nf5 pins g7 to Kg8; the pinned pawn cannot recapture on h6, so Nxh6+ and Rxg7+ both threaten.
- G3: pin a defender to its king on a rank (Rb6 v Nc6/Ke6); then R + N on two pawns guarded by one knight (overload).
- G3: before simplifying into a rook ending, place the king on the pawn the enemy rook will hit (Kf1-e2 for d3).
- G3 near-misses x3 (43.Rf6+?? Rxf6, 50.Rb6?? Rxb6, 52.Rg6?? Rxg6): a rook landing on a line facing the enemy rook with
  nothing between is lost if unprotected, even when it gives check. DEST: "enemy rook facing mine: is mine protected?"
- G3 R-ending technique that worked: rook on the 7th; cut the king off along a file; interpose on the 7th with a rook
  protected by a pawn (Rc7 with d6); king escorts the pawn from the side (Ke6-e7) sheltered from checks from behind.
- G4 (loss): LEAF must include every enemy CAPTURE WITH CHECK, even an apparent queen sacrifice (28.Qxf8+ Kxf8), followed
  two more plies: where my king lands, which line it then shares with my queen/rook (Rxc8 pinned Qd8 to Kf8).
- G4: when my queen leaves a square, list the diagonals/files it stops blocking toward my rooks (Qe7-d8 opened d6-f8).
- G4: before putting a knight near the edge (Nb6, Na5, Ng6...), list its retreat squares after a pawn kick; my own Qd7 and
  Rc8 blocked d7/c8, so a4-a5 forced Na8.
- G4: if the opponent doubles/triples on an open file and my only blocker is a piece pinned to my rook behind it, count
  attackers of the blocker AND of the square behind it if the blocker moves. Trade a pair of rooks early (...Rxc1) or put
  my own second rook/queen on the file before the battery forms; do not drift with queen shuffles.
- G5: when ANY piece moves (mine or the opponent's), list the lines it opens: 24...Rxd5 25.dxe5 Rxe5 vacated d5 and opened
  b3-e6, so Qe6 attacked my Qb3; my planned Nxe5 (winning the exchange) would have lost the queen to ...Qxb3.
- G5: Bc4+Qb3 battery pinning a knight on d5 to a queen on e6 paralysed Black; Bg5 + Ne4 trapped the queen on d6
  (only d7 left). Keep the bishop IN FRONT of the queen for a real pin (Bxe6 wins the queen; Qxe6 would only trade).
- G5: a passed a6 pawn blockaded by the enemy bishop ties it down, but my rook behind it was then passive; the enemy b/c
  majority (...c5, ...b4-b3-b2) gave counterplay. Fix or blockade the enemy majority early (c3-c4, king to the queenside).
- G6: when my queen leaves a guard post, list what it stopped guarding, not only the lines it opened. After 22...Qb4
  (queen off e7) 23.Qf2 threatened Bxg6 fxg6 Nxe6+ forking Kg7 + Rd8 (e5 blocked Re1, so the knight was safe);
  23...Ne7 covered g6. Pattern: Bd3/Bb1 on g6 + Ng5 on e6 + my rook on d8 = fork square e6.
- G6: count BATTERIES when counting attackers/defenders. 27...Bc4 "a2 attacked twice, defended once" was false: Qf2
  stood behind Rd2 on the 2nd rank (x-ray), so Bxa2 Rxa2 Qxa2 Qxa2 loses. Likewise 29...Rc2 v 30.Rd2 (+Qf2 behind)
  hung to Rxc2 Qxc2 Qxc2; I traded 30...Rxd2 in time.
- G6 technique: a queen-trade offer on a square protected by my knight (32...Qb4 with Nd5) when the enemy has a loose
  piece (Ne4) and an empty back rank: every decline lost material (Qe1+ hitting e4/h4, Qxd4+). Also 21...cxd4 so that
  f4-f5 could be met by ...dxc3 hitting the queen.
- G6 N ending: my knight tying the king (Nf5 v g3) was good, but my king could not guard both wings: a5/b6 (b6 loose
  after 44...a5) and g6/h5 (after 38...f6 traded my f-pawn). One knight harassing the far wing = draw. Before entering a
  N ending, make sure at least one wing is a self-protecting chain; avoid pawn moves that leave a pawn loose.
- G6: before allowing a forced knight trade into K+P, count the race: with my knight on b4, 41.d5 exd5+ 42.Nxd5+ would
  have forced Nxd5 Kxd5 (White king active) - 40...Nc6 avoided it. Knight checks (Nf6+/Ne4) can force a repetition;
  accept it only when level (here: balanced, I took the draw at 3.5-2.5).
- G7 (loss from a won game): before capturing (even a free queen), list the opponent's replies that give CHECK, especially
  discovered checks: my Ke2 stood on the 2nd rank behind Black's c2 pawn with Black's Rb2 on the same rank, so ...c1=Q+
  came with check from b2 and the new queen escaped. Pieces sharing a line with my king and an enemy rook = danger.
- G7: in a race, compare candidate captures by what each leaves: 57.Rxc2+ (capture WITH check, protected by Ne1) kept the
  initiative and let Nxc2 hit a1; 57.Rxa1 left my king in a battery. Prefer the capture that checks and removes the battery.
- G7 conversion: a piece up with loose pawns (a5/b4/c3/d3/e3) I let Black's R+K win pawns and escort a passed c-pawn.
  Up material: (1) keep pawns protected/compact before trading, (2) bring my king toward the enemy passer early (Kd2-c3),
  (3) keep the rook active rather than tied to a weak pawn (Ra4 guarding a5 was passive), (4) after the knight was
  tied to blockading, the opponent's second passer (a-pawn) decided; stop passers before they get support.
- G7 good: 15.Bd2 against ...f6 (a2-g8 diagonal opened): every ...Nd5 move lost to Bxe6+ and Qxe6+; 16...Nf4? 17.Bxf4.
  51.g4! gave counterplay when my pieces were tied (create my own passer instead of waiting in zugzwang).
- G8 (loss): 30...Qa4?? relied on 31.Rxd2 Qd1+ 32.Kh2 Qxd2, but after Rxd2 the rook guards d1. When a line depends on a
  check after the opponent's capture, redraw the board after the capture (LEAF note). The c-pawn (c3-c2-c1=Q+, with the
  rook behind it on the c-file) rescued the game.
- G8: up the exchange (R+Q v Q+N) against ONE passed d-pawn I was fine; my queen moves (Qc7-d7-e6-d7) dropped a5 to a
  queen check (Qa8+ then Qxa5) and created a SECOND passer (a-pawn). Two passers far apart + queen support: a queen
  trade on c7 (dxc7) would leave two passers my rook could not stop, so my queen was stuck as a blockader and the a-pawn
  walked in. Rules: (1) never let the second passer appear (keep the pawn that fixes it, here a5 v a4); (2) trade queens
  while only one passer exists and my rook/king can then win it; (3) a blockading queen that can be hit by an enemy
  queen offering a trade (Qc7 v Qd7) is not a real blockade; put the king or rook in front instead, earlier.
- G8 good: 20...Ne4! (Bh4 hung after the knight moved; Nxc4?? Nxc3), 36...Qe6 against the Rg3 pin (covers h6 and g4),
  38...Qd6 (blockade + pin of Rg3 to Kh2 along d6-h2, so the rook could not recapture on d3), 40...Rxg3+ (Kxg3 illegal
  because Qd6 hit g3), and ...f6 to block the long diagonal so my king could use g7.
- G9 (loss) opening: Italian with ...d5 exd5 Nxd5 leaves MY d3 on Black's half-open d-file. Count d3 attackers (Nf4 +
  Qd7 with Rd8 behind = 3) v defenders (Bc4 only; Qb3 is blocked by c3) BEFORE kicking the Nd5 (18.Ne3 sent it to f4).
  15.Bd2 also blocked d2, so the b1-knight needed Na3-c2-e3. Next White game: 15.Bh4 (or Be3) keeping Nbd2, or
  13.Nbd2/13.Re1 instead of 13.Bg5; keep d3 covered twice (Rad1, Bf1) or play d4 before ...Nf4 arrives.
- G9 (loss) N ending: v a far passed ROOK pawn, the KNIGHT should stop it early from in front/aside (Nb5 covering a3,
  or Nb3/Nc2 v a1) and the KING should guard the wing the enemy king raids (Ke2-f1 for g2/h3). I swapped roles
  (king to c2/c1, knight to e3): ...a3-a2 plus ...Nc4 (covering b2; the a2 pawn covers b1) tied BOTH my king and Na1,
  and the enemy king ate g2/h3/h4 in the 4 moves my king needed (Kc2-b3xa2).
- G9: knight v king + connected passers: list the squares that control each queening square (h1: f2/g3; g1: e2/f3/h3;
  h2: f1/f3/g4), how many moves my knight needs, and whether the enemy king/knight covers them (Kg4 took g3/f3, Ne5
  took g4/f3). The enemy can switch runner (g-pawn to h-pawn). Checks (Ne3+, Nf1+) and a blocking sac (Nh2+) gain
  only one or two tempi; count the race before choosing the plan, not during it.
- G9 good: 21.Nc4/32.Nd3/34.Nc5/36.Nxa6/37.Nxc7 won the pawn back; 45.h4 made the king spend two moves for it;
  49.Nb3 offered a trade (pawn race favoured me); 50.Na5 idea (trade = bxa5 a-pawn 3 moves from queening).
- G10 (loss from a better position): the decisive error was a one-move blunder, 46...Qxb2?? with Qb6 guarding b2
  along the b-file. I had even written "b2 unprotected" in several lines. When a capture looks free, ask: which
  enemy piece on the same LINE (any distance) guards it? Especially the enemy queen sitting on that file.
- G10 defence that worked v Rh3/Qg4/Bf5/Bg3 attacks: block lines with a protected piece (25...Bd6 v Bg3-c7),
  trade the attacking knight (26...Nxg4), step the king out of pins (27...Kh8, 39...Kg6), block the g-file battery
  with a pawn protected by another (32...g5), keep f7/f6 covered by rook+king and the rook on the 7th rank.
- G10: 45...Qe2 (hitting the loose Rf1 and b2) was right; after 46.Ra1 the safe follow-up was 46...Qe4 (covers a8 and
  b7 on the long diagonal) or 46...Rf8, not grabbing b2.
- G11 (loss, one move): 24.Qe8+?? Qxe8. I had written "Qc6 covers d7, e8" one move earlier and still played it.
  Knowing a fact is not enough; the RAY SCAN must be done on the board right before submitting. Two games in a
  row lost to the same error type: my queen landing on a square the enemy queen reaches from a distance.
- G11 good patterns: 7.Bb3 + 8.Nbd2 (no ...d5 tempo on c4); 11.Nc4 hitting Bd6/e5 (forced ...f6, bishop pair);
  queen on the same file as an UNPROTECTED enemy queen behind a knight (Qd3 v Nd5/Qd6) paralyses the knight;
  check with a capture first (20.Bxf7+) when the opponent has a mate threat that a piece supports, then remove
  the supporting piece (21.Rxe3).
- G12 (loss from a level ending): 38.Nf5+ Ke6?? 39.Nxg7+ Ke7 40.Nf5+ Ke6 41.Nxh6. A knight check that lands where it
  can next CAPTURE A PAWN WITH CHECK is a fork of king + pawn; my pawns on g7/h6 (dark) could not be defended by my
  light bishop, only by the king. In B v N endings keep the king next to pawns on the bishop's opposite colour, or
  move them to the bishop's colour early (...g6/...h5 so the bishop guards them); and step the king to the square
  that keeps them guarded (38...Kf8), even if passive.
- G12 B v N plan: White's king walked in (Kf4, Kd4, Kc4xb4, Kc5-d6) while my bishop chased pawns. Use the king as the
  blockader of the passers' front square and the bishop for the light-square push squares (e6/g6 from f5 is unique),
  and do not trade my last queenside pawns into an isolated one the enemy king collects (48...b4? axb4 axb4).
- G12 fortress lessons (N + e5/f6/g5 v B + f7): the bishop on f5 covers BOTH e6 and g6 (and d7, h7); Kf8 keeps the king
  off e7/g7. White's breaks: e6 with Kd6 + N hitting e6 (after ...fxe6 Nxe6+ comes with tempo), and g6 when the
  bishop has left the b1-h7 diagonal (59...Bg4? allowed 60.g6!). After a knight lands on h8/d8 guarding f7, f6-f7 and
  e6-e7 decide. Two connected passers on the 5th/6th plus N + K usually win; the decisive error came earlier (pawns lost).
- G13 (loss, one move): 48.Rb1?? axb1=Q. The square b1 was "protected" in my head (R guarding b5 and a1) but the a2
  pawn captures there and promotes. Every square adjacent-diagonal to an enemy pawn on my 2nd rank is poison.
  4 of my 5 match losses since G9 were one-move oversights in level positions; the PAWN SCAN + RAY SCAN are not optional.
- G13 structure: Black's ...c4/...b5/...a5 majority v my a2/b2/c3. My 29.a4?! (to undermine c4) let 30.axb5 Qxb5 hit
  b2 and 31...a4 created a protected-then-passed a-pawn that reached a2 and froze my bishop on a1 (and my rook on the
  1st rank). Against a queenside majority keep my pawns back, blockade with pieces (Nd2-b1-c3/Bc2), do not open files
  for it. A pawn on a2 + my bishop on a1 = I am a piece down in practice; trade it off or win it early.
- G13 back rank: rooks on the open e-file + no luft = constant Rxe1# motifs (22...Re8, 24...Qe6-e1 ideas). Play h3
  in time (before the e-file opens), as in my G1/G3 wins.
- G13 good technique to keep: with a blockading bishop on a1, covering a1 also from b2/c3 or with the rook along the
  1st rank lets the bishop move; Kf1-e2 protecting d1 freed my rook; counter-passers (c4-c5-c6, b5) forced Black's
  pieces back. In such endings compare "simplify into equal B v N" (48.b6) with "keep tension" honestly.
- G14 (loss, calculation): 27...Bb7?? 28.Nxb7 Rxd8 29.Nxd8 - I counted "+2" because I imagined the captured rook's
  square undefended; the knight that captured on b7 now guarded d8. Same family as G8 (31.Rxd2 guarded d1).
- G14 earlier: 25...Bc8?! (hitting Rd7, pinning nothing yet) allowed 26.Rd8+ Kh7 27.Nd6: a check first, then a
  knight jump that attacks my piece a SECOND time plus two pawns. LEAF must include "check, then double attack".
  Safe was 25...Ba6 then ...Bd3 (bishop protected, e4 covered).
- G14 middlegame: after ...Ne4/...dxe4 my queen alone guarded g7 against Qg3/Qg4 + Nf5; every queen move had to keep
  g7 covered (21...Qf6, 23...Qg5). Trading queens on my opponent's terms (23...Qg5 24.Qxg5 hxg5) left a loose
  bishop and a weak e4 v R+N activity. Prefer ...Kh8/...f6-type prophylaxis or keep queens with a solid king.
- G14 illegal attempt 36...Kb3 (a2 covers b3): the PAWN SCAN also applies to KING moves (legality), not only to
  piece safety. One of three allowed tries used; never assume a king square is free near enemy pawns.
- 3 of my last 4 losses: a single miscounted capture/cover in a level position. Before every move in a level or
  better position: (1) list opponent checks, (2) for each capture in my line, redraw the board, (3) PAWN SCAN.
- G15 (loss, slow positional, OCB ending): opposite-coloured bishops are NOT an automatic draw. They are drawn if both
  wings can be held. Black had two targets (my b2 base and my g3 base) and a freer king; I had none. Rules for
  defending an OCB ending:
  (1) My KING must go to the wing the enemy king attacks, and my BISHOP must hold the other wing alone. When the
      enemy king changes wing, switch early, along squares the enemy bishop does not cover.
  (2) Only my king can stop the enemy king using squares of ITS bishop's colour (light squares e4/f3/e2/f1 here).
      46.Ke2 held them; 47.Kd2? (only to hit Bc2) let ...Bd3 cut my king off and ...Kf3-g2-f1 walk in.
  (3) Before fixing a pawn chain (33.g3 34.f4 37.h4), list the squares from which my bishop guards its base (g3: e1, f2,
      h2) and look for one enemy-king square touching them all (f1 touched e1 and f2). My bishop on e1 was also boxed in
      by its own c3/g3 (only d2/f2 left). Then the enemy bishop on the d1-h5 diagonal took d1/e2/f3 from my king:
      zugzwang. The enemy bishop has unlimited waiting moves, so count my spare tempi (I had only b2-b4).
  (4) With the bishop pair against B+N, do not trade into OCB when the opponent has the more active king and a pawn
      majority (29.Bxc4?!); keep the pair (29.Bc1).
- G15: when a zugzwang is coming, choose the move that needs a QUIET reply from the opponent (51.Kd2 made ...Be2 a
  non-check). Astra still found it; assume it finds quiet zugzwang moves too.
- G16 (loss from +1): winning a pawn is not enough if my pieces end up passive. After 24...Rxd5 my Rb8 had to guard
  b7, my Bc8 blocked my own back rank (Re8+ then Rxa8/Rxc8 tricks all game) and White's Nd6 + Re7 + Re1 got full
  compensation. Right after winning material, (1) trade the most active enemy piece (the Nd6 knight: ...Rd5 or
  ...Bd7/...Be6 to challenge it), (2) un-block my back rank (bishop off c8) so a rook guards it, (3) give my king a
  safe square that is NOT on the enemy rook's rank (Kh7 behind g7 with Re7 on the 7th = pinned g7).
- G16 king safety v two rooks + knight: two enemy rooks on the 7th rank / g-file = mating nets (Rxg7+, Rh7+, Reg7+,
  Rh8#). Before a king move, count which squares each enemy rook covers on the next move and keep one flight square
  that is not on any rook line. The g-file check 36.Rg3+ left only Kf5/Kh5 and g7 fell; earlier ...h5/...g5-type
  pawn moves (when legal) or a rook on the g-file would have kept the file closed.
- G16 good: 13...Qd6 (off the e-file before e4-e5/Bh7+ tricks), 16...Nb4-d5 blockade, 20...Qb6 (queen-trade offer
  v an unprotected Qb3), 23...f6! (hit the rook guarding d5), 27...Rb8 (avoided 27...Kf8?? 28.Re8#), 33...Rd5
  (exploited White's back rank: Nxb7? Rd1+ and Rxb7? Rd1#). Back-rank threats saved me several times; keep using them.
- G17 (draw): the bishop pair is only an edge if lines open. Black fixed pawns on light squares (...a6/b5/c4,
  ...g6/f5) and gained space; a bishop needs a retreat square - 37...g5 hit Bf4 when my own king blocked d2.
- G17 same-coloured bishop fortress (useful both ways): lock the pawns on the colour the enemy bishop cannot hit
  (my a3/b4/c3 dark), keep my bishop on the square covering the king entry squares (Bc2 covered b3 and d3), keep my
  king next to the one light pawn (f3), put h3 in before ...h5 so a later ...hxg4 is met by hxg4, and do not take
  toward the side where the enemy king would enter (no bxa5+, recapture axb4 not cxb4). Never trade bishops on b3
  if cxb3 creates a passed pawn my king cannot catch.
- G17 procedure: `./play offer-draw` records the offer but does NOT end my turn; I still make a move afterwards.
  Offer only in dead-level positions (policy).
- G18 (loss, checkmated from an equal ending): a king boxed on the back rank by an enemy passed pawn on the 6th
  (covering both diagonal squares), the enemy king + knight in front, and MY OWN bishop on the only free square is a
  mate in one against any rook check along the rank. Before every move in such positions: name the checking moves
  and count real flight squares (MATE SCAN). The cure was simple: keep a free square (bishop off e8, or king to c8
  earlier) or keep my rook covering the back rank (Rd2 left the 8th-rank defence to nobody).
- G18 self-blocking twice: a rook placed between my bishop and the pawn it guarded (Rc4 on d5-a2, Re6 on d5-f7). When
  my bishop is a key defender, list its guard lines before every move of my other pieces.
- G18 good: the Lasker ending again gave me a plus (+1 with an a2 passer); ...b5 exploiting White's luft-less king;
  pinning the enemy passed pawn to its king with my rook on the same rank (Rb6 v d6/Kf6) made d6-d7 illegal; a
  rook on the 2nd rank behind my passed pawn plus checks (Re2+) regained material.
- G19 (draw from a better rook ending): (1) a blocker pawn in front of an enemy pawn (my c3 v c4) is worth more than
  a far passer - once ...Rxc3 happened, Black's c-pawn with its king beside it cost my whole rook. Guard the blocker
  or trade the enemy pawn before it gets king support. (2) The bind Ra7 + Ke5 (enemy rook tied to a6/g6, no entry
  via d6/e6/f6) was the high point; 39.Kf4 released it. Keep the bind and improve with pawn moves (h3, f3/g4) first.
  (3) Pinning an enemy passed pawn to its king along a rank (Rb3 v c3/Kd3, Rb2 v c2/Kd2) forces king moves = tempi.
  (4) K + pawns v R: when the enemy king goes for my last far pawn while its rook watches my advanced one, force the
  rook to take a queen (h8=Q) BEFORE the far pawn falls; R+K v K+rook pawn on the 7th is lost. Use the rule of the
  square: push the far pawn so the enemy king must stay inside its square (a5/a6 v Kd6/Kc6).
- G20 (loss from a winning ending): the third time a won/better ending was thrown away by one tactical miss (G16,
  G18, G20). In a winning position slow down most: before every capture, list the opponent's recaptures and checks
  and every piece the recapturing unit hits from its new square (here a knight fork of king + rook). Keep my rook
  off squares a knight can hit with check (d3 with Kg6: f4 knight attacks both). Also: a rook "protected by a pawn"
  is still lost for a knight. Good play to repeat: undoubling with Rc5/bxc5+, ...b5+ creating connected passers,
  trapping a rim knight with the king (Kf7/Kg6 v Nh5), pinning-free bishop retreats (31...Bd7 not Bxd5?).
- G20 R v B technique (useful both ways): the side with R + outside pawn wins by attacking the defender's last pawn
  with the rook and trading R for B+P when the K+P ending is won (outside a-pawn v a king on the h-file). The
  defender's king must stay near its own pawn and away from rank/file pins with its bishop (58.Rd4 pinned Be4-Kh4).
- G21 (loss, slow + one tactic): (1) I traded queens (31.Qxf6) into a bishop-pair ending while Black's queenside
  majority (a5/b4/c4) was already advanced; ...b3! then fixed my b2, ...a4-a3 broke through later. The bishop pair
  needs targets and open lines; a rolling enemy majority beats it. Stop the majority first (a3/cxb4), trade queens after.
  (2) 39.Bb5 put my bishop where 40...Bc4+ hit it with check; I wrote "...Bc4+ ideas" and still missed that the
  recapture Nxc4 would fork Be3 + b2. The G20 knight-fork rule applies to MY recaptures as well as theirs.
  (3) N v pawns: my pawns f2/g2/h3 were safest unmoved. 48.h4 relied on Black's f5/g6 pawns blocking the knight's
  squares; 50.f3 gave up e3/g3. Then ...f4 fixed g2 (en passant made g4 impossible too) and the knight took h4/g2.
  (4) In the 5P v N+3P ending the decisive factor was the active enemy king (Kd5-c5) next to my split a/c passers:
  my king had to protect them from b3 (Ka4 v ...Na5+, keeping a3 for that), so it could not defend the kingside.
  Good: 42.Bc1 (Bxa3 v ...Nxa3), 46.Kc2/47.Kb3 restricting the knight, 50.f3 kicking ...Ne4, resigning when the
  black king was about to collect both queenside pawns with my king tied to the h-pawn.
- G22 (loss from a good ending, two oversights in four moves): (1) 36...Bf5?? moved the ONLY guard of b5 (Bd7);
  my scan looked at what the bishop attacks from f5, not at what it stopped defending on d7. (2) 39...Kc7?? walked
  into a pawn check (d5-d6+) that unmasked White's Rb5 along the 5th rank onto my loose Bf5. Both are "what does
  this move unguard / unblock" errors. Fix: for EVERY move, (a) list what the moving piece defends before it moves,
  (b) list enemy pawn checks against the destination and the lines they open, (c) list my LOOSE pieces on lines
  through enemy rooks (Bf5 stood on the 5th rank with Rb5 behind only the d5 pawn).
  Good: 33...Rc2/34...b5/35...Ra4+ (active rooks v a boxed king), 41...Ra3+ 42...Rd2+ 43...Rc2 (Rc4# threat; Nd3?
  would lose the knight to ...Raxd3+), 54...Rc5+ (repetition try). The Lasker line stays good for me.
- G23 (loss, OCB ending): (1) Entering an opposite-coloured-bishop ending is only safe if none of my pawns stand on
  the enemy bishop's colour without a guard; g2 (light) was guarded by Kf1 alone and 29.Ke2?? dropped it. Before
  the queen trade, list my pawns on the enemy bishop's colour and fix them (g3, h4 on my colour) or keep pieces on.
  (2) In OCB defence the enemy king + bishop + TWO passers on one wing beat a king that must block one and a bishop
  that must guard both the other passer and the far wing. Keep the pawn count: every pawn lost on the wing where
  the enemy king works (f4 after 42.Kg1 Kg3 43.Be1+ Kxf4) is decisive. (3) Pawn forks still matter in endings:
  ...f5-f4+ would have forked Ke3 and Bg3 (37.f4+ stopped it). (4) My draw/loss record says: avoid simplifying into
  endings where the opponent has the more active king; keep pieces when the position is level.
- G24 (loss from a winning rook ending, one move): 42...Rxb4+?? 43.axb4. I had checked that a3 was guarded by the
  rook on the 3rd rank one move earlier, but never asked what guards b4 - the a3 pawn itself. My rook had just
  harvested c4, a2/a3-type pawns for ten moves; the habit "this pawn is loose" made me skip the scan. Rule: every
  capture of a pawn = look diagonally behind it first. In a won ending, before every capture, also ask "what is the
  worst reply?" (here axb4 = rook lost).
  Good to keep: the Caro-Kann Classical gave a sound position; trading into an ending with a strong knight (Ne4) and
  then tactics against an overloaded rook (Re5/Re4 guarding e3 and h5) won material step by step.
- G25 (loss from a +1 rook ending, one move): 43.Rh7?? Kxh7. I wanted Rh7 to win h6 for my e6 pawn and spent the
  whole think on ...Rxe6/...h5/...Kf8 replies, but the rook landed NEXT TO the black king on g8. Fourth game in a
  row lost by one move in a good or winning position (G22 Bf5??, G23 Ke2??, G24 Rxb4+??, G25 Rh7??). Each time the
  mistake was on the FIRST ply - the square itself - not deep in the line. New rule, before typing the move:
  (1) name every enemy unit that attacks the landing square, the KING included; (2) only then calculate replies.
  The plan itself was fine with the king elsewhere: 43.Kf2 Kf8 44.Rh7 Rxe6 45.Rxh6 kept +1 (or 43.Ra7 for a6).
  Good to keep: the slow Italian (h3, Bb3, Nbd2-f1-g3, Qe2/Qc2, Be3, Rad1) gave a lasting edge; Qc2 to guard e4/b3
  when Be3 blocks the e-file; a queen on c3 pinning e5 to Kg7 plus doubled rooks on the e-file won the e5 pawn.
- G26 (loss): (1) 28...Bd4?? 29.a3! - I checked that Bd4 was defended (by Rb4) but not whether that defender could
  be attacked: a2-a3 hit the rook, and rook + bishop could not both be saved. Before placing a piece defended by ONE
  unit, list enemy pawn pushes/checks that hit that unit. (2) B+2P v R: putting all pawns on the bishop's colour made
  them safe, but left me with ONLY king moves (any bishop/pawn move dropped a pawn) - a zugzwang-prone fortress the
  enemy king could probe (Kf5-g6xh6). Keep one free pawn move or a bishop with two safe squares, and do not let the
  enemy king reach my pawns' side. (3) Back-rank pattern again: my K on g8/h8 + enemy K on g6 + rook on the 8th =
  mate (Rf8#/Rd8#); with an enemy pawn on h6/h7 every escape square is covered. A rook check on the file next to my
  king (47.Rf2+) pushed my king to that edge or away from the passed pawn - check where my king can go BEFORE it is
  needed (46...Kf7 lost to Rf2+; the king had no good square left).
  Good to keep: the Caro-Kann Classical again gave a level, active ending; ...b6xc5 undermining the d6 knight and
  ...Rab8/...Rb4 activity were strong.
- G27 (loss, one move): 33.c5?? Qxb3. I analysed every knight retreat after c5 and the d6 outpost, but not the line
  my c4 pawn had been closing: Qe6 x-rayed my Qb3 through d5-c4. The OPEN-LINE rule (step 7) existed; I applied it
  to pieces, not to my own pawn pushes. Sixth game lost by one move in a level/good position (G21-G27). The checks
  that would have saved each one are all "first-ply" checks: who attacks the landing square (G25), what my moving
  unit stops guarding or blocking (G22, G23, G27), what guards the target (G24), can the guard be hit (G26).
  For the last three games: before typing the move, do the FIRST-PLY checks out loud in this order - (1) attackers
  of the landing square incl. king, (2) what the moving unit blocked/guarded (rays from my Q/K/R through its square),
  (3) for captures: defenders of the target. Only then calculate.
- G28 (loss from a +1 ending - a plan error, not a one-move blunder; the FIRST-PLY checks caught 41...Rb2?? and
  every later move was sound). (1) KING PLACEMENT: with R+B v R+N and an extra pawn, my king walked to c6-b5-a6 to
  help the a-pawn. The enemy rook then checked it to the edge (Rb8+/Ra8+), took my unguarded kingside pawn (Rxg7),
  and the a6 king became a mating-net target (White Kc6 + rook to a8 = mate), which cost the decisive tempo
  (57...Kb6 forced, then 58.Nxf5). In endings with rooks on, keep my king near the pawns the enemy rook can reach and
  off the edge; let rook + bishop escort the passer. (2) TRAPPED BISHOP: a bishop tied to a fixed pawn next to the
  edge (h6 v h5) has few squares. With the enemy rook on my back rank and a pawn covering f6, Bg7 had none and fell
  to a double attack (Rg8 + Nf5). Count my bishop's safe squares every move; with one or none, act before it is hit
  twice. (3) 52...f5+ removed e6, opened the 6th rank for rook checks and gave White's king d5 with tempo plus a free
  e5 passer. (4) Read correctly: after 61.Kd6 the knight was poisoned (61...Rxf5 62.e7 Rf6+ 63.Kd7 and nothing covers
  e8) - K on d7 + pawn on e7 + rook covering e7 beats a lone rook.
  Good to keep: third good ending from the Caro-Kann Classical (...b6xc5, ...Rb8-b4-b5, ...Rxc5 = +1 by move 30).
- G29 (loss from a level Q+N middlegame): (1) PIN + PAWN: 45.Ng4 blocked the g-file in front of my king, 46.Kxg3
  recaptured onto that same file, and 46...f5 attacked the pinned knight - a piece lost to a pawn. 45.gxh4 Qxh4+
  46.Kg2 kept material level. (2) STRUCTURE: 35.c5 (v ...e5 and a knight) gave Black a permanent d4 outpost and,
  after ...b5, left my knight no square (c4/d5/f5/g4 all covered by pawns). Keep the c-pawn able to guard d4.
  (3) KING COVER: 41.g3 (to kick Nf4) left f3 weak; ...h5-h4 then opened my king. Before a pawn move near my king,
  list the squares it stops guarding. (4) PATH again: 47.Qd7+ was illegal (Nd4 on the d-file). (5) When down
  material with queens on, Q+N against my exposed king won more (55...Nxf3 protected along the 3rd rank by Qb3,
  56...Nd4+ discovered check) - check every rank/file my king shares with the enemy queen behind a knight.
- G30 (WIN, the conversion I had failed in G24/G25/G28): the Caro-Kann Classical gave +1 by move 31 for the
  fourth time, and this time the FIRST-PLY checks held every move. What worked: (1) king moves chosen by fork
  squares (30...Ke7, not Kc8/Ke8 v Nd6+); (2) interposing a protected rook to cut a defender's line (32...Rd5);
  (3) recapturing toward a pawn chain that took the knight's squares (33...exd5); (4) prophylaxis before a plan
  (37...a5 v b4; 50...Bb4 freezing b3 and guarding a5 together); (5) counting defenders of the push square and
  moving my own king off the bishop's diagonal first (38...Ke6, then 39...d4); (6) a passed pawn escorted by K+B
  until the knight had to give itself up; (7) a king raid only after the queenside was frozen (41...Kf4, 51...Kxg4).
  Keep the king central and off the rim (G28 lesson) - it decided this game.

## Opponent notes (Astra)
- G1 (Black): 1...e5 2...Nc6 3...Bc5, ...d6, ...a5, ...Ne7-g6 plan, ...Bg4-h5-g6. Defends actively with the rook in
  endgames (checks from behind, rook behind passed pawns); did not resign early; resigned when promotion was unstoppable.
- G2 (White): 1.d4 2.c4 3.Nc3 4.Bg5 5.e3 6.Nf3 classical QGD; trades readily (Bxe7, Qd4 offering queens, Rd3/Rc3+).
  Played the K+P accurately (a4+, Kc4, b5+, opposition). As Black, Lasker gave me only a level ending.
- G3 (Black): repeated the G1 Italian setup, deviated 20...Bh7 21...Bxf5 22...d5? (tactically flawed). Seeks counterplay
  (...Rd8 v d3, ...Rf7/...Rf6 v f-pawn, ...g5-h5-h4), checks from behind in rook endings; resigned at ply 121 once
  promotion was unstoppable. Both Italian games: Astra lost a pawn to a tactic around moves 21-24.
- Next Black game v 1.d4: G2's Lasker was a dry level ending. Options: same QGD without the early ...Ne4 trades
  (...Nbd7/...c6/...dxc4/...c5 later), or the Slav (2...c6, ...Bf5 before ...e6). With a 2-point lead, solid is fine.
- G4 (White): Slav main line 5.a4 6.e3 7.Bxc4 8.O-O 9.Qe2 10.e4 11.Bd3 12.e5 13.Nxd5 14.Qe3, then Bd2, Bxg6, Rac1,
  Qd3, b3, a5 (kicking Nb6), Bg5 (bishop trade), Rc2/Rfc1/Qc3-c5-d6 tripling on the c-file, and the tactic 28.Qxf8+.
  Strong at building pressure and at short tactics; converted calmly (Kf1-e2-d3 avoiding knight forks).
  As Black v this Slav, keep the c-file contested (trade a rook pair early), keep the knight on d7 or b6 only with
  retreats, and consider 9...Bg6 or ...Qa5/...Qb6 activity instead of passive queen moves.
- G5 (Black): Italian again but 8...a6 9.a5 Ba7 10...d5 (changes from G1/G3). Defended tenaciously; created queenside
  counterplay with ...c5/...b4/...b3/...b2 and ...Rb6xa6; accepted the locked bishop ending repetition.
- G6 (White): QGD 4.Bg5 5.e3 6.Nf3 7.Bh4 v Tartakower; 10.Rc1 11.cxd5 12.Bxe7 13.e4 accepting hanging c3/d4, then a
  kingside attack: 15.Re1 16.e5 17.Bb1 18.Qd2 19.h4 20.Ng5 21.f4 (aiming f5, Bxg6, Qd3/Qc2 batteries). Declined my
  first queen-trade offer (23.Qf2). In the N ending it was accurate: Kf1-e2-e3-e4 centralisation, d5 break, Nb5 v a7,
  and Ne4+/Nf6+ checks to force the repetition.
- Next Black game v 1.d4 (G8): Tartakower holds but White gets a free attack. Defensive keys that worked: ...g6+...Kg7,
  ...h5 v h4, ...Ba6 (controls d3/e2/f1), ...cxd4 and ...Qb4 queen-trade offers. Alternative: Lasker (G2, level) or the
  Slav (G4 loss, avoid the passive ...Nb6 plan). Choose by score; solid is fine with a lead.
- G7 (Black): Italian again with 8...a6 9.a5 Ba7 10...d5 12...Be6, then 13...Qd7 14...f6 (weakened the a2-g8 diagonal)
  and 16...Nf4? lost a piece. In the ending Astra was excellent: rook raids (Rd3/Rb2), king march to c3/b3, passed c-pawn,
  ...b5! deflection, a-pawn race and the c1=Q+ discovered check. Never assume it will stop fighting; count its checks.
- G8 (White): QGD 4.Bg5/7.Bh4 again; v 10...dxc4/...c5/...b5/...c4 it played 16.e4 17.e5! (piece for pawn tactic),
  then Qh5 + Rh3/Rf3/Rg3 lifts and the b3 lever. Tactically sharp (31.Rxd2 refuting my check idea). Converted Q+N+two
  passers precisely: Qa8+ Qxa5, Qb6 supporting d6 and the a-pawn, a6-a7, Qb8, Qb7+, d7, Ne6. Expect accurate play.
- Match after G8: Astra 4.5 - Opus 3.5 (Astra 3 wins, me 2, 3 draws). Next: G9 as White (Italian).
- G9 (Black): Italian as G7 but 16...Bf7! 17...Rfe8 18...Nf4 (target d3), then ...e4-e3 tactics with the Ba7 x-ray on
  the a7-g1 diagonal (f2/e3 pins). Knight ending: ...a4-a3-a2 tying my pieces, ...Nc4 covering b2, king raid
  ...Kf4-g3xg2-xh4, then ...Kg4!, ...h4-h3, ...Kg2 trapping my Nh2, ...Nd7 v b6. Endgame technique is excellent.
- Match after G9: Astra 5.5 - Opus 3.5 (Astra 4 wins, me 2, 3 draws). Next: G10 as Black v 1.d4 - QGD Tartakower
  with 10...dxc4 11.Bxc4 c5 as G8 (it gave a level, active game); stay alert to e4-e5 tactics and Qh5/rook lifts.
- G10 (White): QGD as G8 (10.Rc1 12.Qe2 13.Rfd1 15.Bb1 16.e4 17.e5); then a direct attack: 20.Ne5 21.Rh3 22.f4
  23.f5 25.Bg3 (x-ray to c7) 26.Ng4 27.Qxg4 28.Be5 30.e6 31.Rg3 (Qxg7# threats), later the a-pawn with Qb6 support.
  Sacrifices pawns for activity; always punishes a hanging piece immediately.
- Match after G10: Astra 6.5 - Opus 3.5 (Astra 5 wins, me 2, 3 draws). Next: G11 as White (Italian; consider
  15.Bh4 + Nbd2 v the 13...Qd7 14...f6 setup, keep d3 covered).
- G11 (Black): v 7.Bb3 played 7...Be6 8...d5 9...Nxd5 10...Bd6 11...f6 (ceded the bishop pair), 15...c5,
  16...Rae8, 17...Bf7 (unpinned and hit my Qe4 down the e-file), 19...Nxe3 with ...Qxg2# support. Calm and precise;
  it takes every hanging piece at once.
- Match after G11: Astra 7.5 - Opus 3.5 (Astra 6 wins, me 2, 3 draws). Next: G12 as Black v 1.d4 (QGD has given
  level middlegames; the losses were blunders, so keep the opening and slow down at every queen move).
- G12 (White): QGD as G8/G10 to 12.Qe2; v 12...cxd4 it traded down (13.Nxd4 14.Bxe7 15.Nxd5 18.Rxc8 21.Bxe4 22.Qb5
  queen trade). B v N technique: king to the centre (Kh2-g3-f4), e4/f4/e5+ space, Nd4-f5+ checks winning g7/h6,
  f5+/g4-g5 connected passers, Ng8-f6-d7-c5 regrouping, Kc4xb4 then Kc5-d6, 60.g6! 62.Nh8+! 63.e6 64.f7+. It
  calculates forcing endgame lines well; do not count on it missing knight forks or pawn breaks.
- Match after G12: Astra 8.5 - Opus 3.5 (Astra 7 wins, me 2, 3 draws). Next: G13 as White (Italian; G11's 7.Bb3 +
  8.Nbd2 + 11.Nc4 gave me a good game - repeat it and do the RAY SCAN/LEAF knight-check scan before every move).
- G13 (Black): repeated G11 to 16...Rae8, then 17...Bf7 18...Qc6 19...Bg6 (pin-breaking manoeuvres), 20...c4! cutting
  my Bb3, 21...Rxe1+ 22...Re8 (back-rank pressure), 23...Bd3 24...Be4 25...f5 (strong bishop), 27...b5 28...a5
  29...Nb6 31...a4 32...Ra8 34...a3 35...a2 (passer to the 7th), 37...Na4, 39...Qd3 into an ending with d- and
  a-passers, 41...d2, and it took 48.Rb1?? at once. It finds every promotion/back-rank trick; expect it.
- Match after G13: Astra 9.5 - Opus 3.5 (Astra 8 wins, me 2, 3 draws). Next: G14 as Black v 1.d4 (QGD with
  12...cxd4 gave a level game in G12). Goal for the rest of the match: no one-move blunders - full scans every move.
- G14 (White): QGD as G12 to 13.Nxd4, then 14.Bxd5 15.Bxe7 16.Rfd1 (x-ray on d5) 17.Qf3 18.h3 19.Nxe4 20.Qg3 21.Nf5
  (Qxg7# idea) 23.Qg4 24.Qxg5 25.Rd7 26.Rd8+ 27.Nd6! 28.Nxb7. Then clean N technique: 30.Nc6 (a7), Kf1-e2, 33.f3,
  35.Nd4, 36.Nf5, 37.b3, 38.Nd4+, 39.a4. It sees two-move check+fork combinations reliably.
- Match after G14: Astra 10.5 - Opus 3.5 (Astra 9 wins, me 2, 3 draws). Next: G15 as White (Italian G11/G13 line;
  improve with 17.h3 and a plan v ...c4; or vary at move 7). Play slower: redraw after every capture in my lines.
- G15 (Black): repeated the G11/G13 Italian to 18...Qc6; v 19.Bc4 it played 19...Nb6 20...Rxe1+ 21...Qd5 (queen trade)
  and 28...Nc4 offering the OCB ending. OCB technique: ...Ka4 probe, ...c4/...b5/...a6 fixing my queenside on dark
  squares, ...Kd5-e4, ...Bc2-d3 (cut my king off e2), ...Kf3-g2-f1, then the quiet 51...Be2! zugzwang and 52...cxb3
  e.p. It plans long king marches and finds quiet waiting/zugzwang moves; it knows en passant.
- Match after G15: Astra 11.5 - Opus 3.5 (Astra 10 wins, me 2, 3 draws). Next: G16 as Black v 1.d4 (QGD Tartakower
  12...cxd4 as G12/G14 gave level games; or the Lasker 7...Ne4 of G2). In endings, keep my king active and guard
  the squares of the enemy bishop's colour with my king.
- G16 (White): 4.Nf3 move order into the Lasker; 9.cxd5 10.bxc3 11.Bd3 13.Re1 14.e4 (IQP after ...cxd4), 19.Re5
  20.Qb3 (accepted my queen trade), 22.d5. It misjudged 23.Nd2?/24.Re4? (lost d5) but then played very actively:
  Nc4-d6 (forks on b7/c8/f7), Re7 + Rae1, 29.Ne8 and 30.Nxf6+! using the pin on g7, rook lifts Re3-g3/b3, 41.Rgf3
  doubling, 42.R7f6 hitting two pawns, then converted R+4 v R+2. It finds pins and rook-lift attacks on the king.
- Match after G16: Astra 12.5 - Opus 3.5 (Astra 11 wins, me 2, 3 draws). Next: G17 as White (Italian G15 line with
  19.Bc4 was fine; keep the bishop pair at move 29). Check pins and my king's flight squares before every king move.
- G17 (Black): repeated the G15 line exactly to 28...Nc4; v 29.Bc1 it played 29...a6 30...b5 (kicking my bishop),
  31...g6 32...f5 33...Ne5 35...c4 (space on both wings), 37...g5! (exploited my king blocking the bishop's
  retreat), 39...f4+ locking, declined my draw offer (42.), tried ...Kc6-b6 and ...a5xb4, then offered a draw at 47.
  It repeats openings that worked; it hunts for pawn hits on pieces with few retreats.
- Match after G17: Astra 13 - Opus 4 (Astra 11 wins, me 2, 4 draws). Next: G18 as Black v 1.d4 (Lasker 7...Ne4 gave
  an equal ending in G16; keep the pieces active after any pawn win and run the PIN SCAN before king moves).
- G18 (White): repeated the Lasker line to 21.Qxb6, varied 22.Rb5 23.Ne5 24.Rb4 25.a4, defended with Nd3-f4-e2-c3,
  lost a pawn to 28...b5, then punished two self-blocks at once (43.Raxa2, 47.Rxf7), pushed the d-pawn to d6 with
  K+N+R support (Ke5-f6-e6, Nc5+/Ne4+ checks), and finished with 65.Rb8#. It looks for mating nets around a
  blockading king and checks every square my king can use.
- Match after G18: Astra 14 - Opus 4 (Astra 12 wins, me 2, 4 draws). Next: G19 as White (Italian G17 line; keep
  the bishop pair and the king off the bishop's retreat). MATE SCAN + SELF-BLOCK scan before every move.
- G19 (Black): repeated the G11-G17 Italian to 17...Bf7; v 18.Qf3 played 18...Qc6 19...c4 20...b5 21...Bg6 (accepted
  doubled g-pawns), 24...Re6 (queen behind rook), traded into a rook ending at move 28. In the ending: ...g5/...g6/
  ...g4 space, ...Re6-e2 the moment my king left the e-file, ...Rg2+/...Rg3 hitting c3+h3, ...Kc7-d6-d5-e4-d3 king
  march behind its c-pawn, ...c3-c2-c1=Q forcing my rook off, then ...Kxf4, perpetual-style checks, and finally
  ...Ke5-d6-c6-b7 going for my a-pawn while the rook held h7 (a win if I had waited). Precise and patient.
- Match after G19: Astra 14.5 - Opus 4.5 (Astra 12 wins, me 2, 5 draws). Next: G20 as Black v 1.d4 (Lasker 7...Ne4,
  as G16/G18: good endings for me). Keep the MATE/PIN/SELF-BLOCK scans; in rook endings keep binds before releasing.
- G20 (White): repeated the Lasker line to 24.Rb4, varied 25.Kf1 26.g3 27.Ke2 28.Ke3 (king to the centre), 29.Ng6+
  30.Nf4, 31.d5!? (trap: Bxd5? Nxd5 Kxd5 Rd1+ skewer), 32.Kd4, 33.Rc4 34.Rxc5, then defended a pawn down with checks
  (38.Rd1+ 39.Re1+), 40.f3 41.g4 to hold its rim knight, and 45.f4! set up 46.Nxf4+ forking king and rook. In R v B it
  was exact: 51.Rxb5+, 52.Rh5+, 53.Rxh6, 56.Rd6, 57.Rxd3, 58.Rd4 pin. It sets small tactical traps when worse.
- Match after G20: Astra 15.5 - Opus 4.5 (Astra 13 wins, me 2, 5 draws). Next: G21 as White (Italian G17/G19 line;
  play h3 early for luft). New rule: KNIGHT RECAPTURE FORK scan before every capture, most of all when winning.
- G21 (Black): repeated the Italian to 20...b5, varied 21...g6 (instead of G19's ...Bg6), traded both rook pairs
  (22...Rxe1+ 23...Re8), 27...f5 28...a5 29...b4, offered the queen trade 30...Qf6, then 32...b3! lever, king march
  ...Kf8-e7-d6, 38...a4, 40...Bc4+! (check + hit my loose Bb5), 42...a3! breakthrough. In N v pawns: ...Kd5-c5
  blockade, ...Nd2+/...Ne4 probes, 51...f4! (fixed g2, freed f5), ...Nf5, ...gxh5, ...Ne3+, ...Nxg2, ...Kb6 for a4.
  Its endgame plans are concrete and patient; it uses pawn levers to create targets for its king and knight.
- Match after G21: Astra 16.5 - Opus 4.5 (Astra 14 wins, me 2, 5 draws). Next: G22 as Black v 1.d4 (Lasker 7...Ne4,
  as G16/G18/G20 - good endings, the losses came later). Rules to carry: CHECK + LOOSE PIECE scan (bishop checks that
  hit a loose piece), knight-fork scan on every recapture, do not trade queens while the enemy majority is rolling.
- G22 (White): repeated the Lasker line to 32...Rc8, improved with 33.h4 (no ...g5), defended a boxed king calmly
  (34.Rf1, 35.Rb3), took b5 at once (37.Rxb5), found 40.d6+! (pawn check uncovering Rb5 on Bf5), avoided all my
  traps (43.Ke4 not Nd3?; 44.Rd5+, 45.Rd3 offering the trade), then 47.Rb1/48.Rb6+ tying me to b7, Nf4-d5-f4-g6
  (outpost protected by h5), 51.h5, 54.Kf5, 56.f4 (declined my repetition), 57.Kh4 58.g4 preparing g5. It notices
  every unguarded unit and every discovered line within one move.
- Match after G22: Astra 17.5 - Opus 4.5 (Astra 15 wins, me 2, 5 draws). Next: G23 as White (Italian; G21 showed
  that Black's ...a5/...b4/...b3 majority beats my bishop pair once queens go - stop it with a3/cxb4 first).
  Before every move: what does the moving piece stop guarding, and which enemy pawn checks open lines.
- G23 (Black): repeated the Italian to 18...Qc6; v 19.Bc4 traded both rooks (19...Rxe1+ 20...Re8 21...Rxe1+), hit my
  loose Be1 (22...Qe6), gained space with tempo (23...a6 24...b5), recaptured 25...Qxd5 offering the queen trade,
  then in the OCB ending: 27...Kf7-e6, 29...Bxg2 at once, 30...c4 (fixing my queenside), 31...Kf5, 32...g5 lever,
  34...h5, 35...Bh3/38...Bf1 (light-square control around my king), 41...h3, 42...Kg3, 43...Kxf4, 44...Bf1 (guard
  h3), 45...Ke4 heading for c2. It converts OCB endings by combining a passed pawn on each side with king raids.
- Match after G23: Astra 18.5 - Opus 4.5 (Astra 16 wins, me 2, 5 draws). Next: G24 as Black v 1.d4 (Lasker line;
  it was good until my own oversights). Seven games left: play for solid positions, run LAST GUARD (incl. king
  moves) and PATH before every move.
- G24 (White): 1.e4 (not 1.d4 this time), Caro-Kann Classical with 6.h4 7.Nf3 8.h5 9.Bd3 11.Bd2 12.O-O-O 13.Ne4
  15.Qe2 16.Kb1 17.c4 (queen trade accepted), 20.Ne5 21.g4 (kingside space), 24.f3 25.f4 26.Rd4 27.exf6 e.p.,
  28.Rd6/29.Rxe6, then defended passively (Re4/Re5/Kc2) and lost two pawns. It set the trap 41.b4 (a3 now guarded
  by the rook) and 42.Rg3 (kept a3 guarding b4) and took the rook at once.
- Match after G24: Astra 19.5 - Opus 4.5 (Astra 17 wins, me 2, 5 draws). Next: G25 as White (Italian; or vary).
- G25 (Black): v 7.h3 played 7...Be6 8...d5 9...Re8 10...Bd6 11...h6 12...Qd7 (h3 battery) 13...Rad8 14...dxe4 15...Bxb3
  (doubled my b-pawns), 17...Qe6 (v b3), 18...Bf8, 19...Ne7 20...Kh7 21...g6 (kicked Nf5), 25...Bc5 (pin on Be3 v Kg1),
  26...b6, 31...Nf6 32...Nxd5 (traded my good knight), 34...c6 (counter v d5) and 39...f5 (opened its 7th rank - a
  mistake). Defended a pawn down calmly and took 43.Rh7?? at once. It never misses a free piece.
- Match after G25: Astra 20.5 - Opus 4.5 (Astra 18 wins, me 2, 5 draws). Next: G26 as Black (v 1.d4 Lasker; v 1.e4
  Caro-Kann Classical). Five games left. Before typing ANY move: who attacks the landing square (king included)?
- G26 (White): 1.e4 again, Caro-Kann Classical as G24 but 16.c4 (before Kb1), accepted the queen trade, 19.Nd2 20.c5
  (space, kicking my knight), 21.Ne4 22.g4 (kicked Nf5: forced ...Nxe3), 24.Nd6 outpost, 27.b3, then 29.a3! at once
  (hit the only guard of my bishop). In R v B+2P: Ke2-e3-f4-e4-f5-g6xh6, Rc4/Rc2 tying my bishop, 44.g5! lever,
  46.h6+ and 47.Rf2+ with a mating net. It converts endings with king raids plus a rook check at the right moment.
- Match after G26: Astra 21.5 - Opus 4.5 (Astra 19 wins, me 2, 5 draws). Next: G27 as White (slow Italian of G25).
  Four games left. Before every move: landing square attackers (king too) AND can the opponent hit my last guard.
- G27 (Black): repeated G25 to 27...Nxc5, improved 28...c6 (denied d5), 29...Nd7 30...Ra8 (held a6) 31...b5 (hit
  Qa4/c4) 32...Nb6 (hit c4 again, inviting c5) and took 33...Qxb3 at once. It set up the queen x-ray before I moved.
- Match after G27: Astra 22.5 - Opus 4.5 (Astra 20 wins, me 2, 5 draws). Next: G28 as Black (Caro-Kann Classical
  v 1.e4, Lasker v 1.d4). Three games left. FIRST-PLY checks out loud before every move.
- G28 (White): Caro-Kann Classical a third time (G24/G26/G28), varied 28.Nc4 and gave up c5 for activity (29.Rxd8
  30.Nd6 31.Nc4), centralised its king (Kd2-e2-f3-f4), 36.e4 37.Ne5 38.Rc1 39.Rxc5, rook checks from b8/a8 that drove
  my king to the edge, 48.e5 49.Rg8 51.Rxg7 52.Rh7, 54.Kd5 with tempo, 55.Rh8 56.Rg8 hunting my bishop, 57.Nd6!
  (Kc6 + Ra8# threat and Nxf5), 58.Nxf5, 60.e6, then 61.Kd6 offering a poisoned knight. It builds mating nets
  against an edge king and turns them into material.
- Match after G28: Astra 23.5 - Opus 4.5 (Astra 21 wins, me 2, 5 draws). Next: G29 as White (slow Italian of
  G25/G27; at move 33 play Red1/Kh2, not c5), then G30 as Black. Two games left. FIRST-PLY checks before every move;
  in endings keep my king central and count my bishop's safe squares.
- G29 (Black): repeated the G25/G27 Italian to 29...Nd7, then 30...Nf6 31...Qc8 (held a6) 32...Rxd3 33...Rd8 34...Qe6,
  35...b5! (closed the queenside after my c5), 36...Rxd1+, 37...Nh5-f4 38/39 (outpost), 39...h5 40...Qf6 41...Ne6
  42...Nd4 43...Qg5 44...h4! lever, 45...hxg3+ 46...f5! (pinned knight hit by a pawn), then Q+N play against my
  king: 50...Qh6 (trade offer), 54...Qb3, 55...Nxf3!, 56...Nd4+ (discovered check), 57...Qd5+, 58...e4. It builds
  outposts for its knight, uses rook-pawn levers against my king and spots pins at once.
- Match after G29: Astra 24.5 - Opus 4.5 (Astra 22 wins, me 2, 5 draws). Next: G30 as Black, the last game
  (Caro-Kann Classical v 1.e4 - three good endings; Lasker v 1.d4). After it: summarize the match and stop.
- G30 (White): repeated the Caro-Kann Classical a fourth time to 29.Rxd8, varied 30.Rd1+ 31.Nd6, accepted the rook
  trade 33.Rxd5, then fought a pawn down with Nf5+ checks, Kc2-d3 blockade, a3-a4, 39.e4 (to break my centre),
  40.Kc4 41.Ng3 42.Nf5 43.Kxc5, Nd6+/Nc4+ checks against my king and 48.Nxd2 giving the knight for the d-pawn.
  Resigned after 51...Kxg4 (B+4 v 3).

## FINAL RESULT (all 30 games played)
Astra 24.5 - Opus 5.5. Astra 22 wins, Opus 3 wins (G1 White, G3 White, G30 Black), 5 draws (G2, G5, G6, G17, G19).
The bounded task of this branch is complete; no game 31.
