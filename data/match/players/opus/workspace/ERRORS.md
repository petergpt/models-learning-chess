# Error taxonomy and recurrence (my own post-game assessments; unverified by engine)

Format: game/ply - category - short description

Categories: HANG (left piece en prise), TACTIC (missed opponent tactic: fork/pin/skewer/discovery),
MATE (missed mating threat), READ (board misread / illegal), PLAN (strategic drift), CONV (failed conversion),
OPEN (opening knowledge error), TIME (budget overrun).
- G1/41 - TACTIC(pin) - 21.Qxf7?: counted f2 as defender of Ng3, but f2 was pinned by Bd4 to Kg1 -> ...Qxg3.
- G1/43 - TACTIC(pin) - 22.Qf3??: planned gxf3 recapture; g2 pinned by Rg8 on g-file -> lost queen.
  Lesson: before counting a pawn/piece as a defender or planning a recapture, check it is not pinned to my king.
- G2/30 - READ(path) - 15...Qe7? planned ...Bxd6 vs Nd6+, but Qe7 blocked Bf8 (then submitted illegal Bxd6).
  Lesson: when counting a defender, trace its full path square by square (own pieces block too).
- G2/38 - MATE - 19...Nd8? allowed Qa4+ (only block Nc6) then Qxc6#. King escape squares mis-assessed:
  stepping back along the checking line (Ke8 on a4-e8 diagonal) is illegal.
- G5/77-79 - CONV(line) - 39.Rh8?? Rxh8 40.c8=Q Rxc8: a rook on the 8th rank also attacks my promotion square;
  "my new queen attacks their rook" is meaningless when it's THEIR move. Before promoting, check who controls the square.
- G6/7 - READ(path) - 4...Qd8-b6 submitted: c7 pawn blocks the diagonal (2nd illegal attempt from same cause).
- G6/40 - HANG(removed defender) - 20...Qb6?: Qe6 was the only defender of c4 -> Qxc4. Also walked into Rb1 x-ray:
  Bb2 then pinned in front of Qb6 -> lost a piece.
- G6/54 - HANG(self-block) - 27...Nc5?: knight on c5 blocked Qc7/Rc8 defence of c4 along the c-file -> Rxc4.
- G6 - TIME - ~170k tokens on one game; kept playing a lost position too long.

## Block 1 summary (games 1-6, T0 baseline)
Recurring theme = LINE errors: pins on my defenders (G1 x2), my own pieces blocking my lines (G2, G6 x2 incl. 2 illegal
attempts), abandoning a defended square (G6), enemy rook controlling a promotion square (G5).
- G8/36 - MATE/READ(self-block in calc) - 18...O-O-O?? allowed Ncd6+ Bxd6 Nxd6#: I "planned" Rd8xd6 but my Nd7 blocked
  the d-file, Qa6 blocked by c6, Rh6 by e6. Line audit must also cover the recaptures/defences used in calculation.
- G9/41 - HANG(Q) - 21.Qc8?? "attacks Rh8, Ba8, Nd7" but the Rh8 attacks c8 along the same rank -> Rxc8. 2nd time (G5).
  Root cause: I checked only SOME enemy pieces for attacks on my destination square.
- G9/117 - READ(path) - Rf3-f1 submitted with my own K on f2. Then a careless wrapper "test" (d3d3) = 2nd illegal attempt.
  Rule: NEVER submit anything but an intended, verified move to ./play move.
- G10/60 - TACTIC(fork) - 30...Rxf3?: Ne2-d4+ forked K c6 + Rf3. I checked who attacks f3 now, not the knight's NEXT move.
- G10/74 - MATE - 37...Rh1??: my K on c4 was in a net; Rb2-c2 was mate. I did not list White's checks.
## Block 2 interim (G7-G10): 0/4. Main cause: I do not reliably enumerate the opponent's CHECKS / forks after my move.
- G11/31 - HANG(removed defender) - 16.Be3?: Bc1 was the only defender of b2 -> Bxb2.
- G11/37 - HANG(self-block) - 19.Nb3-d4??: knight on d4 cut Be3's defence of Nc5 -> Bxc5 (lost a knight).
- G11/73 - HANG(destination) - 37.Rd4??: square attacked by Nc6 (I had moved the rook OFF d4 for that reason 3 moves earlier).
- G12/50 - READ - submitted Ke7-e5 (king moved two squares).
- G12/82 - MATE - 41...Kxd5??: listed "Bf3+" as a check but never enumerated escape squares -> Bf3# (Rd6 blocked d6).
## Block 2 summary (G7-G12, T1 line audit): 0/6. Rated: skill0 0/2, 1800 0/2. Every loss came from one-move oversights
(destination attacked, removed/blocked defender, knight forks, mates with the K walking into enemy pieces), several from
winning positions. 3 illegal attempts. The protocol existed but was executed superficially ("... ✓" without checking).
- G13/25 - HANG(destination) - 13.Rfb1??: b1 on the f5-b1 diagonal of Bf5. Skipped the table because "unrated" -> habit leak.
  Rule: the destination check (S) is never optional, in any game.
- G14/34 - TACTIC(discovered/unblocking) - my Qa6 sat on the d3-a6 diagonal behind W's Nc4; Ncd6+ (with tempo)
  unmasked Qd3xa6. Same blind spot as the P1 drill: lines that open when an ENEMY piece moves (discoveries).
- G15/33 - HANG(destination) - 17.Ne5?: e5 attacked by Ng6 AND Re8 (open e-file); I listed only the knight.
- G15/45 - TACTIC(fork) - 23.Rd3?: allowed Ng6xe5 forking Qc4+Rd3 (didn't list knight targets after my move).
- G16/42 - READ(path) - Bf5-d7 submitted through my own e6 pawn (6th path error: G2,G6,G9,G12,P1,G16).
  My own PAWNS are the usual blockers I forget. Rule: read the FEN rank of every intermediate square.
- G17/65 - READ(path) - f2-f4 double push through my own Bf3 (7th path error). Double pawn pushes need the
  intermediate square empty too. Also caught in-game (not played): 26.Rd2? Rc1+ Bd1 Bc2! back-rank mate motifs;
  Rd2 next to an enemy rook on c2 is simply hanging; 53.g6? Rh5+ (unblocking rank 5) would have lost the g-pawn.
- G18/80 - HANG(census) - 40...Qd7?: W's Qc6 attacked c7 AND c4 (down the c-file); I counted only c7. c4 had lost its
  only defender 5 moves earlier (35...Qd7 left the c-file). Fix: every move, census ALL my men attacked by the last-moved
  piece (all 8 lines of a queen), with attacker/defender counts. -> lost pawn, then a 2nd pawn, then mated material.
- G18/49 - READ(shape) - Qf6-d5 submitted: not on a rank/file/diagonal. Fix: before any long move write the delta
  (files, ranks): queen/rook/bishop moves need df=0, dr=0 or |df|=|dr|.
## Block 3 summary (G13-G18, T2 safety table): 3/6 overall, rated 3/4 (skill0 2/2, 1800 1/2) vs block 2 rated 0/4.
Rated-game blunders ~1.0/game (target 0.5 not met), 3 illegal attempts (path x2, shape x1). Big win: endgame technique
(G17 R+2P v R, KR v K). Main costs: token use (G17 ~300K, G18 ~135K) and incomplete threat census.
- G19/25 - HANG(self-block) - 13.Nf3? put my knight on the d1-g4 line that defended g4 -> Bxg4. "B" in the table
  (does the destination block my own lines?) was skipped.
- G19/27 - READ(path) - Bc4-e2 through my own d3 pawn (8th path error; 6 of 8 involve my own pawns).
- G19/33 - TACTIC(discovery) - 17.Bxa6?: Ba7 screened Ra8 from a6; ...Bc5 (tempo on Qb4) unmasked it. Before moving a
  piece onto a line, list enemy pieces BEHIND enemy pieces on that line.
- G20/44 - TACTIC(discovered double check) - my K on the open e-file behind W's Ne6 with Re1 behind: any knight move
  = discovered check. Rule: if my K is on a line with an enemy slider and only an ENEMY piece between, treat every
  move of that piece as check and get the K off the line first (22...Kf7/Kd7 ideas came too late).
- G21/31 - HANG(unblock) - 16.Na3??: my Nb5 was the only piece between Black's Bc6 and my Qa4. Moving it = Bxa4.
  This is the 4th "moving piece was screening an enemy line" loss (G14, P1, G19, G21). Rule (D): before ANY move,
  draw the 8 lines through the FROM-square and ask "which enemy slider sees through it to my piece/K?"
- G21/95 - READ(path) - Be7-b4 through my own c5 pawn (9th path error; 7 involve my own pawns).
- G22/32 - HANG(guard removal) - my Nd3 had ONE defender (Bg6) that W could simply capture (Nxg6). A piece guarded
  only by a capturable piece is effectively loose. Census must count "removable defenders".
- G22/59 - MATE(back rank) - K g8 + f7/g7/h7, both rooks left rank 8, no luft -> Ra8+ and every block fails.
  Rule: before moving my LAST rook off the back rank, play h6/g6 (luft) unless enemy rooks/queen can't reach rank 8.
- G23/45 - HANG(x-ray recapture) - e4 was "defended" by my Q, but the recapture square was attacked by Ra4 along
  rank 4 -> Nxe4 won a pawn. A defender only counts if recapturing doesn't hang it.
- G23/65 - TACTIC(sac miscalc) - 33.Bxh6?? planned Qxh6+ but forgot the enemy KING can capture an undefended
  checking piece next to it. Every sacrificial line: after each of my checks, can the king just take?
- G24/41 - HANG(self-block) - 21...Ke7?? blocked Re8's defence of Be5 (K stepped onto the e-file between them).
## Block 4 summary (G19-24, T3 compact protocol): 1/6, rated 1/4 (skill0 1/2, 1800 0/2). Avg ~44K tokens/game (budget
met) but decisive blunders in 5 games, 2 illegal path errors. Nearly all are LINE errors of the moving piece:
unblocking an enemy line (G21), blocking my own defensive line (G19 Nf3, G24 Ke7), removable/x-rayed defenders
(G22, G23), plus 1 back-rank mate (G22) and 1 sac miscalc (G23).
- G28/56 - TACTIC(check+second target) - 28.Qg6+ also attacked Re8 along g6-f7-e8. When answering a check, list
  EVERY other piece the checking piece attacks (and what my block uncovers) before choosing the reply.
- G28/68 - TACTIC(check+second target) - 34.Qd3+ also hit the undefended Bd5. Same pattern twice in one game.
- G29/15 - HANG(guard removal) - 8.Qa4?? left Bc1 (on the open c-file facing Qc7) with no defender. The FROM-square
  check must list what the moving piece GUARDS, especially pieces on files/diagonals an enemy queen already sees.
## Block 5 summary (G25-30, T4 written FROM/TO line check): 2/6, rated 2/4 (skill0 1/2, 1800 1/2), 0 illegal (first
block ever), ~40K tokens/game. Decisive blunders: G28 (block of check allowed Qxe8+), G29 (Qa4 dropped Bc1 to Qxc1+).
Both = an enemy CAPTURE available right after my move that I never listed.
- G31/33 HANG(to-square line): Nb3?? onto the b-file of Rb6 (b6-b5-b4-b3 empty). I had noted "Rb6 sees b1" one move
  earlier but checked only what Nb3 attacked, not who attacked b3. Rule: for the TO-square, scan its 8 lines + 8 knight
  squares for enemy attackers EVERY time (T5 capture scan applies to full-strength games too).
- G32/44 KING(open centre): Ke7 king in the centre with Re1 + queen checks (Qa3+ on the a3-e7 diagonal) -> e6 fell
  with a Q-for-R+N trade. When my king stands on an open file/diagonal, list every enemy queen CHECK next move.
- G34/22 HANG(defender census): Qxc2?? counted only Qd1 as c2's defender; Ne3 also covered c2 (I had listed it
  4 moves earlier). Before any capture, list EVERY enemy piece that can recapture - knights first.
- G34/18 READ(diagonal): Rfc8 onto the h3-c8 diagonal of Bh3 (opponent missed it).
- G34/52 ILLEGAL(check line): Kd6-e7 stayed on the checking queen's diagonal b4-e7. A king can never retreat along
  the line of a checking slider; squares behind the king on that line are attacked.
- G35/42 HANG(pawn was the defender): c5-c6 pushed the ONLY defender of Bb6 (Rb8 x-ray); before any pawn push,
  ask "what did this pawn defend?" (the from-square rule applies to pawns too).
