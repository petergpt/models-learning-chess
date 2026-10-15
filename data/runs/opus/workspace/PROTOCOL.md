# Move protocol (read before each game; keep short)

Board reading: python-chess ASCII, rank 8 at top, files a..h left->right. UPPER = White, lower = Black.
Index each row carefully (count 8 cells). Cross-check suspicious squares against the FEN.
NEVER send test input to ./play move (every submission counts; 3 illegal = forfeit).
UCI only: e2e4, castling e1g1/e1c1/e8g8/e8c8, promotion e7e8q. 3 illegal tries on one turn = forfeit.

SAFETY TABLE (mandatory, written out, every move in rated games; block-2 lesson G7-G11 = 0/5 from blunders):
  K: enemy knights -> their target squares (write all 8 squares for each knight).
  S: destination square Y: which enemy pieces attack Y? (go through EVERY enemy piece; sliders: trace line).
  D: what was the moving piece defending? still defended after the move? AND what enemy line was it BLOCKING
     (moving it may open a rook/bishop line onto my pawn/piece/king: P1 drill Rxc7, Rxf7)?
  B: does Y block one of my own lines (rook/bishop/queen defence or attack through Y)?
  C: opponent checks & forks after my move (incl. knight forks of K+R/Q, back-rank mates).
     For EVERY check: write my king's escape squares one by one (and blocks/captures). Zero escapes = mate = reject.
  KING RULE: with enemy R/Q + minor still on board, my king must not step next to enemy pieces/pawn chains
     unless C has been done square by square. Endgame king walks caused G10 and G12 mates.
  Only then submit.

Every move:
1. Opponent's last move: what does it attack / threaten now (checks, captures, forks, discovered lines,
   mate threats)? What did it stop guarding?
2. My loose pieces: anything attacked and under-defended, or attacked by a cheaper piece?
3. Candidates: my checks, captures, threats first; then the plan move.
4. LINE AUDIT (T1, from block-1 errors) for the moving piece:
   - Path: name every square between from- and to-square; all empty? (2 illegal tries came from this.)
   - What does it defend NOW (list), and will those still be defended after it moves?
   - Does its new square block one of MY lines (rook/queen/bishop defence through that square)?
   - Any enemy rook/bishop/queen x-ray that becomes a pin or skewer after the move?
5. DESTINATION CHECK (hard rule after G5/G9 queen-loss pattern): write the enemy piece list from the FEN and,
   for EACH enemy piece, ask "does it attack my destination square?" Especially: a rook/queen I attack along a
   line attacks me back along that line, and it is THEIR move. Never place Q/R on a square an enemy piece hits
   unless it is a deliberate, calculated trade.
6. Before submitting the chosen move:
   a. Legality: from-square holds my piece; path empty; piece not pinned; king not left in check.
   b. Blunder check: after the move, list EVERY opponent check and capture (incl. queen/bishop long
      diagonals, knight forks, back rank). Does anything lose material or allow mate?
   c. What did the moving piece stop defending?
   d. PINS: any of my recapturing/defending pawns or pieces pinned to my king (open files/diagonals
      to the king)? A pinned unit is not a defender. (G1: lost queen to this.)

Budget: aim ~1k tokens/move in quiet positions; think long only at real tactical moments.
Resign clearly lost positions vs full/1800 (e.g. down >=3 pts, no counterplay) instead of grinding.

Conversion (ahead in material): trade pieces not pawns, keep king safe, push passers, mate methodically.
STALEMATE CHECK whenever opponent has only king (+ blocked pawns): after my move, does their king have a move?
Draw claims are automatic: avoid repeating positions when winning.
