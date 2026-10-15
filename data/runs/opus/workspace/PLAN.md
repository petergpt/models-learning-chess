# Plan and learning log

## Facts about the measurement (from reading the referee code; operator-owned)
- Rotation per 6 games: full-strength W,B; skill-0 W,B; elo-1800 W,B. Engine: 1M nodes/move.
- Elo uses ONLY skill-0 (anchor 1320) and 1800-setting games; rolling window = last 50 rated games.
  200 games -> ~132 rated; final estimate ~ games 125-200.
- Full-strength games are benchmark evidence but excluded from Elo.

## Approach (initial hypothesis, unverified)
Main expected error sources for me: misreading the board, hanging pieces, missing opponent tactics,
illegal-move submissions, sloppy conversion (stalemate/repetition), long games burning budget.
Method: fixed per-move protocol (PROTOCOL.md), simple repertoire (REPERTOIRE.md),
post-game review of every non-win vs rated opponents (own analysis only; no engine),
error taxonomy with recurrence counts (ERRORS.md), targeted practice from my own failed positions.

## Evaluation
Each full rotation (6 games) = checkpoint; compare rated score and error recurrence per 12 games.

## Trials log
- T0 (games 1-6): baseline with PROTOCOL.md + REPERTOIRE.md. Next checkpoint: after game 6.
- T0 result (games 1-6): full 0/2, skill0 2/2, 1800 1/2 (won because opp blundered a knight on move 4; lost G6
  from my own line errors). Elo 1870 [1410,2460] after 4 rated games. Tokens used ~508k (too many: ~85k/game).
- T1 (games 7-12): weakness = line-of-sight errors (pins on defenders, self-blocking, abandoned defences, path
  errors). Trial = explicit LINE AUDIT step in PROTOCOL.md + token discipline (resign hopeless games early).
  Observable: 0 illegal attempts; fewer self-inflicted material losses in rated games (block 1: G6 had 3);
  average tokens/game <= 60k. Next evaluation point: after game 12.
- T1 result (games 7-12): 0/6 (full 0/2, skill0 0/2, 1800 0/2). Line audit helped occasionally (caught Ne7 self-block,
  Bb4?? Qa4+, Qxb2?? Qxe8+) but one-move blunders still decided every game: G9 Qc8??, G10 Rxf3?/Rh1??, G11 Nd4??/Rd4??,
  G12 Kxd5??. Decision: the method is right but the execution is superficial -> T2.
- T2 (games 13-18): explicit SAFETY TABLE every rated move with escape-square enumeration for each enemy check, and the
  KING RULE for endgames. Full-strength games: lighter version, resign hopeless positions early.
  Observable: one-move blunders per rated game (block 2 ~1.5) -> target <=0.5; rated score > 0/4. Evaluate after G18.
- Practice P1 (G12 ply 44, vs 1800, Black, +1 endgame): 30 moves, stopped at +2 (drawish). With written escape-square
  checks: no mate/fork blunders; but 2 "unblocking" oversights + 1 illegal (own K in rook path). Added to table (D).

- T2 RESULT (G13-18): rated 3/4 (was 0/4); Elo 1560 [1310,1810] after 12 rated. Blunder rate ~1/rated game (target
  0.5 missed); errors moved from mate/fork to "attacked-pawn census" and move-shape/path legality. Keep the table.
- T3 (games 19-24): COMPACT protocol + token budget. Each move: (1) census of every enemy line from the piece that just
  moved (all its targets) + list my loose men; (2) 1-3 candidates; (3) compressed safety table (K/S/D/B/C);
  (4) shape+path check for the chosen move (delta, every intermediate square from the FEN, incl. double pawn pushes).
  Budget <=60K tokens/game (185 games left need ~74K/game). Resign lost positions vs full/1800 at once.
  Observable: avg tokens/game <=75K over G19-24 AND rated blunders <=1/game AND 0 illegal attempts. Evaluate after G24.

- T3 RESULT (G19-24): tokens ~44K/game (met), but rated 1/4, Elo 1490 [1270,1700] after 16 rated; blunders >1/game,
  2 illegal. Compactness cut the from/to-square line checks that caught these errors.
- T4 (games 25-30): budget by opponent (full ~20K, rated ~90K) + a mandatory written LINES note on every rated move:
  FROM-sq: 8 lines through it -> enemy slider behind it aiming at my piece/K? what did it guard? TO-sq: whose lines
  does it now block (mine!), who attacks it, and if it is a recapture square is it attacked again (x-ray)?
  + back-rank status + path squares read from FEN. Observable: <=1 decisive blunder in the 4 rated games, 0 illegal.