- G35 ILLEGAL x3: Qd5-b5 through own Bc5; Rc7-f7 through own d7 pawn; f4xg5 with Kf5 pinned on the f-file by Rf2.
  The path check must include MY OWN men, and every pawn/king-adjacent piece must be checked for pins to my king.
- G35/63 STALEMATE TRICK: with R+P v R and the enemy king boxed, a rook "sac" next to my king can be stalemate.
  Before Kg6 (adjacent to f6) ask: if he gives up his rook, does his king still have a move?
- G36/23 HANG(discovered line): ...bxa3 e.p. vacated b4 and opened Bd2's diagonal to my Na5, whose only "defender"
  (Qb5) could not recapture because Nc4 covered a5. When a pawn/piece leaves a square, scan enemy sliders through it.
- G36/57 FORK(knight check): ...Qg7?? allowed Nd4xf5+ hitting K h6, Q g7, R d6. List every enemy knight check.
- Block 6 summary (G31-36): 2.5/6, rated 2.5/4, Elo 1540 [1360,1710] after 24 rated. 5 illegal attempts (3 through
  my OWN pieces, 1 pinned pawn, 1 king on the checking line). ~85K tokens/game. T5 capture-scan was skipped on the
  moves that lost material - adherence, not knowledge, is the bottleneck.
- G37/17 HANG(battery): Rac1 put a rook on a file where Q+R were lined up; count the battery (Q in front, R behind)
  as two attackers. G37/23 READ(board): Kg2 illegal - my own g2 pawn (doubled g-pawns after hxg3).
- G39/26 KING WALK: with enemy R+N+B near my open king, I answered Rc1+ with Kg2 instead of Rf1 (block = rook trade).
  Two checks later every king square was covered -> mate. RULE: when checked near my king and a block trades pieces,
  BLOCK; before any king move, list the enemy's next checks and the king's flight squares after each.
- G40/21 PROCESS: I emitted TWO move commands in one turn (a6 and an unanalysed c8c3); 21...Rxc3?? bxc3 lost a rook
  for a pawn. HARD RULE: exactly one ./play move call per turn; never batch move calls.
- G40/33 FORK(bishop check): ...g5 left the b1-h7 diagonal open to Bd3+ hitting Kh7 and Rc2 at once.
  Before every move list enemy CHECKS (all pieces) and what else each checking move attacks.
- G41/38 COUNT(exchange): a rook "defended" by a knight but attacked by a bishop is still lost for B-for-R. When a
  bishop forks R+N, defending the rook is not enough; move the rook or counter-attack.
- G41/48 HANG(rank line): Bxh4 onto the 4th rank where Rc4 had an open line (d4-g4 empty). Rooks see whole ranks.
- G42/27 BACK RANK: grabbing a3 put my N on the a-file as the only shield vs Ra8+ with no luft. Make luft BEFORE
  rook/knight raids. G42/49 ILLEGAL: Rb2 pinned to Ka3 by Bc1 (moving K next to own R on a diagonal = pin).
  G42/53 COUNT: c3+ "attacks" assumed Rxc3 Kxc3, but Kd2 guarded c3. Count defenders of the ENEMY capturer too.
- G44/25 PROCESS AGAIN: batched c5b4 + b6a6 in one turn (second move unseen). One call per message, always.
- G45/10 PROCESS x3: batched Be3+Qd2. Before sending, count tool calls in the message: must be ONE.
- G46/26 PROCESS x4: batched Rd8+Rcc8 -> Bh3 hit Rc8. Added a 5-second guard to workspace/tools/mv.
- G46/62 HANG(pawn capture): Bc7 next to an enemy pawn on b6 (pawns capture diagonally forward: b6 hits a7/c7).
  In endgames list the capture squares of EVERY enemy pawn before placing a piece. Also illegal f7-f5 through own Bf6.
- G48/10 HANG(mutual attack): Bf5 'attacking' Qc2 on the same diagonal - the queen attacks the bishop too, and it was undefended -> Qxf5. A piece that attacks along a line is attacked back along that line.
- Block 8 (G43-48) summary: rated 2/4 (W L W L), Elo 1470 [1320,1620] after 32 rated. Decisive misses: G46/62 pawn
  capture square, G48/10 mutual line attack; process slips: 3 batched moves (G44-46), 2 illegal (G44, G48).
  Pattern unchanged since block 4: the losing move is almost always a ONE-MOVE oversight on a move I thought was
  "routine" (development, recapture, endgame shuffle) - not a deep tactic.
- G49/27 HANG(mutual line, same FILE): Black's Rb3 attacked c3 AND my Rb5 up the b-file (b4 empty); I read only the
  c3 threat and played Ke2. Rxb3 was available. RULE: after every enemy slider move, trace ALL its lines (rook 4,
  bishop 4, queen 8) square by square to the first piece and name it - "Rb3: b4 . b5 = MY ROOK".
- G50/16 ILLEGAL: Qd5-f5 along rank 5 straight through White's e5 pawn. Path check must list EVERY square (e5!).
- G50/19-21 KING IN THE CENTRE x3 (G32, G44, G50): uncastled K with Ng8 at home; after Rc8+ the K had no squares
  (e5 pawn covers d6; rook on c8 covers d8/e8). RULE: develop the g8 knight and castle before move 12 unless there is
  a concrete reason; when my K is uncastled, count its flight squares after each enemy check before choosing.
- G51/18 ILLEGAL: Qb8-b4 through Black's b7 pawn (2nd queen-path illegal in 2 games). RULE for every slider move of
  2+ squares: write the path as "b7? b6? b5?" and look each square up in the piece list before sending.