- T4 RESULT (G25-30): rated 2/4, Elo 1500 [1310,1700] after 20 rated; 0 illegal moves (path check works);
  ~40K tokens/game. Still 2 decisive one-move losses, both missed enemy captures after my move.
- T5 (games 31-36): keep T4 + CAPTURE SCAN: after picking a candidate, for every enemy piece list each of my men it
  attacks in the NEW position (incl. through squares my move vacated) and whether the capture wins material.
  Rated games may use ~60K tokens, full-strength ~20K. Observable: 0 lost-material blunders from enemy captures.
- T5 RESULT (G31-36): rated 2.5/4 (W,W,D,L), Elo 1540 [1360,1710] after 24 rated; but NOT met: 4 material-losing
  misses (G31 Nb3, G34 Qxc2, G35 c6, G36 bxa3/Nxf5+) and 5 illegal attempts; ~85K tokens/game (over budget).
- T6 (games 37-42): THREE WRITTEN LINES before every rated move, no exceptions, kept short:
  P = path: every square between from/to with its occupant (mine too) + "is the mover pinned to my K?";
  F = from-square: what did the mover defend/block (pawns included);
  C = captures: each enemy piece -> which of my men it can now take (knight jumps first, lines through the vacated
  square), and for any capture I make, every recapturer.
  Plus: when ahead, trade pieces; vs full strength resign at -3. Budget: full <=15K, rated <=70K.
  Observable: 0 illegal attempts and <=1 material-losing miss over the 4 rated games. Evaluate after G42.
- T6 RESULT (G37-42): 0/6, rated 0/4 (2 losses to skill 0!), Elo 1460 [1300,1620] after 28 rated. ~36K tokens/game:
  the "three short lines" became perfunctory; misses: battery (G37), king walk into mate (G39), batched second move
  (G40), fork/rank lines (G41), back rank + pin + defender count (G42). 3 illegal attempts. NOT met.
- Budget check: 12.34M tokens / 158 games left. Full-strength games (~53) at <=12K each leave ~110K per rated game.
- T7 (games 43-48): SPEND the budget on rated games (target 90-120K each, no compact mode) and run the FULL check on
  every rated move: (1) what the opponent's last move attacks / opened; (2) 2-3 candidates; (3) for the chosen move:
  path squares incl. my own men, is the mover pinned, what it used to defend; ALL enemy checks and captures after it,
  each with an attacker/defender count including the defenders of the capturing piece; knight forks; back rank.
  Exactly one move command per turn. Full-strength: quick play, resign at -3.
  Observable: rated score >= 2/4 and <= 1 material-losing miss per rated game. Evaluate after G48.
- T7 RESULT (G43-48): rated 2/4 (G45 W, G46 L, G47 W, G48 L), Elo 1470 [1320,1620] after 32 rated (13.5/32).
  Target half met: score 2/4 yes; "<=1 material-losing miss per rated game" yes in count, but each loss was one such
  miss on a "routine" move. Spend ~290K tokens for 6 games (~65K per rated game, under the 90-120K target).
- Budget check: 12.04M tokens / 152 games left -> full-strength ~10K each (~510K), rated ~110K each.
- T8 (games 49-54): (a) RENDERING: mv prints rank-labelled board + piece lists from the FEN (pure rendering, no
  chess logic) so misreads of who stands where drop. (b) NO ROUTINE MOVES: the full enemy-reply scan (every enemy
  piece: its captures and checks after my move, incl. lines through the square I vacated and lines my moved piece
  now shares with an enemy piece) is written for EVERY rated move including development and recaptures; the scan
  must name the enemy pieces one by one. (c) vs skill 0 play safe, simple chess: when ahead, trade; never allow
  counterplay. Observable: rated score >= 3/4, zero one-move material losses. Evaluate after G54.
- T8 RESULT (G49-54): rated 1.5/4 (G51 W, G52 D, G53 L from +2, G54 L), Elo 1470 after 36 rated. NOT met. Rendering
  helped (fewer misreads) but 3 illegal attempts (all slider paths/knight geometry) and 4 one-move oversights.
  ~550K tokens for the block.
- T9 (games 55-60): SQUARE SCAN instead of piece-by-piece scans. For (1) the destination square of every move,
  (2) every square in a capture sequence I plan, (3) my K's flight squares whenever a check is possible, walk the
  rays OUTWARD from the square: 2 enemy-pawn squares, 8 knight squares, 4 diagonal rays to first piece, 4 straight rays
  to first piece, enemy K. For every slider move, list the path squares by name with occupants. Prefer simple moves
  in sharp positions; no speculative grabs (G54 Bxg4) unless the scan proves them. Observable: zero one-move material
  losses and zero illegal attempts in rated games; rated >= 2/4. Evaluate after G60.
- T9 RESULT (G55-60): rated 2/4 (G57 W mate, G58 L, G59 L, G60 W mate), Elo 1480 after 40 rated. Met: rated >= 2/4,
  0 illegal in rated games. Not met: 2 one-move material losses (x-ray rook battery; vacated-line queen loss).
  ~270K tokens for the block.
- T10 (games 61-66): keep T9 square scans, and add two fixed sub-steps to every rated move: (1) ORIGIN SCAN - list
  enemy rays (Q/R/B lines) that pass through the square my piece leaves and what they hit once it is empty;
  (2) X-RAY COUNT - when counting attackers along a line, look past the first attacker for a second enemy slider
  on the same line (doubled rooks, Q+B, Q+R). Observable: zero one-move material losses in rated games, 0 illegal,
  rated >= 2/4. Evaluate after G66.
- T10 RESULT (G61-66): rated 3/4 (G63 W, G64 W, G65 W vs 1800, G66 L vs 1800), Elo 1510 [1380,1640] after 44 rated
  (best so far). Score target met. Process targets NOT met: 1 illegal attempt (G65, rook path through own pawn), one-move
  losses G64 (B lost for P after a capture left two pieces loose) and G66 (discovered attack on my Q). ~460K tokens for
  the block (~76K/game).
- Budget check: 10.76M tokens / 134 games -> ~80K per game average; keep full-strength games short (~12K).
- T11 (games 67-72): keep T9/T10 scans and add the DISCOVERY CHECK: on each ray from my destination square, if the
  first piece is an enemy piece not attacking along that ray, look behind it for an enemy Q/R (file/rank) or Q/B
  (diagonal); if found, ask whether the blocker can move with check/capture. Also after any capture I make, list
  every one of my pieces that is attacked after the opponent's most forcing reply (checks first). Write slider paths
  for retreats too. Observable: no discovered-attack or fork losses, 0 illegal in rated games, rated >= 2/4.
  Evaluate after G72.
- T11 RESULT (G67-72): rated 2/4 (G69 W, G70 L from +5, G71 W vs 1800, G72 L vs 1800), Elo 1510 [1390,1640]
  after 48 rated. Score target met, 0 illegal. NOT met: three single-move losses - G69 own knight unblocked a rook
  onto my queen (origin scan skipped), G70 knight fork after a queen move (reply scan skipped), G72 bishop moved
  onto an enemy rook's open file (destination scan skipped). All three were on "quiet" moves in good positions.
- T12 (games 73-78): (1) Every move's reasoning must contain three explicit lines before the command:
  DEST (rays + knight squares + pawns from the destination), ORIGIN (lines through the vacated square),
  REPLY (all enemy checks and captures next move; for each check, what else the checker hits). No exceptions for
  "obvious" moves. (2) When ahead by >= 2: trade queens/rooks, keep every piece protected, no pawn grabs with
  pieces near the rim. Observable: zero one-move material losses in rated games, rated >= 2/4. Evaluate after G78.
- T12 RESULT (G73-78): rated 1.5/4 (G75 W, G76 D from a rook down, G77 L, G78 L vs 1800); full 0/2.
  Elo 1490 [1370,1620] after 52 rated (flat since T9). 0 illegal in rated games except G76 (1).
  NOT met: three one-move losses, each in a category the DEST/ORIGIN/REPLY lines did not force me to enumerate:
  G76 37...Rxa3?? (a knight's attack square skipped), G77 31.Rxb5?? (my R and Q lined up on one diagonal ->
  ...Ba6 skewer), G78 22...Qxh3+?? (in a "forced mate" I listed the king's flight squares but not KING CAPTURES
  THE UNPROTECTED CHECKER). Also G77: a knight outpost (Ng5) with no retreat got trapped by a pawn push.
  Decision: keep T12 lines but replace the free-text REPLY with fixed checklists (T13).