- G52/30 COUNT(fork that isn't): "exd3+ forks K and R" ignored that the checking pawn could simply be captured (Rxd3).
  A fork by a pawn/piece only works if the forking unit cannot be taken.
- G52/43 ILLEGAL: Nf3-g4 is not a knight move. Knight squares from f3: d2 d4 e1 e5 g1 g5 h2 h4 - list them.
- G52/87 SKEWER: Ke3 put my K on the same rank as my own Rc3 with the enemy R able to check along it (Rg3+).
  Before a K move in R endings: is my K about to share a line with my own R that an enemy R can reach with check?
- G53/39 BACK RANK (won game thrown away): luft h3 made h2 the K's only square, but Black's Be5 covered h2 along b8-h2.
  My check scan said "Rc1+ -> Kh2" without testing h2. RULE: an escape square counts only after I check every enemy
  line into it (bishop diagonals included). In endgames with my K on the back rank: list K squares + which enemy piece
  covers each; if all covered, the back rank must stay blockable/defended before any other plan.
- G54/16 COUNT(pawn defender): "Bxg4 Bxg4 Qxg4" - h3 pawn also guarded g4. G54/22: noticed in time that gxf5 was
  illegal (g6 pinned by Rg2 to Kg8). G54/27-28: K h7 with the g-file open to Rg2 and Q coming to h5: no escape squares.
- Block 9 (G49-54) summary: rated 1.5/4 (W D L L), Elo 1470 [1320,1610] after 36 rated. T8 piece-by-piece enemy scans
  were long but still missed single lines: pawn defenders (G54), bishop covering the luft square (G53), own-K/own-R
  line (G52), same-file rook (G49). The misses are always "is square X attacked?" questions answered from memory.
- G58/28-29 PIN ON MY K: ...g5 vacated g6 and put Kh7 on the d3-h7 diagonal behind my Re4 (Qd3 then f3 won it; W
  missed). G58/41 X-RAY: R on e7 "defended twice (Q,K)" vs two attackers, but the second W rook stood behind the first
  (Re5+Re1): the K cannot recapture on a square the x-ray rook still sees. Count x-ray attackers behind the first one.
- G59/23 VACATED LINE (queen lost): Re3-g3 unblocked g5-f4-e3-d2; I scanned g3 (destination) but not e3 (origin).
  RULE: the SQUARE SCAN must be run on the ORIGIN square too: which enemy rays pass through it, and what do they hit
  once it is empty? (Same family as G36 e.p. and G49.)
- Block 10 (G55-60) summary: rated 2/4 (W L L W), Elo 1480 [1340,1610] after 40 rated. 0 illegal attempts in rated
  games (1 in full-strength G55). Square scans caught G57 15.g3?? Qh2# and G60 Bxh7+/Ng5 ideas. Remaining misses:
  x-ray battery behind the first attacker (G58/41) and the ORIGIN square's opened line (G59/23).
- G61/21 BACK RANK again (cf. G42, G53): K g1 with f2/g2/h2 and one rook; Q+R could deliver Rc1+ with the blocker
  then left loose. RULE: once queens/rooks are active and my last rook may be drawn away, play h3/g3 BEFORE anything else.

## G64 (skill0, B, won) notes
- 13...Bxe5 (taking a checking N) left my B on e5 en prise to d4 AND let 14.Ba6 hit the undefended Rb7: two hanging pieces at once. Rule: before a capture, list every piece of mine that is attacked AFTER the recapture move too (here: Rb7 on the a6-c8 diagonal).
- Doubled enemy rooks on my 7th with my K on the back rank = forced mate pattern (Rf7+, Rxg7+, Rxh7+, Rag7+, Rh8#). My own Rb8 does not cover f8-h8 when my K stands between. Defence must be prepared BEFORE the second rook arrives: knight covering f7/h7 (Ng5), or K off the back rank in front of pawns.
- Good: knight fork sequence Ng5-h3+ (K forced to h1) then Nf2+ forked K and Bd3.

## G65 (1800, W, won) notes
- Illegal 16.Re5-e3: own e4 pawn on the path. I skipped writing the path squares because the move "looked" simple. Rule stays: write every path square for EVERY slider move, including retreats.
- 19.Bxe6?! Kf6! (not recapturing) hit Be6 with the K while Bf8 hit Rc5 through the now-empty e7: a K move can unblock a bishop line. Before a capture that removes a piece next to the enemy K, check what the K move uncovers.
- Good: known trick 9.Nxe5 dxe5 10.Bxf7+ (d-file x-ray to d8); Bd4 pin of Re5 against Kf6; Rc7+ check-or-lose-the-rook.

## G66 (1800, B, lost) - discovered attack on my queen
- 14...Qxd4 put my Q on the d-file with only White's Bd2 between it and White's Qd1. 15.Bb5+ Kd8 16.Bg5+ moved that
  bishop WITH CHECK and the Qd1 hit my Qd4: every legal reply lost the queen. My scan from d4 stopped at the first
  piece on each ray (Bd2 = "a bishop, not attacking along the file") and never looked behind it.
- Rule (T11): on every ray from my destination square, if the first piece met is an ENEMY piece that does not attack
  along that ray, look BEHIND it. An enemy Q/R behind on a file/rank, or Q/B behind on a diagonal = DISCOVERY THREAT.
  Then ask: can the blocker move with check or capture? If yes, the square is unsafe for anything worth more than
  the blocker's tempo (queen especially).

## Block 11 summary (G61-66)
- Rated 3/4 (G63 W, G64 W, G65 W, G66 L). Losses still come from single tactical blind spots: G64 two pieces hanging
  after a capture (fork + pawn attack), G65 one illegal path (own pawn), G66 discovered attack on the queen.

## G69 (skill0, W, won) - my own piece unblocked an enemy rook onto my queen
- 21.Nc3?? : the Nd5 was the only piece between Black's Ra5 and my Qf5 on the 5th rank. Moving it = Rxf5.
  This is the ORIGIN SCAN failing again: I scanned the knight's destination (c3) carefully and never asked which
  enemy lines pass through d5. Rule: before moving ANY piece, read the 4 lines through its current square; if an
  enemy R/Q/B on one side and my piece of value on the other side -> that piece is a blocker, do not move it.
- Good: Rb6+ forcing Kd7, then Rb7+ skewering K and Rh7 along the 7th; Rc7# found by checking all 8 K squares.

## G70 (skill0, B, lost from +5) - knight fork after a "safe" queen move
- 62...Qf5?? (double attack on Nf1 and h5): f5 was not attacked by anything ON THE BOARD, but the knight could
  jump to e3 WITH CHECK and from e3 it hits f5. I checked "Ne3+ is just a check" one move earlier, then moved my Q
  onto a square that check also attacked. Rule: after choosing a destination for Q/R, list every enemy CHECK
  available next move and ask whether the checking piece also attacks my moved piece (knight forks especially).
- Also: when far ahead (Q+2P vs N+3P), simplify the safest way; a lone queen near an enemy knight is fork bait.
- Endgame lesson: N+2P vs P: my extra f-pawn could not promote past a blockading knight while White's g5 break
  created a passed h-pawn. Earlier, keep the queen and mate instead of chasing pawns.

## G72 (1800, B, lost) - piece put en prise on an open file
- 44...Bc2?? : c2 is on the c-file of White's Rc8 (c7-c3 empty). I was looking at the diagonal target (b3) and
  never ran the destination scan. Simplest possible miss: a straight ray from the destination to an enemy rook.
- 28...Bxh2: the pawn grab let f4 trap the bishop (h2-g3-f4 blocked, g1/g3 covered); cost a piece-for-pawn later.
  Rule: before grabbing with a bishop on the edge, list its retreat squares after the opponent's most natural reply.

## Block 12 summary (G67-72)
- Rated 2/4. Two of the losses were from winning positions (+5, +1). Each loss = one skipped scan on a quiet move.

## G73 (full, W, lost from +6) - a pinned pawn is not a defender
- 19.g3?? relied on f2 protecting g3, but Ba7-g1 pinned f2 to my king. Qxg3+ followed; fxg3 was illegal.
- Rule: when counting defenders, check each defender for a pin (enemy slider behind it on a line to my K/Q).
  Especially f2/f7 pawns on the a7-g1 / a2-g8 diagonals and knights in front of the king.

## G76 (skill0, B, drawn after losing a rook)
- 37...Rxa3?? : a3 was covered by the Nc4 (knight squares from c4: a3,a5,b2,b6,d2,d6,e3,e5). Destination scan skipped
  the knight list. Rule unchanged (T12 DEST line must enumerate enemy KNIGHT squares too, not just rays).
- Illegal f7-f5 attempt: my own king stood on f6 (path/occupancy check on my own pieces).
- Defence that worked: knight on e6 protecting c5+g5+g7, king adjacent to the knight, no pawn moves, only piece
  shuffles; check each king step for knight forks (Nd5+/Nc7+/Ne8+) and rook pins along the 6th rank (Rd6/Rf6).
  Keep the K off the 6th rank when a rook can reach d6 with the N on e6 (Rd6+ fork). Repetition draw resulted.

## G77 (1800, W, lost a winning bind)
- Trapped piece: 16.Ng5 (outpost) later had no retreat: e4 occupied by my own N, f3/h3 covered by ...g4,
  e6/f7/h7 covered. ...f6 attacked it. Rule: for any piece on an advanced square, list its retreat squares
  each time the opponent pushes a pawn toward it (f6/g5-type pawn hits) - keep at least one exit.
- Skewer by line-up: 31.Rxb5?? landed on b5 which is on the same diagonal (a6-f1) as my Qe2 -> ...Ba6
  attacked R with the Q behind. Rule (add to DEST): after my move, do two of my pieces (or piece + K) stand
  on one line with an EMPTY gap that an enemy bishop/rook can reach next move? If so, it is a skewer/pin.
- X-ray through a moving enemy piece: I thought ...Rxb2 hung to Qxb2, but the rook that left b6 opened the
  b-file so Qb8 protected b2; and Rb2 then pinned Qe2 to Kh2. Rule: when an enemy rook/queen sits behind
  another enemy piece on a file, count it as a defender of anything the front piece lands on.
- King box: K h2 with my pawns g3/h4 and Black pawn g4 (covers h3) + Black rook on the 1st rank = no flight
  squares; a rook check on the 2nd rank was mate. Rule: when the enemy has a pawn on g4/b4-type square next
  to my king, keep the back rank covered or keep a defender on the 2nd rank; never let both ranks be cut.

## G78 (1800, B, lost a winning attack in one move)
- Equal QGD-exchange structure; won the bishop pair (Ne4xd2), Qf6-h6, Re6-g6 vs K on g1/h1. After 21.Kh1
  I played 21...Rxg2 22.Kxg2 Qxh3+?? and 23.Kxh3: the queen gave check from a square ADJACENT to the king and
  was protected by nothing. My "forced mate" analysis listed flight squares and interpositions, never the king
  capturing the checker. (Correct was probably keeping the pressure: ...Rg6/...Qh6 setups were already strong.)
- Rule (T13-1): at every check node write "capture by: K? Q? R? B? N? P?" before "flights" and "blocks".

## Block 13 summary (G73-78)
- Full 0/2, skill0 1.5/2, 1800 0/2. All three one-move losses were enumeration gaps, not lack of ideas:
  knight squares, line-up skewer, king-captures-checker. T13 turns these into fixed checklists.

## G79 (full, W) - strategic, not tactical
- 8.h3 + castled king + Black's ...g5-g4 lever opened the h/g-files; with Ba7 pinning f2 and Rg7 pinning g2,
  my Nf3 was defended only by a pinned pawn. Lesson: vs ...g5 storms with my king short, do not open the h-file
  (12.hxg4 opened it); keep pieces that defend g2 without relying on pinned pawns (Nf1-g3/Nh2 setups, Kh1 early).

## G80 (full, B) - opening/king safety
- After 9.Bg5 (pin Ne7 to Qd8) and fxg3 the f-file opened toward f7 while my king was still on e8 and castling
  either side hung Be7/f7. Lesson for the 4.h4 h5 Caro: castle (or prepare ...O-O-O) before trading pieces that
  open f-lines; avoid ...Bxg5 when Nxg5 lands on f7/e6 squares with my king in the centre.
- Illegal: Qc7-e7 slid along the 7th through my own Nd7. DEST must list the PATH squares for sliders (T13 (3)).

## G81 (skill0, W, won)
- 26...f4: a PAWN push forked Be3 and Ng3. My DEST/REPLY scans list piece moves; add "enemy pawn advances:
  does any one-step pawn push attack two of my pieces?" (knight+bishop on adjacent diagonals of a pawn square).
- Illegal again: g2-g4 with my own king on g3. Two-square pawn pushes must check the intermediate square.
- What worked: T13 (2) line-up scan explicitly found K+R on one file (...Rf8+) and K+R on one diagonal
  (...Bh6+) before I played into them. Keep it.

## G82 (skill0, B, lost a won game) - loose pieces on queen lines
- 20...Qb4? offered a queen trade whose ONLY recapture (Ra4xb4) would open the a-file to Ra2xa8. Rule: when I
  plan "trade and recapture", run ORIGIN on the recapturing piece too.
- 34...Kh4?: my Nf3 stood on the f-file of Qf5 with nothing defending it. 38...Kg5?: Ne4 had left, d5 was loose
  on the queen's diagonal. 44...Kh7 (forced) after Qe8+: my Ra4 sat on the e8-a4 diagonal -> Qxa4.
- Rule (T13-REPLY sharpened): list EVERY loose (unprotected) piece of mine and, for the enemy queen, every line
  from its current square AND from each square it can check from. With a queen on the board, loose pieces die.

## G83 (1800, W, draw a pawn down)
- 23.g4?: a two-square pawn push next to an enemy pawn on h4 allows EN PASSANT; after hxg3+ Kxg3 Rxh3+ the
  rook on h3 was guarded by Bd7 along d7-h3 (opened when my g-pawn vanished). Check e.p. + lines it opens.
- Illegal Rd1-h1 through my own Re1: slider path squares again (3rd path error in 4 games). Write the path.

## G84 (1800, B, draw from an exchange down)
- 16.Bb4: my Qd6 and Rf8 stood on one diagonal (b4-c5-d6-e7-f8) -> skewer, exchange lost. LINE-UP scan must
  include Q+R on DIAGONALS (bishop skewers), not only ranks/files. Same pattern as G77 (...Ba6, Q+R on a6-e2).
- 36.Bxg6+: I counted on Kxg6, but g6 was on Qc2's b1-h7 diagonal. Before relying on a recapture, list the
  enemy pieces that attack the recapture square AFTER the exchange (lines opened by the captured piece).
- 39.fxg4: planned ...Nxg4, but g4 was guarded by Qe2 (e2-f3-g4). Same root: queen lines not listed.
- Illegal Qd6-f6 through my own e6 pawn: 5th slider-path error (G76 f7-f5, G80, G81, G83, G84). From the
  middle of G84 I wrote "PATH: squares" before every slider/2-step move and caught 57...b5 passing b6 ok.
- What worked (endgame): defending a pawn twice (Nc7), forcing queens off with a counter-attack on the queen
  (Rf8 vs Qf3/Rf1), checking EN PASSANT (57...b5? axb6 e.p. promotes), knight forks of loose pawns (Nc4),
  choosing the only king square that stops g7 tricks (Kg8; Kf6/Kf8 lost), steering into repetition.

## Block 14 summary (T13, G79-84)
- Full 0/2; rated 2/4 (G81 W, G82 L, G83 D, G84 D). Elo 1510 [1390,1640] after 56 rated (+20, noise).
- One-move material losses still occurred in 3 of 4 rated games (G82 x3, G83 g4 e.p., G84 Bb4/Bxg6/fxg4).
  Common root: ENEMY QUEEN/BISHOP DIAGONALS and lines opened by captures, plus slider paths (illegals).

## G85 (full, W)
- 19.d5?: after ...Bxd5 exd5 my e4 pawn had left e4, so ...e4 forked Bd3+Nf3. The T14 RECAPTURE check must
  include squares VACATED by my recapturing pawn (here e4) - enemy pawn pushes into them can fork.
- 27.Bxe4 Rxe4: the recapturing rook landed on my knight's rank (Nc4 loose) and e3 lost its only guard when the
  knight moved. Loose pieces + "piece that guards a pawn must move" = lost pawn.
- 29...Re1/...Rc1: a knight on b1 between my Ra1 and an enemy rook is pinned along the 1st rank; my rooks
  became passive defenders. Keep the back rank connected (rooks not separated by a minor piece).

## G86 (full, B)
- 20...b6?: vacating b7 left Ra8 on the long diagonal of Qf3, "blocked" only by White's own Ne4 and d5 pawn -
  both could move WITH TEMPO (dxe6, Nxc5). A line blocked only by enemy pieces that can capture/check away is
  effectively open: in ORIGIN/LINE-UP scans, treat enemy blockers that have forcing moves as absent.
- 17.Ng5 + Qd3 on b1-h7: castling short would have walked into Qh7# (h7 guarded by the knight). Before castling,
  list enemy pieces that can reach h7/h2 with check after the king arrives.
- 7...Qa5+/...Qa6 vs the 4.h4 Caro: White declined the trade with c4; my king never castled. Next time
  prefer ...Nd7/...Ne7/...Be7 and early short castling (or the main-line ...c5) over queen sorties.

## Block 15 summary (T14, G85-90)
- Full 0/2 (G85 19.d5? Bxd5! exd5 e4 fork; G86 20...b6? opened the long diagonal for Qf3 via tempo moves).
- Rated 4/4, 0 illegal, 0 one-move losses. Recapture-square and enemy-slider scans found: G89 d5 defended
  only while both knights stayed, Qa7 would hang to a discovered ...Qd7 (rejected); G90 15...Nf4?? would
  have been unprotected once the e-file pin ended (rejected); stalemate check before quiet mating moves (G88).

## G91 (full, W) - opposite castling storm again
- 16.h4 kept the h-file closed but left h4 hanging once Nf3 was traded (22...Qxh4+), and with my king on g1
  the Rg8 pinned g2 so ...Nh3+ forked K+Rf2 unanswerably. Rule: when an enemy rook sits on my king's file,
  list pinned pawns and every knight check square they no longer cover (h3/f3 here).
- Plan error: 12.d4/13.a4 queenside play was slower than ...g5-g4-g3; vs full strength with opposite castling,
  open lines at the king FIRST (c4-c5, b4-b5) or keep the queens/pieces near my king.

## G92 (full, B)
- 15...Nge7?: the Na5 could reach b7, forking Qc5 and Rd8. My ENEMY-SLIDER sweep covers bishops/queens/rooks;
  knights also need a "fork squares" sweep: for each enemy knight, list the squares it reaches next move that
  attack two of my K/Q/R/loose pieces (b7 hit c5 and d8 here) and whether those squares are covered.

## G93 (skill0, W, won)
- Illegal x2: Be3-c1 onto my OWN king (DEST check looked at attackers but not occupancy) and Rd1-d5 through an
  ENEMY knight on d4 (no written PATH line that move). PATH line = every square from origin to destination,
  including the destination's occupant.
- 32.Kc3??: the king was the only guard of Ba3 (Ra8 on the a-file). ORIGIN must include "what did the moving
  piece protect?" - for king moves too.
- Two-rook mate: the rook on the 7th must not stand next to the enemy king (it gets captured once the other
  rook leaves); use R on e7/d7 + check from d8 with the king on g8/h8.

## G95 (1800, W, won despite three slips)
- 22.Bxf4?: Be3 was the only guard of Nc5 (Rc8 on the c-file). Same root as G93 Kc3: ORIGIN must list what the
  moving piece was protecting.
- 23...Rxf2 24.Kxf2 Bxa1: the rook on b2 had been masking Bg7's diagonal to my Ra1. After an ENEMY move,
  re-scan the lines it unmasked (discovered attacks on my pieces), not only what it attacks itself.
- 27.Rxa7? Bd4+: an enemy CHECK that also hits a loose piece (Ra7 on the d4-a7 diagonal). In REPLY, for each
  enemy check list everything else the checking piece attacks from its new square.

## G96 (1800, B, won) - no material slips
- What worked: the LINE-UP scan on my king's long diagonal (13...O-O? 14.Ng5 fxg5?? Qxg7# with Bb2 behind
  Qc3), so I blocked the diagonal with ...Ne5 first; listing everything the enemy queen attacked (20.a4? left
  Qc4 hitting Re6 and Ng4) found the interference 20...Re4! (Qxe4 Nf2+ fork); a pawn fork (21...c6).
- Near-miss: 16...Qe7/Qe8 would have walked into Re2xe7 (my queen on a file held by an enemy rook) - caught.

## Block 16 summary (T15 = T14 replication, G91-96)
- full 0/2; rated 4/4 (G93, G94 skill 0; G95, G96 1800); Elo 1610 [1480,1730] after 64 rated (+50).
- NOT met: 2 illegal (G93) and one-move losses in G93/G95. All four slips were ORIGIN ("what was the moving
  piece guarding?") or UNMASK (line opened by the enemy's last move) or CHECK+HIT (check that also attacks a
  loose piece). These lines exist in my notes but were not written every move.

## G97 (full, W) - walked into a mating net on the h-file
- 23.Nxg4? won the exchange but the recapture hxg4 removed the only blocker of the h-file in front of my Kh1
  (king had no flight squares: Rg1, g2). Material gain is worthless if the recapture opens a line to my king:
  before any capture, ask "which file/diagonal does the RECAPTURE open, and does it lead to my king?"
- 24.g3??: I listed Qh4+, Qh6+, Qf3+, Rh8+ but not Qh8+ (queen to the far end of the file via f6-g7-h8); then
  Kg2 Qh3# because g3 now blocked my queen's rank to h3 and the g4 pawn covered f3/h3. A queen-check list must
  be generated mechanically: for each of the 8 lines from my king, every square on it the queen can reach.
- Pattern: king in the corner + open file + own pawns/rook on the flight squares = mate in 1-2. Make luft
  (free g1 / move a rook) BEFORE the file opens, not after.

## G98 (full, B) - two-move combination through a removed defender
- 14...Qa6?: I checked 15.Nd6+ (answered by ...Bxd6/...Nxd6) but not 15.Bxe7! first: the forced recapture
  Nf5xe7 removed one d6-guard and Be7 the other, so 16.Nd6+ uncovered Qd3 on my Qa6 and the knight then forked
  my rooks from f7. Rule: when my defence of a square relies on pieces that can be captured or deflected
  with tempo (a capture I MUST recapture), re-run the attack after that exchange ("remove-the-guard" scan).
- f7 was undefended once the king castled long: knight forks via f7 hit d8+h8 rooks. Note loose f7/f2 pawns
  as fork squares when rooks sit on d8/h8.

## G100 (skill0, B, draw from +4)
- 18...Nxe1 won the exchange but left a knight on e1 with no retreat; after 19.Nxc5 Qxc5 20.Bxd4 the knight
  and my queen were both loose and 21.Rb4 (rook lift hitting the queen on the 4th rank) cost the knight.
  When I win material with a piece that lands deep in enemy territory, plan its exit BEFORE the recaptures.
- 24.Bc5!: the bishop on d4 was the only piece between Rb4 and my Qe4 (same rank) - any bishop move was a
  discovered attack, and it went to c5 hitting Rf8: fork. LINE-UP must include "my Q/R on a line with an enemy
  R/Q and exactly one ENEMY piece between" (discovered-attack battery), not only my own pieces.
- 59...Qd6?: Qd3 was the only guard of e4 -> Qxe4+. GUARD line missed again.
- 79...g5 illegal: my K h6 and pawn g6 on the 6th rank with the enemy Q on c6 = pinned pawn. Before any pawn
  move, check whether my king stands behind it on a line with an enemy slider.
- Q endgame +1 with my king exposed: the queen had to sit on g7 as a shield; with the opponent's queen free,
  no progress -> repetition. Better: trade queens when ahead (the K+P ending was won: passed a-pawn vs a
  distant king) - offer trades with tempo earlier (e.g. ...Qd5/...Qe5 blocks while the enemy queen is loose).

## G102 (1800, B) - lost from +2 by two loose-piece misses
- 19...Rd7??: my knight had left c6 the move before, so Bb5 now hit d7 along b5-c6-d7. DEST must be recomputed
  from the CURRENT board, including lines my own previous moves opened.
- 26...h6?: correct idea (luft before ...Rxb7, else Rc8#) but Ne5 had just lost its guard (Nd3 took on c5) and
  stood on the same rank as Rc5 -> Rxe5. LOOSE scan must list every piece of mine attacked by every enemy piece,
  not just the piece I am moving.
- R+B vs 2R with the enemy's passed a-pawn: my bishop was the wrong colour and blocked by my own e-pawns, so
  nothing could cover b8. Keep the minor piece able to reach the promotion path before entering such endings.

## Block 17 summary (T16, G97-102)
- full 0/2 (G97 h-file mating net after opening the file myself; G98 Bxe7 + Nd6+ remove-the-guard combo).
- rated 2.5/4 (G99 W, G100 D from +4, G101 W, G102 L from +2); Elo 1640 [1520,1770] after 68 rated (+30).
- 1 illegal (G100, pinned pawn). One-move losses in G100 and G102: every one was an ENEMY piece attacking one of
  my pieces that I did not move (loose knight on a rook's rank, discovered battery, queen's guard duty).

## G103 (full, W) - queen hung to a knight guard
- 24.Qxe6+??: I wrote "e6 undefended" from the pawn structure; the knight on f4 covered e6. The T17 attack map
  was not written for the destination square. For EVERY capture: list all enemy pieces that attack the target
  square, knights first (knight squares are the ones I miss).
- 16.Qxb7 (pawn grab, queen offside) let Black sac the exchange on f3 and then pin Ng2 to Kh1 with ...Qxf3,
  threatening Qxg2# - vs full strength, don't take b7 while my kingside is defended only by pieces that can be
  pinned/removed.

## G104 (full, B)
- 13...Nh6? let Bxh6 and the recapture Rxh6 put my rook on h6, a knight-fork square from f7 (Nxf7+ later
  forked Kd6 + Rh6). Rooks on the 6th next to my king's pawns need the KNIGHT fork-square sweep: f7/g8/e8.
- 19...Kd7 walked into 20.Ne5+ (check + attack on c6 + f7 fork set-up): before a king move, list enemy knight
  checks on the destination and what each check also hits.

## G105 (skill0, W, won)
- 15.axb3?: capturing toward an open file opened it for BOTH sides - my Ra1 hit Qa5, but Black moved first and
  took Ra1. When a capture opens a line between my piece and an enemy piece, the side to move wins the exchange:
  check who moves next.

## G107 (1800, W, lost by mate from +4)
- 25.g3? (instead of gxh3) left a Black pawn on h3: my Kh1 had no g2 square for the rest of the game, so every Q trade lost to a back-rank Ra1+, and Qg2# was a standing threat.
- 33.Bxh3?? (a bishop up, stopping Qg2#): REPLY listed 33...Qf3+ but not CHECK+HIT - Qf3 also hit Rd1, which had lost its only guard when Bg4 left. Rule: after a capture/retreat, list every piece of mine whose guard I just removed; then for each enemy check ask what else that square attacks.
- 38.Qf4??: forced line Qxh2+ Kg4 Qh5#. I wrote "K moves to f3" without checking that f3 lies on the checking diagonal behind g4 (x-ray through the king's own square). Rule: in a king hunt, for each enemy check list every flight square and test it against the checking piece's line extended through the king.
- Pattern: with my king in a net, I evaluated material grabs/defences one move deep. In a net, every candidate must survive ALL enemy checks two plies deep (check, my forced reply, next check).

## G108 (1800, B, lost)
- 10...Bxf3 11.gxf3 handed White the g-file against my castled king (Rg1 + Qh4 + Bg5 later). Grabbing d4 with it was sound on material but cost the game on king safety.
- 13.Bxh7+: the bishop leaving d3 unmasked Qd1 onto my loose Nd4. UNMASK must include "if this enemy piece moves with check/capture, what does the piece behind it hit?"
- 20.Kg2 gxf6?: the KING move itself opened g1-f1-e1 onto my Qe1. I checked UNMASK for pieces but not for the king. 20...Qe4 (escapes and covers h7) was the move.
- 33...Bg5?: blocked a g-file check with a piece that was then pinned to my king and attacked by a pawn (f4). Rule: an interposed piece is pinned; ask what can attack it next move (pawns first).
- Near-miss caught: 17...Bxg5 was illegal (own Nf6 on the diagonal) - PATH check saved an illegal move.

## Block 18 (G103-108, trial T17 = T16 + ATTACK MAP + pawn-pin check)
- Full 0/2; rated 2/4 (G105 W, G106 W skill0; G107 L, G108 L 1800). 0 illegal.
- Process target missed: one-move losses in G105, G107 (two, from +4), G108 (two).
- All four 1800-game errors happened with a king exposed (mine or both) in sharp play; three were lines opened by a moving piece/king (unmask), two were checks that also hit something.

## G109 (full, W, lost)
- 25.Nxd4? Nc4! forked Rb2/Re3/Nd2, and the natural 26.Nxc4 lost to ...Ra1+ (back rank, no luft) once the a5 knight left the a-file. I never played h3 although the a-file had been open since move 17 with rooks on.
- Rule (luft): when the enemy has a rook on an open file that reaches my first rank, make luft (h3/g3) BEFORE starting tactics; add "back-rank check: if every piece guarding rank 1 is captured/deflected, is it mate?" to the king-danger tree.
- Good: 19.Rc1 instead of 19.cxb4?? (opening the c-file would have hung Qc2 to Qc8) - the x-ray check worked.

## G110 (full, B, lost)
- 18...Ke7?: I checked 19.Nxf7 Rxf7 20.Rxf7+ but not 20.Qg5+ (diagonal check through f6 onto e7), after which Qxg6 pinned/attacked Rf7 with Qxf7# threats. The king-danger tree was written for my move but not for the position after the forced recapture.
- 15...g6 (with no dark bishop) gave White g5/f6; h5 + g6 left Qg6/Qh6 entries. In this Caro line the kingside pawn moves (h5, g6) make castling short unsafe; consider ...O-O-O plans or keeping g7.
- Good: saw that 13...Qxb2? and 16...Qxb2? were poisoned (Rfb1 traps the queen), and that 18...Rf5 was impossible (own f7 pawn on the path).

## G112 (skill0, B, LOST by mate from +6)
- 14...Qxb1+?? 15.Qxb1: I counted "free knight with check" without listing the enemy recaptures on b1 (Qb5 on the open b-file). Every capture: list ALL enemy pieces that attack the target square (file/rank/diagonal/knight), not only the obvious defender.
- 25...Bb6? 26.Bxc6: the bishop on b5 had the queen on a4 behind it; once it captured, Qa4 hit c6 (UNMASK of the piece behind the capturing piece).
- 42...Bxe5?? Qxh5#: my king h7 was boxed (Rg8, g7). The only enemy check was Qxh5+, and the only defence was the interposition Bh6 - I moved that bishop away for a pawn. Rule (BOX): when my king has no flight squares, list each enemy check and which of my pieces can capture/interpose; never move the last interposer. Also x-ray: h8 was covered by the queen through h7.

## G113 (1800, W, draw from +4)
- 58.Re4?? Rxg2: GUARD check skipped in a "simple" endgame - the rook on g4 was the only guard of g2. In endgames with few pawns, every pawn I own is a winning asset: list each pawn's guard before every rook move.
- 51-56: I let Black's a-pawn reach a2 while my king and rook were tied up; trading the f/g/h pawns' guards for activity turned +4 into a bind. Rule: when ahead in an endgame, first stop passed pawns with the king, then advance my own.
- 69.Ra1! found in time: Black's ...Rb1 (supported by a2) would have overloaded my first-rank rook.
- Good tactics: 18.dxe6 (opened d-file onto Qd6), 21.Bd4 (discovered Qxg7# threat), 27.Rd8+?? rejected (Bxd8).

## G114 (1800, B, lost by mate)
- 11...Bh7 was illegal: own Ng6 stood on the path. PATH check skipped for a "retreat". 11...Be4 then got trapped by 12.f3 and I gave the bishop for two pawns.
- 62...Kg6?? 63.Qxh5#: h5 was attacked twice (Qd1, Ng3) and defended once (K). I treated it as "a pawn that will fall" and forgot that Qxh5 is a CHECK next to my king, protected by the knight, so the king cannot recapture. My check list after ...Kg6 had Qd3+, Qg4+, Qg1+ but no capture-checks. Rule (CAPTURE-CHECK): list enemy captures that give check FIRST; a king never steps next to a square the enemy can occupy with a protected piece.
- Moves 33-55: Q+N kept my rook tied to the 8th rank (Qg8 mate with Ne7 guarding g8) for 20+ moves. Good: 37...Rg7 (blocked the g-file), 39...Rg8, 42...Nc3 (covered d5/b1); 42...Bf8? rejected by a two-ply tree.

## Block 19 (G109-114, trial T18 = T17 + risk policy + king-danger tree)
- Full 0/2; rated 1.5/4 (G111 W, G112 L skill0; G113 D, G114 L 1800). 1 illegal (G114, path).
- One-move losses: G112 (three), G113 58.Re4??, G114 62...Kg6?? (mate in 1). Two were queen mates on h5 next to a boxed king (G112 42...Bxe5??, G114 62...Kg6??).

## G115 (full, W, lost)
- 19.Nf3? (both knights attacked after ...g5/...exf4): after 19...fxe3 20.Rxe3 the exchange sac 20...Rxf3 21.Rxf3 Ne5 forked Qc4 and Rf3. I had planned "Qe2 defends f3" without a PATH check: c4-d3-e2 was blocked by my own d3 pawn. Rule: after any forced recapture, look where the enemy knight can land with a fork, and path-check my planned defensive queen move (own pawns block).

## G116 (full, B, lost)
- 14...Qc7 illegal: my own Nc6 stood on c6, between c5 and c7. Second PATH failure in three games.
- 26...Nxc4+??: the discovered check was given by my queen on b6, which White's Rd6 already attacked; 27.Rxb6 answered the check by capturing the checker. Rule (CHECKER SAFETY): before any check, direct or discovered, list every enemy piece that attacks the checking piece. A check is not a tempo if the checker can be taken.
- Good: 18...g6 stopped Qxh5 and Qh7#; 24...Ne3! (double attack on both rooks with discovered threats on b6-g1) won material back.

## G117 (skill0, W, won)
- 45.Ra6 illegal: Black's e6 pawn stood between h6 and a6. Third PATH failure in four games (G114 own N, G116 own N, G117 enemy pawn). The PATH check must literally name each square between origin and target.
- 38.Nxf4?: the knight on d3 was the only guard of b2; ...Rxb2+ came with check and then my f4 knight hung to g5. GUARD check before moving a defender, even in a trade.
- Good: caught that 52.dxe6 was illegal (d5 pinned along rank 5 to Kg5) and unpinned first; counted the h-pawn race (h7 then h8=Q could not be stopped from e7); avoided the h7/Kg6 stalemate pattern.

## G118 (skill0, B, won)
- 11...f5 illegal: the double step passes f6, where my own knight stood. Fourth PATH failure in five games (G114, G116, G117, G118), now including a pawn double step. 5...Qb6 (blocked by own c7) was caught before submission.
- Good: 21...Kg8 - saw that Ne5 moving with CHECK (Nxg6+/Nd7+) would unmask Qf4 onto my Qc7; with the king off f8 every knight move lets me take the queen first. 24...Nc2 forked Qe3/Ra1.

## G119 (1800, W, lost)
- 10.Ne2??: I wrote "Nxe2+ Qxe2" without listing what attacks e2 after the recapture: Black's Qe8 on the open e-file. Rule (RECAPTURE SAFETY): a planned recapture square is checked for long-range attackers exactly like a move destination.
- 30.Re2?? Ra8: my queen on a5 had no safe square left (a3, b4 hit by Bd6 and defended only by pawns; b6 by c7; a4 by b5; b5 by Qd7); one rook move trapped it. Rule (QUEEN MOBILITY): when my queen is on the rim or in enemy territory, count its safe retreat squares every move; with one or none, retreat first.
- Good: rejected 10.Qe1? (...Bxf3 gxf3 Nxf3+ forks Qe1) and 10.Be2 (d3 blocks the path) during the pin analysis.

## G120 (1800, B, lost)
- 12...h6??: White's 12.Bc4-d3 vacated c4 and opened Qc2's file onto my undefended Nc6. I checked the new bishop diagonal (h7) but not the line through the square the bishop LEFT. Rule (OPPONENT UNMASK): after every enemy move, list the lines through its origin square.
- 13...Bd7??: the bishop landed on d7, between Qd8 and Bd6, and cut the only guard of d6. Rule (LINE BLOCK): before a move, check whether the destination lies between one of my defenders and the piece it defends.

## Block 20 (G115-120, trial T19 = T18 + capture-checks + king-move audit + path for retreats)
- Full 0/2; rated 2/4 (G117 W, G118 W skill0; G119 L, G120 L 1800). 3 illegal (G116, G117, G118: all PATH, own or enemy piece on the path).
- Rated one-move losses: G117 38.Nxf4? (guard of b2), G119 10.Ne2?? (recapture square on an open file) and 30.Re2?? (queen trapped), G120 12...h6?? (opponent unmask) and 13...Bd7?? (blocked my own guard line).
- The king-specific checks worked (no mates against me; G118 21...Kg8 and G116 18...g6 found). The remaining losses are attack-map maintenance: lines opened or closed by a move (mine or the opponent's), and safety of the recapturing piece.

## G121 (full, W, lost)
- 30.Rg1??: the interposed rook stood on the pin line Rh1-g1-Kf1, and my check list missed 30...Bh3+ (the d7-h3 diagonal had been open since ...g4-g3). The king had to move and the pinned rook fell. 31.Rg2 was then illegal (absolute pin).
- Rule (PIN): before moving any piece, ask whether it is pinned to my king (any enemy slider on the far side). Interposing on a line that the enemy can recheck along with a second piece is not a solution.
- Good: 17.Bxf4 once the path was clear (caught 15.Bxf4 being blocked), 20.Re3 against the ...Nf3 fork, saw 27.fxg3 was illegal.

## G122 (full, B, lost)
- 13...Bd4? allowed 14.Nd6+ and my king never castled; White's rooks then took the d-file and the 7th rank.
- 20...Ne6: I evaluated 21.Rxf7+ Qxf7 Nxf7 Kxf7 as about level and stopped. The next move, 23.Rd7+, attacked the king and the e6 knight it had been guarding. Rule: after a forced exchange sequence, run the REPLIES step again on the final position (checks that hit loose pieces).

## G124 (skill 0, B, won by mate)
- 20...Bxg3??: I calculated only 21.hxg3 Qxg3+ and missed that the f2 pawn could also recapture (21.fxg3 shut the g-file and left the queen's 3rd rank blocked). Result: a piece down for a pawn. Rule (RECAPTURE LIST): for a sacrifice, list every enemy unit that can take back, pawns included, and check the follow-up against each.
- Recovery worked by keeping pieces active and each loose piece guarded: 28...Rf6 broke the Bc4 pin, 29...Qf5 (not Qh6??, which drops d5 to Bxd5 Rxd5 Qxd5), 30...Rxb6 attacked the queen on b3 and made its e3 guard leave. Skill 0 then left its queen hanging.

## G125 (1800, W, won by mate)
- Good catch (LINES, origin square): 28.Qe7+ looked like mate, but moving the queen off f7 would open the 7th rank for ...Rh7xe7. Found 28.Bg5+ Nf6 29.Bxf6# instead. Rule confirmed: when my piece leaves a square, check enemy lines that pass through that square (it may have been blocking a defender).
- The f-file plan worked: f4-f5 locked the e6 outpost, fxg6 and gxf7+ opened the king, and 21.Bxf6 used the pin on the f-file.

## G126 (1800, B, draw)
- 7...Nc6 8.Nxd5: d5 had been defended tactically (Nxd5? Qxb3), but 7.Bb5+ put a piece on the b-file between the queens. Rule: after an enemy interposition or check, re-test every defence that relied on a line through that square.
- 11...Qb5?: the REPLIES step listed Qe5's diagonals but not its rank (e5-d5-c5-b5). Only the c6 pawn turned it into a queen trade. Rule (DESTINATION SCAN): for a queen/rook/king destination, scan all eight directions and knight jumps for enemy attackers.
- 25.Nb6: the Bc7 "defended" b6, but it was shielding Rc8 from Rc1 on the c-file, so Bxb6 lost the rook. Rule (TIED DEFENDERS): when counting defenders, drop any piece that is pinned or is blocking a line to something bigger.
- Good: 32...exd4?? rejected (my pawn move would open g3-c7 onto the pinned Bc7), 38...Bxa4?? rejected (Rc7+ and Rxe7), 43...Bc2?? rejected (Rxb2+ then Rxc2), 44...Bc2! saved the game via opposite bishops.

## Block 21 summary (T20, G121-126)
- Full 0/2; rated 3.5/4 (G123 W, G124 W skill0; G125 W, G126 D 1800). 1 illegal (G121 31.Rg2, pinned rook).
- One-move losses in rated games: G124 20...Bxg3?? (miscalculated sacrifice), G126 8.Nxd5 (line blocked by a check) and 25.Nb6 (tied defender). The 4-line block caught many tactics (G125 28.Qe7+? rejected; G126 three rejections).

## G127 (full, W, lost)
- 12.hxg4 opened the h-file in front of my castled king; together with ...Bg4 pinning Nf3 (later Rf3) to Qd1 and the g-file rooks, the defence collapsed. Rule: against a flank pawn storm, do not open the file toward my own king by capturing; prefer keeping the pawn chain closed (e.g. h3 holds, Nh2) or striking in the centre.
- Good: destination scan found 23.Kh1 illegal (h-file open to Qh4) before I sent it.

## G128 (full, B, lost)
- 19...Ke7??: the king moved onto the 7th rank, where 20.Rxb7+ (a capture that gives check along the rank) won. My Qa6 could not recapture because it was tied to the Qa6/Qd3 standoff: any king move let Qxa6. The REPLIES step listed knight checks only. Rule (KING-MOVE AUDIT, again): for a king destination, scan every rank/file/diagonal through it, including lines that an enemy capture opens or lands on, and check whether my queen is in a mutual-attack standoff (then any tempo loss drops it).

## G129 (skill 0, W, won by mate)
- 17.Qh8+??: my check put the queen on the a1-h8 diagonal where Black's Qf6 could capture it. I had even noted that Qh8 "attacked" Qf6 but did not apply CHECKER SAFETY (can the checking piece be captured?). Rule reminder: for every check I give, list the enemy pieces that attack the checking square, sliders along all lines.
- Good: PATH caught 7.Bxh6 (own Ng5 on the c1-h6 diagonal); back-rank awareness caught 24.Re2?? (Ra1+ mate) and led to 24.h3; 20.Rae1 pinned the queen to the king and recovered the material.

## G131 (1800, W, won by mate)
- Illegal 20.Re8: after 19...Rxd1 the black rook on d1 pinned my Re1 against Kg1 along the 1st rank. I checked only that the e-file was clear (PATH) and that the target gave mate, not whether the moving piece was pinned. Rule (PIN, again): before any move, look along all 8 lines from my king for an enemy slider with exactly one of my pieces between; that piece can only move along that line.
- Good: 11.f4 gained a tempo and closed the e5-h2 diagonal; 13.Bc4 plus 14.f5 used the e-file pin; 16.exf7+ was a double check; 17.g3 parried ...Qxh2+; 38.Qg8 boxed the king without stalemate (pawn move left) before 39.Re6#.

## G132 (1800, B, won by mate)
- 37...Bf1+ was not mate: the bishop landed on f1, between my Rb1 and g1, so the rook no longer covered g1 (LINE BLOCK by my own destination). Harmless here (38...Bh3# followed), but the same error loses games when it removes a defender.
- Good: 17...Bxe4 took an undefended knight after checking its defenders one by one; 20...Qg5 forced a queen trade when far ahead; 35...Rb1 left White a legal pawn move (no stalemate).

## Block 22 summary (T21, G127-132)
- Full 0/2; rated 4/4 (G129 W, G130 W skill0; G131 W, G132 W 1800). 1 illegal (G131 20.Re8, pinned rook).
- One-move loss in rated games: G129 17.Qh8+?? Qxh8 (checker capturable along the diagonal); recovered by the e-file pin 20.Rae1.

## G133 (full, W, lost)
- 12.Qxb7??: pawn grab into a corner with no retreat. After 12...Bb6 the b-file was blocked and every exit (a6, a7, a8, b8, c6, c7, c8) was covered, so ...Ra7 trapped the queen. Rule (QUEEN MOBILITY, again): before a queen capture in enemy territory, list its exit squares after the opponent's best blocking move; if fewer than two stay safe, do not take.

## G134 (full, B, lost)
- My queen sat on a6 for many moves while White's a4 pawn and Nc4 took away a5, b5 and b6; 18.Nc5 then attacked it with no exit. Rule (QUEEN MOBILITY): every few moves, count my queen's safe squares; if fewer than two, relocate it before the opponent can attack it.
- Good: KING-MOVE AUDIT found 16...O-O?? Qh7# (Ng5 covering h7 on the open b1-h7 diagonal) and 16...Nf5 blocked it.

## G137 (1800, W, won 1-0 mate; 1 illegal)
- 26.Qe2 ILLEGAL: I slid the queen g2->e2 along rank 2 through my own f2 pawn. I skipped PATH on a "simple" queen retreat.
  Rule: PATH for every move, queen retreats included: name each square between origin and target and its occupant.
- 37.Bf7? put my bishop on the 7th rank between my Rg7 and the king; the box opened and the king slipped to c7.
  Same LINE BLOCK as G132. Rule: before parking a piece, check it does not sit on a line my rook/queen uses for a box or mate.
- Good: 17.Qe4? f5 traps the queen (QUEEN MOBILITY caught it); 20.Nxe5 (loose Nf3 under Ne5 attack); 23.dxe6? Rxd2 rejected;
  26.Qf1? rejected (Nf3+ then discovered checks on h1/g2); 27.Bf4 (knight pinned to queen) -> 29.Bxc7 won the queen;
  Rxf5? Bxf5 and Rh5 (path f5 blocked) both rejected; 40.Re8+ Bc8 41.Bf5 (pinned interposer) mate.

## G138 (1800, B, lost; 0 illegal)
- 12...dxe4?! 13.dxe4: White's RECAPTURE moved the d3 pawn, opening d1-d6 onto my Bd6 (undefended: Nd7 blocked Qd8),
  while the new e4 pawn hit Bf5. Double attack, -2. I checked my own move's lines but not the lines the recapture opens.
  Rule (RECAPTURE LINES): when I start an exchange, for each enemy recapture name the square that unit leaves and what
  of mine the opened line reaches. Rule (LOOSE PIECES): list my undefended pieces every move; a loose piece on an
  enemy file/diagonal behind a pawn is a target the moment that pawn moves.
- Good: 18...Nxa6? 19.Rxa6 seen; 24...Nxa6? bxa6 seen; 26...e4 with ...Qh2+? rejected (Kxh2, queen unprotected:
  CHECKER SAFETY worked); 44...Rc8 vs the Qe4-a8 diagonal; 49...Kh8? Qe8+ Kh7 Qg8# found.

## Block 23 summary (G133-138)
- Full 0/2 (G133 queen trap, G134 queen trapped). Rated 3/4: G135 W, G136 W (skill 0); G137 W, G138 L (1800).
- Illegal 1 (G137 queen slid through own f2 pawn). One-move material loss: G138 12...dxe4 (recapture opened a line).
- Recurring themes: PATH not written for "obvious" moves; lines opened by the opponent's recapture; own-piece line blocks.

## G139 (full, W, mated)
- 16.Nxg4? moved the e3 knight that was blocking Ba7's a7-g1 diagonal (LINES: the square my piece leaves). I checked
  16...Qxf2+ (Nxf2) and 16...Bxg4 17.Qxg4 (+1), but not Black's CHECKS after 17.Qxg4: 17...Nh3+! gxh3 opened f2 for
  the queen plus bishop, then Qxe1+ and a mating chase. Rule: after my planned recapture, list every enemy check
  (sacrifices included) before counting material; a blocker in front of my king stays put unless I recheck that line.

## G140 (full, B, lost)
- 16...Qc7? I checked the knight fork Nd6+ but not the PAWN FORK 17.d6 (Qc7 and Ne7; d6 protected by e5 and Nc4).
  Rule: in REPLIES, list enemy pawn pushes that attack two pieces, especially a hanging pawn that can advance with tempo.

## G141 (skill 0, W, won 1-0 mate; 1 illegal)
- 23.Bc2?? put the bishop on c2, between my Rc1 and Nc5, removing the knight's only defender: Rxc5 (-3).
  Third own-piece LINE BLOCK (G132, G137). Rule: before any move, ask what each of my rooks/queens currently defends
  along its line, and whether my moving piece lands between them.
- 29.Rc5 ILLEGAL: path c7-c6-c5 had Black's bishop on c6. PATH skipped again (second in two blocks).
- Good: 19.Ng5 / 20.Nh3 avoided the ...e4 pawn fork of Bd3+Nf3; 42.Ne5+ discovered check plus fork; endgame mating
  net with stalemate checks once Black's last pawn was blocked (b3 vs b2).

## G143 (1800, W, mated; 1 illegal)
- 11.Nc4? b5! pawn fork of Ba4 and Nc4 (-2). Same pattern as G140 (REPLIES must list enemy pawn pushes that fork).
- 26.Qc4 ILLEGAL: my own Rd3 stood on e2-c4. Third PATH error in two blocks.
- 29.b4? moved the pawn that guarded c4: Qxc4 (LOOSE PIECES: the defender I move).
- 51.Kf1?? I counted f1 as safe because Black's own Rd3 blocked Bc4-f1. ...Rd1 was discovered double check mate.
  Rule (KING-MOVE AUDIT): a line blocked only by an ENEMY piece is a live line (discovered attack); treat the square as
  attacked. Also: if the moving enemy piece can give check on its own, it is a double check and captures do not help.

## G144 (1800, B, mated; 1 illegal)
- 7...Qc7 ILLEGAL: destination occupied by my own c7 pawn. I named neither the destination occupant nor the path.
- 10...Bxh2: the bishop could never leave h2, because any bishop move opened the h-file and Rxh8+ hit my undefended rook.
- 22...Nf4?? Bxf4 and the recapture Qxf4 loses to Qc1xf4 (c1-f4 diagonal): recapturing piece's safety not checked.
- 31...Ne5?? Rh8# : I listed Rh8+ but assumed Kxh8, missing the queen BEHIND the rook on the h-file (battery).
  Rule (X-RAY): when judging whether a checking/attacking piece can be captured, look BEHIND it along its line for a
  supporting piece of the same side; and treat any line blocked only by an enemy piece as open (G143 discovery mate).

## Block 24 summary (G139-144)
- Full 0/2 (G139 mated after 16.Nxg4?, G140 pawn fork 17.d6). Rated 2/4: G141 W, G142 W (skill 0); G143 L, G144 L (1800).
- Illegal 3 (G141 Rc5 through Bc6, G143 Qc4 through own Rd3, G144 Qc7 onto own pawn): all PATH/destination.
- One-move losses in rated games: G141 23.Bc2 (line block), G143 11.Nc4 (pawn fork), 29.b4 (defender moved),
  51.Kf1 (discovered mate), G144 22...Nf4 (recapture unsafe), 31...Ne5 (battery mate). Worst block since T15.

## G145 (full, W, resigned)
- 18.Qxd3?? put my queen on the d-file facing Black's Qd7 with only Black's Bd6 between; Bh2+ discovered the attack
  with check. The T24 X-RAY rule (a line blocked only by an enemy piece is open) was written one game earlier and
  not applied. Rule, applied to my own destination: before moving my queen/rook/king to a square, scan its lines for
  an enemy slider whose only blocker is an enemy piece that can move with check or tempo.

## G146 (full, B, resigned)
- 18.Nfd2 hit my queen AND vacated f3, opening d1-h5 onto my loose Nh5. I answered the visible threat (queen) and
  skipped OPP's second half (the line through the square the enemy piece LEFT). Loose piece + discovered line.

## G150 (1800, B, won by mate; 1 illegal)
- 30...a5 ILLEGAL: the double step a7-a5 passes a6, where White's knight stood. PATH applies to pawn double steps:
  name the passed square as well as the destination.
- 10...Nc6?? blocked Qb5+ with an UNDEFENDED pinned piece while Bg5 covered d8/e7 and the queen would cover d7:
  11.Qxc6# was mate in one (the engine played 11.Qxb7). 10...Nd7 (defended by the king) was correct. Rule: when
  blocking a check, ask "if the blocker is captured with check, does my king have a square?" before choosing it.
- The 7...Qb6/8...Qxb2/9...Qxa1 raid won a rook but left my king in the centre under Bg5; the rest was defence.
- What worked: listing every enemy check each move found the mating patterns in time (Rc8# at 40; Re7+ Kf8 g7+
  fork at 50; Nd6+ then Rd7# at 55; Rh8# with e6 covering d7/f7 at 57). In R+P v N, listing the knight squares that
  attack both my king and rook before each king move avoided Nd4+/Nd2+ forks.

## Block 25 summary (T24, G145-150)
- full 0/2; rated 4/4 (G147, G148 skill0; G149, G150 1800). Elo 1790 [1670,1930] after 100 rated (+30).
- Illegal 1 (pawn double-step path). Mate-in-one allowed once (G150 10...Nc6??, unpunished).

## G151 (full, W, resigned)
- 20.Qd2?? Rxg3: my Ng3 was "defended" only by f2, and f2 was pinned by Bd4 against Kg1. Rule (DEFENDER PINS):
  when counting defenders of a piece, drop any defender pinned to my king (or whose capture-back walks into a
  discovered check). The g-file rook x-ray behind the knight made the loose piece an immediate target.

## G152 (full, B, resigned)
- 15...Qf5? relied on "if the pinned Ne4 moves, Qxd3 wins the queen", but 16.Nxc5 captured my loose bishop and
  from c5 the knight defended d3. Rule (LANDING-SQUARE DEFENCE): when a pinned or discovered piece moves, check
  what its LANDING square defends; a capture that also covers the exposed piece breaks the pin tactic. The real
  problem was the loose Bc5 (LOOSE PIECES): 15...Bb6 or ...Qd6 first.

## G155 (1800, W, resigned)
- 38.Kd2? Ne4+: I moved the king onto a square a knight could check, and the check also hit c3 and f2.
  KING-MOVE AUDIT must include enemy knight checks onto the new square plus what else that knight hits.
- 49.Bc5? Nxc5+ dxc5 Rxc5!: bxc5 was impossible because it opened the b-file (my Rb3 vs Rb7). A pawn that
  "defends" a square but is tied to blocking a file is not a real defender (same family as G151 DEFENDER PINS).
- Then: passive rook on the 3rd rank defending c3/g3 led to zugzwang. In R endgames activate the rook before
  pawns become targets.

## G156 (1800, B, won by mate)
- 29...Rxa2? let Rxb6+: the rook I moved was the only defender of b6. LOOSE PIECES must be re-listed for the
  squares my moving piece used to guard (a "defender leaves" check), not only for the piece itself.

## Block 26 summary (T25, G151-156)
- full 0/2; rated 3/4 (G153, G154 skill0 W; G155 1800 L; G156 1800 W). Elo 1840 [1720,1980] after 104 rated (+50).
- Zero illegal. No mate-in-one allowed. Losses came from: a defender that was pinned (G151), a capture whose
  landing square re-defended the target (G152), a king step into a knight check (G155), and a defender pinned to
  a file (G155 49.Bc5).

## G157 (full, W, resigned)
- 17.Kg2? put my king on the g-file behind g3, the only defender of Nh4. Black's Ng4 was the piece blocking Rg8;
  ...Nxe3+ removed it WITH CHECK, and after Qxe3 the g3 pawn was pinned, so ...Qxh4. The new DEFENDER AUDIT must
  include FUTURE pins: if an enemy piece blocking a file/diagonal toward my king can leave with tempo, treat the
  defenders on that line as pinned already.

## G158 (full, B, resigned)
- 17...Kf8? left my king on the same a3-f8 diagonal as White's queen, with only White's own c5 pawn between.
  20.c6+ moved that pawn with discovered check AND attacked my knight. X-RAY rule extension: an ENEMY PAWN
  between his queen and my king is a discovered-check battery; pawn pushes that also capture/fork are the
  worst case. Step the king off the diagonal (Kg7/Ke8) rather than along it.

## G159 (skill0, W, won)
- 21.Qxe1? (recapturing a rook) moved my queen off d2, the only defender of Nd3; ...Qxd3. Exactly the T26
  "what was my moving piece defending" check, skipped on a "routine" recapture. Recaptures need the audit too.

## G160 (skill0, B, won) - audit lapse
- 24...Nb4 (forking Qc2/Bd3, opening the c-file) planned 25.Qxc7 Bxc7 but the recapturing Bd6 was the ONLY defender of b4; after Bxc7 the knight hung to Rb5. Exactly the T26 "recapturing piece" rule; I listed it for the first move but not for the forced recapture in my own line. Rule: in every planned exchange line, re-run the defender audit after EACH recapture, not just the first move.
- Two-rook mate vs king on b1/c1 with White pawns f/g/h: cut rank 3 from e3, then Re2 (rank 2 cut from the far side), then Rd1#. The d-file rook is adjacent if the king is on c1 - keep the rank-2 rook far (e2/f2) and give the rank-1 check from distance.

## G161 (1800, W, lost) - FROM-SQUARE LINE + rook PATH
- 17.Ra2-c2 illegal: rank path a2-b2-c2 ran through my own b2 pawn. PATH must be checked for EVERY slider move, including short rook slides along a rank.
- 22.bxa4?? : the b3 pawn was the only thing between Qd5 and my undefended Ra2 (d5-c4-b3-a2). My audit listed what b3 DEFENDED, not what it BLOCKED. New check (FROM-SQUARE LINES): for every move, including pawn moves and captures, trace the 4 lines through the square being vacated; if an enemy slider sits on one side and my piece on the other, the move opens that line.
- 25.Qd2 put the queen on the b4-e1 diagonal in front of my pinned Ne1; ...Bb4 would have won the queen or mated. Avoid placing the queen on the line of a pinned piece's defender.
- Endgame lesson: a passed pawn supported by a rook from behind plus a bishop covering the king's approach square (c1) cannot be stopped by K+N. Fight passed pawns before they are protected (blockade on the square in front with a piece the rook cannot hit).

## G162 (1800, B, lost) - TRAPPED BISHOP + king legality
- 31.g4! : my Bf5 had exactly one "safe" retreat (e4) and that square was trappable by f2-f3 (c2/d3/b1 all covered). I never counted its retreats while it sat on f5 for six moves. New check (TRAP): before each move, for every minor piece of mine that an enemy pawn could hit with one push, count its safe retreat squares; if <=1, relocate it or create a square first.
- 56...Kf6 illegal: the Bd4 diagonal d4-e5-f6 covered f6. 57...Kg5 would also have been illegal (h4 pawn covers g5) - caught. KING LEGALITY: for king moves list bishop diagonals and pawn captures onto the destination, not only knights.
- B vs pawns ending: two separated weak bases (e6 after ...f5, and h5) plus a bishop taking my king's dark squares = zugzwang (61.Kf4). Keep pawns in one compact chain the king can guard from one square; a rook pawn whose queening square matches the bishop's colour (h8 here) decides.

## Block 27 summary (T26, G157-162)
- full 0/2 (G157, G158 lost); rated 2/4 (skill0 2/2: G159, G160; 1800 0/2: G161, G162).
- Illegal: 2 (G161 rook path through own pawn; G162 king into bishop control). Observable "zero illegal" NOT met.
- Material lost to defender/line errors: G157 (future pin), G160 (recapture left b4; unpunished), G161 (b3 pawn was a blocker), G162 (trapped bishop). Observable NOT met.
- Common thread: checks were applied to the destination and to defenders, but not to the squares/lines the move VACATES or to the piece's future mobility.

## G163 (full, W, lost) - pinned defender after an enemy piece vacates a file
- After 14...Nxe3 the g4 knight left the g-file, so Rg8 pinned g2 to Kg1. My recapture 15.Nxe3 ignored that the Nf3's only defender (g2) was now pinned: 15...Qxf3. FROM-SQUARE LINES must also be run on the OPPONENT'S last move (what line did their vacated square open?) - that is the OPP check, applied to pins on my defenders.

## G164 (full, B, lost) - 11...dxc4 handed White the d6 hole
- After 11...dxc4 12.Qxc4 the d-file opened for Rd1 and Nb5-d6+ followed; with my king stuck on f8 (Nd6 covers e8, Bf4/Ng5 nearby) f7 fell. In the Advance Caro-Kann keep the d5 pawn (support it with ...Nf5/...Qb6) rather than releasing it while my king is uncastled; check every enemy knight route to d6 (b5, e4, c4, f5) before opening the centre.

## G166 (skill0, B, draw) - discovered attack by an enemy knight + queen PATH
- 10...Qa5+ illegal: d8-c7-b6-a5, and c7 is my own pawn. Third slider-path illegal in 12 games. Rule: before typing any queen/bishop/rook move, list every square strictly between from and to and name its occupant.
- 25...Rxb4/27...Reb8: my Qc4 stood on the c-file behind White's Nc3 with Rc1 behind it. 28.Na2 opened the file AND attacked Rb4 (knight move = discovered attack). OPP check must ask: for each enemy piece that blocks a line to one of my pieces, where can it move with a threat?
- N+3P vs R: a rook checking along the rank my king needs, with the pawn base (g5) needing the king, is a fortress/repetition. Keep pawns on squares the knight can guard (e6 knight guards f4/g5/g7) before the rook arrives.

## G168 (1800, Black) - ARRIVING PINS
- 19.Bf4: my Rd6 and Qc7 stood on one diagonal with nothing between; a bishop arriving on f4 in one move pinned the
  rook to the queen -> lost the exchange. Two of my pieces on a common open line are a pin/skewer target whenever an
  enemy slider can reach the far end of that line in ONE move, not only when it is already there.
- 47...e5: vacating e6 opened rank 6 between Nb6 and Kf6. The rook was on a7, one move from a6 -> 48.Ra6 won the
  knight. FROM-SQUARE LINES looked only for sliders already on the line; it must include sliders one move away.
- 51...Kd4? (rejected) would have been Rd5#: own pawn c4 and knight d3 blocked the flight squares, the enemy king
  covered c3/e3, the rook landed on d5 defended by e4. Before a king move next to own pieces, list the opponent's
  checks and my flight squares after each.
- Endgame: R+B vs 2N held while c4 + Nd3 (pawn-protected outpost) stayed and nothing was loose. In R+rook-pawn vs N
  my king must already be near the queening corner; a lone knight cannot stop h7-h8 when the rook can check or
  deflect it.

## Block 28 summary (T27, G163-168)
- full 0/2; rated 2.5/4 (skill0 1.5/2, 1800 1/2); Elo 1780 [1650,1910] after 112 rated (-30).
- 1 illegal (G166 queen path through own c7 pawn); three more path errors were caught by the LEGALITY step.
- Material lost to lines: G163 (vacated g4 -> pin on g2), G166 (enemy discovered attack Na2), G168 (arriving Bf4
  pin; ...e5 opened rank 6 for Ra6). Common thread: an enemy slider ARRIVING on a line through two of my pieces.

## G169 (full, White) - BOXED KING ON AN OPEN FILE
- Third Italian loss to ...h6/...g5-g4 after h3. Taking hxg4 and later allowing ...hxg2 opened the g-file; an enemy
  rook behind its own knight on that file then gives discovered checks at will. ALIGNMENT saw it (21...Rdg8) but too
  late: Kf2 was the only flight square and my own pieces on e1/e2/e3/f1/f3 boxed the king (...Qg2 mate).
- Rule: against ...g5 with my king castled short, strike with d4 at once or avoid h3 (no hook); never leave the king
  with zero flight squares when an enemy rook can reach its file.

## G170 (full, Black) - MISSED MATE AT THE END OF A FORCED LINE
- 13...Qxc4?? 14.Qxf7+ Kd8 15.Nxe6+ Kc8 16.Qc7#. I calculated the forced king walk but at the end looked only at
  captures (16.Nxf8) and never listed the opponent's checks. Pattern: knight on e6 covers c7 and d8, queen lands on c7.
- 12...Nb4 also took the knight off d5, where it covered c7/e7/f6. With my king in the centre and f7 hit by Q+N,
  defend or castle before grabbing material.
- Rule (CHECKS AT THE LEAF): at the end of every forcing line, list every check the opponent has before judging it.

## G173 (1800, White) - DESTINATION ON AN OPEN RANK, PATH, KNIGHT FORK
- 16.Ng5+?? Rxg5: I planned Ng5+ then Ne6 (forking Rc5 and Bg7) but never checked that g5 itself was attacked by the
  c5 rook along the empty 5th rank. DEST must trace every enemy rook/queen rank and file to the landing square.
- 21.Rb3 illegal: my own Nc3 stood on the f3-e3-d3-c3-b3 path (fifth slider-path illegal in ~18 games). Write the
  path squares out loud for every rook/queen/bishop move, no exceptions.
- 31.Re4? put my rooks on b7 and e4, both reachable by one knight jump to c5 (Nd7-c5 fork). Before leaving two
  pieces a knight-move apart from one square, check which enemy knight can reach that square.

## G174 (1800, Black) - BOXED KING, KNIGHT ON THE RIM
- After 13...O-O-O the Bf4 covered b8 and c7, so my king on c8 had no flight squares; 21.Bh3+ down the open
  h3-c8 diagonal could only be blocked by a piece that was then taken (lost the exchange). Count the king's flight
  squares after castling and every few moves; with zero flights, close every line into the king first.
- 20...Nh5 had one retreat (f6) that g5 already covered; after g4 and Qh4 it was trapped. TRAP applies to my own
  pieces on the rim, including after the opponent's next pawn push.

## Block 29 summary (T28, G169-174)
- full 0/2; rated 2/4 (skill0 2/2, 1800 0/2); Elo 1740 [1620,1870] after 116 rated (-40 from 1780).
- 1 illegal (G173 Rb3 through own knight). Material lost to lines/forks/traps in G169, G173, G174; G170 missed
  mate at the end of a forcing line. ALIGNMENT caught arriving pins but the failures were simpler: a destination
  attacked along an open rank, a boxed king, a trapped rim knight, and unlisted checks at the leaf.

## G175 (full, White) - QUEEN TRAPPED ON THE RIM
- 14.Qxh5?? grabbed a knight on the rim; after 14...Bg4 every queen square was covered (Qd8 on the h4 diagonal,
  g6 by f7, g5 by h6, h3 by the bishop). BOX/TRAP must be applied to my own queen after any capture on the edge:
  list its safe squares assuming the opponent's best developing move with tempo.

## G176 (full, Black) - KING STEP INTO ZERO FLIGHTS
- 28...Kh7?? left the king with no flight square (Qg5 covered g6/g7/g8 and h8 sat on the h-file), so 29.Rxe6 and
  Rh6 mate could not be stopped. BOX applies to every king move: before stepping, count the destination's flight
  squares against the enemy queen and every rook that can reach the king's file or rank in one move.
- 15...g6 and 19...fxe6 stripped the king's cover; with the enemy queen near, keep f7/g7/h7 pawns intact.

## G178 (skill0, Black) - OPPONENT'S VACATED SQUARE, TRAPPED BISHOP AGAIN
- 21.Nd2 moved the knight off b1 and opened rank 1 between Rh1 and my Qa1; I answered 21...Rxg7?? and lost the
  queen. FROM-SQUARE LINES on the opponent's last move (T27) was skipped: every enemy move, ask what line it opened.
- 13...O-O-O? 14.g4 trapped Bf5: after h4-h5 had taken g6, its only squares were e4 (d3 covered) and g4 (defended
  twice by Be2 and Qd1 behind it). Re-run TRAP on my bishop after every enemy pawn move near it.

## G180 (1800, Black) - COUNTING, OPENING LINES FOR BISHOPS, CHECK-FORK
- 23...Nc3? DEST counted wrongly: c3 was attacked by Rb3 and Qc4 and defended only by Be5, so 24.Rxc3 Bxc3
  25.Qxc3 cost knight and bishop for a rook (-1). Count attackers and defenders of the landing square explicitly.
- R vs 2B with equal pawns held for 18 moves while every pawn stayed on its square (engine shuffled Kg1/Kg2/Kf1).
  45...h5? was an "active" pawn move that let gxh5+ and fxe4+ open the kingside for the bishops. In a holding
  endgame against the bishop pair, keep the position closed and make waiting moves.
- 51...Kxe3?? 52.Bg5+ checked the king AND hit my loose Rh6 from g5. I had listed "Bg5+ -> king moves" in LEAF but
  never asked what else the checking bishop attacked. A check from a square that also hits a loose piece is a fork.

## Block 30 summary (T29, G175-180)
- full 0/2; rated 2/4 (skill0 1/2, 1800 1/2); Elo 1720 [1600,1840] after 120 rated (-20 from 1740).
- ZERO illegal moves for the first time in a block (PATH step works). Pieces still lost to things the steps
  should catch: G175 queen trapped on h5 (BOX on the rim queen), G176 Kh7 into zero flights (BOX), G178 Rxg7??
  after Nd2 opened rank 1 onto my loose queen, G180 Nc3? miscount and Kxe3?? check-fork on a loose rook.
- Common thread: a LOOSE (undefended) piece of mine plus an enemy move that gains a tempo (check, or a newly
  opened line) and hits it at the same time.

## G181 (full, White) - PATH ON QUEEN MOVES, BATTERY ON THE 2ND RANK, OWN VACATED LINE
- Two illegal attempts in one game, both a queen sliding along rank 3 through my own c3 pawn (Qd3-b3, Qb3-d3).
  PATH was skipped because "it is just a queen shuffle". Every queen move needs PATH too.
- 19.bxa5 Rxa5 left my a4 isolated on a file Black could triple on (Ra5, Ra8, Qd7): 3 attackers vs 2 defenders.
  Before opening a file next to my pawn, count how many heavy pieces each side can bring to it.
- 25...Ra2 behind Qc2 on the 2nd rank: Qxf2+ would come with the rook guarding f2, so the king could not recapture.
  A queen-rook battery aimed at f2/g2 must be listed as a threat (LEAF) before it is set up.
- 27.Ne3 moved my knight off c4, which stood between Black's Qe4 and my Qb4 on rank 4 -> Qxb4 (only a trade because
  c3 guarded b4). FROM-SQUARE applies to my own moves: what line does my moving piece stop blocking?

## G182 (full, Black) - "DEFENDED" PAWN WITH UNPLAYABLE RECAPTURES; CHECK THAT ALSO HITS A LOOSE ROOK
- 18...Rg8 left c5 "defended" by Qb6 and Nd7, but both recaptures failed tactically (Nxc5 opened the d-file for
  Qd6+ and Rxc5; Qxc5 lost the queen to Rxc5). Count only recaptures that survive the opponent's reply.
- A knight on d7 pinned in front of my queen and king on the d-file, against Q+R+R, could never move; every plan
  had to keep three defenders on it. Avoid putting the king behind a knight on a file the opponent can triple on.
- 26.Nxe6: the e6 pawn was "defended" by f7, but the knight landed on a square forking two rooks (c7, g7). For a
  capture on a defended pawn, list what the capturing piece attacks from that square (LOOSE/fork step).
- 30.Qd6+ Qe7?? 31.Qxc7: my c7 rook had been loose since 28...Qe8, and the checking queen on d6 attacked it. This is
  the exact T30 LOOSE pattern (check + loose piece) and I did not run the step under time-pressure-like stress.

## G184 (skill0, Black) - OWN PIECE OPENING A FILE, RANK DEFENDER MISSED, PROTECTED ADJACENT CHECK
- 8...Bxh2 grabbed a pawn with a bishop whose exits (g1, g3) were covered; 10...Bg1?? then vacated h2 and my Rh8
  was taken with check down the h-file. I had seen this for Bg3/Bf4 one line earlier and still played Bg1.
  FROM-SQUARE for MY move: any move of a piece that blocks an enemy rook's file opens that file.
- 27...Nxc3?? c3 looked undefended but the Rh3 guarded it along the 3rd rank. DEST must include rank defenders.
- 42...Kd6?? 43.Qe7#: I listed Qd8+, Qf8+, Rd7+, Qh2+ but not the adjacent queen check on e7 guarded by Rf7.
  When the king has <= 2 flights, list EVERY square adjacent to the king that an enemy piece can reach with support.

## G185 (1800, White) - RECAPTURE THAT OPENS A LINE; BACK RANK + DIAGONAL MATING NET
- 19.Qc2?? Rxd4!: my only recapture cxd4 would have moved the c3 pawn that blocked the c-file between Qc6 and my
  Qc2, so Qxc2 followed. Before relying on a pawn recapture, check what file/diagonal that pawn currently blocks.
- With Kh1 and pawns g2/h3, h2 was my only flight; Black's Bc7 aimed at h2 through d6, so my Rd6 became the sole
  block and every rook move allowed Re1+ Rxe1 Qxe1#. Give the king a safe luft square early (not on an enemy
  bishop's diagonal) and avoid a back rank defended by a single rook.

## Block 31 summary (T30, G181-186)
- full 0/2; rated 1.5/4 (skill0 1/2: W, L; 1800 0.5/2: L, D); Elo 1730 [1610,1860] after 124 rated (+10).
- 2 illegal (G181, queen along rank 3 through own c3 - PATH skipped on "quiet" queen moves).
- Material lost: G181 (Ra2+Qc2 battery, Ne3 opened rank 4), G182 (Rg8 left c5, Nxe6 fork, Qd6+ hit loose Rc7),
  G184 (Bg1 opened the h-file, Rh3 rank defender of c3, Qe7# missed), G185 (cxd4 would open the c-file).
- Dominant pattern now: a line OPENED by a move or recapture (mine: G181 Ne3, G184 Bg1, G185 cxd4) - the checklist
  asks about the destination square but I still do not ask "what does the from-square stop blocking?".

## G187 (full, White) - GRABBING THE QUEEN INTO MATE; PATH AGAIN
- 27.Qxh4?? Bf3#. My queen on f2 was the only guard of f3; Rg8 already covered g1 and g2 and Kh1 had no luft. I
  saw "win the queen" and did not list Black's checks after the capture (LEAF) or what my queen stopped guarding
  (FROM-SQUARE). Before ANY capture of a big piece, list every enemy check in the resulting position.
- 10.Be3 illegal (own Nd2 on c1-e3); I even wrote "path d2 is own knight" in the command note and still sent it.
  PATH must be completed BEFORE composing the move command.
- Kingside pawn storm (...h6, ...g5-g4, ...Nh5-f4, ...h5, ...f4-f3) again broke my Italian king; my central
  break d4 came too late. Against ...g5 with the king uncastled, play an early d4 or avoid the Italian.

## G188 (full, Black) - DEFENDER THAT CAN BE DEFLECTED BY CHECK
- 21...Qd6 "defended" e6 twice (Qd6, Ke7) but 22.Qg7+ forced the king off e7; 23.Rxe6+ then took with check and
  hit the queen. When a defender is the king, ask whether a check can drive it away first.
- After 14...g6/15...Kxe7 the king stayed in the centre while the f-file opened; ...f6 (17th move) let exf6+ open
  more lines. With the king uncastled, avoid pawn breaks next to it.

## G190 (skill0, Black) - CHECKING WITH AN UNPROTECTED QUEEN NEXT TO THE KING
- 24...Qc2+?? 25.Kxc2: I wrote "check on b1 (adjacent diag)" and never asked whether the king could simply take.
  Any check delivered on a square adjacent to the enemy king must be protected (DEST: count my defenders too).

## G192 (1800, Black) - WHAT THE OPEN-LINE STEP CAUGHT
- 7.Ng5 (Qc2 + Ng5 on h7): the Nf6 was h7's only guard besides the king, so 7...Nxd5?? and 7...h6?? both lost to
  Nxf6+/Qxh7#. Only 7...g6 (blocking the b1-h7 diagonal) held.
- 24.Bd5: my Be6 was pinned on TWO lines (to Kg8 by Bd5, to the unprotected Qe7 by Re1). 24...Bxd5?? would have
  opened the e-file for Rxe7. 24...Rf6 added a second guard; 25.Rxe6 Rxe6 26.Bxe6+ Qxe6 traded evenly.

## Block 32 summary (T31, G187-192)
- full 0/2; rated 4/4 (skill0 2/2, 1800 2/2); Elo 1760 [1640,1890] after 128 rated (+30 from 1730).
- 1 illegal (G187 10.Be3 through own Nd2; the path was even written in the move note and still sent).
- Material lost: G187 27.Qxh4?? Bf3# (the queen left its guard of f3 next to my king), G188 21...Qd6? (the king as
  defender of e6, deflected by Qg7+), G190 24...Qc2+?? (unprotected check next to the king). G189, G191, G192 clean.

## G193 (full, White) - KING ON AN ENEMY ROOK'S FILE BEHIND AN ENEMY PIECE: DISCOVERED CHECK INTO MATE
- After 19.Nxg7 (+1), Bb7 + Nf4 + Rg8 + Rf8 hit g2/f3. 22.Kf1 put my king on the f-file in front of Rf8; 25.f3 then
  became a pinned pawn (it could not take 25...Rg4).
- 27.Ne3?? left the king with zero flights (e2 covered after any bishop move, f2 on the file, g1/g2 by Rg4) while
  Black's own Bf3 was the only thing between Rf8 and Kf1: 27...Bd1+ (discovered check), 28.Nf5 forced, Rxf5#.
- BOX must include DISCOVERED checks: when an enemy piece sits between an enemy rook/bishop and my king, list every
  square it can go to and my king's flights afterwards. Do not leave the king on a line behind an enemy piece.

## G194 (full, Black) - MY OWN QUEEN BOXED ON THE RIM
- 8...Qa6 (queen-trade offer) stayed on a6 for ten moves while White took its squares one by one: 9.c4 (the diagonal),
  13.a4 (b5), Nc4 (a5, b6), 15.Rxa3 (a4), and my own b7 pawn (b7/c8). 18.Nc5 hit it with no escape.
- BOX applies to my queen too: every move count its safe squares; at 2 or fewer, recentralise it or open a line
  (...b6/...b5) before the opponent can attack it.

## G196 (skill0, Black) - PATH ON A QUEEN MOVE AGAIN
- 5...Qb6 was illegal: my own c7 pawn sits on d8-c7-b6. Third queen-path illegal in 16 games (G181 twice, G196).
  Before ANY queen move, name the squares between from and to (diagonals included) and check them for own pawns.
- Good: 20...Nb4 forked Qd3 + Ra6; the R-vs-B ending was won by checks that drove the king off its pawn guards,
  and stalemate was checked before every move of the K+Q v K mate.

## G197 (1800, White) - X-RAY RECAPTURE; MY OWN KING MATED IN THE ENDGAME
- 30.Rc2? Qxe5!: I counted e5 as attacked once (Qc5) because Ra5's line was blocked by that same queen. When the
  queen captured, the rook behind it supported it along the 5th rank. LEAF must count pieces BEHIND a capturer on
  the same line (batteries/x-rays).
- 48.g3?? took the last flight square from my king on f4 (e3/e4 covered by Re5 after 48...Re5, f3 by Bc6, g4 by
  f5, g5 by Kf6, g3 my own pawn), and 49.Bg2?? allowed ...g5#. BOX applies to MY king in endgames too: an
  advanced king near enemy pawns can be mated by a pawn check. Before every move with my king on ranks 4-6, count
  its flights; if <= 1, create a flight or retreat it first.

## G198 (1800, Black) - DEST MISSED A LONG BISHOP DIAGONAL
- 32...Ra2?? 33.Bxa2: I checked a2 against the d1 rook only; the d5 bishop covered a2 through c4 and b3. DEST must
  trace EVERY enemy diagonal into the landing square, including long ones from the far side of the board.
- 24...Nxb6 (forced recapture) took the knight off d5, which had been blocking Be4's line to b7 (25.Bxb7, -1).
- Good: 20...Qc7! instead of 20...Bxf5?? (Be6 pinned to Qe7 by Re1 would have lost the queen to Rxe7).

## Block 33 summary (T32, G193-198)
- full 0/2; rated 2/4 (skill0 2/2, 1800 0/2); Elo 1760 [1640,1890] after 132 rated (unchanged).
- 1 illegal (G196, queen path through own c7).
- Decisive errors: G193 discovered-check mate (king on an enemy rook's file behind an enemy piece), G194 own queen
  boxed on a6, G197 x-ray recapture missed (Qxe5 backed by Ra5) then my king mated by a pawn (...g5#) after I took
  its last flight, G198 rook dropped onto a long bishop diagonal.

## G199 (full, White) - SAME MOTIF AS G193: Bb7 + KNIGHT ON f4/h4 + ROOK ON THE f-FILE AGAINST f3
- After ...Bxf3 gxf3 the f3 pawn sat on the half-open f-file under Rf8; ...Nh4 (protected by ...g5) attacked it again
  and took g2 from my king. 26.Rd4 put a rook on a knight-fork square: 26...Nxf3 (protected by Rf8) hit d4 and e1.
- Before placing two rooks, check which knight jumps reach both (f3 forks d2/d4/e1/e5/g1/g5/h2/h4).