- T13 (games 79-84): (1) For any check or sacrifice I calculate, enumerate replies in fixed order at EVERY node:
  a) capture the checker/sacrificed piece - by each enemy piece INCLUDING THE KING (is my piece protected?);
  b) interpositions; c) every king square. A line is "forced" only if all three lists are written.
  (2) LINE-UP scan after each move: any two of my K/Q/R/unprotected pieces on one rank/file/diagonal with only
  empty squares between and an enemy slider able to reach that line next move = skewer/pin, reject.
  X-ray: an enemy rook/queen behind an enemy piece on a line counts as a defender of that piece's targets.
  (3) DEST must list enemy knight attack squares explicitly ("knights: Nc4 hits a3,a5,b2,b6,d2,d6,e3,e5").
  (4) Advanced pieces: after each enemy pawn push, list my piece's retreat squares; keep one.
  (5) Vs 1800/full: no speculative sacrifices unless (1) is written out to mate or material gain.
  Observable: zero one-move material losses in rated games; rated >= 2/4. Evaluate after G84.
- T13 RESULT (G79-84): full 0/2; rated 2/4 (G81 W, G82 L, G83 D, G84 D) -> "rated >= 2/4" met.
  Elo 1510 [1390,1640] after 56 rated (flat since T9, within noise). NOT met: zero one-move losses
  (G82 x3, G83 23.g4 e.p., G84 16.Bb4 skewer / 36.Bxg6+ / 39.fxg4); 4 illegal path errors in 6 games.
  The fixed check-node order (capture-by-king first) and en-passant check did work when written (G84 b5 trap).
  Decision: keep T13; add the two scans that cover the remaining root causes (enemy diagonals, recaptures).
- T14 (games 85-90): T13 plus
  (1) ENEMY-SLIDER sweep before submitting: for each enemy Q and B (then R) list the squares it can reach next
      move that attack two of my K/Q/R/loose pieces, or one of them with another behind it on the same line
      (skewer/pin). Diagonals explicitly - both of my Q+R and K+R on a diagonal are targets.
  (2) RECAPTURE check: whenever my plan relies on a capture or recapture (by any piece, incl. the king), list the
      enemy attackers of that square AFTER the exchange, including lines opened by the pieces removed.
  (3) PATH line mandatory for every slider and two-step pawn move ("PATH: e7 d7 empty").
  Observable: zero illegal attempts; zero one-move material losses in rated G87-90; rated >= 2/4. Evaluate after G90.
- T14 RESULT (G85-90): full 0/2; rated 4/4 (G87 W skill0, G88 W skill0, G89 W 1800, G90 W 1800), all by mate.
  Zero illegal attempts in 6 games (PATH line caught 4 blocked moves: Bc1-f4, c2-c4, Rf2-c2, Rh4-e4).
  Zero one-move material losses in rated games. Elo 1560 [1440,1680] after 60 rated (+50 from 1510).
  Caveat: two 1800 wins came after big opponent errors (15...h6? allowing bxa8=Q; 26.Ng2?? dropping the queen),
  so 4/4 overstates the change; the observable process targets (0 illegal, 0 one-move losses) are the real signal.
  Decision: keep T14 unchanged for one more block as a replication (T15 = T14), evaluate after G96.
- T15 RESULT (G91-96): full 0/2; rated 4/4 (G93 W, G94 W skill0; G95 W, G96 W 1800). Elo 1610 [1480,1730]
  after 64 rated (+50; T14+T15 rated 8/8). Process targets NOT met: 2 illegal (G93: own-king occupancy,
  enemy knight on the path) and one-move losses in G93 (32.Kc3?? Rxa3) and G95 (22.Bxf4?, 24.Kxf2 Bxa1,
  27.Rxa7? Bd4+). G96 had none. Opponent errors again helped (G96 20.a4?), so the result streak overstates it.
  Decision: keep the T14 checklist; make the three lines that the slips came from mandatory written lines (T16).
- T16 (games 97-102): T14 plus, written for EVERY move:
  (1) GUARD: "X on <sq> was guarding: ..." for the moving piece (king moves included) - is anything left loose?
  (2) UNMASK: after each enemy move, the lines its origin square opened (discovered attacks on my pieces).
  (3) CHECK+HIT: for each enemy check in REPLY, what else the checking piece attacks from that square.
  (4) KNIGHT fork squares for each enemy knight (two targets of mine from one square).
  Observable: zero illegal; zero one-move material losses in rated G99-102; rated >= 2/4. Evaluate after G102.
- T16 RESULT (G97-102): full 0/2; rated 2.5/4 (G99 W, G100 D, G101 W, G102 L). Elo 1640 [1520,1770] after
  68 rated (+30, within noise; T14-T16 rated 10.5/12). NOT met: 1 illegal (pinned pawn, G100) and one-move
  losses in G100/G102. The GUARD/UNMASK lines were written but the misses were pieces I did NOT move: a loose
  knight on an enemy rook's rank, an enemy battery masked by its own bishop, a guard I removed.
  Decision: keep T16; add an enemy-centric ATTACK MAP as the last check before every move (T17).
- T17 (games 103-108): T16 plus, as the final written line before submitting:
  ATTACK MAP: for each enemy R, Q, B, N (and pawn captures), list which of MY pieces it attacks on the board
  AFTER my move (current lines, including lines opened by my last two moves and enemy batteries with one enemy
  piece in between), and the number of attackers vs defenders of each. Any piece with attackers > defenders, or
  attacked by a lower-value piece, blocks the move.
  Also: before any pawn move, check whether my king is behind it on a line with an enemy slider (pin).
  Observable: zero illegal; zero one-move material losses in rated G105-108; rated >= 2/4. Evaluate after G108.
- T17 RESULT (G103-108): full 0/2; rated 2/4 (G105 W, G106 W skill0; G107 L, G108 L 1800). Elo 1620 [1490,1740]
  after 72 rated (-20, within noise; T14-T17 rated 12.5/16). 0 illegal (met). One-move losses NOT met: G105 15.axb3?,
  G107 33.Bxh3?? (check that also hit Rd1) and 38.Qf4?? (Qxh2+ Kg4 Qh5#), G108 20...gxf6? (Kg2 unmasked Rg1 onto Qe1)
  and 33...Bg5? (pinned interposition). Every 1800 error came with a king exposed in a sharp position; G107 was lost
  from +4. The attack map was written but checked only one ply deep.
  Decision: keep T17; add a king-danger procedure and a risk policy (T18).
- T18 (games 109-114): T17 plus
  (1) RISK POLICY: when ahead by >= 2, prefer the move that trades queens or removes the enemy's best attacker;
      eliminate enemy pawns lodged next to my king (G107 h3); do not recapture/grab in a way that opens a file or
      diagonal onto my own castled king (G108 ...Bxf3 gxf3) unless the king-danger tree below is clean.
  (2) KING-DANGER TREE, mandatory when either king has an open line to an enemy Q/R or < 2 shield pawns:
      for each candidate write every enemy check and capture; for each check, my legal replies; and for each reply
      the enemy's next check. For every flight square, test the checking line extended through my king (x-ray).
  (3) UNMASK covers enemy KING moves too, and for each enemy piece: "if it moves, what is behind it?"
  Observable: zero one-move material losses in rated G111-114; rated >= 2/4. Evaluate after G114.
- T18 RESULT (G109-114): full 0/2; rated 1.5/4 (G111 W, G112 L skill0; G113 D, G114 L 1800). Elo 1640 [1520,1770]
  after 76 rated (+20 vs block 18, within noise). Observable NOT met: one-move losses in G112 (14...Qxb1+??,
  25...Bb6?, 42...Bxe5?? Qxh5#), G113 58.Re4??, G114 62...Kg6?? Qxh5#; 1 illegal (G114 11...Bh7, own piece on path).
  The two-ply tree did catch tactics (G114 42...Bf8? rejected) but missed capture-checks next to my king.
  Decision: keep T18; add capture-check and king-move audits (T19).
- T19 (games 115-120): T18 plus
  (1) CAPTURE-CHECKS: the enemy-check list starts with every enemy capture that gives check; for each, is the
      capturing piece protected (then my king cannot recapture)? Compute the flight squares.
  (2) KING-MOVE AUDIT: before any king move, write the 8 neighbours of the destination and which enemy piece
      attacks each now or can land there next move with protection; reject the move if some enemy check then has
      no non-losing reply.
  (3) PATH for every slider move, retreats included: name each square on the path and what stands there.
  Observable: zero illegal; no mate-in-1 or one-move material loss in rated G117-120; rated >= 2/4. Evaluate after G120.
- T19 RESULT (G115-120): full 0/2; rated 2/4 (G117 W, G118 W skill0; G119 L, G120 L 1800). Elo 1660 [1540,1790]
  after 80 rated (+20, within noise; T14-T19 rated 16/24). Rated >= 2/4 met. Zero illegal NOT met (3 PATH errors).
  No mate-in-1 losses (met for the king audits), but one-move material losses in G117, G119 (two), G120 (two).
  Decision: keep T19; the remaining failures are line effects, so add them to the per-move block (T20).
- T20 (games 121-126): T19 plus a written 4-line BLUNDER BLOCK on every move:
  (1) OPP: what did the opponent's last move attack, and what line opened through the square it LEFT?
  (2) PATH: origin -> each intermediate square (name the occupant) -> target, for every slider and double step.
  (3) LINES: after my move, which of my guards are cut (destination between defender and defended) or lost
      (the mover's old duties), and which enemy lines open through my origin square?
  (4) REPLIES: every enemy check (captures and discovered checks first), every enemy capture with the safety of
      my recapturing piece on that square (long-range attackers included), and my queen's safe squares.
  Observable: zero illegal; no one-move material loss in rated G123-126; rated >= 2/4. Evaluate after G126.
- T20 RESULT (G121-126): full 0/2; rated 3.5/4 (G123 W, G124 W skill0; G125 W, G126 D 1800). Elo 1690 [1560,1810]
  after 84 rated (+30, within noise; best rated block so far). Rated >= 2/4 met. Zero illegal NOT met (1, G121 pin).
  No one-move loss NOT met (G124 sacrifice miscount; G126 pawn and exchange). Many rejections recorded in-game.
  Decision: keep T20; add three narrower checks (T21).
- T21 (games 127-132): T20 plus
  (1) SAC CHECK: before any sacrifice, list every enemy recapture (pawns included) and judge each resulting position.
  (2) TIED DEFENDERS: when counting defenders, exclude pinned pieces and pieces shielding a line to a bigger target.
  (3) DESTINATION SCAN for Q/R/K moves: scan all 8 directions and knight jumps from the destination for attackers.
  Observable: zero illegal; no one-move material loss in rated G129-132; rated >= 2/4. Evaluate after G132.
- T21 RESULT (G127-132): full 0/2; rated 4/4 (G129 W, G130 W skill0; G131 W, G132 W 1800). Elo 1760 [1630,1890]
  after 88 rated (+60 vs block 21; first perfect rated block). Rated >= 2/4 met. Zero illegal NOT met (1, pin).
  No one-move loss NOT met (G129 17.Qh8+?? Qxh8). Opponents also blundered more in open positions I created.
  Decision: keep T21; put the two recurring misses at the very start of the per-move block (T22).
- T22 (games 133-138): T21 with step 0 added before OPP:
  (0a) PIN: scan the 8 lines from my king; if the moving piece stands on one with an enemy slider behind it,
       it may only move along that line.
  (0b) CHECKER SAFETY: for any check I give, list every enemy piece that attacks the checking square
       (sliders along all lines) before sending.
  Observable: zero illegal; no one-move material loss in rated G135-138; rated >= 2/4. Evaluate after G138.
- T22 RESULT (G133-138): full 0/2; rated 3/4 (G135 W, G136 W skill0; G137 W, G138 L 1800). Elo 1760 [1630,1890]
  after 92 rated (unchanged). Rated >= 2/4 met. Zero illegal NOT met (1, G137 PATH through own pawn).
  No one-move material loss NOT met (G138 12...dxe4: White's recapture opened the d-file onto my loose Bd6).
  Step 0 (pin, checker safety) worked: no pin errors; checker safety caught 26...Qh2+? in G138.
- T23 (games 139-144): T22 plus
  (1) PATH written for EVERY slider move, retreats included (square-by-square with occupants).
  (2) RECAPTURE LINES: before I start an exchange, for each enemy recapture name the square it leaves and what the
      opened line reaches (G138).
  (3) LOOSE PIECES: list my undefended pieces each move and check every enemy file/diagonal pointing at them.
  Observable: zero illegal; no one-move material loss in rated G141-144; rated >= 2/4. Evaluate after G144.
- T23 RESULT (G139-144): full 0/2; rated 2/4 (G141 W, G142 W skill0; G143 L, G144 L 1800). Elo 1760 [1630,1890]
  after 96 rated (unchanged). Rated >= 2/4 met (only just). Zero illegal NOT met (3 PATH/destination errors).
  No one-move material loss NOT met (six, two of them mates by lines through pieces). The extra checks were not
  applied consistently in long games; the failures were x-ray/battery and discovered lines plus skipped PATH.
- T24 (games 145-150): T23 plus, written before EVERY move: (1) "DEST:" the destination square and its occupant, and
  every path square with its occupant; (2) X-RAY: for each enemy check/attack I list, look behind the attacker for a
  supporting piece on the same line, and treat lines blocked only by an enemy piece as open (discovered attacks).
  Observable: zero illegal; no one-move material loss or mate in rated G147-150; rated >= 2/4. Evaluate after G150.
- T24 RESULT (G145-150): full 0/2; rated 4/4, best block so far. Elo 1790 [1670,1930] after 100 rated (+30).
  Rated >= 2/4 met. Zero illegal NOT met (1, pawn double step through an occupied square). "No one-move loss" not
  strictly met: G150 10...Nc6?? allowed mate in one (unpunished). Decision: keep T24 and add three narrow checks.
- T25 (games 151-156): T24 plus (1) PAWN PATH: for a double step name the passed square; (2) BLOCKER: when blocking
  a check, verify that capturing the blocker with check still leaves my king a square (else block with a defended
  piece or move the king); (3) ENDGAME FORKS: before king/rook moves with an enemy knight on board, list the knight
  squares that attack two of my pieces. Observable: zero illegal; no mate-in-one allowed; rated >= 2/4. Evaluate
  after G156.
- T25 RESULT (G151-156): full 0/2; rated 3/4; Elo 1840 [1720,1980] after 104 rated (+50, highest so far).
  Zero illegal met. No mate-in-one met. Rated >= 2/4 met. Decision: keep T25 and add one check family.
- T26 (games 157-162): T25 plus DEFENDER AUDIT: when I count defenders of a square, drop any defender that is
  pinned (to king or to a file/rank it must block), and when I move a piece, list what it was defending. For enemy
  captures, look at what the capturing piece defends from its landing square. King moves: list enemy knight checks
  onto the new square. Observable: zero illegal; no piece lost to a pinned/overloaded defender; rated >= 2/4.
  Evaluate after G162.
- T26 RESULT (G157-162): full 0/2; rated 2/4 (skill0 2/2, 1800 0/2); Elo 1810 [1690,1940] after 108 rated (-30).
  Rated >= 2/4 met. Zero illegal NOT met (2: rook path through own pawn; king into bishop control). "No piece lost
  to pinned/overloaded defender" NOT met (G157 future pin, G161 moved a blocking pawn, G162 trapped bishop).
  Decision: keep T26 checks, add the vacated-square / mobility checks that all three failures share.
- T27 (games 163-168): T26 plus (1) FROM-SQUARE LINES: for every move, pawns and captures included, trace the four
  lines through the square being vacated; enemy slider on one side + my piece/king on the other = the move opens
  it. (2) TRAP: for each of my minor pieces an enemy pawn push could hit, count safe retreats; <=1 -> fix now.
  (3) LEGALITY: write the slider path squares; for king moves check bishop diagonals, pawn captures, knights and
  king adjacency on the destination. Observable: zero illegal; no material lost to an opened line or trapped
  piece; rated >= 2/4. Evaluate after G168.
- T27 RESULT (G163-168): full 0/2; rated 2.5/4 (skill0 1.5/2: W, D; 1800 1/2: W, L); Elo 1780 [1650,1910] after
  112 rated (-30). Rated >= 2/4 met. Zero illegal NOT met (1: G166 queen path; three others caught by LEGALITY).
  No material lost to an opened line NOT met (G163, G166, G168). Decision: keep T27; extend FROM-SQUARE LINES to
  sliders that can arrive in one move.
- T28 (games 169-174): T27 plus ALIGNMENT: after the candidate move, list every rank/file/diagonal holding two of my
  pieces with only empty squares between (existing and newly created by the move). For each, find any enemy slider of
  the matching type that is on, or can reach in one move, the line beyond the front piece; if one exists, the front
  piece must be adequately defended or expendable, else change the move. Apply the same scan to the opponent's
  blockers (discovered attacks on me). Observable: zero illegal; no material lost to a pin, skewer or discovered
  attack; rated >= 2/4. Evaluate after G174.
- T28 RESULT (G169-174): full 0/2; rated 2/4 (skill0 2/2: W, W; 1800 0/2: L, L); Elo 1740 [1620,1870] after 116
  rated (-40). Rated >= 2/4 met. Zero illegal NOT met (1). No material lost to pin/skewer/discovery NOT met
  (G169 discovered check; also G173 Ng5 into a rook line, G174 boxed king + trapped knight, G170 missed mate).
  Decision: the checklist has grown long and the misses are basic; replace it with four short mandatory steps.
- T29 (games 175-180): before every move, in this order and written briefly: (1) PATH - list each square a slider
  crosses; (2) DEST - for the landing square, trace every enemy rank/file/diagonal to the edge and every enemy knight
  jump; (3) BOX - count my king's flight squares and the safe squares of any piece on the rim; zero -> fix first;
  (4) LEAF - at the end of any forcing line, list all of the opponent's checks and captures before judging it.
  Keep ALIGNMENT/FROM-SQUARE as a quick glance. Observable: zero illegal; no piece lost to an unlisted
  check/capture/trap; rated >= 2/4. Evaluate after G180.
- T29 RESULT (G175-180): full 0/2; rated 2/4 (skill0 1/2: W, L; 1800 1/2: W, L); Elo 1720 [1600,1840] after 120
  rated (-20). Zero illegal MET (first time). Rated >= 2/4 met. No piece lost to an unlisted check/capture/trap NOT
  met (G175 queen trap, G176 king box, G178 loose queen on an opened rank, G180 check-fork on a loose rook).
  Decision: keep PATH (it removed illegals) and the other three steps; add one step aimed at the shared cause.
- T30 (games 181-186): T29 plus (5) LOOSE - after my candidate move, name every piece of mine that is undefended;
  then for each opponent check and each opponent capture found in LEAF, list ALL squares the moving piece attacks
  from its landing square. If a loose piece of mine is among them (fork), or a line just opened onto it, change
  the move. In holding endgames keep the position closed (no pawn breaks that open lines for the bishop pair).
  Observable: zero illegal; no piece lost to a check-fork or a double attack on a loose piece; rated >= 2/4
  (G183-186). Evaluate after G186.
- T30 RESULT (G181-186): full 0/2; rated 1.5/4 (skill0 1/2: W, L; 1800 0.5/2: L, D); Elo 1730 [1610,1860] after 124
  rated (+10). Zero illegal NOT met (2, G181). No piece lost to a check-fork/double attack NOT met (G182 Qd6+ on
  loose Rc7; G184/G185 lines opened by my own move or recapture). Rated >= 2/4 NOT met.
- T31 (games 187-192): T30 plus OPEN-LINE: for every candidate move AND every recapture I am counting on, name the
  file/rank/diagonal the moving unit currently blocks and which two pieces would then face each other; if an enemy
  piece gains a capture or check through it, reject. Against the 1800 setting accept a repetition when the position
  is level or worse. Observable: zero illegal; no material lost to a line opened by my own move/recapture; rated
  >= 2/4 (G189-192). Evaluate after G192.
- T31 RESULT (G187-192): full 0/2; rated 4/4 (skill0 2/2: W, W; 1800 2/2: W, W); Elo 1760 [1640,1890] after 128
  rated (+30). Zero illegal NOT met (1, G187). No material lost to a line opened by my own move: met in G188-192
  (G192 OPEN-LINE rejected 7...Nxd5?? and 24...Bxd5??), NOT met in G187 (27.Qxh4?? gave up the queen's guard of f3:
  Bf3#). Rated >= 2/4 MET (4/4).
- T32 (games 193-198): T31 unchanged plus GUARD: when a piece of mine that guards a square next to my king moves
  (including to capture), list the squares it stops guarding and every enemy check that then becomes possible.
  Observable: zero illegal; no material lost to an opened line or vacated guard; rated >= 2/4 (G195-198).
  Evaluate after G198. G199-200 (full strength) close the run with the same method; no new trial after that.
- T32 RESULT (G193-198): full 0/2; rated 2/4 (skill0 2/2: W, W; 1800 0/2: L, L); Elo 1760 [1640,1890] after 132
  rated (unchanged). Zero illegal NOT met (1, G196). No material lost to an opened line or vacated guard NOT met
  (G193 discovered check, G197 x-ray recapture and king boxed by my own g3, G198 long diagonal). Rated >= 2/4 MET
  (exactly 2/4). Decision: no new trial; G199-200 (full strength) finish the run with the T32 checklist unchanged.
