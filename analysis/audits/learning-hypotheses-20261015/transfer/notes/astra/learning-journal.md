# Learning journal

## Method and constraints

I choose every move by my own reasoning. No engines, tablebases, move-selection code, outside move advice, or live-game lookups. The referee is the only source of opponent moves and legality checks. Reviews below are my own assessments, not engine evaluations. Measured games and results remain in the automatic records.

Before submitting a move: reconstruct the relevant occupied squares; check the move's path and king safety; consider the opponent's forcing checks and captures, including sacrifices; follow each forcing line through recaptures and check which pieces become undefended.

## Game 1 — White, full-strength, 0–1

Resigned after 32...Kd6 (64 plies). One illegal submission: 17.Rxd5 was impossible because my knight on d2 blocked the rook on d1. The accepted recapture was 17.exd5. This was a board-tracking mistake, not an infrastructure fault.

The decisive observed sequence was 23.Rac1 Bxa3+ 24.Kxa3 Rxc3+ 25.Kb2 Rxe3. I had underestimated the bishop sacrifice, the exposed king, the doubled c-file rooks, and the undefended bishop on e3. Black recovered the sacrificed bishop and won both queenside pawns. I exchanged the knights and one pair of rooks to seek activity, but 29...Re2+ also won g2. At resignation Black had six pawns to my three and threatened the d5 pawn.

Lessons to test:

- Updating a piece's square must also update blocked rook and bishop paths. My intended rook recapture no longer existed after Nd2.
- A pawn defended by the king may still fall to a sacrifice if the recapture exposes a forcing check. Count the whole sequence, including loose pieces elsewhere.
- Before defending one target, examine whether moving a loose piece removes the opponent's combination. In this game, moving the bishop off e3 deserved consideration before 23.Rac1; this is an unverified alternative, not a proven improvement.
- The king route to c2/b2 and the knight retreat cost coordination. Reconsider that plan in similar queenless positions rather than assuming queen exchanges make king safety irrelevant.

No external chess sources or post-game engine analysis used. This one loss establishes a baseline; it does not establish improvement or an Elo estimate.

## Game 2 — Black, full-strength, 0–1

Checkmated by 34.Rh6# (67 plies), confirmed from the referee's compressed PGN. No illegal submissions. Full-strength baseline is now two losses, one with each color.

Opening: Caro-Kann Advance with 4.h4 h5 and exchanged light-squared bishops. After 13...Bb6 14.Neg5 g6, White played 15.Nxe6! and obtained four pawns and a sustained king attack for the knight. I anticipated the sacrifice but underestimated the continuing attack, particularly Qxe6+ and Bh6. Exchanging queens required giving up a rook for a bishop. There is no demonstrated opening improvement here. A more defensive bishop placement on move 13 deserves examination in a future game; it has not been verified.

Final observed pattern: after 31...Kh5 32.Kh3, my king had no safe adjacent square. The knight on g6 temporarily blocked the rook's sixth-rank line. After 33.Nf7, the white knight also protected h6. I played 33...Nxe5 while focusing on the possible g4+ threat, and missed the immediate 34.Rh6# that removing the blocker allowed. This is a direct one-move mate oversight.

Revised decision check for the next games:

1. Before considering plans, enumerate the opponent's immediate checks from the resulting position.
2. For an exposed king, name its available escape squares and their attackers. A blocking piece can be essential even if it appears free to capture a pawn.
3. Recheck the opponent's forcing replies after choosing a move; do not stop after finding an answer to only one threat.
4. Assess sacrifices through the next attacking piece's arrival, not only through the initial material count.

No external sources or engine review used. Reviews are hypotheses plus observed tactical facts, not verified evaluations. Recorded cumulative goal-token observations: 56,051 after game 1 and 126,444 after game 2; these are the active goal's reported counter, not per-game usage or whole-account totals.

## Game 3 — White, skill-0, 1–0

Won by 26.Rxd8# (51 plies), with no illegal submissions. The opponent setting came from the fixed rotation.

After a Scandinavian-style opening, 12.c4 displaced the rook and 13.b4 displaced the queen. The observed fork was 14.c5, attacking the queen on b6 and rook on d6. Black replied 14...Rd7, leaving the queen to 15.cxb6. I subsequently captured an undefended bishop and converted the large advantage.

The final mating pattern was 24.Rc8+ Bd8 25.Qc7 a6 26.Rxd8#. The queen on c7 supported d8 and controlled the seventh-rank escape squares. Capturing with the rook preserved that control; capturing with the queen would have changed it.

This was a successful conversion after major opponent errors, not evidence of improvement against the maximum setting. Keep the same forcing-move and blocker checks in the next game rather than reducing attention because of an opponent label.

## Game 4 — Black, skill-0, 0–1

Won by 64...Qh1# (128 plies), confirmed from the recorded PGN. Two illegal submissions. The skill-0 pair is now two wins; the maximum-strength pair remains two losses. These four games do not establish improvement against the target.

Observed mistakes:

- After 12...Ra4 13.Ng5 Bxa3 14.Nc5 Bxc5 15.Rxa4, I could not safely recapture the rook with the queen: moving the white knight off b3 had opened Qc2–b3–a4. I had failed to update that defender. White obtained a rook for a knight and pawn.
- After 18...hxg5 19.Qxc5, I submitted the illegal 19...dxc5. I had repeatedly treated the black pawn on d4 as defending c5. Black pawns capture toward lower ranks: d4 attacks c3 and e3. The accepted move was 19...g4. The imagined defense of c5 had already distorted my preceding calculations.
- After 32.Qd5, I submitted the illegal ...Qd6. The queen on e6 was pinned to the king on g8 along d5–e6–f7–g8. The accepted 32...Kf7 defended the queen while remaining behind its block. Later ...Rh8 and ...Ke7 supported h3 and released the pin.

The advance ...e3 and the en passant capture 22...gxh3 produced restrictive pawns. I kept two extra pawns for the exchange through a long maneuvering phase. That is a material description, not a verified evaluation. White gave repeated checks on moves 51–54; I allowed the repeating king route rather than claiming a forced win. White broke the repetition with 55.Qh6.

The decisive errors were 55...Qh5 56.Kg2 Qxh6 and 57.Rxb6+ Kxb6: White left its queen and then its last rook capturable. After 58...gxf5, its remaining pawns on c4, d3, and e2 were blocked by my c5, d4, and e3 pawns. I brought the king from b6 through c6, d6, e5, and f4 to g3, preserving White's king moves until 64...Qh1#.

Method revision for the next pair:

1. Before calculating captures, state the relevant pawn's actual attack squares. White pawns increase ranks; Black pawns decrease ranks.
2. Check whether the proposed move removes a blocker on a line to either king. Being out of check does not mean a piece is free to move.
3. Update opened lines after the opponent's move as well as after my own move. Recheck defenders at the position where the capture occurs; do not carry an earlier defender list forward unchanged.
4. Check the opponent's immediate checks and captures after selecting a candidate. Give short, reconstructed forcing lines priority over long speculative continuations; extensive thinking in this game did not prevent basic geometry errors.
5. When the opponent has no mobile pieces except its king, verify at least one legal reply to every quiet move. Use the king to help finish the mate rather than accidentally closing the last escape square.

These revisions are untested working rules. No external sources, engines, or delegated move advice were used. The observed cumulative active-goal token counter after this game was 559,524; it is not per-game usage or a whole-account total.

## Game 5 — White, elo-1800-setting, 1–0

Won by 35.Qh6# (69 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are three wins and two losses; the maximum-strength results remain two losses.

Black lost time with ...Nf6–g8 and repeated queen moves. I developed, defended the exposed e5 pawn with Bf4, used Qe2 to defend Bc4 after ...Qc7, and castled. These are observed defensive purposes, not an engine assessment of the opening.

The main material gains depended on opponent mistakes: 14.Nxc5 d5 left the bishop uncaptured, and 16.Nxc6 Kf8 left another captured piece uncompensated. I withdrew the knights safely. After Nd3 blocked the d-file, the rook on d1 no longer defended Nd4; 19.Be3 supplied a defender against Qb6. This was a useful application of the blocker check from earlier games.

The tactical sequence 22.Nxe6+ opened Be3–d4–c5–b6 against the queen while checking the king on g7. Black chose 22...Qxe6, and 23.dxe6 won the queen. The connected passed pawns then reached e7 and f7. The promotions 28.f8=Q+ Rhxf8 29.exf8=Q+ Rxf8 removed one black rook; the other remained on f8. After 30.Nf4 Rxf4 31.Qxf4, both black rooks were gone.

The final net used 32.Rd6 to control the sixth rank and support the queen. Black's 32...Bd5 blocked the bishop's diagonal to g8, so 33.Bxd5 removed that defender. Then 34.Qf6+ forced 34...Kh7, and 35.Qh6# was supported by Rd6 while Bd5 controlled g8.

Continue checking changed defenders and forcing replies. This clean conversion against the weaker setting does not establish improvement against the maximum opponent. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 779,486 tokens; this is not per-game or whole-account usage.

## Game 6 — Black, elo-1800-setting, 1–0

Lost by resignation after 53.Qxf3 (105 plies), with no illegal submissions. Confirmed from the recorded PGN. The 1800-setting pair is one win and one loss. Overall: three wins and three losses; maximum strength remains 0/2.

I developed normally, castled, and played in the center. White's 24.b5 axb5 and the sequence 30...Nxb4 31.axb4 Rxb4 gave me two extra pawns. I exchanged rooks and reached queen-and-bishop play with opposite-colored bishops. I did not establish a forced win from that advantage.

The first missed defense was 42...f6 43.Bxb7. White's queen on f3 supported the bishop on b7 along f3–e4–d5–c6–b7 after the bishop vacated d5. My queen on c7 could not recapture without being lost to Qxb7. This repeats the opened-line error from game 4; one queen defending a pawn was not sufficient against the supported bishop capture. I was then only one pawn ahead.

The decisive mistake was 51...Kd5 after 50.Qa1+ Ke6 51.Qa6+. White replied 52.Qb7+, lining up Qb7–c6–Kd5–e4–Qf3. My king screened my loose queen, so a legal king escape uncovered the capture. The recorded continuation was 52...Kc4 53.Qxf3. My preceding calculations considered king escape squares and my own mating threat but failed to check what White's next check would expose behind the king.

I resigned with a queen lost for no compensation sufficient to continue: ...b3 could be met by Bxb3+, with the bishop protected along the third rank by Qf3. Resignation preserved the loss in the record.

For the next games, use the short protocol in `move-check.md`. In particular, after choosing a king move, inspect lines that would join the king to the queen or a rook, and consider the opponent's checking squares on those lines. In my reconstruction, 51...Ke7 would not create the same b7–f3 skewer; that is an untested alternative, not a proven winning continuation.

Long speculative analysis did not prevent this one-reply tactical loss. Zero illegal moves is useful but is not evidence that move quality improved. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 1,071,029 tokens; not per-game or whole-account usage.

## Game 7 — White, full-strength, 0–1

Checkmated by 31...Bc3# (62 plies), confirmed from the recorded PGN. No illegal submissions. Maximum-strength results are now three losses; overall results are three wins and four losses. There is no demonstrated improvement against the target.

The early queen trade followed 7.Nxd5 Qxd5 8.e3 Be7 9.Nf3 Qxd1+ 10.Kxd1. My plan for an isolated black d-pawn did not occur because Black recaptured with the queen. Moving the knight off d4 opened the queen exchange and removed my castling rights. I again sent the king toward c2 in a queenless position, but the remaining rook and bishops kept king safety important.

The first material loss followed 19.Kd2 Bd5 20.a3 Ne4+ 21.Ke1 Nxc3 22.Rc1 Rc7 23.bxc3 Bxa3. The b2 pawn could not both recapture the knight and keep a3 defended. After 24.Rc2 Be4 25.Ra2 Rxc3, Black had won both queenside pawns. The intermediate rook pressure did not prevent that loss.

The mating sequence was 27.Kd1 Bd5 28.Ra1 Bb3+ 29.Kd2 Rc8+ 30.Kd3 Bc2+ 31.Kd4 Bc3#. My initial spoken diagnosis blamed 30.Kd3; checking the occupied and attacked squares shows that d3 was the only king escape after 29...Rc8+. After 30...Bc2+, d4 was likewise forced. At the final mate, Rc8 controlled c3/c4/c5, Bc2 controlled d3/e4, Bc3 checked d4 and controlled e5, the e6 pawn controlled d5, and my own e3 pawn occupied the remaining adjacent square.

The earlier error was allowing the net with 28.Ra1. After 28...Bb3+, the alternative 29.Ke1 also fails to 29...Rc1#: moving the rook off c3 uncovers Bb4–c3–d2–e1 as well as giving the rook check. Rxc1 would remove only one check, so the first-rank rook was not an adequate defense. In the played line, ...Rc8+ instead uncovered the bishop against Kd2. This is my own reconstruction, not an engine review.

Lessons to test:

- When a checking move vacates a line, identify every checking piece. A capture of one attacker may leave a second check unresolved.
- Before moving an exposed king, count actual escape squares after the opponent's forcing reply. In this game my own bishop and pawns closed several squares.
- A defended piece can still be lost through an overloaded pawn. Follow the recapture and then recheck the pawn's previous defensive duties.
- Earlier active rook moves such as 19.Rd4 or 28.Ra4 deserve consideration. These are untested candidates, not established improvements or claims that the position could be saved.
- Long speculative lines again contained stale blockers and missed forced checks. Use the current board to verify short forcing replies before extending a variation.

No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 1,177,322 tokens; not per-game or whole-account usage.

## Game 8 — Black, full-strength, 1–0

Checkmated by 33.Qxg8# (65 plies), confirmed from the recorded PGN. No illegal submissions. Maximum strength is now 0 wins, 0 draws, 4 losses; overall results are 3 wins and 5 losses. The second maximum-strength pair did not demonstrate improvement.

I played a Ruy Lopez structure, castled on move 8, and developed both bishops. The central sequence was 13...exd4 14.cxd4 Nb4 15.Bb1 c5 16.d5 c4. My 17...Qa5 supported Nb4 but also put the queen behind it on the d2–c3–b4–a5 diagonal. After 18.Bd2 Nd7 19.Re3 g6 20.Qe1, the queen on e1 supported the bishop's capture on b4 through the square that bishop would vacate. Thus Bxb4 Qxb4 Qxb4 would lose my queen. Counting Qa5 as a defender of Nb4 had missed the final recapture.

I did not find a satisfactory repair. The recorded attempt 20...Nd3 21.Bxd3 Qb6 22.Bc2 lost the knight. White did not choose the queen exchange I had sought. The bishop retreat preserved White's extra piece. This does not prove that every earlier alternative failed; the pin needed attention before Qe1 made it decisive in the played line.

The later exchange sequence was 25...f5 26.Nxe5 Bxe5 27.Bxe5 Rxe5 28.exf5 gxf5. This opened the g-file. White used 29.Rg3+ Kf7 30.Qxh6, and I played 30...Qxd5 to recover the passed pawn. That did not address the mating threat. The finish was 31.Rg7+ Ke8 32.Qh8+ Qg8 33.Qxg8#.

The rook on g7 controlled f7, e7, d7, and c7, stopping at my bishop on b7. My calculation repeatedly treated d7 as a possible king escape while forgetting that whole rank. Once the queen arrived on h8, my own king on e8 also blocked Ra8 from crossing to f8 or g8. Interposing Qg8 did not save the game. In my reconstruction, 30...Rg8 from a8 was legal and would guard g7; it is an untested defensive alternative, not a claim that the game could be saved.

I created `geometry-cards.md` with short reconstructions from these games. The next trial is to verify occupied rays and the last recapture explicitly, instead of extending speculative variations while carrying stale square information. No engine, external source, or delegated advice was used. Observed cumulative active-goal usage after this game: 1,309,508 tokens; not per-game or whole-account usage.

## Game 9 — White, skill-0, 0–1

Checkmated by 56...Qh1# (112 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 3 wins and 6 losses; skill 0 is 2 wins and 1 loss; maximum strength remains 4 losses. The existing review protocol has not prevented recurring tactical errors.

The early mistake was opening the h-file while my king remained exposed. After 14.h3 h5, I recognized that immediately taking the knight on g4 would allow mate on the h-file while Bc5 controlled g1. I played 15.Na4 Bd6, then 16.hxg4 hxg4+ 17.Kg1. That freed g1 temporarily but did not resolve the attack: 17...g3 supplied further mating support. I had underestimated this continuation. I chose 18.Qg4 Qxg4, sacrificing the queen, then moved the rook off f1 and eventually captured the g3 pawn. I did not prove that the queen sacrifice was forced or best.

The passed d-pawn recovered some material: 29.d6, 31.d7, and 32.Bc7 preceded 33.Bxd8 Rxd8, winning a rook for a bishop. Black then captured the pawn with 35...Rxd7. After 36.Rxd7+ Qxd7, I had rook and knight against queen and bishop. The rook and knight later coordinated to recover c4; checking along the sixth and seventh ranks drove the king away and allowed 51.Rxg7. These were local material gains in a position still materially inferior, not an established recovery.

The final checks were 51...Qd4+ 52.Ke1 Bb4+ 53.Ke2 Qd2+ 54.Kf3 Qd5+ 55.Kg3 Be1+ 56.Kh3 Qh1#. I chose h3 while focusing on avoiding Qxf4 with check and the subsequent loss of the knight. I failed to enumerate Qh1+, reached along d5–e4–f3–g2–h1. The queen then controlled the h-file and g2; Be1 controlled g3/h4; f5 controlled g4. There was no capture, interposition, or king escape. Avoiding a material threat was irrelevant once the selected square allowed mate.

The next trial adds a specific king-move check: inspect reachable queen checking squares on the new king's rank, file, and diagonals, including a change of line such as Qd5–h1 followed by an h-file check. Check mate before comparing possible material losses. The early h-file error also reinforces that winning a knight is insufficient justification for removing the king's pawn cover without calculating the next attacking pawn move.

No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after this game: 1,706,838 tokens; not per-game or whole-account usage.

## Game 10 — Black, skill-0, 0–1

Won by 23...Qxg2# (46 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 4 wins and 6 losses; skill 0 is 3 wins and 1 loss; maximum strength remains 0/4. This is one successful attacking sequence, not evidence of improvement against the target.

I developed both knights and bishops, castled on move 5, and challenged the center with ...c5. After the exchanges, the c5 and d5 pawns gave central space. I exchanged Ne4 for Nc3 before advancing its defending d-pawn: 14...Nxc3 15.Rxc3 d4. The rook retreat gave time for ...Qb6 and ...Rad8. The later 18...Bf8 kept c5 defended along f8–e7–d6–c5 while opening the e-file, so 19...Ne5 was defended by Re8 and attacked Rc4.

After 20.Bxc5, my queen on b6 was attacked. In the rejected line 20...Bxc5 21.Rxc5 Qxc5, 22.Qxc5 would capture my queen along the newly opened c-file. Checking that last recapture prevented another version of the opened-defender error. I instead played 20...Nxf3+ 21.gxf3 Qg6+, using the check to gain time to move the attacked queen and reach the opened g-file.

The observed finish was 22.Bg2 Bxf3 23.h4 Qxg2#. Bg2 was pinned to Kg1 by Qg6 and could not capture the bishop on f3. That bishop protected the queen's capture on g2. The queen then controlled f1, h1, and h2; f2 remained occupied by White's pawn; and Kxg2 was illegal because of Bf3. There was no interposition between the adjacent queen and king. The pawn on d4 also blocked White's rook on c4 from reaching g4 to interfere with the g-file attack.

Keep verifying complete recaptures and short forcing replies. The useful behavior here was updating the c-file after the rook moved and checking the actual final king escapes. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 1,820,888 tokens; not per-game or whole-account usage.

## Game 11 — White, elo-1800-setting, 0–1

Resigned after 45...Nxe5 (90 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 4 wins and 7 losses; the 1800 setting is 1 win and 2 losses; maximum strength remains 4 losses. The recurring material oversights show that the existing review method is still unreliable.

I developed, castled on move 8, and placed rooks behind the center. The sequence 17.Nxd4 Bf6 18.e5 blocked the attack on the knight while attacking the bishop. This avoided an immediate loss, but it did not establish an objectively favorable position.

The first major error was 21.Qe4. Both Qf4 and Bb7 attacked e4. I imagined an exchange continuing through captures by both queens and minor pieces, without checking whether Black needed to continue. Black played 21...Bxe4, taking the queen with its bishop. After my recapture, Black could preserve its queen. The played 22.Rxe4 g5 23.Rxf4 gxf4 instead let me exchange a rook for Black's queen, reducing the damage to an exchange deficit. That opponent choice did not make the original queen offer sound. A queen move off the bishop's diagonal, such as Qe3, is an untested alternative rather than a verified improvement.

I continued the ending with bishop and knight against rook and knight. The rook trade 29.Be2 Rxd1+ 30.Bxd1 used the bishop to make the recapture legal. I won a pawn with 33.Bxa6 and activated the king. After 38...f5+, 39.exf6 was a legal en passant answer to check. Black later captured that pawn with 40...Nxf6. I moved the bishop out of the opened d-file with 41.Bb5+ rather than overlooking the rook's attack on d3.

The decisive second error was 45.Ne5 after 44...Ng4. I called the knight protected by Kf4, but 45...Nxe5 left the black knight backed by Rd5. Kxe5 would move into rook check. The king could not recapture, and I lost a knight outright. I resigned with a bishop against rook and knight, with four pawns against three. The resignation records the loss; I did not prove a forced mate.

For the next game, the immediate test is narrower: first test the cheapest enemy capture of the valuable piece, allowing the opponent to stop the exchange; then verify the legality of the intended recapture. In particular, a king cannot recapture an attacker that is protected by another enemy piece. Long variations in this game repeatedly obscured these short tests. The hypothetical 45.Bc4 would keep the bishop defended and avoid this specific knight loss, but has not been tested as a saving line.

No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 2,076,877 tokens; not per-game or whole-account usage.

## Game 12 — Black, elo-1800-setting, 1–0

Resigned after 58.Rxc2 (115 plies), confirmed from the recorded PGN. One illegal submission. Overall results are 4 wins and 8 losses; the 1800 setting is 1 win and 3 losses; maximum strength remains 0 wins, 0 draws, 4 losses. There is still no demonstrated improvement against the target.

I developed, castled, and used ...e5 to exchange central pawns. I noticed at several points that Bd6 blocked my queen from defending d5, and moved the bishop or supplied a rook defender. The sequence 30...Nf3+ 31.Nxf3 Qxf3 exchanged knights and briefly put pressure on f2. These were specific local checks; they did not make the later audit reliable.

White's queen moved away from b3 with 33.Qd3. After 33...axb4 34.axb4 Rxb4, I had an extra pawn. I exchanged queens and maintained d5 with ...Rd8. The central exchange 40...d4 41.Rc5 dxe3 42.Rxe3+ removed White's e-pawn and my d-pawn, leaving my extra b-pawn as a passer. I activated the king and advanced that pawn, but did not establish a forced win.

After 48.Ra5, I submitted ...b4 while Kc5 remained behind the pawn on the fifth rank. The a5–b5–c5 line made the pawn absolutely pinned, so the move was illegal. I corrected it with ...Kb6, then played ...b4 after Ra8. This was a reasoning error and the game's sole rejected submission.

The pawn reached b3, but the sequence 52...Rc2 53.Ne5 Bxe5 54.Rxb3+ Kc5 55.Rxe5+ removed both minor pieces and returned material to equality. Ne5 attacked Rd7, and the checking pawn capture let White take b3 before recapturing the bishop. This was the loss of my extra pawn, not an established unavoidable draw.

The decisive error was 56...Rf5 after 55...Rd5 56.Re7. I focused on defending f7 and missed 57.Rc7+, skewering Kc5 against Rc2 along the c-file. My king also blocked Rc2 from capturing the checking rook or interposing above it. After 57...Kd6 58.Rxc2, White had two rooks against one with three pawns each and no concrete compensation for me. I resigned; no forced-mate claim is made.

The new geometry card enumerates the four rook checks after the actual final candidate: Rc7+, Re5+, Rc3+, and Rb5+. I considered other checks but omitted the decisive one. This repeats game 6's skewer error despite already having a reminder about king/major-piece alignment. The narrower trial is to enumerate each enemy rook's reachable checking squares before the material audit. The alternative 56...Rcd2 removes this particular skewer while allowing pressure on f7; it is an untested candidate, not a proved saving line.

No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 2,355,400 tokens; not per-game or whole-account usage.

## Game 13 — White, full-strength, 0–1

Checkmated by 22...Qh1# (44 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 4 wins and 9 losses; maximum strength is 0 wins, 0 draws, 5 losses. The target performance has not improved in the measured results.

I played a quiet Ruy Lopez with 4.d3 and castled on move 5. After ...Nd4 I exchanged that knight, then developed with c3, Nd2, Nc4, and Bc2. Black's ...d5 drove the knight back. The later ...Bg4 pin and ...a5–a4 expansion left Black active while I spent further moves reorganizing. No claim of opening equality is made.

The key weakening was 15.h3 Bh5 16.g4 Nxg4 17.hxg4 Bxg4. I had explicitly considered the knight sacrifice, but accepted the removal of my king's two pawns without establishing a sound defense. This repeats the broader king-cover error from game 9. The nominal extra knight was insufficient evidence of a favorable position.

The played defense was 18.Kg2 f5 19.Qe1 fxe4 20.Nd2 Bf3+. Qe1 removed the knight's relative pin to the queen, and Nd2 saved it from the pawn attack, but this permitted the bishop to enter f3 with check. The bishop was protected by e4 and the rook on f8, so Kxf3 was not legal.

I chose 21.Kh2, after which 21...Qh4+ forced 22.Kg1 and 22...Qh1# followed. Bf3 protected h1 along f3–g2–h1. My Rf1 and f2 pawn occupied escape squares; Kg1 blocked the rook from reaching h1. I had focused on queen checks leading to possible repeated king moves while missing the queen's supported move to h1. The mistake was the earlier escape choice, not a failure to find a legal alternative to the forced 22.Kg1.

The new card records 21.Nxf3 as a candidate to examine: after ...exf3+, 22.Kg3 is legal in my reconstruction and the bishop no longer guards h1. I have not proved that this saves the game. Likewise, 16.Qe2 is an untested way to retain the kingside pawn cover instead of playing g4. The next practical trial is to retain king shelter unless the attacking continuation is concretely justified, and to inspect captures of a checking bishop before accepting a king retreat that leaves its mating support intact.

No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 2,476,028 tokens; not per-game or whole-account usage.

## Game 14 — Black, full-strength, 1–0

Resigned after 23.Qxe7 (45 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 4 wins and 10 losses; maximum strength is 0 wins, 0 draws, 6 losses. There is no measured improvement against the target.

I played a French structure, castled, and exchanged the central knights and one pair of bishops. White castled queenside and advanced h4–h5–h6. My 15...g6 kept the h-file closed but left the advanced pawn controlling g7. After 16.Nxd5 I declined the capture: the illustrative 16...exd5 17.e6 fxe6? 18.Qg7# shows one concrete danger, although it does not prove that every defense after ...exd5 loses. I instead played 16...Re8 17.Rh3 Qd8.

The queen retreat was meant to support the knight and permit ...Nxf6 followed by exf6 and ...Qxd4. After 18.Nf6+, I found that White need not recapture with the pawn. The alternative 18...Nxf6 19.Qxd8 Rxd8 20.Rxd8+ Ne8 21.Rxe8# exploits the opened d-file, the vacated eighth rank, Bc8 blocking Ra8, and h6 controlling g7. I rejected the capture, but discovering this only after ...Qd8 exposed a defect in the planned exchange. The opponent's choice of capture order was again decisive.

The played defense was 18...Kf8 19.Nxh7+ Kg8 20.Nf6+ Kf8 21.Qb4+ Re7. The knight checks took h7, leaving White's h-pawn free to advance. After 22.h7 Kg7, my queen could cover h8 along the now-cleared eighth rank, but 23.Qxe7 removed the rook. Recapturing with 23...Qxe7 would allow 24.h8=Q#: Rh3 protects the promoted queen, and the knight, e-pawn, queen, and my own f7/g6 pawns close the king's escape squares. The alternative ...Qh8 is legal but leaves the rook lost. I resigned a rook and two pawns down without concrete compensation; this is not a claim that every legal continuation immediately mates.

This game adds two practical checks. First, inspect capture order and the rook check that can follow a queen exchange. Second, assess an enemy pawn near the king even when it currently blocks its own rook: removing the pawn ahead of it can create a promotion threat. My long analysis also carried a cleared e6 square from one hypothetical line into another in which Black's e6 pawn had never moved; the imagined e5–e6 advance in that second position was impossible. Rebuilding the current board must precede reuse of a variation.

The earlier candidate 15...gxh6 16.Rxh6 would remove the advanced pawn while opening lines. It has not been tested and is not claimed to save the game. The expanding checklist has not yet produced reliable tactical accuracy. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 2,762,593 tokens; not per-game or whole-account usage.

## Game 15 — White, skill-0, 1–0

Won by 33.Qh7# (65 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 5 wins and 10 losses; skill 0 is 4 wins and 1 loss; maximum strength remains 6 losses. This win does not establish improvement against the target.

I used a d4/c4 center, developed both knights and Bd3, and castled on move 7 while retaining the f2/g2/h2 pawn cover. After 9.e4 Bxc3, the recapture 10.bxc3 kept Qc2 behind Bd3. Thus 10...dxe4 11.Bxe4 Nxe4 12.Qxe4 completed an equal exchange; Qxc3 would not have supplied that final recapture on e4. The doubled c-pawns were a cost of retaining this tactical defense.

The sequence 13.Bd2, 15.c5, and 16.c4 defended c3, then cleared the bishop's diagonal with an attack on Qa5. Bf4 gained another tempo against Qc7, and Bd6 occupied a square protected by c5. Rab1–b6 activated the rook on another square protected by that pawn and prevented ...b6 from undermining it. After 21.d5 Qf7 22.dxc6 bxc6 23.Qxc6, I was a pawn ahead. This is a material count, not an engine evaluation of the preceding position.

The decisive opponent mistake was 23...Qb7. I captured with the cheaper piece, 24.Rxb7, having checked ...Bxb7 25.Qxb7 through the final recapture. Black instead played ...a4 and left the queen unrecovered. I moved the attacked rook with 25.Re7, then used 25...Bb7 26.Qxb7 Rxe7 27.Bxe7 to take the bishop and exchange rooks. The subsequent ...Rc8 allowed Qxc8, and Qxf8+ removed Black's last piece. These large opponent concessions, rather than the opening alone, produced the winning material advantage.

After 30.Re4 f5, moving the knight with check answered the attack on the rook without sacrificing it. The vacated f6 square let Be7 protect 31.Ng5+. The played ...Kh6 32.Qh8+ Kg6 33.Qh7# used Ng5 to protect the mating queen and cover f7, Be7 to cover f6 and protect g5, and Black's pawns to block f5/g7/h5. This finish was checked square by square and confirmed by the referee. The alternate line against ...Kg6 is recorded separately as my unplayed mental reconstruction.

Useful local checks succeeded here: preserving the queen's recapture ray, choosing the cheaper attacker against an exposed queen, and verifying the mating square's support. Repeated long analysis remains costly and is not itself evidence of learning. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 2,973,867 tokens; not per-game or whole-account usage.

## Game 16 — Black, skill-0, 0–1

Won by 32...Re2# (64 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 6 wins and 10 losses; skill 0 is 5 wins and 1 loss; maximum strength remains 6 losses. The paired skill-0 wins relied on large opponent mistakes and do not establish progress against the target.

Against 1.c4 I used ...e5, ...Nf6, and ...d5. After Bg5 pinned the knight to the queen, ...d4 attacked Nc3 and ...Be7 removed the pin. I answered Qa4+ by developing ...Nc6, recaptured Nxf6+ with the bishop, and castled on move 8. ...Bd7 reinforced c6 against the queen and a future Bg2. The later ...a5 supported ...Nb4, which attacked Qc2; ...c5 then strengthened d4 before the knight retreated from a3.

The central sequence 15...Bf5 16.Rb1 e4 17.dxe4 Bxe4 opened the bishop's attack on both Qc2 and Nf3. White's 18.Rc1 defended the queen but still allowed the favorable capture 18...Bxc2. A rook recapture would not restore material equality. White instead played h3, so I preserved the bishop with ...Be4 before exchanging it for Nf3.

After 21.exf3, the departure of the e2 pawn made ...Ne5–d3 available. The knight attacked Rc1 and f2. White's Rf1 left the c1 rook exposed, and ...Nxc1 took it. White again declined to recapture, allowing ...Nb3. I checked that 25...Kxf7 legally captured the unsupported checking bishop; White's own pawns blocked its rook's f-file. After 26.Bxa5 attacked my queen, ...Nxa5 removed the last bishop and preserved the queen.

The finish coordinated the remaining pieces: ...Qe7–e2+ forced Kb1, and ...d3 opened the bishop's diagonal to b2. White interposed Rc3 against the queen-mate threat. After ...Bxc3 bxc3, ...Qe1+ forced the king onto the second rank and ...Re2# finished. Qe1 covered the first rank, Re2 the second, Na5 covered b3, and White's own a3 pawn blocked the last escape. Capturing that bishop on a5 had therefore also placed the knight on a useful mating square.

The successful local checks were the bishop's capture of a rook-defended queen, updating d3's safety after exf3, verifying the king recapture on f7, and counting the final escape squares. I still spent excessive analysis on remote alternatives after obtaining a decisive material advantage; the win is not evidence that this amount of analysis is necessary or that the earlier recurring errors are resolved. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 3,159,722 tokens; not per-game or whole-account usage.

## Game 17 — White, elo-1800-setting, 1–0

Won by 55.Qg6# (109 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 7 wins and 10 losses; the 1800 setting is 2 wins and 3 losses; maximum strength remains 6 losses. Three consecutive wins against weaker settings do not establish improvement against the target.

I developed with d4/c4, brought the c1 bishop outside the pawn chain before e3, and castled on move 8. After ...cxd4 I recaptured with the e-pawn. Be3 answered ...Nh5 without opening my king's pawn cover. Once ...Nb6 vacated d7, Ne5 no longer faced an immediate exchange by that knight. The later Nxc6 bxc6 changed Black's pawn structure, and Na4 attacked both Nb6 and Bd6. The played 19...Nc4 20.Bxc4 dxc4 21.Rxc4 gave me a pawn. This is a count of the observed exchanges, not a claim that the opening forced an advantage.

After further maneuvering and a bishop exchange, 29.Nd3 prepared Ne5 and opened the c-file. Black answered 30.Ne5 with ...Rxb4. I declined 31.Rxb4 Nxb4 and instead used 31.Rxc6: Ne5 protected c6, so the queen on e8 could not profitably capture that rook. Taking c6 restored the pawn count to a one-pawn lead while keeping the rook active. I initially lost track of the pawn count during earlier analysis and corrected it from the actual captures; the result should not be inferred from a stale material impression.

The decisive played sequence was 31...Nb6 32.a3 Rxd4 33.Rxd4 f6 34.Nc4 a5 35.Nxb6. Black's ...f6 allowed my attacked knight to retreat; ...a5 then left Nb6 available to the cheaper knight capture. I had rejected 34.Nd7 because the illustrative ...Nxd7 35.Rxd7 Qxd7 would lose a rook. That rejected line was a mental check, not a referee-tested variation. The actual continuation produced a rook-and-knight advantage and depended on Black's material concessions.

I anticipated the queen check after vacating d1. The played 35...Qe1+ 36.Kh2 was legal, and the later 37.Rc8 Rxc8 38.Nxc8 exchanged Black's remaining rook. Against 38...Qe5+, 39.Qf4 both interposed and defended Rd4. My rook also defended the interposing queen, so ...Qxf4+ 40.Rxf4 safely removed the queens. This was a useful successful check of a forcing reply and the final recapture.

In the ending I captured a5 and f5, moved the rook away from pawn attacks, and advanced the a-pawn. The king's capture on h3 removed another pawn without entering an attacked square. Promotion at move 52 left Nc8 blocking the new queen's eighth-rank ray. The finish 53.Ne7+ Kg7 54.Qg8+ Kh6 55.Qg6# cleared that ray and used the knight to protect both g8 and g6. At the end, Qg6 covered g5/g7/h7, Ne7 prevented Kxg6, and Black's h5 pawn occupied the remaining escape. The referee confirmed mate.

The useful local behaviors were declining an automatic recapture, checking the defender behind a knight exchange, meeting a queen check while defending the rook, and verifying the mating queen's protection. The analysis still spent too long on remote variations and sometimes missed an obvious capture before correcting it. This game does not show that the full checklist is reliable or that more reasoning alone is the cause of improvement. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 3,461,957 tokens; not per-game or whole-account usage.

## Game 18 — Black, elo-1800-setting, 1–0

Resigned after 84.Kh7 (167 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 7 wins and 11 losses; the 1800 setting is 2 wins and 4 losses; maximum strength remains 0 wins, 0 draws, 6 losses. The target has not been achieved, and these results do not establish improvement against it.

I answered e4 with e5, developed, and castled on move 5. Central exchanges and the sequence ...Ne7–d5, ...c6, and ...Nxf4 reduced the minor pieces. I exchanged queens with 28...Qxf4 and advanced ...g5 only after the queens were gone. These choices retained the king's pawn cover during the earlier play, but did not prevent the later endgame errors.

White's 35.Ra6 pinned c6 against my king. The later 38...Rd6 39.Rxd6 Kxd6 restored that pin: after 40.cxb5, ...cxb5 would expose Kd6 to Ra6 and was illegal. I recognized the pin before submitting a move, but had already allowed the pawn loss. The played ...Rc8 and ...Kc5 defended c6 and freed the pawn. After 42.bxc6 Rxc6, however, 43.Ra5+ drove the king off the fifth rank and 44.Rxf5 took a second pawn. I had considered the rook check without initially carrying its opened horizontal attack through the king's departure.

King activity and rook checks created practical counterplay. The first checking sequence did not force a draw: White chose Kg3, then interposed Bf3 against ...Re3+. That bishop was pinned to the king along the third rank. White's h3 created an escape on h2. I switched to the central pawns with 55...Ba4 56.d4 Bxc2, using the bishop as the cheaper attacker while Kd2 made a rook recapture on c2 unfavorable.

The passed d-pawn was then removed with 59...Bb3 60.Kg4 Bxd5 61.Bxd5 Rxd5. Kg4 had removed the pin on Bf3, so the actual capture must not be justified by the old pin. Instead, bishop and rook both attacked d5, while Re6 did not defend that square. The bishop exchange recovered the pawn. White subsequently took h6, restoring the one-pawn deficit. The later 66...gxh4+ vacated g5 and opened Rd5's check against Kh5; White's Kxh4 left only the g-pawn on the board.

The critical rook-ending mistake was 69...Ke5 after 69.g4. I attacked Rf6 but allowed 70.Rf5+. White's g4 pawn protected f5, so Kxf5 was illegal. My own king on e5 blocked Rd5 from capturing the checking rook. Keeping Rd5 defended after ...Ke6 did not solve the problem: 71.Rxd5 Kxd5 forced the transition to a pawn ending with my king on d5 and White's king on h4, followed by Kg5. I examined some of this geometry in advance but accepted the exchange without establishing that the pawn ending could be held. This repeats the king-blocks-own-rook pattern from earlier games, now through an adverse exchange rather than a free rook loss.

My assessment of the pawn ending was unstable. I explored many lines, repeatedly corrected pawn attacks and king distances, and alternated between hopes of a draw and recognition of White's promotion route. No tablebase or engine analysis was used, and I do not claim a proved evaluation of every earlier ending or an established drawing alternative to 69...Ke5. The actual king maneuvers did not reach a claimable repetition. White advanced g5 and g6, then placed the king on h7 before pushing the pawn farther.

At the final position, White Kh7/Pg6 faced Black Kf8. The pawn controlled f7, and the white king controlled g7 and g8. Black could only move to e7 or e8; White could then play g7 and g8=Q with the promotion square protected. For example, ...Ke8 g7 ...Kf7 g8=Q+ is an unplayed mental illustration. I resigned because I could not prevent a supported queen promotion, not because checkmate had already occurred.

The specific next trial is to reconstruct the position and side to move after a proposed final rook exchange before treating it as safe. A king's legal recapture does not establish that the resulting pawn ending is defensible. The analysis again spent excessive time on remote variations and did not deliver reliable tactical or endgame judgments. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 4,232,253 tokens; not per-game or whole-account usage.

## Game 19 — White, full-strength, 0–1

Resigned after 40...Rd2 (80 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 7 wins and 12 losses; maximum strength is 0 wins, 0 draws, 7 losses. The goal remains unmet, with no demonstrated improvement against the maximum setting.

The d4/c4 opening led to early central exchanges and a queen trade on d1. I developed both bishops and brought the king to c2, then b2. Material stayed equal through move 22's bishop exchange. Keeping the queens off and avoiding an immediate king attack did not make the resulting position easy to defend.

I played 17.Nd2 to support e4 and control c4. This also blocked Rd1's route up the d-file. I had considered a rook recapture on d5 in earlier variations, then recognized after 17...Bxd5 that it was unavailable; 18.exd5 created a passed d-pawn instead. The own-piece obstruction was caught before an illegal submission, but the intended recapture had not been rebuilt after Nd2.

The plan Rac1 followed by 20.c4 counted Rc1 and Nd2 as defenders. Black's 20...Bb4 attacked that knight. The played 21.a3 Bxd2 22.Bxd2 Nxc4+ removed the defender before taking the pawn. I did not find a satisfactory answer during play, but have not proved that the pawn loss was forced from move 20 or that an earlier alternative saved the position. My long examination of ...Bc5 had missed the more direct ...Bb4 mechanism.

There was a useful successful capture-order check. After ...Nxc4+, 23.Ka2 protected a3 and avoided a checking ...Nxd2. The actual 23...Nxd2 was answered by 24.Rxc7+ Kxc7 25.Rxd2. Exchanging the c-file rooks first let me recover the knight without leaving Rc1 undefended. An immediate Rxd2 would have allowed ...Rxc1. This reached a rook ending one pawn down.

Black blockaded d5 with ...Kd6 and restricted my king with ...Rc8. After 27.Rd3 e4, I played 28.Re3 to attack e4. The reply ...Kxd5 both captured my passer and protected e4: Kd5 controls e4, so Rxe4 would lose the rook. I repeatedly underestimated that new king defense while considering the line. The later f3 and fxe4+ exchanges cleared a lateral route for my rook but did not remove Black's passed e-pawn.

Rg3–g5+–xh5 recovered one pawn, while ...Kd4 and ...e3–e2 created the decisive promotion threat. Rear checks drove the king through e3 and d2 to c1. I then kept the rook on the e-file, but ...Rc2 and ...Kd1 supplied a shelter and a protected interposition. The final played 40.Rd3+ Rd2 ended the checking sequence. In my unplayed reconstruction, 41.Rxd2+ Kxd2 leaves an unstoppable e-pawn; 41.Re3 e1=Q 42.Rxe1+ Kxe1 leaves Black with a rook against no piece. I resigned because the promotion would cost my remaining rook or produce a queen, not because checkmate had already occurred.

The next practical check is to test whether an enemy exchange can remove a necessary defender before the intended pawn capture, and to update all king-controlled squares after a king capture. These are specific errors to work on, not evidence that the existing protocol is reliable. Extensive remote analysis again failed to prevent basic geometric mistakes. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 4,420,972 tokens; not per-game or whole-account usage.

## Game 20 — Black, full-strength, 1–0

Resigned after 39.cxb8=Q (77 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 7 wins and 13 losses; maximum strength is 0 wins, 0 draws, 8 losses. The target remains unmet, and the maximum-setting results still show no demonstrated improvement.

I answered e4 with e5 and reached a closed Ruy Lopez structure, castling on move 8 with the kingside pawn cover intact. After White's d5, I used ...c4 and intended ...Nb7–c5. White's b4, the en-passant exchange, and a second b4 advance kept c5 controlled. My intended knight route was therefore unavailable. I challenged the queenside with ...a5, developed ...Bd7, and moved the queen to b6 to defend b5. These choices did not solve the accumulating pressure, and Be3 drove the queen back to c7. The played 22.Nxb5 Bxb5 23.Bxb5 left me a pawn down. I have not established a proved saving alternative or an engine evaluation of the preceding opening.

Several local geometry checks were useful but inconsistent. Bd7 connected the rooks before ...axb4 opened the a-file. However, I then imagined an unavailable ...Rxa1 before noticing that White Na3 blocked that file. Later, moving Ra8 to b8 changed which squares were protected by the rear rook; an old justification for ...Ra2 could no longer be reused. These errors were caught before submission, but consumed substantial analysis. The rook maneuvers ...Ra2–a3 attacked the queen without forcing a draw. White used Rec1 to counterattack my queen, then eventually chose Qc4 instead of repeating.

After Bc6, ...Rb8 removed the relative pin on Nb7 and ...Nd8 brought that knight off b7. White's 32.Nc4 attacked Ra3. I chose 32...Ra6, relying on Qc8's support along c8–b7–a6. White's 33.b5 attacked that rook with a pawn and supported Bc6 again. Queen support did not make a pawn attack harmless, and I had not checked a satisfactory subsequent retreat before placing the rook on a6. I found no satisfactory retreat during play and used 33...Rxc6 34.dxc6, giving the exchange and leaving connected passed pawns. This is not a proof that every earlier alternative also lost material.

The capture 34...Nxe4 correctly took a loose pawn: White's knight had left d2, and Be3 blocked Qe2's e-file. It reduced the material deficit but did not address the next fork. After 35.Nb6 Qc7, White played 36.Nd5, attacking both Qc7 and Be7. I had spent extensive analysis on Nd7 while omitting this different landing square. The actual ...Qa5 37.Nxe7+ lost the bishop. In an unplayed local illustration, ...Qc8 would also allow Nxe7+, forking Kg8 and Qc8; retreating the queen along that file would not solve the problem.

The finish repeated the error of analyzing only one opponent choice. After ...Kf8 38.c7, I played ...Kxe7, legally capturing the undefended knight. I concentrated on the unplayed 39.cxd8=Q+ Rxd8, where the rook could recapture the promoted queen. White instead chose 39.cxb8=Q, capturing that rook and obtaining a second queen. I had recognized that c7 attacked both b8 and d8, but failed to compare both promotion captures when selecting the actual king move. I resigned in the resulting overwhelming material deficit; this was not checkmate.

The next trial is to audit the immediate reply more systematically: include pawn pushes that attack the candidate's destination, scan every reachable enemy knight landing square for forks, and inspect the forward promotion and both capture promotions separately. These are specific checks to apply, not evidence that extending the written checklist has made it reliable. Long remote analysis again failed to prevent basic mistakes. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 4,686,424 tokens; not per-game or whole-account usage.

## Game 21 — White, skill-0, 1–0

Won by 36.Qh7# (71 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 8 wins and 13 losses; skill 0 is 6 wins and 1 loss; the 1800 setting remains 2 wins and 4 losses; maximum strength remains 0 wins, 0 draws, 8 losses. This win does not establish improvement against the target.

The d4/c4 opening met ...c6 and an early ...Qa5+. Nc3 and Bd2 answered the check and released the pin. I developed Bd3, castled, and expanded with e4 after checking the central recaptures. After Nxf6+ Bxf6, Bh6 attacked Rf8. Black's ...a5 ignored the attack, and 15.Bxf8 Nxf8 won an exchange. This material gain depended on the opponent's concession.

The queen maneuver Qe3–f3 met ...Bg5 and ...Bf6. I then used 19.Qxc6, with Ne5 protecting c6. Black removed that defender with ...Bxe5. I had checked this reply and chose 20.Qxa8, capturing the second rook. The alternative Qxc7 Bxc7 would only exchange queens while leaving my knight lost for a pawn. The actual rook capture preserved a material advantage. Against ...Bxh2+, I recognized that Qc7 protected the bishop along the diagonal and used Kh1 rather than an illegal Kxh2.

The central pawn advance d5 drove Ne6 to d4. Re4 attacked that knight, but ...Bb7 attacked my queen first, so I moved Qa8 to e8. Black then left the knight available with ...Bg3, allowing 25.Rxd4. After ...Bxf2 attacked that rook diagonally, Re4 returned it to the bishop's protection. I rejected an immediate Rxe7 once ...Bc5 had added a second defender: Rxe7 Qxe7 Qxe7 Bxe7 would lose the rook in the exchange. Instead, Rf1 activated the other rook. The played ...e6 dxe6 fxe6 Rxe6 cleared the f-file and recovered the pawn while saving the e4 rook from Bb7's opened diagonal.

The major failure was the calculation of 30.Qf7+ Kh6 31.Rxg6+. I examined ...Qxg6 and ...Kh5, and incorrectly treated that as a complete reply set. I omitted the h7 pawn's legal ...hxg6, which Black played. The queen and bishop protected g6 against a king capture, but did not prevent a pawn capture. The checking rook sacrifice was therefore not justified by the mating argument I had used. No claim is made that the position was lost or that the sacrifice has been fully evaluated; the specific claimed forcing line was incomplete.

After ...hxg6, I also initially considered Qxg6+ Qxg6 Bxg6 without carrying the exchange through ...Kxg6. The black king on h6 could legally take that bishop. I corrected this before submission and chose 32.Qf4+, a checking attack on Qg3 supported by Rf1. The illustrative ...Qxf4 Rxf4 or ...Qg5 Qxg5+ Kxg5 would exchange queens. Black instead interposed ...g5, leaving the queen available to 33.Qxg3. The subsequent ...Bxg2+ allowed 34.Kxg2; the remaining bishop did not attack g2.

The actual finish was ...Be7 35.Qh3+ Kg7 36.Qh7#. On h7 the queen was protected by Bd3 through e4/f5/g6. Rf1 controlled f6, f7, and f8, and the queen covered the other king escapes. The g5 pawn both occupied a potential escape from h6 and blocked Be7's route to h4 during the preceding check. The referee confirmed the final mate.

The immediate next trial is a literal capture audit of the chosen destination: for a white piece on g6, inspect black pawns on f7 and h7 before discussing king escapes or a queen recapture. The analogous direction must be reversed when playing Black. This supplements the existing capture check; it is not evidence that the protocol now works. Long analysis again omitted a simple pawn capture, and the result relied on several weaker-opponent concessions. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 4,875,400 tokens; not per-game or whole-account usage.

## Game 22 — Black, skill-0, 0–1

Won by 31...Qe1# (62 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 9 wins and 13 losses; skill 0 is 7 wins and 1 loss; the 1800 setting remains 2 wins and 4 losses; maximum strength remains 0 wins, 0 draws, 8 losses. These weaker-setting wins do not establish progress against the maximum target.

I answered e4 with e5, developed in an Italian structure, and castled on move 6. After ...h6, White exchanged Bg5 for Nf6, and Qxf6 retained the pawn cover. Be6 completed development. White then exchanged the other bishop for Nc6, and ...bxc6 left me the bishop pair and doubled c-pawns against two knights. The central ...d5 and ...exd4 opened lines. I considered the pawn push e5 against Qf6 before taking on d4 with the bishop, and chose ...dxe4 first. That was a local tactical precaution, not proof that every immediate bishop capture lost.

After Rxe4, ...Bd5 drove the rook to e3, and ...Bxd4 captured a pawn. White's 18.Ne4 attacked Qf6. I initially spent too long looking for a queen retreat, then used the direct 18...Bxe4 to remove the attacking knight. White captured the other bishop with Nxd4; ...Bd5 saved the remaining bishop. This left a bishop against a knight and an extra pawn, with the queen's threat resolved through a capture rather than a retreat.

The move 20...Rfe8 met 21.Qe1. Nd4 had lost its queen defender on d1, but taking it immediately would allow the illustrative ...Qxd4 Rxe8+ Raxe8 Qxe8+, conceding the second rook. I therefore exchanged first with 21...Rxe3. The actual fxe3 removed White's active rook and made the e3 pawn the knight's defender. The unplayed e8 sequence was checked mentally; it was not submitted as a variation to an engine or referee.

After ...Qg6 and Qe2, ...a5 challenged b4 while keeping the rook behind the a-pawn. The actual ...axb4 axb4 cleared the entire a-file. I used 25...Ra2, with Bd5 protecting a2 along c4/b3, and attacked the queen on e2. White's 26.Qxa2 allowed ...Bxa2, exchanging my rook for the queen. This decisive material gain depended on White's choice to capture the supported rook.

White's 27.Nxc6 removed a pawn and created the possible Ne7+ fork of Kg8 and Qg6. I moved the queen to e4 before that check arrived. The actual 28.Ne7+ could then be answered by Qxe7: the knight had left the c-file, where Rc1 had protected it, and e7 had no white defender. I subsequently captured e3 and moved the attacked bishop from a2 to d5.

White's final 31.Ra3 attacked Qe3 but left the first rank. I answered with Qe1#. The queen controlled f1/g1/h1, White's own g2/h2 pawns occupied the other king escapes, and Ra3 could neither capture Qe1 nor interpose on f1 or g1. Returning the rook to a1 would be outside the checking segment and would not stop the check. The referee confirmed mate.

Useful local checks were removing the queen-attacking knight, counting the complete rook exchange on the e-file, verifying the bishop's support of a2, and anticipating Ne7+ before moving the queen. They do not establish error-free play or a reliable protocol. Analysis remained excessively long, with many discarded remote lines and repeated corrections of blockers and attack geometry. I am retaining the existing move check rather than treating another checklist addition as improvement. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 5,148,348 tokens; not per-game or whole-account usage.

## Game 23 — White, elo-1800-setting, 1–0

Won by 31.Qf8# (61 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 10 wins and 13 losses; the 1800 setting is 3 wins and 4 losses; skill 0 remains 7 wins and 1 loss; maximum strength remains 0 wins, 0 draws, 8 losses. The target remains unmet, with no demonstrated improvement against maximum strength.

The opening reached a Benoni structure with White pawns on d5/e4. I developed and castled, used a4 against the queenside break, and played Re1. I initially treated that rook as an e4 defender without accounting for Be2; 12.Bf1 then actually cleared the file. After ...Bxc3, bxc3 preserved the bishop pair. Bf4–g3 answered the queen attack from f6, and c4 supported d5. These local choices are not an established evaluation of the opening.

Black answered 18.Nxe5 with ...h4 instead of recapturing. The intermediate 19.Nxd7 captured the second knight and attacked both Qf6 and Rb8. Black could have captured Nd7 with Bc8; the fork did not force a queen move as the only legal answer. The actual ...Qe7 allowed Nxb8, and ...Rf8 then left time for Bh2 to save the pawn-attacked bishop. These concessions produced the large material advantage.

The proposed knight exit Nc6 was initially misjudged: I relied on d5's protection and overlooked Black's b7 pawn, which could capture a knight on c6. I caught this before submitting Nc6, but only after having used that false exit in earlier analysis of Nxb8. A defended knight is still lost to a cheaper pawn capture. The knight remained on b8 until Black later placed the bishop on d7, allowing Nxd7 and Nf6+.

The central e5 and exd6 opened the e-file and created a bishop-supported passed pawn on d6. Black played ...Qxe1, and Qxe1 took the queen. I had checked the unplayed continuation ...Rxe1 Rxe1, with the a1 rook reaching e1 after d1 was vacated. Black instead played ...Bd7. Nxd7 removed the bishop; the analogous ...Rxe1 Rxe1 would leave Black with only king and pawns, but Black again declined and retreated to d8. The actual result therefore depended on additional material concessions, not merely on the earlier knight fork.

After Nf6+ Kg7, Qe7 defended the knight and attacked Rd8. Black retreated to h8. The d-pawn reached d7 and promoted while Black advanced b6–b5. Before choosing the finish, I rejected the unplayed 30.Qf8+ Rxf8 31.Qxf8+ because the last queen would no longer be protected: Kg7 could capture it on f8. This was another initially missed final king recapture, corrected before submission.

The actual 30.Qxh8+ used the promoted queen to capture the rook. Kxh8 was the only answer: Qh8 covered f8/g8/h7/h6, Nf6 also covered g8/h7, Qe7 protected Nf6 against Kxf6, and Black's own f7/g6 pawns occupied those escapes. Then 31.Qf8# covered g8 and g7 while Nf6 covered h7. No remaining black piece could capture the queen or interpose on g8. The referee confirmed mate.

Useful checks included the intermediate knight fork, the complete rook recapture, preserving queen support for Nf6, and the final mating-square audit. The repeated omissions of pawn attacks, friendly blockers, and king recaptures show that the existing protocol remains inconsistent; no new checklist item or training-success claim is warranted. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 5,263,546 tokens; not per-game or whole-account usage.

## Game 24 — Black, elo-1800-setting, 0–1

Won by 66...Rh3# (132 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 11 wins and 13 losses; the 1800 setting is 4 wins and 4 losses; skill 0 remains 7 wins and 1 loss; maximum strength remains 0 wins, 0 draws, 8 losses. The target remains unmet. The provisional engine-relative estimate is 1770 with a 1550–2000 interval, based on 16 weaker-setting games and excluding the 8 maximum-setting games; it is not human Elo or evidence of success against the target.

I developed behind ...d5/...c5/...e6 and castled on move 7. The central ...e5 and exchanges on e5 opened Bd6–e5–d4–c3–b2–a1. White's 11.Ba3 left Ra1 available to ...Bxa1 Qxa1, giving me the exchange. ...Qa5 defended c5 and attacked Ba3. After ...Ne4 Nxe4 dxe4, I developed the rook to d8. The later ...Qd2 attacked both Qc1 and Be2, with Rd8 behind the queen, and ...Qxc1 Bxc1 removed the queens. I rejected a premature rook entry on d2 because Bc3 would fork Qa5 and Rd2; this was a mental geometric check, not a proved evaluation of all alternatives.

The extra rook did not make the middlegame simple. White retained two bishops and advanced its king and kingside pawns. I used ...b6/...Bc6, doubled the rooks on the d-file, and then moved toward the kingside with ...g6, ...gxh5, ...f6, and ...Rg7. After Bxh5 attacked Re8, ...Ree7 saved the rook. White's Bb2 then introduced Bxf6, which would attack both rooks on e7 and g7. The played ...Be8 attacked Bh5, and Bxe8 Rxe8 exchanged one bishop pair. Moving the king to f7 became possible after the bishop on h5 had gone.

After ...Reg8, White's 34.g5 was answered by ...Rxg5. I retained f6 as a blocker of Bb2's diagonal to g7. The alternative pawn capture ...fxg5+ would open that diagonal once White answered the pawn check, while the rook's exits were obstructed by Black's own king and pieces and White's f5 pawn. This was a local danger identified during play, not a proved losing variation. White's Kxe4 removed my advanced central pawn; rook checks then drove the king away from f5. After Rxh7+ I interposed ...R8g7. The actual Rxg7+ Kxg7 was legal because f6 still blocked Bb2's attack on g7. Only after Kf3 did I take f5 with check; the king was then too far away to recapture the rook.

The ending had rook against bishop with pawns. I centralized the king and advanced ...f5, then transferred the rook to b8 and used ...a6/...b5 to open the file. White's e4 allowed ...fxe4, creating the passed e-pawn. The sequence axb5 axb5 cxb5 Rxb5 used the a-pawn for the first recapture; taking immediately with the rook would have exposed it to the c4 pawn. ...Rxb3 removed White's final pawn. The later ...Kd5, ...c4, and ...Kd4 coordinated the king and the two remaining pawns.

Before advancing ...e3 I checked the final rook recapture: with Kd4 supporting e3, Bxe3 could be answered by Rxe3 without allowing the white king to take the rook. After 58.Kf3, the tempting ...Kd3 would instead obstruct Rb3's route through c3/d3 to e3. White could take the pawn with Bxe3, and Kxe3 would be illegal because Kf3 protected e3. I chose ...Rd3. White's Kg4 then moved out of capture range, allowing ...e2. Against Bb2+ I moved to d5. White's Bc3 covered e1 through d2, so I captured the bishop with ...Rxc3 before promoting.

After ...e1=Q, ...Qe5+ used the king's protection of e5. ...Rf3 cut off the f-file and left White only h6 or h7; the actual Kh7 allowed ...Qg5. The queen covered g6/g7/g8 and h6, leaving Kh8 as the sole move without stalemate. Then ...Rh3# checked on the h-file while Qg5 covered g7 and g8. The referee confirmed mate.

Useful checks included the bishop fork of the rooks, retaining a pawn that blocked a bishop ray, the legal king recapture in the rook exchange, using the pawn before the rook in the b-file exchanges, avoiding a king move that obstructed the rook, and removing the bishop before promotion. These are individual successful checks, not proof that the protocol is reliable. The game still involved excessive remote analysis and repeated corrections, including a long search for a simple queen-and-rook finish. The win depended on an early material concession and subsequent weaker-setting play. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 5,836,916 tokens; not per-game or whole-account usage.

## Game 25 — White, full-strength, 1/2–1/2

The referee recorded a draw by threefold repetition after 37.Kb2 (73 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 11 wins, 1 draw, and 13 losses. Maximum strength is now 0 wins, 1 draw, and 8 losses: the first half-point, for a score of 0.5/9, approximately 5.56%. The goal remains far from achieved. One draw does not establish sustained improvement, and the final position had three fewer white pawns. I have not established that it was defensible without Black's repeated checks.

After d4/c4/Nf3/Nc3, Black challenged the center with ...c5. The sequence cxd5 cxd4 Nxd4 Nxd5 e4 Nxc3 bxc3 left c3/e4 pawns, and ...e5 drove the remaining knight back to f3. I checked the legal king recapture before the queen trade ...Qxd1+ Kxd1. Be3, Kc2, Bd3, and Rhd1 developed the pieces. Black's ...Ba3 restricted the king's queenside routes, while ...Be6 continued to attack a2, initially defended by Ra1.

The maneuver Nh4–f5–g3 met ...g6 and ...Nc6 without producing a concrete gain. Kb1 freed c3 from the c-file pin but obstructed Ra1's horizontal movement. Bc1 challenged Ba3, but ...Bc5 attacked f2, so I returned to e3 and exchanged bishops with ...Bxe3 fxe3. After ...Na5, Ne2 defended c3 against Rc8. Black's ...Nc4 then attacked the undefended e3 pawn. The reply Bxc4 removed that knight, but ...Rxc4 attacked e4 after its bishop defender disappeared. I chose Rd3 to hold c3/e3, and ...Rxe4 took the first pawn. This is the observed deterioration, not proof that all earlier alternatives lost a pawn.

Ng3 attacked the rook and Kc2 freed Ra1 while defending Rd3/c3. I rejected h3 while h2 was the knight's sole defender: ...Rxg3 would then capture the knight without a recapture, since Pe3 blocked Rd3's horizontal route. Rd2 defended g2 in preparation for ...h4. The subsequent Nf1 kept that second-rank defense clear; Ne2 would instead have blocked Rd2's line to g2. The move a3 took the a-pawn off Be6's diagonal before using the a1 rook.

Black doubled the rooks with ...Rgc4. A proposed Rd3 defense of c3 would allow ...Bf5 to attack and pin that rook against Kc2. I moved to b2 and conceded c3 instead. I did not prove that the pin forced every possible material concession. After ...Rxc3, I caught a concrete danger before moving the d2 rook: the illustrative Rd6 Rb3+ Ka2 Rc2# would leave no interposition, capture of the checking rook, or king escape. Ra1 and Pa3 would occupy the king's own escapes, and Be6 would protect Rb3. The actual Rad1 cleared a1 and kept Rd2 available against a rook check on c2.

After ...Rb3+ I chose Ka2 to keep a3 defended. Black then played ...Rxe3+, moving the rook off b3 and uncovering Be6–d5–c4–b3–a2. Nf1 attacked e3, but Nxe3 would leave that bishop check unanswered and was therefore illegal. My earlier argument that the knight defended e3 did not survive the king's relocation onto the bishop diagonal. I recognized the check before submission and moved to b2, but Black had won the third pawn and retained the rook. This was a tactical failure despite the absence of illegal attempts.

The remaining moves repeated ...Rb3+ against Kb2 and ...Rbc3+ against Ka2. I retained the same legal king escapes. The referee automatically recorded the threefold-repetition draw after 37.Kb2. I did not inspect the opponent's search, evaluate the final position with an engine, or establish why it chose that sequence. The recorded result is a draw; it does not prove a forced perpetual check from the earlier position.

The next positional trial is to make both rooks usable before spending further tempi on a wing-knight maneuver in a queenless position, unless a concrete tactical reason takes priority. This is a working hypothesis, not a demonstrated improvement. The existing tactical checks remain necessary: the successful mating-net check did not prevent the later missed discovery against e3. Analysis was again excessively long and repeatedly corrected basic geometry. No external sources, engine analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 5,978,412 tokens; not per-game or whole-account usage.

## Game 26 — Black, full-strength, 1–0

Lost by 45.Qh8# (89 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 11 wins, 1 draw, and 14 losses. Maximum strength is 0 wins, 1 draw, and 9 losses, scoring 0.5/10 = 5%; skill 0 remains 7 wins and 1 loss, and the 1800 setting remains 4 wins and 4 losses. The goal remains far from achieved. The provisional engine-relative estimate remains 1770 with a 1550–2000 interval from the 16 weaker-setting games, excluding all 10 maximum-setting games; it is not human Elo or evidence of target success.

The opening used ...e5, ...Nc6, ...a6, ...Nf6, ...Be7, and castling. The queenside knight then spent several moves on a5–c4–b6–c8 as White advanced b3 and a5. White gained central space with d5. I intended 15...Bg5 to exchange the restricted bishop and clear e7 for the knight, but failed to audit the intended queen recapture: after 16.Bxg5, the proposed ...Qxg5 would allow Nf3xg5, losing the queen to the knight. I recognized that only after White had captured the bishop. The actual ...f6 blocked Bg5's diagonal to Qd8, and White retreated with Be3, keeping the extra bishop. This was a concrete piece-losing error, not a sound exchange plan.

I redeployed the knights, connected the rooks with ...Qd7, and tried to blockade the advanced d-pawn. After c5 dxc5 bxc5, ...c6 prevented a c6 pawn fork of Qd7/Bb7, but White's d6 then drove Ne7 to g6. The sequence Bb3+ Kh8 Bxa4 bxa4 Rxa4 traded a bishop for the other knight and cost a pawn. ...Qf7 and ...Bd7 kept a blockade on d7 while freeing the remaining rook's route to a8. These local defensive purposes do not establish an adequate position after the earlier bishop loss.

Later ...Nf4 and ...f5 were met by Bxf4 exf4, removing White's last bishop and Black's last knight. White's e5 cleared the fourth rank, so ...g5 defended f4 against Rb4. Rb7 aligned the bishop on d7 with the queen on f7; ...Qe6 changed that alignment. ...Rg8 supported g5, and ...f3 attacked Ne2 and g2. After Nd4 attacked the queen, I rejected ...Qe7 because Pd6 could capture it, and chose ...Qe8. This was a successful correction of a different basic capture omission in a remote variation, not evidence of generally reliable calculation.

After e6 Bxe6 Qa1, the queen on a1 aimed toward Kh8, initially blocked by White's own Rb2 and Nd4. I used ...Rg6 to free g8 and cover g7, then answered Nxe6 with ...Qxe6 to retain that rook. White's 42.Rb8+ came from the upper rook, b7–b8; the lower rook still blocked Qa1. The tempting ...Raxb8 would allow Rxb8#, simultaneously opening the queen diagonal and checking along the eighth rank. I correctly rejected that capture, but spent excessive time on other branches and failed to finish the actual king-move line correctly.

The played 42...Kg7 was legal because Rb2 still blocked Qa1's diagonal. White then used 43.R2b7+, giving double check from the rook and queen. ...Kh6 was the only king escape. White's 44.Rxh7+ forced ...Kxh7, and 45.Qh8# finished: Rb8 protected Qh8, while also obstructing Ra8's attempted capture of that queen. Qh8 covered g8/g7/h6, and Black's own Rg6 occupied g6. There was no capture of the checker, interposition against the adjacent queen, or king escape. The referee confirmed mate.

During the earlier calculation I examined Rh8+ and noticed that Ra8 could capture that rook once b8 was vacated. That did not answer Qh8#: the rook stays on b8, protecting h8 and blocking Ra8. Focusing on one superficially similar mating attempt caused me to miss the stronger queen move. I recognized the actual finish only after Rxh7+ had appeared on the board. I have not proved that any earlier alternative saved the already inferior position.

The existing protocol already required checking cheap captures after a queen recapture and inspecting all immediate queen checks after a king move. Adding further checklist length is not a substitute for applying those checks to the exact candidate. Before the next game I rehearsed these two concrete failures: Nf3 captures a queen on g5; Qh8 is protected by a rook that remains on b8 and blocks Ra8. The positional trial remains to finish useful development before repeated wing-knight moves. Neither rehearsal nor this review establishes improved performance. No external sources, engine analysis, automated chess analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 6,403,626 tokens; not per-game or whole-account usage.

## Game 27 — White, skill-0, 1–0

Won by 25.Qh7# (49 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 12 wins, 1 draw, and 14 losses. Skill 0 is 8 wins and 1 loss; the 1800 setting remains 4 wins and 4 losses; maximum strength remains 0 wins, 1 draw, and 9 losses, scoring 5%. The target is unmet. The provisional engine-relative estimate is 1780 with a 1560–2010 interval from 17 weaker-setting games, excluding the 10 maximum-setting games; it is not human Elo.

I developed both knights, established d4/c4/e4, placed the king's bishop on d3 to support e4, castled, and developed Be3. Against ...Nxd4 I used Nxd4, checking the possible ...cxd4 Bxd4 recapture. Black instead castled, allowing Nf3 to save the extra knight. ...b5 then left a pawn available to Bxb5. Black's ...Nxe4 allowed Nxe4, and after ...f5 I used Nxc5, initially supported by Be3. These were substantial weaker-setting concessions.

After ...f4, Bd4 preserved the knight's defender. The subsequent ...Qb6 attacked Bb5 and added a queen behind the c5 exchange. I chose Bc4 without completing the changed capture chain: ...Bxc5 Bxc5 Qxc5 would remove both my c5 knight and its bishop defender in return for Black's bishop. I recognized the extra queen recapture at the next position, before submitting Bxc5, and expected to retain only the extra knight. This was another incomplete exchange audit, despite the prior review. Black actually declined ...Qxc5 and played ...Rd8, leaving its queen on b6 available to Bxb6.

Before Bxb6 I checked the possible ...Rxd1 and the legal rook recapture on d1. Black instead played ...Rd5, allowing Bxd5. I accepted the possible ...exd5 as a favorable rook-for-bishop exchange, but Black again declined and played ...Bd7. The same bishop could then reach a8 through c6/b7 and take the last rook. Black's ...axb6 captured my other bishop, and Qxd7 removed the final black piece. The resulting overwhelming advantage depended on these concessions; it does not show improvement against maximum skill.

After ...h6, I calculated and played Qe8+ Kh7 Be4+ g6 Qxg6+ Kh8 Qh7#. Qe8 covered the eighth rank and f7. After Be4+, Black's own h6 pawn blocked that king escape and ...g6 was the available interposition. The bishop protected Qxg6 against Kxg6, then protected Qh7 along e4–f5–g6–h7. Qh7 covered g7/g8, and Black had no piece able to capture the checker or interpose. The referee confirmed mate.

The finish was correctly checked, but the c5 exchange omission remains a failure. No new checklist item is needed: the existing requirement to continue through the last recapture was not applied after ...Qb6 changed the position. No external sources, engine analysis, automated chess analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 6,503,498 tokens; not per-game or whole-account usage.

## Game 28 — Black, skill-0, 0–1

Won by 45...Rf1# (90 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 13 wins, 1 draw, and 14 losses. Skill 0 is 9 wins and 1 loss; the 1800 setting remains 4 wins and 4 losses; maximum strength remains 0 wins, 1 draw, and 9 losses, scoring 5%. The target is unmet. The provisional engine-relative estimate is 1780 with a 1570–2010 interval from 18 weaker-setting games, excluding the 10 maximum-setting games; it is not human Elo.

I developed both knights and bishops, castled on move 5, moved the queen off d8, and developed the a8 rook to d8 before the later knight redeployment. ...Bxe3 fxe3 removed one bishop pair. Against Bb5 I used ...a6, and Bxc6 bxc6 left me with doubled c-pawns. I put the remaining knight on d7 to keep e5 defended before ...d5. This followed the development trial more closely than game 26, but it did not prevent subsequent positional and tactical problems.

After ...dxe4 dxe4, I used ...Qf6 to support e5. I considered several knight departures that would uncover the f-file but did not anticipate the actual 18.Nd4. It simultaneously exposed the rook's attack on Qf6 and attacked Be6/c6. The played ...Qg6 retained the bishop's defense but allowed Nxc6 to win a pawn and attack Rd8. I retreated to e8. I have not established that the pawn loss was forced from the earlier position; this was an incomplete audit of the knight's available moves.

...f5 and ...fxe4 recovered the e4 pawn temporarily. After 22.Rxf8+, I initially intended a rook recapture, then caught the unplayed ...Rxf8 Ne7+: the knight on e7 would check Kg8 and attack Qg6, while the rook would no longer be on e8 to capture it. I instead used ...Nxf8 and retained Re8. The later ...Bd7 used the square vacated by that knight, attacked Nc6, and cleared the rook's defense of e5. I also checked that White could use Qc4+ after the bishop left e6; the actual check was answered by ...Kh7.

After Na5, ...Bf5 defended e4 with a bishop as well as the queen. White's g4 drove the bishop back to e6, and Qxe4 Qxe4+ Nxe4 exchanged queens with White a pawn ahead. The queen capture on e4 gave check along e4–f3–g2–h1 because the g-pawn had left g2. I did not establish an adequate middlegame position merely by finding legal recaptures and queen retreats.

The decisive concession came after 28...Bd5, which pinned Ne4 to Kh1 along d5–e4–f3–g2–h1. White's Kh2 removed the pin but did not defend the knight, allowing ...Bxe4. The bishop then took c2. ...Kg6 legally attacked Rf7, and Rf2 allowed ...Bxa4. Against Ra2 I retreated to b5, where Pa6 protected the bishop and the bishop protected a6. White's Rc2 attacked c7; ...Ne6 developed the knight and defended that pawn.

After h4, a previously considered ...Ng5 was no longer safe because the h4 pawn could capture it. I used ...h5 instead and verified the actual king capture after gxh5+: on h5 the king was not attacked by White's h4 pawn, Kh2, Na5, or Rc2. The played ...Kxh5 was legal. White's 37.Rc5 then allowed ...Nxc5. I accepted the possible bxc5 as a favorable rook-for-knight exchange, but White instead moved its king to h3. ...Nd3 saved the knight with support from Bb5, and ...Nxb4 removed the remaining queenside pawn. Only after White's king returned to h2 did I take h4; while it was on h3, that king had defended h4.

For the finish I used ...Rf8 and ...Rf2+ to force the king to the first rank, then ...Kg3 to cover f2/g2/h2. White's 44.Nc4 obstructed Bb5's protection of f1. An immediate ...Rf1+ would therefore permit Kxf1 from g1. I used ...Bxc4 first, removing the knight and restoring the bishop's line through d3/e2 to f1. White had only Kh1 available: its e4 pawn was blocked by e5, f1 was bishop-controlled, and the second-rank king squares were covered. Then ...Rf1# checked along f1–g1–h1; Kg3 covered g2/h2, and no white piece could capture or interpose. The referee confirmed mate.

Useful checks included preserving Re8 against the knight fork, exploiting the actual pin on e4, revisiting pawn attacks after h4, verifying both king captures, and removing the blocker before the final rook check. The win depended on the undefended knight, the rook concession, and White's refusal to recapture on c5. The earlier missed Nd4 and the excessively long, repeatedly corrected analysis remain limitations. These local successes do not establish improvement against the target. No external sources, engine analysis, automated chess analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 6,681,379 tokens; not per-game or whole-account usage.

## Game 29 — White, elo-1800-setting, 1–0

Won by 40.Qdh8# (79 plies), confirmed from the recorded PGN. No illegal submissions. Overall results are 14 wins, 1 draw, and 14 losses. The 1800 setting is 5 wins and 4 losses; skill 0 remains 9 wins and 1 loss; maximum strength remains 0 wins, 1 draw, and 9 losses, scoring 5%. The target remains unmet. The provisional engine-relative estimate is 1810 with a 1610–2040 interval from 19 weaker-setting games, excluding the 10 maximum-setting games; it is not human Elo.

I developed both knights and bishops, castled, and placed the rooks on d1/c1 before the later knight maneuvers. After ...cxd4, Nxd4 retained the e-pawn. Black advanced the a-pawn to a3; b3 contained it and supported Bc4. The e4–e5 advance supported d6. Ne4–d6 met ...Bxd6, and exd6 produced a bishop-supported passed pawn. This followed the development trial, but one weaker-setting win does not validate that trial against maximum strength.

After ...Qb6, both Bb5 and Nd4 were under pressure from the queen and rook. Qc4 defended Bb5 diagonally and Nd4 horizontally while attacking Rd5. I checked the final queen recaptures in the possible rook exchanges. Earlier in this calculation I had temporarily forgotten that Qe2 also defended Bb5 through d3/c4; changing a queen's square required rebuilding those lines. Qc7 used Pd6's protection and attacked the queen on b6, which retreated to a5. Qxf7 won a pawn. After ...e5 attacked Nd4 and blocked Bg3's support of d6, Nf3 Rxd1+ Rxd1 cleared the d-file and left the remaining rook behind the passer. Black's ...Bf5 then protected Ng6, so Qxg6 was no longer a free capture. Bc4 saved the bishop that had lost Nd4's protection.

The fork Nh4 attacked Bf5 and Ng6. Black answered ...Ne7, allowing Qxe7 to take an undefended knight. I used the queen rather than treating dxe7 as equivalent: moving Pd6 would open the d-file and allow ...Rxd1+, requiring a different calculation. Bxe5 then won the central pawn with Qe7's support. The subsequent ...Nh5 defended g7, so a queen capture there would still be answered by ...Nxg7; bishop support against the king did not remove that knight capture.

Be2 attacked Nh5. Black's ...Rd7 attacked Qe7 but left the rook capturable, and Qxd7 won it. I had allowed for the possible ...Qxe5, which would return a bishop while retaining a larger advantage. Black instead played ...Nf6 against the queen, and Bxf6 gxf6 exchanged that knight for a bishop. Qe8+ Kh7 cleared d7 for the pawn. After d7, Black's ...Qd8 simply left its queen available to Qxd8. The knight, rook, and queen concessions were decisive; I have not proved that the earlier middlegame forced them.

Qxf6 removed the f6 pawn and cleared d8. After ...Bc6, d8=Q and ...Bd5, the promoted queen reached h8. Qf6 protected h8 through g7 and covered g6/g7; Qh8 covered g8 and the h-file escapes. The adjacent check could not be interposed against, and Bd5 could not capture either the checker or its defender. The referee confirmed mate. I also considered the unplayed ...Be8 after promotion, which would obstruct the promoted queen's path and require a different continuation.

Calculation remained inefficient and repeatedly corrected basic geometry before submission. In particular, I spent substantial time on a proposed Bc6 before noticing that b7 could capture the bishop, repeating game 23's cheap-pawn-capture omission. I also had to restore Qa5's control of d8 in promotion variations. The next execution focus is to perform the existing landing-square capture check before expanding branches, rather than adding more checklist text. No external sources, engine analysis, automated chess analysis, or delegated advice used. Observed cumulative active-goal usage after the game: 6,897,352 tokens; not per-game or whole-account usage.

## Game 30 — Black, elo-1800-setting, 1–0

Lost by resignation after 73.f6 (145 plies), confirmed from the PGN. No illegal submissions. Overall: 14 wins, 1 draw, 15 losses. The 1800 setting is 5–5; skill 0 is 9–1; maximum strength is 0 wins, 1 draw, 9 losses. The provisional engine-relative estimate is 1780, with a 95% credible interval of 1590–1990, from 20 rated games; the 10 maximum-setting games are excluded from that estimator. This is not human Elo. The operator's authorized objective clarification during this game superseded the former maximum-strength success criterion: improve measured Elo through focused learning and periodic evaluation, retaining the active goal and all usage/results.

The early queen exchange followed by ...e4 forked Bd3/Nf3 and won a knight. I subsequently failed to preserve the resulting coordination. After ...Rd2 Bxe4, my ...Rxb2 allowed Bxf5 to take the other knight. I had also omitted the bishop's possible final recapture on b1 in a proposed rook-exchange line. These were further failures to account for the defense and capture lines changed by each move. Later ...Rxh3 allowed Bxf5, so that sequence exchanged pawns rather than simply recovering one.

The a-file exchanges and ...Rxa6 eventually left me a pawn ahead in a rook-and-opposite-bishop ending. I let the white e-pawn advance while pushing my c-pawn. After e6 and e7, ...Bxe7 Rxe7 surrendered the bishop for that passer. I have not established the correct earlier defense or proved that the loss was forced at an earlier point. The advanced c-pawn subsequently tied down White's rook and bishop; I retained both king and rook protection until White chose Bxc2+ Rxc2 Rxc2 Kxc2.

I misjudged the resulting pawn ending: Black Kc2/Ph5 against White Ke3/Pf4, White to move. The actual Kf2 Kd3 f5 h4 Kg2 Ke4 f6 showed why simply counting pawn pushes was inadequate. White's king could stop the h-pawn while the f-pawn outran my king. In the final position, ...h3+ permits Kxh3, and ...Kf5 f7 ...Kg6 f8=Q does not catch the pawn. These are my own calculations, not an engine-certified endgame verdict. I resigned when I judged the promotion unavoidable.

No external sources, engine analysis, automated chess analysis, or delegated advice were used during the game. Analysis remained extremely long and repeatedly corrected basic geometry; no improvement claim follows from the review. Observed cumulative active-goal usage after the game: 7,801,899 tokens; this is not per-game or whole-account usage. Before starting game 31, carry out the separately recorded pawn-race practice trial and then evaluate transfer at game 36.

## Game 31 — White, full-strength, 0–1

Lost by resignation after 42...Rd3 (84 plies), with no illegal submissions. Overall: 14 wins, 1 draw, 16 losses. Maximum strength: 0 wins, 1 draw, 10 losses. The unchanged Elo estimator remains 1780 [1590, 1990], based on 20 rated weaker-setting games; it excludes the 11 maximum-strength games. This is the first game of the predeclared games 31–36 evaluation block following pawn-race practice trial 01.

After the central exchanges and queen trade, I developed the bishops, moved the king to c2, and put the rooks on d1/b1. The bishop exchanges produced a passed d-pawn. The concrete material error was 21.e4: I noticed that ...Nxe3+ would capture the e3 pawn and fork Kc2/Rd1, but moving that pawn did not stop the knight from playing ...Ne3+ without a capture. The same checking fork remained available. Kd3 Nxd1 Rxd1 left me down the exchange. The existing immediate-check audit was not correctly applied; this was not a lack of checklist text or a pawn-race error.

I later used c4 to support d5, moved the king off the d-file, and sought knight activity. Nf7+ displaced the king from its defense of e5, allowing Nxe5, but the doubled rooks captured g2 and the f-pawn then took e4. Black's second-rank control repeatedly made a quiet pawn push impossible. Before move 38 I caught the threatened ...Rg1 mate against Ke1: Rc2 cut off the second rank and my own Rd1 obstructed a capture of the checking rook. After Kf1 and ...Rxh2, I similarly avoided ...Rh1 mate with Kg1. These local checks did not repair the material disadvantage.

The actual ...Rcg2+ Kf1 Rh1+ forced Kxg2 and opened the first rank for ...Rxd1. I recognized the skewer before the forced king capture; taking g2 was not a net rook gain. Ne3 attacked the remaining rook and blocked the e-pawn, but ...Rd3 attacked the knight again. I resigned with Kg2/Ne3/Pa2/Pd6 against Ke6/Rd3/Pa7/Pe4/Pg7/Ph7. In my own illustrative continuation, Nc4 Rxd6 Nxd6 Kxd6 leaves one white pawn against four black pawns. Other knight retreats generally abandon d6; I have not engine-certified the full ending.

Trial observation: no pure pawn ending was actually played. I did explicitly examine the kings and remaining pawns in two proposed liquidations. Earlier, a d2 exchange would let Black take d6 and leave two white pawns against four; after h2 was lost, the final illustrative liquidation leaves one against four. These are unverified counterfactual calculations, not independent proof of transfer. The game provides no rating improvement and shows recurrence of a more basic checking-fork omission. Complete the planned evaluation block before deciding the next learning method.

No external sources, engine analysis, automated chess analysis, or delegated advice were used during this measured game. Analysis remained excessively long and required repeated corrections of attack geometry. Observed cumulative active-goal usage after the game: 8,059,833 tokens; not per-game or whole-account usage.

## Game 32 — Black, full-strength, 1–0

Lost to 30.Qxh8# (59 plies), confirmed by the referee and PGN; no illegal submissions. Overall: 14 wins, 1 draw, 17 losses. Maximum strength: 0 wins, 1 draw, 11 losses. Elo remains 1780 [1590, 1990] from 20 rated games, with 12 maximum-strength games excluded by the fixed estimator. This is game two of the planned games 31–36 evaluation block.

I completed minor-piece development, castled, and brought the rooks to e8/d8. The sequence ...Nb4, ...c5 and d5 closed the center. I later played ...g6 and ...Bg7, then ...h5 when White arranged Qc1/Bd2 against h6. These moves weakened the kingside while the queen and other pieces remained on the queenside. After ...Qxb5, ...c4 and ...Qc5, White offered 24.Ndf5. I accepted with ...gxf5 25.Nxf5, gaining a knight for a pawn while opening the king position. I have not established that accepting the sacrifice was itself a forced loss or that the earlier defense was adequate.

I tried ...h4 to obstruct a rook lift to g3. After Bh6, I chose ...Bh8, then answered Qg5+ with ...Kh7. White's Bg7 was protected by Nf5 and attacked Bh8/Nf6. I recognized that ...Bxg7 would permit Qxg7 mate, but chose ...Nxe4 to attack Qg5 and control g3 without completing the immediate queen-check audit. White played Qh5+, ...Kg8, Qxh8#. The queen captures the bishop on h8; White's Bg7 protects h8 and covers f8. Black's f7 pawn obstructs another king escape. The adjacent queen check cannot be blocked, and no black piece can capture the queen. The referee confirmed the mate.

My reasoning dwelt on possible Bxh8 and rook-lift continuations after ...Kg8 while omitting the simpler Qxh8 capture. I also carried attack and recapture assumptions between hypothetical Qh4 and actual Qh5 positions before correcting them. This is further evidence that long analysis and an existing checklist have not made immediate forcing-move coverage reliable. The material gain did not compensate for the mating attack. I have not proved which earlier alternative would have saved the position.

Trial observation: no pawn ending or candidate pawn liquidation arose. The pawn-race practice remains untested by this game. Preserve the planned evaluation after game 36; the recurring immediate-check omission is a candidate for the next focused learning trial, not grounds to claim success for the current one. No external sources, chess-analysis tools, automated analysis, or delegated advice were used during the measured game. Observed cumulative active-goal usage after the game: 8,418,026 tokens; not per-game or whole-account usage.

## Game 33 — White, skill-0, 1–0

Won by 38.Re8# (75 plies), confirmed by the referee and PGN; no illegal submissions. Overall: 15 wins, 1 draw, 17 losses. Skill 0: 10 wins and 1 loss. Maximum strength remains 0 wins, 1 draw, 11 losses; the 1800 setting remains 5–5. The provisional engine-relative Elo is 1790 [1600, 1990] from 21 rated games, excluding 12 maximum-strength games. This small movement from the trial baseline of 1780 [1590, 1990] does not establish improvement.

After d4/c4/d5 and the central exchange, I blocked ...Qa5+ with Nc3, then used Bd2 to remove the pin before relying on that knight to defend e4. Rb1 met the queen's threat to b2. Both bishops and knights developed, I castled, and Rfe1 preceded the central e5 break. Black answered e5 with ...Nxe5, then played ...g5 after Nxe5 rather than recapturing. I used Nxf7 to fork Qd8/Rf8, and after ...Rxf7, Bxg5 saved the attacked bishop and won a pawn. The further ...c4 allowed Bxc4 to gain another pawn.

I retreated Bd3 against ...Rc8, then exchanged Bxe7 Rxe7 Rxe7 Qxe7 after ...Ng4 exposed Black's e7 bishop and threatened f2. Removing the f-file rook changed the recapture situation on f2. The subsequent h3 drove the knight to e5. Bf5 attacked Rc8. I anticipated ...Nf3+ and chose gxf3 while considering the immediate queen checks. Black actually replied ...Rxc3, allowing Qxc3. That concession removed the remaining black rook; I have not proved that the preceding play forced it.

After ...Bg6, Bxg6 was intended as a bishop exchange, but Black declined the pawn recapture and checked with ...Qg5+. Kf1 left the g-file. Against ...Qh6, Bf5 both saved the bishop and defended h3; against ...Qg5, Bg4 put it under the protection of f3/h3. I then played Re1. Black's ...Qc4+ was a checking move I had already noticed could be captured by Qxc4. It lost Black's queen. The large winning advantage depended on these weaker-setting concessions.

The finish was Qf4+ Kg7 Re7+ Kg6 Qf5+ Kh6 Re6+ Kg7 Qf6+ Kg8 Re8#. I calculated the final four-move forcing sequence before starting it, accounting for the queen's support of Re6 and the rook's support of Qf6. At mate, Re8 covers the eighth rank, Qf6 covers f7/g7, and Black's own h7 pawn occupies the remaining nearby square. There is no black piece that can capture or interpose; the referee confirmed mate.

No pawn ending or candidate pawn liquidation occurred, leaving trial 01 untested in this game. Useful local checks were removing the c3 pin, accounting for rook/queen recaptures on e7, and anticipating the knight and queen checks. I still spent unnecessary analysis on rejected bishop checks and simple mating alternatives before correcting their protection geometry. These observations are not an independent accuracy score. No external sources, chess-analysis tools, automated analysis, or delegated advice were used. Observed cumulative active-goal usage: 8,494,679 tokens; not per-game or whole-account usage. Continue the predeclared block through game 36.

## Game 34 — Black, skill-0, 0–1

Won by 32...Rh1# (64 plies), confirmed by the referee and PGN; no illegal submissions. Overall: 16 wins, 1 draw, 17 losses. Skill 0: 11 wins and 1 loss. Maximum strength remains 0 wins, 1 draw, 11 losses; the 1800 setting remains 5–5. Elo is 1790 [1600, 2000] from 22 rated games, with 12 maximum-strength games excluded. There is no established sustained rating improvement.

I developed both knights and bishops and castled. White's b3 removed the b2 pawn's defense of Nc3. I used ...Bb4 to pin that knight, then ...Ne4 after Qd3 defended it. Against Rc1 I calculated ...Bxc3+ Rxc3 Nxc3 through the eventual Qxc3: a rook and knight are removed in exchange for a bishop and knight, winning the exchange. White inserted Bg5 against Qd8 before recapturing. I used ...Qd7; the tempting ...Qxg5 would have allowed Nf3xg5, the same geometry missed in an earlier game. The played line preserved the exchange gain.

...Rae8 activated the rook. ...Bg4 both attacked Nf3 and uncovered pressure on Be2. After h3, ...Bxf3 Qxf3 removed the knight that had supported d4. I played ...dxc4, then recognized that White's Be3 restored a defender of d4. The actual ...Nxd4 remained supported by Qd7 and attacked Qf3; a possible Bxd4 could be met by ...Qxd4. White instead played Qh5, and ...Nxe2+ Qxe2 exchanged the knight for the other bishop while retaining the extra pawns.

...cxb3 and ...bxa2 produced an advanced pawn. ...Qe6 protected it; ...Qa6 later protected both a2 and the eventual promotion square a1 along the same file. I correctly rejected an immediate promotion after White's Bh6: Rc1 would block the first rank, so ...a1=Q would not give check, and Qxg7 would be mate with Bh6 supporting the queen. The actual ...Qxh6 crossed the open sixth rank, removed that bishop, and answered the threat. After Rf1, ...Qa6 restored the pawn support. White then captured the defended pawn with Qxa2, allowing ...Qxa2 to win its queen. This was a major weaker-setting concession.

I used ...Re2, ...Rxf2 and ...Rxf1 to remove White's last rook and the f-pawn. Against Kh2/Pg2/Ph4, ...h5 blocked the h-pawn and controlled g4. The g2 pawn was pinned on the second rank by Qa2. After Kg3, ...Qf2+ was protected by Rf1. White chose Kh3; ...Rh1# then covered h2/h3, Qf2 covered g3, h5 covered g4, and White's own pawns occupied g2/h4. The referee confirmed mate. The unplayed Kh2 branch after ...Qf2+ would allow ...Qxh4 mate by my own calculation.

Trial observation: no pure pawn ending or actual promotion occurred. The new middlegame position did require checking a promotion's check status and the final rook/queen recapture, which overlaps with the practice target. These were my own counterfactual calculations, not an independently established transfer score or proof that the trial caused the result. Preserve the planned evaluation after game 36. Calculation still spent excessive time on remote alternatives and simple conversion positions. No external sources, automated chess analysis, chess-analysis tools, or delegated advice were used. Observed cumulative active-goal usage: 8,650,287 tokens; not per-game or whole-account usage.


## Game 35 — White, elo-1800-setting, 0–1

Lost by resignation after 69...Rf7+ (138 plies), confirmed by the referee and PGN; no illegal submissions. Overall: 16 wins, 1 draw, 18 losses. The 1800 setting is now 5 wins and 6 losses. The provisional engine-relative Elo is 1770 [1580, 1960] from 23 rated games, excluding 12 maximum-strength games. This is below the trial baseline of 1780 [1590, 1990]; neither that small difference nor the broad overlapping intervals establish a change in underlying strength.

The central exchanges left an extra pawn. I met ...Nxd4 with Nxd4 before taking the bishop, avoiding a proposed line where ...Nxf3+ and the opened d-file would attack the queen. Bxb5 gained a pawn, and Bc6/Be4 retained the central recapture. I rejected an early rook move to b1 after noticing the possible queen-for-two-rooks sequence would end in a back-rank mate, then made h3 before activating both rooks. Qe3 and d5 enabled the rook and queen exchanges. My move-27 comment called e5 passed too early: Black's f7 pawn still controlled e6. I noticed that error before the queen exchange; the review corrects the recorded comment rather than silently repeating it.

In the rook ending I brought the king through e2/d2/d3/d4/e4/e5/f5, supported e6, and recaptured after ...fxe6+. Several possible rook trades were examined as pawn endings; Black declined them. Those were my own unverified calculations, not established winning endings. Re5, Rxg5+ and Rxa5 eventually left White with a rook and two pawns against a rook. The a-pawn and h-pawn then advanced with rook/king protection. No claim that this position was a forced win has been independently established.

The critical failure was late and elementary. After 64.h7 Re6+ 65.Kf7 Rf6+, I correctly noticed that Kxf6 would stalemate Kh8: Rg7 and Ph7 cover the remaining king squares. I chose 66.Ke7, and Black played ...Rf5. The actual 67.Rg8+ Kxh7 removed the h-pawn that had protected g8 and placed the black king next to the rook. I then played 68.a6, overlooking the immediate ...Kxg8. My planned continuation had implicitly kept the rook alive. A simple rook retreat such as Ra8 was available in my own postgame inspection; that observation is not a best-move or full-ending verdict.

This is a failure to reconstruct the actual board after a forced capture, not an obscure pawn-race issue. I also repeatedly changed assumptions about h7/g8 protection in hypothetical lines and spent excessive time on distant continuations. Catching the stalemate did not make the next position safe. After 69.a7 Rf7+, the rook was protected by Kg8, promotion would not answer check, and a king retreat would permit ...Rxa7. I resigned rather than claiming a promotion that could not legally occur.

Trial observation: no pure pawn ending was actually played, but this new rook-and-pawn ending directly tested the broader final-capture and king-intervention concern. The missed ...Kxg8 is negative transfer evidence: the short pawn-race practice did not make that check reliable in full play. Earlier correct counterfactual counts and the caught stalemate do not erase the decisive error. Finish game 36 as predeclared, then revise or replace the practice method at the evaluation point. No external sources, chess-analysis tools, automated analysis, or delegated advice were used. Observed cumulative active-goal usage: 8,971,681 tokens; not per-game or whole-account usage.


## Game 36 — Black, elo-1800-setting, 1–0

Lost by resignation after 35.Rfd1 (69 plies), confirmed by the referee and PGN; no illegal submissions. Overall: 16 wins, 1 draw, 19 losses. The 1800 setting is 5 wins and 7 losses; skill 0 is 11 wins and 1 loss; maximum strength is 0 wins, 1 draw, 11 losses. The provisional engine-relative Elo is 1740 [1570, 1930] from 24 rated games, excluding 12 maximum-strength games. This completes the predeclared games 31–36 evaluation block.

I developed, castled, exchanged central pawns, and met Ng5/h4 with ...Be6 rather than opening the h-file. After Nxe6 I used ...fxe6: ...Qxe6 would have lost the queen to Bxe6. ...Nxe4 Qxe4 exchanged the other knight, and ...Qf7/...Rad8 activated the major pieces. I recognized that Ba2 pinned e6 to Kg8 and used ...Kh8 before considering an e6 recapture on f5. These correct local observations did not prevent the later decisive error.

...Rf6 and ...Rg6 put pressure on g3; White answered Kg2. After ...a5, White played Bb1. I noticed one consequence: Qxf5 exf5 Bxf5 would lose a pawn. I responded with 25...Qf6, intending to keep e6/e5 and Rg6 defended, but failed to carry the different exchange on g6 through its last capture. The actual 26.Qxg6 Qxg6 27.Bxg6 removed my rook and queen in return for only White's queen. Calling the rook defended by Qf6 was insufficient because Bb1 recaptured that queen. This is another direct failure of exchange accounting after a new bishop line, not a need for a more elaborate attack plan.

...axb4 and ...bxa3 gained two pawns and created a passer protected by Bd6 through c5/b4. After Ra2, I played ...Nb4 to attack the rook. That knight itself blocked Bd6's diagonal to a3. White's Rxa3 therefore won the pawn safely; my intended ...Bxa3 was not legal while Nb4 remained in the way. I recognized the obstruction only after the pawn had been taken and used ...Nd5 to uncover an attack on the rook. ...Be7 then cleared the d-file, letting Rd8 join e6 in defending Nd5.

I advanced the remaining b-pawn and recaptured Bxd5 with ...exd5. White doubled rooks with Rfd1. The final material was Black Rd8/Be7 and five pawns against two white rooks, Bc1 and four pawns. The advanced a-pawn counterplay was gone, and the doubled rooks pressured d5. I resigned the rook-for-pawn deficit; I have not engine-certified the exact preceding position or a forced mate.

Trial observation: no pure pawn ending occurred. The decisive g6 sequence is nevertheless another recurrence of the broader final-capture concern, and ...Nb4 supplies a separate blocker error. The short pawn-race practice did not make those checks reliable. Analysis remained too long and repeatedly contradicted elementary occupancy and recapture facts. No external sources, automated chess analysis, chess-analysis tools, or delegated advice were used. Observed cumulative active-goal usage after the game: 9,181,135 tokens; not per-game or whole-account usage. Trial 01 is evaluated in its own record; carry out the replacement practice before starting game 37.


## Between games 36 and 37 — replacement practice trial 02

Completed eight short exchange/blocker reconstructions and eleven explicitly supplied legality branches. Four positions were remembered and four were self-composed contrasts with known mechanisms, not an independent test. All supplied legality predictions matched, including the final king capture, blocked bishop ray, bishop recapture and stalemate contrast. The full plan, per-ply inventories, limits and results are in `workspace/trials/exchange-reconstruction-02.md`. Practice finished by 21:58:52 UTC on 2026-09-30. No improvement claim follows from these easy, known examples. Apply the explicit current-position inventory before expanding a tactical branch, then evaluate new-game transfer in the unchanged games 37–42 rotation. Observed cumulative active-goal usage including practice: 9,213,891 tokens.

## Game 37 — White, maximum strength, loss

Completed 2026-09-30 at 22:27:01 UTC; resigned after 27...Rxh8 (54 plies), zero illegal submissions. The recorded PGN is `data/games/000037.pgn.gz`. Record now 16 wins, one draw, 20 losses. The provisional engine-relative estimate remains 1740 [1570, 1930]; this maximum-strength game is excluded from that fixed estimator.

The Nimzo-Indian central and minor-piece exchanges were materially accounted for correctly through 20.dxe5: both sides retained one queen, one rook, one bishop and six pawns. This is an accounting observation, not a claim of equal evaluation or best opening play.

Actual failure: after 22...Qd2, I chose 23.b3 to remove the b2 target and missed 23...Be2. The bishop on e2 interrupted Qe4's defense of Re1 while Qd2 continued attacking that rook. I then correctly rejected the immediate bishop captures on back-rank grounds. My manually calculated illustrative line was 24.Rxe2 Rc1+ 25.Re1 Qxe1+ 26.Qxe1 Rxe1#; this was not played or mechanically checked. That catch came after the damaging position had already arisen.

A second actual failure followed: 24.Qh7+ Kf8 25.Qh8+ Ke7 26.h3 Qxe1+ 27.Kh2 Rxh8. I considered Qh8 as attacking Rc8 but omitted the rook's reciprocal capture of the queen. Once the king left f8, the entire c8-d8-e8-f8-g8-h8 rank was clear. My reasoning carried the king's former blocking effect forward and failed to inspect the actual queen's immediate exposure. Black first took the rook with check, then the queen. Final White inventory was Kh2/Bb1 and six pawns, against Black Ke7/Qe1/Rh8/Be2 and six pawns; resignation followed. No forced-mate claim is needed for that material conclusion.

Trial 02 transfer: failed its no-recurrence criterion in the first measured game. Correct early exchange bookkeeping and a later rejected capture do not offset the actual defender interruption and newly opened rook ray missed in play. Complete the predeclared games 37–42 block, then revise the method as promised; do not infer improvement from the practice legality score or from this game's long analysis. Keep the selected move's actual final board in view, especially a king vacating a rook ray.

## Game 38 — Black, maximum strength, loss

Completed 2026-09-30 at 22:56:27 UTC; resigned after 35.Rxd7+ (69 plies), zero illegal submissions. PGN: `data/games/000038.pgn.gz`. Total record: 16 wins, one draw, 21 losses. Maximum-strength record: zero wins, one draw, 13 losses. Engine-relative estimate remains 1740 [1570, 1930], based on the unchanged 24 rated weaker-setting games.

The Berlin queen exchange and subsequent ordinary trades were accounted for. One fresh changed-blocker decision was applied correctly: after ...hxg4/hxg4 cleared the h-file, 18...Nh4+ 19.Nxh4 Rxh4 traded the knights evenly because Rh8 now had an unobstructed path to h4. The later central exchanges left an exposed f6-pawn, which White won with 33.Nxf6. I did not establish where the resulting positional disadvantage first became avoidable.

Actual target failure: after 34.Kg5, I played 34...Bd7 and treated Kd8 as sufficient protection for that bishop. White played 35.Rxd7+, with Nf6 protecting d7; ...Kxd7 would therefore be illegal. I also reasoned incorrectly about the alternative Nxd7: Rf7 would protect the capturing knight along f7-e7-d7, so the king would not be a valid recapturer there either. No illegal recapture was submitted. The final actual inventory was Black Kd8/Rh2/Pa7/Pb7/Pc7/Pc6 against White Kg5/Rd7/Nf6/Pa2/Pb2/Pc2/Pf5/Pg4. White was a knight and pawn ahead; I resigned without claiming forced mate.

Before ...Bd7, I correctly noticed that 34.Kg5 had changed a proposed ...Rxc2/Rf8+/...Ke7 line: ...Kxf6 would no longer recover the bishop because Kg5 now protected Nf6. I then failed to apply the same king-capture legality principle to the move I actually selected. Extensive remote branching did not replace that final two-ply check. This is a second played recurrence in trial 02, despite the correct earlier h-file exchange. Complete games 39–42 for the declared evaluation, then revise the method; do not describe these catches or practice results as learning success.

## Game 39 — White, skill 0, win

Completed 2026-09-30 at 23:17:08 UTC with 54.Qd4# (107 plies), zero illegal submissions. Total record: 17 wins, one draw, 21 losses. Skill-0 record: 12 wins and one loss. Provisional engine-relative Elo: 1750 [1570, 1930], with 25 rated games and 14 excluded maximum-strength games. Observed cumulative active-goal usage after this game: 9,600,970 tokens, including earlier games and practice; not per-game or whole-account usage.

The open Sicilian led to a useful fresh exchange decision. After 18.Bxf6 Qc5+ 19.Kh1 Bxf6, the bishop had left e7 and no longer defended d6. The complete 20.Qxd6 Qxd6 21.Rxd6 exchange won that pawn. I then played 22.Rfd1 before ...Ke7, retaining a real rook defender of Rd6 against the adjacent king. Later ...b5 exposed a6 to Rxa6; after 27.Rxc6, Black inserted ...b4 rather than immediately recapturing, and 28.axb4 Nxc6 left me three pawns ahead. I anticipated the subsequent loss of c2 while moving the attacked rook, reducing that margin to two pawns.

The conversion was slow and included repeated rook moves in response to knight attacks. I kept the rook behind the passed b-pawn and advanced it to b7. I rejected Rb6 while the bishop's e3-d4-c5-b6 ray made that square unsafe, and brought the king to g3 before placing the knight on f2 where ...Bxf2+ could be answered by Kxf2. After 44.Ne5+ Ke7, 45.Nc6+ forked the king, rook and bishop; ...Kd6 46.Nxb8 won the rook. I checked that ...h4+ could be met by Kg4. With Ba7 attacking Nb8, I used Na6 rather than landing beside the king on c6 or d7. Black then allowed Nxb4, promotion and capture of its remaining bishop. The referee confirmed the manually checked final Qd4 mate.

Trial 02 observation: fresh correct defender/ray decisions occurred, with no played recurrence of the targeted error identified in this game. This is limited process evidence against the weakest setting, not proof of improved strength or best play. The already-failed block criterion remains failed because of games 37 and 38. Analysis still branched extensively; finish games 40–42 and revise the method at the declared endpoint. All moves were my own reasoning through the referee; no external chess sources, analysis code or delegated advice were used.

## Game 40 — Black, skill 0, win

Completed 2026-09-30 at 23:29:27 UTC with 33...Qf1# (66 plies), zero illegal submissions. Total record: 18 wins, one draw, 21 losses. Skill-0 record: 13 wins and one loss. Provisional engine-relative Elo: 1750 [1580, 1930], with 26 rated games and 14 excluded maximum-strength games. Observed cumulative active-goal usage: 9,663,915 tokens, including earlier games and practice; not per-game or whole-account usage.

After White's Nf3/g3/c3/d4 setup I developed, castled and played ...e5. The Nxe5/Nxe5/dxe5/Qxe5 sequence exchanged one knight and pawn from each side. ...Ne4 gained a tempo on Rd2. A relevant changed-blocker check arose after ...Be6 and Qc2: my bishop on e6 interrupted Qe7's file defense of Ne4, while White's queen and bishop both attacked e4. I used 19...f5 to supply another pawn defender rather than carrying the old queen defense forward.

After ...g5 and f3, 21...gxh4 captured White's knight. White chose 22.gxh4 instead of taking Ne4, and ...Nf6 preserved the extra knight for a pawn. ...Bd7 met Bb5's attack on Re8. White then allowed ...Bxb5 and tried c4. The concrete 25...dxc4 opened the d-file against Qd3 and also attacked that queen with the pawn. After 26.Qxd8, I selected ...Rxd8 rather than the queen recapture, and completed 27.Rxd8+ Qxd8: my queen, bishop and knight remained against one rook. The full final recapture was counted before selection.

I met Rg1+ with ...Kh8, captured the advanced e-pawn, and moved the attacked queen to d3, where c4 defended it. Rxc5 then allowed ...bxc5 to remove White's last piece. After f4, ...Qf1 covered g1 and g2 while White's own h2-pawn occupied the other escape square; the referee confirmed mate.

Trial observation: another game with relevant correct blocker/exchange accounting and no identified played target recurrence. White supplied substantial material errors, so the win offers little evidence of improved performance against stronger opposition. It does not restore trial 02's failed no-recurrence criterion. Finish the two 1800-setting games, review the complete block, then revise. No external chess sources, automated analysis or delegated advice were used.

## Game 41 — White, elo-1800-setting, win

Completed 2026-10-01 at 00:03:49 UTC with 56.Rh8# (111 plies), zero illegal submissions. Total record: 19 wins, one draw, 21 losses. The 1800-setting record is six wins and seven losses. Provisional engine-relative Elo: 1780 [1610, 1950], with 27 rated games and 14 excluded maximum-strength games. Observed cumulative active-goal usage: 9,820,698 tokens, including all prior games and practice; not per-game or whole-account usage.

Black's Nc6/e6/d6/d5 opening developed into a French-style centre. Bxc6+ doubled its c-pawns, and Na4/Ne5 attacked its advanced rook. Instead of retreating after Ne5, Black played ...Bd7, allowing 15.Nxc6 Bxc6 to win the exchange. I then completed 16.Nxc5 Bd7 17.Nxe6 Bxe6 18.Rxe6, counting the bishop recapture and final rook capture. With Be5 supported by Re6 and the d4-pawn, fxe4 won the remaining knight after ...Bf6. This produced a rook advantage and extra pawns.

Actual target failure: 25.Rd6 overlooked the still-present black c7-pawn. Black's 25...cxd6 captured the rook immediately. I had calculated queen captures, bishop support, and remote checks while omitting the cheapest capture of the selected rook destination. The bishop's protection of d6 did not make exchanging a rook for a pawn sound; moreover, an immediate Bxd6 would have allowed Qxd6. I instead took the loose bishop with 26.Qxe3. This is a third measured recurrence in trial 02, despite several correct short exchanges earlier in the game. The good result cannot cancel it.

After ...Qxa2 I moved the threatened rook to d1. Bf4 then defended Qe3 after ...Qe6. ...Qg4 and ...g5 created a difficult combination of threats to the bishop and rook on the f-file. The actual 30.Qb3+ Kh8 31.Be5+ dxe5 32.Rxf8+ recovered a rook advantage: from h8 the king could not recapture on f8. I have not established that the entire preceding combination was forced against every alternative reply. Qf7+/Qf6+ drove the king to h5; Qf3 pinned the black queen to that king and offered a supported exchange, which Black accepted with ...Qxf3/gxf3.

With queens gone, I captured the passed d-pawn, removed Black's remaining pawns, and brought the king forward. The rook confined the bare king to the back rank. Rh7 was a waiting move; after ...Ka8, Kb6 forced ...Kb8, allowing Rh8 mate. The full game was chosen through my own reasoning and the referee, with no external sources, automated analysis or delegated advice.

Trial decision remains unchanged: finish game 42, then replace the method. The next revision needs to prevent omission of an immediate pawn capture on the actual candidate square; more remote analysis or more successful remembered exercises is insufficient. The rating increase is provisional outcome evidence, not proof of sustained learning or a successful mechanism.

## Game 42 — Black, elo-1800-setting, win

Completed 2026-10-01 at 00:39:25 UTC with 70...Qb4# (140 plies), zero illegal submissions. Total record: 20 wins, one draw, 21 losses. The 1800-setting record is seven wins and seven losses. Provisional engine-relative Elo: 1800 [1630, 1970], with 28 rated games and 14 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,018,086 tokens, including earlier games and practice; not per-game or whole-account usage.

The English move order transposed into a central d4/c4 structure. I developed and castled, accepted an isolated d-pawn, and used ...Ne4, ...Bf5 and the open files. The minor-piece exchanges were counted through their final captures. A relevant rejected pawn grab was ...Nxa3 while Qd3 was blocked by Bc3: Bxe5/Qxe5 would clear c3 and allow Qxa3. I instead addressed the kingside alignment with ...g6 and ...h5, exchanged the bishop pair, and used ...Ne5 followed by ...Nxf3+ when White chose Qb1. The actual ...gxf3 recapture exposed White's king. The later ...d4/exd4/...Rxd4 and queen exchange led to an even-material rook ending.

I used both rooks on the d-file and answered Rxd1 by capturing the other rook on c7, retaining queenside protection. After the single-rook ending began, the king reached e5/d5, ...b6 resolved the queenside tension, and ...Rc6 defended b6 and g6. The concrete 45...fxe4 46.Rd8+ Ke5 47.b5 Rf6 48.Ke2 exf3+ gained the second central pawn. ...Rf6 had also pinned f3 before the white king moved. These were fresh correct capture and king-square checks.

The conversion still exposed a process failure. I selected 50...Re6 with an intended ...Re2+ continuation, overlooking my own king on e4 blocking that file. After 51.Rf7 I also initially treated Ke4 as sufficient protection of f3; White's Kf2 would make ...Kxf3 illegal after Rxf3. Both facts were caught before an illegal submission, but after the rook relocation based on that faulty plan. I have not established that 50...Re6 itself objectively loses the winning advantage. This is an invalid played plan, not an engine-certified tactical blunder, and it is another reason not to claim reliable transfer.

I then deliberately chose 51...Re5, anticipating Rxf3 and the pin ...Rf5. The actual 52.Rxf3 Rf5 53.Rxf5 Kxf5 left three black pawns against two white pawns with an active king. White's 54.Kg2 allowed ...Kg4 and ...Kxh4; the supported kingside pawns advanced and the h-pawn promoted. I kept legal king escapes until the final supported Qb4 mate. All moves and endgame assessments were my own; no engine analysis, external chess sources, automated tactical analysis or delegated advice were used.

Trial 02 ends at 4 wins and 2 losses: both maximum-strength games lost, both skill-0 games won, both 1800-setting games won. The estimate rose by 60 points from 1740 [1570, 1930] to 1800 [1630, 1970]. Those intervals overlap substantially, and this small block does not establish sustained improvement or causation. The predeclared no-recurrence criterion failed in games 37, 38 and 41, with the additional invalid conversion plan in game 42. Replace the method before game 43; do not treat the four wins as a reason to repeat it unchanged.

## Between games 42 and 43 — replacement practice trial 03

Completed six destination-capture exercises and ten explicitly supplied legality branches, by 00:46:32 UTC on 2026-10-01. Two positions were remembered; four were self-composed contrasts with known mechanisms. All 30 supplied legal plies and two deliberately illegal replies matched the manual predictions. The examples distinguished both pawn-capture origins, a rook route blocked by its own king, and a king capture prohibited by the opposing king. This is practice correctness, not independently measured chess improvement.

The change for play is a small audit immediately before submitting a selected rook/queen move or capture: identify the landing square, inspect both enemy pawn origins on the actual board, then test the relevant final recapture. It replaces broad branching at that final step; no new general checklist is being added. The complete plan and results are in `workspace/trials/destination-capture-03.md`. Benchmark games 43–48 will test transfer under the unchanged rotation, starting from 1800 [1630, 1970]. Observed cumulative active-goal usage including practice: 10,052,289 tokens.

## Game 43 — White, maximum strength, loss

Completed 2026-10-01 at 01:05:27 UTC by resignation after 24...b4 (48 plies), zero illegal submissions. Total record: 20 wins, one draw, 22 losses. Maximum-strength record: zero wins, one draw, 14 losses. The fixed engine-relative estimate remains 1800 [1630, 1970], with 28 rated games and 15 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,138,006 tokens.

I chose the Berlin queen exchange, counted Bxc6/dxc6, dxe5, and Qxd8+/Kxd8 correctly, and developed Bf4 and both rooks. a3/Bxc3/bxc3 left both sides with doubled c-pawns. Black used ...c5, ...Ne7 and ...Nd5 to target the bishop and c3. My 16.Rd3 plan defended c3 initially, but I had not kept its intended retreat viable after the knight moved. The actual 17.Bh2 c4 attacked the rook. The new final audit rejected Re3 because Nd5 now attacked e3, and rejected Rd3 as a retreat later because the black c4-pawn attacked d3. I chose 18.Rd4 knowing ...Nxc3 could win a pawn; that is a conscious concession after an inadequate earlier plan, not prevention of the pawn loss.

After Re3/Nd5/Ree4, Black supported the c-pawn with ...b5. My a4 was met by the other c-pawn's ...c5, again attacking Rd4. Decisive actual error: 22.Rd1 checked the immediate destination captures but omitted ...Nc3, which forked Rd1 and Re4. I had considered a different knight jump while missing the one that attacked both rooks. The response 23.Rde1 Nxe4 24.Rxe4 arranged a legal recapture, limiting the loss to the exchange. After ...b4, Black had two rooks, bishop and seven pawns against my rook, bishop, knight and six pawns, with advancing connected queenside pawns. I resigned that position without claiming an engine-certified evaluation or forced mate.

Trial 03 observation: the pawn-origin audit was applied to the selected major-piece moves and captures, and it caught unsafe rook destinations before submission. I did not identify a newly played immediate pawn-capture omission or illegal assumed recapture in this game. Nevertheless, the method did not prevent a damaging plan followed by a knight fork. These are material limits on its value; do not turn the narrower successful checks into a claim of stronger play. Preserve the declared games 43–48 evaluation block, log this failure alongside the catches, and assess both outcomes and broader tactical errors at its endpoint. All move decisions were my own reasoning through the referee, without external advice or automated chess analysis.

## Game 44 — Black, maximum strength, loss

Completed 2026-10-01 at 01:18:26 UTC by 20.Nf6# (39 plies), zero illegal submissions. The recorded PGN confirms the mating move. Total record: 20 wins, one draw, 23 losses. Maximum-strength record: zero wins, one draw, 15 losses. The fixed estimate remains 1800 [1630, 1970], with 28 rated games and 16 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,194,508 tokens.

I used the Berlin again, with Black this time, and completed the ordinary pawn and queen recaptures correctly. White chose h3/g4 rather than the previous game's Bf4. ...Bc4 met Nd4 with an attack on Rf1; ...Nd5 and ...Be7 developed the other pieces. b3/c4 drove Ba6 and Nb6. After Nf5, ...g6 allowed the bishop exchange Nxe7/Kxe7, whose actual king capture was legal.

Decisive error: after 19.Ba3+, I chose 19...Ke8 without checking White's immediate Nf6 reply. The resulting 20.Nf6 was mate. Rd1 controlled d7 and d8; Ba3 controlled e7 and f8; f7 was occupied by my own pawn. No black piece could capture Nf6, and a knight check cannot be blocked. The issue was not legality of Ke8 or the earlier king recapture: I failed to test the opponent's next check and all escape squares. Long speculative analysis of other continuations did not perform that basic check.

Trial 03 observation: the narrow destination/pawn-origin checks do not establish successful execution of the whole move protocol. The ordinary reply-check scan, which the trial retained for all moves, was not applied adequately here. Together with game 43's fork, this is direct evidence that the current process remains unreliable. Keep the declared endpoint after game 48, but perform a short reconstruction of this exact mate before game 45 and record it as additional practice within the block. Any later outcome cannot be attributed solely to the original six exercises. No outside advice, engine analysis or automated move selection was used.

The supplemental reconstruction was completed by 01:21:39 UTC. Mechanical checks of the four supplied legal plies and six deliberately illegal responses matched the prior manual account. The Ke6 contrast established only that the same Nf6 move would not check that king, not that every alternative continuation was solved. The existing requirement to scan immediate opponent checks remains part of the actual pre-submission work for game 45 onward; do not substitute another long analysis or a legal king destination for it.

## Game 45 — White, skill 0, win

Completed 2026-10-01 at 01:51:00 UTC with 49.Nf4# (97 plies), zero illegal submissions. Total record: 21 wins, one draw, 23 losses. Skill-0 record: 14 wins and one loss. Provisional engine-relative Elo remains 1800, now [1640, 1970], with 29 rated games and 16 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,354,535 tokens, including prior games and practice; not per-game usage.

Black's early kingside pawn advances and ...Nfg4 attacked my bishop. Bf4/Bxe5 removed one knight, then f4/gxf4/Rxf4 opened the f-file. After ...Rg8, Kh1 removed the g-file pin. I answered the combined ...Qg5 rook attack and Qxg2 mating threat with Rf2, rejecting Qf3 because Ne5 could capture the queen. Re2 met the next queen attack while retaining coverage of g2. Qf1/Qxf4/Bxf4 exchanged queens, and Rf1, Nf5, Rd1 and Red2 coordinated the pieces against d6.

Relevant exchange reconstruction: 24.Nxd6 could be answered by either bishop or rook capture, with the two white rooks completing the recaptures. Starting with the knight avoided leaving Nf5 available to ...Bxf5 during a rook-first exchange. Black instead allowed Nxd6 and Nxb7, then delayed recapturing Bxc4 with ...Ra7. The actual Nd6/Bxd6/Rxd6/Rxd6/Rxd6 sequence left my rook active. After ...Ke7, 31.Rd4 saved the attacked rook and protected Bc4. I rejected Rxc6 because Ne5 attacked c6, and Rd5 because the c6-pawn attacked d5. Black's further failure to recapture the bishop allowed an extra piece to survive the rook exchange.

The king reached d4 and legally recaptured ...Nxc4 with Kxc4: no black pawn or king supported c4. With an extra knight, I removed c6 and converted ...f5 into a passed f-pawn through exf5. Ke6 supported its advance. At f7, I rejected Kf6 as stalemate in my manual reconstruction, since both black pawns were blocked, and used Nd5 to leave ...Kg7 available. Ke7 then protected the promotion square before f8=Q. Qf6+/Kh5/Nf4 produced the referee-confirmed mate; h3 covered the otherwise available g4 escape.

Trial observation: the selected major-piece/capture audits and immediate-check scans were applied, with several fresh catches before submission and no identified played target recurrence. This is limited process evidence, not an independently verified blunder-free game. Black supplied substantial material errors, and a win against the opponent already beaten in 13 of 14 previous games does not establish improved strength. Trial 03 is now one win and two losses, with three games remaining before the declared endpoint. Continue with Black against skill 0, then both 1800-setting games. All decisions used my own reasoning, pre-existing notes and the referee; no external chess advice, automated analysis or delegated moves.

## Game 46 — Black, skill 0, win

Completed 2026-10-01 at 02:25:40 UTC with 39...Be4# (78 plies), zero illegal submissions. Total record: 22 wins, one draw, 23 losses. Skill-0 record: 15 wins and one loss. Provisional engine-relative Elo remains 1800, with interval [1640, 1980], 30 rated games and 16 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,517,644 tokens.

Against d4/c3/Bf4, I challenged the centre with ...c5, developed, and used ...Ng4/...Be7 before returning the knight to f6. Bxf6/Bxf6 preserved the pawn structure, and ...Qe7/...Qxc5 recovered the pawn. After ...e5, b4 drove the queen back to e7. Nb3 then cleared White's d-file, and ...Be6 defended d5. Clarification of my earlier threat description: before Nb3, White's Nd2 itself blocked Rxd5. The queen retreat left d5 without a direct defender, but that does not establish that White could immediately capture it on move 17.

...e4 attacked Nf3; after Nd4, ...Nxd4/exd4 exchanged knights and ...Bf5 preserved the bishop. I rejected the earlier Bf5 idea when Qc2 could simply capture it; the actual move was made only after e4 blocked that queen ray. ...b6 drove the remaining knight to a4. The rooks were connected, ...Bg5 attacked Qd2, and ...Bg6 prepared ...e3 while putting the bishop under pawn protection. After Qa2/e3/f4, ...Bh4 preserved the supported ...Bf2+ entry. The actual f5/Bf2+/Kh2/Bxf5 sequence removed the f-pawn: Bf2 blocked Rf1's route to f5. This was a fresh correct blocker/check reconstruction, reached after excessively long analysis rather than a consistently efficient process.

Bd3 allowed ...Bxd3. White chose Rxf2, and ...exf2 removed the rook; Ra1 then allowed the protected ...f1=Q. With ...Qee2, the original queen supported the promotion square while Bd3 supported e2. Rxf1/Qxf1 removed White's last rook. Against Nb7 I rejected ...Re8 because Nd6 would fork Rc8 and Re8, choosing ...Rd7 instead. White then gave up its queen with Qxd5/Rxd5 and its knight with Nd6/Rxd6. The final ...Qf4+/g3/...Qf2+/Kh1/...Be4 was confirmed as mate by the referee.

Trial observation: the major-piece/capture audits caught relevant pawn, knight, blocker and recapture issues before submission; no played immediate-capture or invalid-recapture recurrence was identified. The avoided ...Re8/Nd6 fork also exercised the existing broader fork check. These are limited self-assessed process observations. Opponent errors, especially the passed-pawn response and Qxd5, were substantial; the win and unchanged point estimate do not establish stronger play. The block stands at two wins and two losses, with both 1800-setting games still to play. Preserve the game-48 evaluation endpoint. All play used my own reasoning and the referee, without external chess advice, automated analysis or delegated moves.

## Game 47 — White, elo-1800-setting, loss

Completed 2026-10-01 at 02:53:43 UTC by resignation after 41...Nxh2 (82 plies), with one illegal submission. Total record: 22 wins, one draw, 24 losses. The 1800-setting record is seven wins and eight losses. Provisional engine-relative Elo fell to 1780 [1630, 1950], with 31 rated games and 16 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,739,469 tokens, including prior games and practice.

The Nc6/Nf6/e6 opening led to a bishop pair and a broad centre after Bxc3+/bxc3. I defended e4 with Bd3, advanced e5, castled, and challenged d5 with c4. After c3, the later ...b5/...b4 allowed cxb4; Black chose ...Nce7 instead of the central capture examined in my reasoning. Bxa6 gained another pawn. Bb2 and a3 then supported the centre and queenside. These captures included actual pawn-origin and recapture checks; their success did not establish that the resulting position was safe.

The king attack exposed repeated limits in the broader procedure. Against ...Nf4 I used Qd1, which retained protection of Nf3, and accepted ...Nxg2 with Kxg2. I had spent extensive reasoning on a later Bxf3/Qxf3/Nh4 fork while failing to account fully for the immediate ...Nh4+ and the pin of Nf3 to Kg2. Kf1/Nxf3/Re3 saved the rook, but the knight sacrifice had traded off my knight and exposed the king. Later 33.Ree1 omitted ...Qc4+ in its check scan. Re2/Qb3 attacked Ba3 and Rd1 together; Ra1 addressed those immediate captures but allowed ...Qxh3+/Ke1/...Qh1+/Kd2. I initially described the resulting rook skewer as if a loss was imminent. Black actually played ...Qd5, not ...Qxa1, and the rook remained on a1. No rook loss should be recorded for that line.

Decisive failure: after ...Rg4/Qh2/...Nxd4, I selected 40.Re3 expecting to answer ...Nf3+ with Rxf3. Moving Nd4 to f3 also opened the d5-d4-d3-d2 queen ray onto my king. The position was double check. My attempted 41.Rxf3 was illegal because it removed only the knight checker; the referee rejected it as attempt one. I then played 41.Kc2 legally, Black captured the queen with ...Nxh2, and I resigned a full queen down. This was an invalid defensive capture assumed in the preceding played plan, followed by an actual illegal submission. The earlier long branch analysis did not substitute for reconstructing the two checking lines on the actual board.

Trial 03 has therefore failed its no-recurrence requirement. The destination audit was frequently applied and caught several unsafe candidates, but it did not prevent this invalid planned capture or the broader king-safety failures. The block now stands at two wins and three losses; the estimate is below its 1800 starting point. Finish the declared paired-color block with game 48, then replace the method at the endpoint. Before that game, reconstruct this exact double check and a small number of explicit contrasts, recording them as additional known-example practice rather than a new strength test. All measured play used my own reasoning and the referee; no outside advice, automated chess analysis or delegated move selection was used.

The short double-check supplement was completed and inspected by 02:57:34 UTC. Four supplied branches covered the remembered rejected capture, the actual king escape and queen loss, an added d3 pawn blocking the queen ray, and a static Kc2 contrast. Seven legal plies and one deliberately illegal capture matched the prior manual predictions; all four initial boards were valid. The mechanical check supplied only legality, check status and board occupancy. The successful known examples do not change the failed trial assessment. Game 48 will retain the declared endpoint and apply the existing requirement to reconstruct all checking lines before attempting a capture or interposition.

## Game 48 — Black, elo-1800-setting, loss

Completed 2026-10-01 at 03:06:28 UTC by resignation after 17.Qb5 (33 plies), zero illegal submissions. Total record: 22 wins, one draw, 25 losses. The 1800-setting record is seven wins and nine losses. Provisional engine-relative Elo is 1770 [1610, 1920], with 32 rated games and 16 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,805,808 tokens.

Against e4/Nc3/f4, I answered with ...e5/...Nf6/...d5 and ...Nxe4. ...Nc6 and ...Be7 allowed ordinary castling. d3 drove the knight to capture c3; after bxc3, ...Bg4 and ...f6 challenged the centre. The actual ...Bxf3/Bxf3/...fxe5 removed the knight defender, gained the central pawn, and left Nc6 able to answer Bxe5. I checked the pawn and bishop recaptures and the available Bxd5+ response. ...Qd6 and ...Rad8 then coordinated the central pieces while e5 blocked the diagonal from Bg3 to Qd6.

Decisive error: after 15.d4, I played 15...exd4. This cleared e5 and exposed Qd6 along Bg3-f4-e5-d6. White immediately played 16.Bxd6 and took the queen. I had calculated the optional cxd4/Nxd4 fork and several checks while omitting the immediate bishop capture of the queen. The landing-square audit of d4 did not inspect the line opened by vacating e5. 16...Rxd6 recaptured the bishop legally, and 17.Qb5 followed. I resigned with two rooks, bishop, knight and seven pawns against queen, two rooks, bishop and five pawns. This was my assessment of a materially losing position, not an engine-certified forced loss or mate.

Trial 03 ends at two wins and four losses: both maximum-strength games lost, both skill-0 games won, both 1800-setting games lost. The estimate fell 30 points, from 1800 [1630, 1970] to 1770 [1610, 1920]. Across the three focused trials, the endpoint estimates have been 1740, 1800 and 1770, versus 1780 before the first trial. Their broad overlapping intervals and the recurring tactical failures do not establish sustained improvement. The trial failed through game 47's invalid defensive capture and game 48's exposed queen, in addition to the earlier missed fork and mate. Successful remembered exercises and numerous correct local audits do not offset these failures.

Decision: replace the destination-only execution change with a compact reconstruction of the selected move's resulting board, starting with the lines opened by its vacated square and the safety of the king and queen. Preserve the longer old protocol as reference rather than enlarging it. Practise eight known or self-composed positions with explicitly supplied moves, then evaluate games 49–54. The new trial file records the method, its limits and its baseline before the next benchmark game. All measured move decisions were my own; no external advice, engine analysis, automated move selection or delegated chess work was used.

## Between games 48 and 49 — replacement practice trial 04

Completed eight known or self-composed positions in ten supplied branches by 03:13:51 UTC, within six minutes and 39 seconds of the planning reference time, including review and file work. All 24 supplied legal plies and both deliberately illegal moves matched the prior manual predictions. The examples rehearsed clearing an origin square, retaining a different blocker, counting both checks, and distinguishing a legal recapture from restoration of the captured queen's value. These are known-example results, not an independent test of chess ability.

The execution change reconstructs the actual candidate's resulting board before remote continuation analysis, with priority to newly opened lines toward king and queen. It applies to quiet moves and pawn moves too. `workspace/move-check.md` is now a short three-step procedure; its previous longer version is preserved as `workspace/trials/move-check-before-04.md`. The complete plan and limitations are in `workspace/trials/vacated-lines-04.md`. Games 49–54 test transfer from the fixed 1770 [1610, 1920] baseline. Sustained Elo improvement remains unestablished.

## Game 49 — White, maximum strength, loss

Completed 2026-10-01 at 03:32:07 UTC by resignation after 19...Rxd3+ (38 plies), zero illegal submissions. Total record: 22 wins, one draw, 26 losses. Maximum-strength record: zero wins, one draw, 16 losses. The fixed estimate remains 1770 [1610, 1920], with 32 rated games and 17 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 10,916,610 tokens.

I chose d4/c4 and reached the central exchanges cxd5/cxd4/Nxd4/Nxd5, then e4/Nxc3/bxc3/e5. Before 9.Nf3, I explicitly reconstructed the newly cleared d-file and accepted Qxd1+/Kxd1 as a legal queen exchange. The king recapture was checked against the actual bishops, knight and pawn attacks. Be3 and Bd3 developed the bishops; Bc4 was rejected because Be6 could capture it. Kc2 connected the rooks. Bxc5/Nxc5 exchanged one bishop pair, followed by Rad1, Black's long castling and Rhe1.

The setup failed to preserve the queenside defense. Moving Ra1 away left a2 available to Be6, and I did not deal with ...Bxa2 before it happened. That capture also removed the pawn which had controlled b3. The resulting ...Bb3+ would attack Kc2 and then Rd1 once the king left c2. Bd3 simultaneously depended on the d-file rook and a usable king recapture against the coordinated Rd8/Nc5 pressure. Long analysis after the pawn loss identified these constraints but did not recover a satisfactory defense.

I played 17.Re3 to add a defender to Bd3, then answered the actual ...Bb3+ with 18.Kd2. This was a single bishop check, and the king move was legal. ...Bxd1/19.Kxd1 exchanged my rook for that bishop. I recognized before Kxd1 that the king's new d1 position could no longer provide a final capture on d3. Black then played 19...Rxd3+, taking the remaining bishop. Rxd3 could remove that checking rook, but ...Nxd3 would remove my last rook and Kd1 could not recapture a knight two ranks away. I resigned with rook, knight and five pawns against two rooks, knight and six pawns, without claiming a forced mate or an engine evaluation.

Trial 04 observation: the short reconstruction correctly handled the initial queen exchange, a rejected bishop destination and the actual check responses. It did not prevent the earlier loss of a defender and the king/rook alignment which produced the skewer. The opened-line loss is a recurrence for the trial's broader condition, even though the skewer was recognized after ...Bxa2 and no illegal response was submitted. The method therefore already needs revision at the declared endpoint; do not call the useful local checks a successful trial or an Elo gain. Continue the remaining games 50–54 to complete the predeclared paired-color evaluation, preserving this failure. Reasoning was again excessively long and did not establish improved efficiency. All decisions used only my own reasoning, pre-existing notes and the referee.

## Game 50 — Black, maximum strength, loss

Completed 2026-10-01 at 03:53:10 UTC by resignation after 38.Bxe5 (75 plies), zero illegal submissions. Total record: 22 wins, one draw, 27 losses. Maximum-strength record: zero wins, one draw, 17 losses. The fixed estimate remains 1770 [1610, 1920], with 32 rated games and 18 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 11,044,688 tokens.

The Ruy Lopez developed through ...Bb7, ...Re8, ...Bf8, ...h6 and the central exchange ...exd4/cxd4. I reconstructed the lines opened by ...Nb4 and ...c5/...c4 without exposing the king or queen. ...Nd3/Bxd3/...cxd3 exchanged a knight for a bishop; the actual Bd2 initially blocked Qd1 from taking the new d3 pawn. ...Nc5 supported that pawn, but b4 drove the knight away after the a-file rook exchange. ...Ne5/Nxe5/...dxe5/Qxd3 then cost the advanced pawn. These legal local exchanges did not establish a sound overall plan.

Decisive failure in my assessment: after ...Qa3/Ra1/...Qb3/Ne2, I treated 28...Bxb4 as a safe recovery of the pawn. I checked the bishop recapture and queen alignment but omitted 29.Rb1, which attacked Qb3 along the b-file. The queen was both shielding and defending Bb4; moving it changed the rook's access to that bishop. White's new Ne2 also meant ...Qxc3 could not force the queen exchange I wanted, since Nxc3 was available. I chose 29...Qc4, and the actual continuation 30.Qxc4 bxc4 31.Bxb4 left me a full minor piece down. White captured with the bishop, not the rook. I have not established that the chosen defense was forced or best.

A second reconstruction failure appeared in the recovery analysis: I repeatedly considered ...Rxe4 after the queen exchange without retaining my own e5 pawn as a blocker between Re8 and e4. I caught that before submitting it and played ...Rc8 instead. No illegal rook move was attempted, but the earlier plan relied on an unavailable capture. This repeats the old blocked-route weakness despite correct checks on several actual moves.

I continued with ...Rc8, ...Ba6, ...f6 and ...Re8 while White blockaded c4 with Nc3. ...fxe5 was a legal pawn recapture, with Re8 supporting the resulting e5 pawn. Against Rb8, ...Kf7 allowed the legal Rxe8/Kxe8 exchange; the white bishop on d6 did not attack e8. White then took e5. I resigned with bishop and three pawns against bishop, knight and four pawns, and a blockaded c-pawn. This was my own material and practical assessment, not a certified forced loss or engine evaluation.

Trial 04 now has two losses. It remains failed on its predeclared recurrence condition from game 49; game 50 adds a missed rook attack on a queen shielding another piece and an invalid assumed rook route. The correct opening reconstructions and legal king recapture do not establish stronger play. Continue the remaining fixed games 51–54 and revise at the endpoint. All measured decisions used my own reasoning, existing notes and the referee, without external advice, automated analysis or delegation.

## Game 51 — White, skill 0, win

Completed 2026-10-01 at 04:05:20 UTC by 28.Qe7# (55 plies), zero illegal submissions. Total record: 23 wins, one draw, 27 losses. Skill-0 record: 16 wins and one loss. Provisional engine-relative Elo is 1770 [1620, 1930], with 33 rated games and 18 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 11,112,833 tokens.

After e4/Nc6/d4/e5/Nf3/Nxd4/Nxd4, Black played ...Bc5 instead of recapturing the knight. Nb3 attacked that bishop; ...Bxf2+ allowed a legal Kxf2. I explicitly checked the destination against Black's actual queen, bishop, knight and pawns. Qf3 blocked ...Qf6+, and Be3 blocked ...Qb6+. Black then gave up the queen with ...Qxe3+, answered by Qxe3. This early opponent error gave a very large advantage and limits what the subsequent conversion can demonstrate.

Before routine development, I identified ...Ng4+ from Nh6 as a possible fork of Kf2 and Qe3. 10.h3 supplied a pawn capture on g4. Nc3, Kg1, Bc4 and Rd1 developed the pieces; ...Nf5 instead put the remaining black knight under the e4 pawn, and exf5 captured it. Kh2 and Rhf1 connected and activated the rooks. A mistyped working-directory path initially prevented the Nc3 command process from starting; the corrected command was accepted once. This was not a rejected chess move or a referee fault.

Qxe5 and Qxd6 removed undefended central pawns. When ...Be6 cleared c8, I noticed that Ra8 could now recapture on f8 and did not use the previously considered Qxf8 route. Instead fxe6 removed the bishop. After ...b5 attacked Bc4, Bd5 both saved the bishop and attacked Ra8 through the newly vacant b7 square. e7, ...Rfe8, Bxa8/Rxa8 and Qd8+ simplified with actual support from the e7 pawn and Rd1. Black chose ...Kh7, and Qxa8 removed the last rook. The pawn promoted, then Qee4+ compelled the pawn block ...g6; Qe7 was mate. Qa8 controlled g8/h8, the checking queen controlled g7, and Black's own g6/h6 pawns occupied the other king escapes. The referee confirmed checkmate.

Trial 04 observation: this game supplied correct fresh checks of king-capture legality, a knight fork, a newly opened rook recapture route, and the final checking net. I did not identify a newly played recurrence of the targeted line failure in this game. These local successes do not reverse the trial's already failed condition or establish an Elo gain. The point estimate stayed at 1770, and this win followed major skill-0 blunders. The block stands at one win and two losses. Continue games 52–54 without additional practice or a changed endpoint. All measured decisions remained my own reasoning through the referee, with no outside advice or automated analysis.

## Game 52 — Black, skill 0, win

Completed 2026-10-01 at 05:21:51 UTC with 88...Re1# (176 plies), zero illegal submissions. Total record: 24 wins, one draw, 27 losses. Skill-0 record: 17 wins and one loss. Provisional engine-relative Elo remains 1770 [1620, 1930], with 34 rated games and 18 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 11,462,083 tokens; this includes earlier games and practice, not just this game.

The opening already contained an inadequate defender update. After b5 attacked Nc6, 14...Na5 saved that knight but removed its defense of e5. Nxe5 forked Qd7, and Bxf4 subsequently removed the knight whose pawn defender had disappeared. The actual ...g5/Nxf5/...Rxf5/Bg3/...Rxe5+/Bxe5/...Qxe5+ reduced the material deficit. Later ...g3/fxg3/...Bxg3 attacked Re1, and ...Bxe1/Qxe1 recovered the exchange. These recoveries do not validate the opening plan.

The major repeat failure came after the queen exchange: 36...Nxd3 assumed that, following Rxd3, ...Rxd5 would recover Bd5 because my own d4 pawn blocked White's rook from recapturing. I had omitted White's c4 pawn, which could capture a rook on d5. I recognized that only after playing Nxd3 and seeing Rxd3. I did not submit the losing Rxd5, but the played knight sacrifice had already relied on that invalid compensation. This is a failed exchange reconstruction despite correct recognition of the d4 blocker. White retained an extra bishop.

The endgame recovery used an active king and the passed d-pawn. I captured h5, g4, c4 and a4 while keeping d2 defended, then survived the rook and bishop checks. At move 63 I rejected Kxc4 because Be2 would pin and attack Rd3 while White's king on e4 prevented the intended king recapture; ...Rd4+ first displaced that king. I also retained the distinction between a pinned bishop and its attacks when considering king destinations. Later ...Rd8 attacked the bishop and covered its checking squares, allowing ...Kc6, ...b5 and ...c4. The pawns reached b3/c3/d2 with king support. I rejected ...Rc8 when Bf5 attacked c8, and did not push c2 while the bishop and king could defeat a king-only recapture plan.

The final ...b3 gave a pawn recapture on c2. Since c3 already protected d2, 87...Re8 could leave the d-file and threaten Re1 mate. White answered Bb1. The actual 88...Re1 was mate: d2 protected e1 and controlled c1, Kb2 controlled c1/c2, c3 protected d2, and the rook covered e2. The referee confirmed the result. This was a long recovery against skill 0, not evidence that the earlier mistakes were harmless or that all alternative defenses were solved.

Trial 04 remains failed. The fresh endgame catches and successful mating net are limited process evidence; the lost defender and unsupported sacrifice show continuing unreliability, and the point estimate did not rise. The block is two wins and two losses. Complete the two scheduled 1800-setting games, then revise the method at the declared game-54 endpoint. All moves were my own reasoning through the referee, without external chess advice, automated analysis or delegation.

## Game 53 — White, elo-1800-setting, loss

Completed 2026-10-01 at 06:03:02 UTC by resignation after 43...Bxa7 (86 plies), zero illegal submissions. Total record: 24 wins, one draw, 28 losses. The 1800-setting record is seven wins and ten losses. Provisional engine-relative Elo fell to 1760 [1610, 1910], with 35 rated games and 18 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 11,635,651 tokens.

The Sicilian centre exchange led to ordinary development and castling. Bxe6/fxe6 changed Black's pawn structure. After f4/exf4/Bxf4, ...Qb6+ used the newly open diagonal; Be3 blocked it and attacked the queen. Kh1 later left that checking line. Against ...Ng4, h3 retained Be3's support of f2, while Qxe3 was available against Nxe3. Black retreated. After ...d5, the actual exd5/exd5/Nxd5 gained a pawn. When Black chose ...Rae8 rather than exchanging knights, I removed Nf6 before trying Qd5+: otherwise that knight would still attack a rook recapturing on d5. Qe6/Qxe6+/Rxe6 completed the queen exchange.

I retained the extra pawn through b3, a4 and rook activity on the seventh rank. Rxb7 and ...Rxc2 exchanged pawns. g3 added pawn support to Bf4, allowing Rd1 to free f1 as a king escape. I rejected gxh4 while it would abandon the bishop to Re4, choosing Bd6 first. After the kingside pawn exchange, ...Re3 drove the bishop away from g3 and exposed h3. Rxa7 recovered another pawn before ...Rxh3+. Kg1 left the corner. The remaining a4/b5 pawns were connected passers, but Black's rooks occupied the second rank and restricted my king.

Decisive recurrence: 42.Bf4 answered the rook attack on Be3 but cleared e3 from the d4-e3-f2-g1 checking diagonal and abandoned the bishop's a7 support. I omitted 42...Bd4+, which checked Kg1 and attacked Ra7 through c5/b6. My later reconstruction rejected Rxd4 because ...Re1 would mate: moving Rd1 removed the first-rank defender while the other black rook controlled the second rank. That mating branch was my own analysis, not a played or referee-certified result. I chose 43.Kf1, and the actual ...Bxa7 captured the rook. I resigned with rook, bishop and two pawns against two rooks, bishop and one pawn, with an exposed king. This was a practical material assessment, not an engine-certified forced loss.

The bishop retreat therefore repeated precisely the changed-line and next-check failure under study. Earlier correct pawn, knight and recapture checks did not prevent it. Analysis was again excessively long without reliably completing the short forcing-reply scan. Trial 04 is two wins and three losses and remains failed. Finish game 54 to preserve the declared endpoint, then revise the learning method. All measured decisions used my own reasoning, pre-existing notes and the referee; no external chess advice, automated analysis or delegation.

## Game 54 — Black, elo-1800-setting, loss

Completed 2026-10-01 at 06:24:57 UTC by resignation after 26.Nxf8 (51 plies), zero illegal submissions. Total record: 24 wins, one draw, 29 losses. The 1800-setting record is seven wins and 11 losses. Provisional engine-relative Elo is 1740 [1600, 1890], with 36 rated games and 18 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 11,740,642 tokens, including prior play and practice.

Against e4/Ne2/Nec3 I developed normally and castled. Bxe3/fxe3 and Be6 led to the central break ...d5. The actual Nxd5/Nxd5/exd5/Bxd5/Bxd5/Qxd5 sequence exchanged both bishop pairs and one knight pair without losing material. ...Rad8, ...f5 and ...e4/dxe4/...fxe4 created an active central pawn and an open f-file. After Rfd1, ...Qe5 answered the queen attack; Qc4+/...Kh8/Nc5 then introduced Nd7 forks and pressure on b7/e4.

The analysis identified the Nd7 fork repeatedly. ...Na5 attacked Qc4 and defended b7, and after Qb4 the retreat ...Nc6 attacked that queen again. I initially spent far too long on other lines before noticing that Nc6 itself attacked Qb4. Following Qa3, ...Qf5 moved the queen away from the fork and retained support for e4. These local catches did not make the later exchange safe.

Decisive failure: against 22.Rf1 I returned the queen with 22...Qe5. I examined the f-file exchange and the diagonal Qa3-b4-c5-d6-e7-f8, but concentrated on Nxe4 and failed to re-test Nd7 after the rook recapture. Before the exchange, Rd8 could capture an unsupported knight on d7; after 23.Rxf8+ Rxf8, that rook stood on f8 instead. The actual 24.Nd7 attacked both Qe5 and Rf8 and cleared c5 from Qa3's diagonal to the same rook. My 24...Qe7/25.Qxe7 Nxe7 allowed 26.Nxf8, losing a full rook after the queen exchange. This line was played, not merely a speculative analysis. I resigned with knight and six pawns against rook, knight and six pawns; this was my own material assessment, not a certified forced loss.

Trial 04 ends at two wins and four losses: both maximum-strength games lost, both skill-0 games won, both 1800-setting games lost. The estimate fell from 1770 [1610, 1920] to 1740 [1600, 1890]. Across trials 01–04, endpoint estimates are 1740, 1800, 1770 and 1740, versus 1780 before trial 01. Their overlapping intervals and repeated tactical failures do not establish sustained improvement. In this block games 49 and 53 directly repeated opened-line failures; games 50, 52 and 54 added defender and exchange errors. All six games had zero illegal submissions, which does not establish sound play.

Decision: end trial 04 as failed and replace it before game 55. The next separate learning period will use harder positions from my own earlier games, with later played moves withheld during the first assessment, plus the remembered game-54 error. It will focus on testing an opponent's forcing exchange and then rebuilding the defender relationships before the next tactical reply. These remain my own assessments; legality checks cannot certify a candidate as best. The next declared benchmark endpoint is game 60, beginning at 1740 [1600, 1890]. No outside chess advice, automated analysis or delegated move selection was used.

## Between games 54 and 55 — replacement practice trial 05

Completed and inspected at 06:39:19 UTC, 12 minutes and six seconds after the planning reference, including manual assessment and file work. Four earlier-game positions were selected by fixed game/ply in advance and displayed without their later played moves: games 8/17/24/29 at plies 25/24/25/24. They were unfamiliar in detail, not independent blind puzzles. The remembered game-54 position supplied a fifth board. I chose all candidate moves and replies myself.

Twelve manually specified branches checked the effect of moving a pawn defender, clearing a rook route, opening a bishop capture, a pawn fork after a recapture, and the game-54 rook relocation. In game 29, the simple e4/Nxe4/Nxe4 plan omitted Bxh4; the alternate Bxe7 line also required handling Nxc3's intermediate fork. Reassessment after another exercise retained Bg3 as the working candidate without claiming it best. In game 54, Qg6 preserved a rook escape after Rxf8+/Rxf8/Nd7, while a different Nxe4 branch conceded a pawn without repeating the full-rook loss.

All 70 supplied legal plies, captured-piece predictions, check statuses and selected end-square occupants matched the mechanical checks. No engine, automated attack enumeration, search, scoring, move generation for recommendations or external advice was used. This establishes only the correctness of those reconstructions, not optimal moves or learning transfer. Inputs, outputs and limitations are in `trials/defender-exchanges-05.md` and its JSON companions.

The new execution emphasis is to reason from the opponent's turn, follow a concrete forcing exchange through the recapture, rebuild the actual defender locations, and test the next short threat before remote analysis. The previous procedure is archived as `trials/move-check-before-05.md`. Begin game 55; evaluate the complete unchanged games 55–60 block against the 1740 [1600, 1890] baseline. Any played recurrence fails the process condition. Sustained Elo improvement remains unestablished.

## Game 55 — White, maximum strength, loss

Completed 2026-10-01 at 07:17:27 UTC by resignation after 31...Rxb2 (62 plies), zero illegal submissions. Total record: 24 wins, one draw, 30 losses. Maximum-strength record: zero wins, one draw, 18 losses. The fixed estimate remains 1740 [1600, 1890], with 36 rated games and 19 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 11,970,893 tokens, including all previous measured play, practice and associated reasoning.

I used d4/Nf3/Bf4/e3/c3, answered ...Bd6 with Bg3, and developed Nbd2/Bd3 before castling. Bxg3/hxg3 retained f2's support of g3. The central e4/cxd4/cxd4/dxe4/Nxe4 sequence and Nxf6+/Nxf6 reached equal material with one bishop and knight each. Rc1 attacked the queen and induced ...Qd6.

There were useful catches before submission. I noticed that Bxf3 could remove d4's knight defender, and then caught a more basic error in my analysis: Qd1 did not defend d4 at all while Bd3 blocked the file. I rejected the contemplated Ne5 and chose Qa4 to support d4 directly. The actual Bxf3/gxf3 changed the pawn cover. Be4 vacated d3 and attacked Ra8; after ...Rac8, Rfd1 added a real rook defender to d4. Against ...h4, Kg2 and hxg3/fxg3 kept g3 occupied and defended. I also rejected a speculative Rc6 line which recaptured a knight before accounting for the removed bishop defender, choosing the actual rook exchange Rxc8/Rxc8 instead.

Bb7 drove the rook to c7, where it attacked the bishop, so I returned to e4 and then used Bc2 to free the f-pawn without leaving the bishop under Nxe4. Against ...Nh5, f4 blocked the Qd6-g3 line. I considered ...Qd5+ and a king escape, but the moved pawn also made other diagonal checks possible. After ...b5 attacked Qa4, I correctly rejected Qxb5 because it would abandon Bc2 to Rxc2+. Qb3 retained one queen defender of the bishop.

Decisive failure: 27.Qb3 did not account for 27...Qc6+. That move checked Kg2 along c6-d5-e4-f3-g2 and added the queen to Rc7's pressure on Bc2. Earlier reasoning about Qc6+ had used the queen's former a4 square; I did not reconstruct the reply after relocating it to b3. The actual 28.d5 blocked the check and attacked the queen, but ...Qxc2+ captured the bishop. Qxc2/Rxc2+ exchanged the queens without recovering the bishop's value. Kf3/exd5/Rxd5 removed the advanced pawn and ...Rxb2 took another pawn. I rejected the apparent Rxb5 recovery because Rb2 now defended b5, then resigned with rook and three pawns against rook, knight and four pawns. This was my own practical assessment, not a certified forced loss.

Trial 05 has already failed its recurrence condition: a missed forcing check made a defender exchange lose a piece. Correct local catches, zero illegal submissions and verified practice did not prevent that error. Reasoning remained excessively long and reused a reply from an earlier queen location. Keep the declared full-block endpoint at game 60 and preserve this failure; the unchanged Elo is a consequence of the maximum opponent being excluded, not evidence that the loss is irrelevant to strength. Continue games 56–60 with the same trial and revise at the endpoint. All measured moves were my own reasoning through the referee, with no outside chess advice, automated analysis or delegation.

## Game 56 — Black, maximum strength, loss

Completed 2026-10-01 at 07:41:54 UTC by resignation after 37.Qg5+ (73 plies), zero illegal submissions. Total record: 24 wins, one draw, 31 losses. Maximum-strength record: zero wins, one draw, 19 losses. The estimate remains 1740 [1600, 1890], with 36 rated games and 20 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 12,088,091 tokens, including all earlier play, practice and associated reasoning.

The Spanish opening reached a closed centre after ...exd4/cxd4, ...Nb4/Bb1, ...c5/d5 and ...Nd7/Ra3/...c4/Ree3/...Nc5/Nd4. I used ...Nbd3 and met axb5 with ...axb5. White's Nxb5 and Nxc4 then took two pawns while a rook exchange and ...Qxb5/Bxd3/...Nxd3/Qxd3 exchanged the knights and a bishop. White's queen recapture on d3, rather than the rook recapture explored in another branch, retained defense of Nc4. I did not obtain the material gain imagined in the weaker recapture line. ...Rc8/b3 and ...Be7 followed, leaving me two pawns down with two bishops against bishop and knight.

Rg3 pinned g7 to Kg8 and threatened Bxh6. ...Kh8 removed that pin, but 28...f5 relied on an inadequate response to Bxh6. I initially envisaged ...gxh6/Qh5/...Bg5, then caught before submission that h6 would be pinned to Kh8: it could not recapture Rxg5. That invalidated the proposed defense and left mating threats. I chose 29...Bf8, which defended both g7 and d6. White's actual Bxg7+/...Bxg7/Qh5+/...Kg8 then relocated that bishop away from d6. The actual Nxd6 forked Qb5 and Rc8; ...Rc1+ compelled Kh2, allowing ...Qd7 to save the queen as well. The check avoided an immediate rook loss, but did not repair the pawn losses or king exposure. The previously identified d6 defense had changed again after the forced bishop capture.

Decisive failure: after 34.Ne8, I chose 34...Qf7 to offer a queen exchange and defend Bg7. I spent time on Nxg7/Qxg7/Rxg7/Kxg7, but omitted the stronger capture order 35.Rxg7+. Ne8 still defended the rook on g7, so Kxg7 was unavailable. The actual ...Qxg7/Nxg7/...Kxg7 exchanged my queen and bishop for White's rook and knight, a four-point material loss on the usual piece values. Thinking about the same destination and nominal defenders did not substitute for testing the immediate rook check with the knight still on e8.

After Qg5+ I resigned with Rc1, Ba8 and Pf5 against White's queen and six pawns, with my king exposed on g7. This was my practical assessment, not an engine-certified forced loss. The result preserves a second failed maximum-strength game in trial 05. The unplayed pawn-recapture catch and the rook-check escape were useful local corrections, but the played f5 defense and Qf7 exchange plan remained unsound by the concrete continuations seen. Reasoning again became too long and did not reliably start with the opponent's most forcing check.

Trial 05 is zero wins and two losses and remains failed. Continue the declared skill-0 and 1800-setting games 57–60, with no added practice or changed endpoint, then revise the method. The unchanged rating reflects exclusion of maximum-strength games, not successful transfer. All decisions used my own reasoning, pre-existing notes and the referee; no outside chess advice, automated analysis or delegation was used.

## Game 57 — White, skill 0, win

Completed 2026-10-01 at 08:02:32 UTC by 36.Rh3# (71 plies), zero illegal submissions. Total record: 25 wins, one draw, 31 losses. Skill-0 record: 18 wins and one loss. The provisional estimate rose to 1750 [1600, 1890], with 37 rated games and 20 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 12,186,268 tokens, including all previous measured play, practice and associated reasoning.

Against ...Qe7, I developed both knights, occupied the centre with d4, played Bc4 and castled. After ...b5/Bb3/...a5, a3 prepared Ba2; ...g6/Bg5/...f6/Be3/...a4/Ba2 used that retreat. Qd2 prompted ...Nf7 rather than leaving the knight exposed on h6. Rad1 and d5 reached a closed centre after ...c5. Nxb5 took an undefended pawn. Against ...Bg7, Nc7+ forked Ke8 and Ra8; ...Kf8/Nxa8/...Bxa8 won an exchange, with the bishop recapture explicitly included beforehand.

Qd3 supplied support for e4 after the c3 knight had gone. Qb5 attacked Bb7 and a4. Black answered ...Qd8, leaving the bishop undefended, and Qxb7 captured it. I accepted the offered queen exchange with Qxb6, expecting ...Nxb6, but Black instead played ...Ke7 and left the queen lost. Qb5 saved my queen from Nd7's still-existing attack on b6. These large opponent errors already made the game a weak test of learning transfer.

Nxg5 removed the other knight when it attacked Nf3 and e4. Black played ...Rb8 instead of recapturing; Qxa4 answered the rook attack on my queen, and Qa7+ answered ...Nb6. After ...Nd7, Ne6 used the d5 pawn's protection and attacked Bg7. ...Rg8 defended that bishop. Later ...Bh6 exposed the tactical importance of my f4 pawn: moving it immediately would uncover Bxe3+ toward Kg1. I first played Rf3 to give an actual rook recapture on e3, then f5. Black returned the bishop to g7 after the rook had returned to b8, leaving it undefended; Nxg7 captured it. The Bxe3+/Rxe3 prevention was my own unplayed branch, not a referee-certified continuation.

Against ...Rxb2, Bb3 saved the attacked bishop with c2 pawn support and retained defense of c2. ...Rb1 then left the rook under Rd1, and Rxb1 removed it. Ba4 attacked the remaining knight. After ...Kf8, Bxd7 removed that knight, but I had not explicitly anticipated the immediate ...Kxg7 capture of my knight before submission. This did not threaten the large advantage, and Bxd7 is not claimed to be objectively losing; it is still a concrete attention omission, not a clean preservation of every piece.

Be6+ cleared d7 from Qa7's seventh-rank line and restricted the king. After ...Kh6, Rh3 was mate: the rook covered the h-file, Qa7 covered g7/h7, f5 controlled g6, and Black's own g5/h7 pawns occupied other escapes. The referee confirmed checkmate. My alternative Rb8 mating branches against the other king escapes were not played.

Trial 05 is one win and two losses and remains failed. The prepared e3 recapture, rook fork, supported bishop retreat and final net are useful local observations; the opponent's lost queen and other pieces, plus the unanticipated Kxg7, prevent treating this win as reliable improvement. The ten-point estimate rise has a heavily overlapping interval and is not sustained Elo progress. Continue games 58–60 without extra practice or changing the endpoint. All moves used my own reasoning and the referee, with no external advice, automated analysis or delegation.

## Game 58 — Black, skill 0, win

Completed 2026-10-01 at 08:20:58 UTC by 36...Qf2# (72 plies), zero illegal submissions. Total record: 26 wins, one draw, 31 losses. Skill-0 record: 19 wins and one loss. The provisional estimate is 1750 [1610, 1890], with 38 rated games and 20 excluded maximum-strength games. Observed cumulative active-goal usage after the game: 12,282,021 tokens, including all earlier play, practice and associated reasoning.

Against e4/Nc3/d3/Nf3, I developed normally, castled and exchanged Bb4 for Nc3 after a3. ...Bg4 and ...Nd4 induced Bxd4/exd4, removing White's other bishop while leaving one knight each. ...c5 supported d4; ...Re8, ...d5, ...Bxe2/Qxe2 and ...dxe4/dxe4 opened the e-file. ...Nd5 used the temporary pin of e4 to Qe2. After Qg4 removed the pin, I moved the knight to c3, then took the undefended b5 pawn when Rbe1 removed its rook defense. ...Rc8 defended c5 against Qh5.

White's c4 allowed ...dxc3 en passant. Re3 left Nd2 under attack, and ...cxd2 took the knight. Rh3 threatened mate, which ...h6 answered before any promotion attempt. Against a4 I rejected immediate ...d1=Q/Rxd1/Qxd1+/Qxd1: Qh5 could reach d1 after the exchanges. This was a manually found flaw in the contemplated continuation, not a played loss. ...Nd6 saved the attacked knight.

After Rd3, the initially attractive ...Nxe4 would have cleared the rook's line to Qd8. I caught that before submission. A contemplated ...Qg5 queen exchange would also have removed the knight's queen defender, leaving Rxd6 available. I instead played ...Qe7, keeping Nd6 defended and clearing the d-file exposure. Only after Qd1 did ...Nxe4 take the pawn. ...Nf6 then answered f3, and White's Rd7 placed its rook on a knight-defended square: ...Nxd7 captured it. These concrete catches were useful, but the calculation again expanded into many remote branches.

...Qe1 used the rook and advanced d2 pawn behind the queen. White made an escape with g3; ...Qxd1/Rxd1/...Re1+/Kg2/...Rxd1 removed its remaining queen and rook. I moved the rook off d1 and promoted. ...Qf3+/Kh4/...Nf6 confined the king. I had prematurely imagined Qxg4 as mate against every pawn reply, but the actual h3 would allow hxg4. I rebuilt that final position and played ...Qf2 instead: its diagonal checked Kh4 through g3; Nf6 covered h5, h6 covered g5, and White's own pawns occupied g4 and h3. The referee confirmed mate. The rejected Qxg4 claim was corrected before a move was submitted; it is still evidence that a future reply can invalidate an apparently complete mating calculation.

Trial 05 is two wins and two losses and remains failed from games 55–56. The skill-0 opponent lost a knight and both rooks, so this result is limited evidence of transfer. The unchanged rounded estimate and overlapping interval do not establish stronger play. Complete the declared 1800-setting pair, games 59–60, then revise at the endpoint. All moves were my own decisions through the referee; no external advice, automated analysis or delegation was used.

## Game 59 — White, 1800 setting, loss

Completed 2026-10-01 at 09:20:44 UTC by resignation after 65...gxf6 (130 plies), zero illegal submissions. Total record: 26 wins, one draw, 32 losses. The 1800-setting record is seven wins and 12 losses. The provisional estimate fell to 1740 [1600, 1880], with 39 rated games and 20 excluded maximum-strength games. Observed cumulative active-goal usage afterward: 12,540,404 tokens, including all earlier play, practice and associated reasoning. This game took about an hour; extensive calculation did not prevent elementary capture omissions.

Against the Spanish with ...Bd6 and ...Qe7, I castled, played d4-d5, developed Nc3 and Be3, and answered ...b5 with Bb3. a4 supplied Ba2 before ...c4 could trap the bishop. However, 14.Ne2 removed e4's knight defender while Be3 blocked the supposed Re1 defense. I recognized this only after ...f5. Qc1 freed d2, and Bd2 answered ...f4; Nxg5/hxg5 exchanged knights. ...c4/Ba2, b3/b4/bxc4 and ...g4/hxg4 gained two pawns while Black built a strong attack. f3, Kf1 and Ng1 met ...Qh4/...Ng5/...Qh1+. Ng1 both blocked the check and freed the rook's e-file defense.

The c-pawn move created a later tactical omission. After c3, ...Bc5, Ke2 and ...b3, the old c2xb3 recapture was no longer available. Bb1 would allow ...b2 to fork Qc1 and Ra1. I recognized the trap only after ...b3 and chose Bxb3/Rxb3, leaving three extra pawns for the bishop. This is an assessment of the observed defensive choices, not a proof that every earlier alternative loses a bishop. ...Qxg2+ subsequently removed another pawn. King moves and a rook challenge provided relief, while Qd1, Be1 and Bf2 eventually established usable defenses around g1 and f3.

There were concrete catches during this defense. A contemplated exchange ending with Qxf4 would allow ...Nh3+ to fork the queen and Kg1. Later, after Bxc5, Black inserted ...Bd7 rather than recapturing: ...Bxa4+ would check Kc2 and expose Qd1 behind it. Kb2 removed that line before the actual ...dxc5. Another rejected Nc6/Bxc6/dxc6 sequence would open Rd8 against Qd3; I moved the queen before reconsidering that idea. These catches did not make the overall process reliable.

After reaching a3/a2, trading one rook pair and moving the queen to d3, the knight finally traveled g1-e2-c1-b3-a5 and captured a5. I retained the pawn by returning the knight to b3 and advancing a4-a5. Before the later Nxc5, I noticed that ...Qxa5+ against Ka3 could create a mating net and moved to a2. I then played 53.Nxc5, seeing both the queen attack and the opened rook file. The actual ...Qxa5+/Kb1/...Rxb2+/Kxb2/...Qxc5 exposed the omission: Qa5 also attacked the undefended knight on c5 along the fifth rank. I calculated the king escape and rook exchange without accounting for that final capture. My spoken summary that both knights remained was premature and was corrected immediately after ...Qxc5. This was another played forcing-sequence failure.

With only queen and pawns against queen, bishop, knight and pawns, I continued looking for checks. Kb3 protected c4 through possible queen exchanges. I rejected Kd3 after ...Ba4+ because ...Qe3 would mate in the branch I calculated. Qh3 and Qe6+ produced one repeated position via ...Kh8/Qh3+/...Kg8, but Black then chose ...Kf8. The final 65.Qf6+ omitted the immediate ...gxf6 capture by g7. I treated the white g5 pawn's support of f6 as relevant safety while exploring king moves and knight blocks. A protected queen can still be captured profitably by a pawn. The referee accepted ...gxf6; I resigned with only six pawns against queen, bishop, knight and three pawns. Resignation was my practical judgment, not an automated forced-loss certificate.

Trial 05 is two wins and three losses and remains failed. It has not improved the rounded Elo from its 1740 baseline; the intervals overlap substantially. The final move repeats the simplest capture-geometry failure despite very long reasoning, and the earlier c5 loss repeats the failure to finish a concrete forcing sequence. Complete game 60 at the declared endpoint, then revise the learning method. All decisions used my own reasoning and the referee, with no external advice, automated chess analysis or delegation.

## Game 60 — Black, 1800 setting, loss; trial 05 endpoint

Completed 2026-10-01 at 09:34:57 UTC by resignation after 24.Rxc3 (47 plies), zero illegal submissions. Total record: 26 wins, one draw, 33 losses. The 1800-setting record is seven wins and 13 losses. The provisional estimate is 1720 [1590, 1860], with 40 rated games and 20 excluded maximum-strength games. Observed cumulative active-goal usage afterward: 12,617,085 tokens, covering the entire goal including earlier play, practice and associated reasoning.

Normal development against Nf3/e3/h3/c4/d4 led to a central ...d4/Nxd4/Nxd4/exd4/Bxd4 exchange. ...Rc8, ...Bxc4/Bxc4/Rxc4 won c4, with the actual rook recapture considered. ...Qc8 and ...e4 retained activity, but after 20.Nd5 I chose ...Bxb2 while considering Nxf6+ and Rxb2. I omitted 21.Ne7+, which forked Kh8's prior square g8 and Qc8. The queen was lost after ...Kh8/Nxc8. The alternative ...Nxd5 was among my own candidates, but I failed to test the immediate check before choosing the bishop capture. This is another played process failure, not a lack of candidate generation.

I tried ...Bc3 against Qd2. White answered Qxc3/Rxc3/Rxc3. Initially I thought this would allow ...Rxc8 and leave a pawn for an exchange. Reconstructing the actual board showed that the white rook now on c3 protected Nc8 along the open file: ...Rxc8 would allow Rxc8+, losing my remaining rook. I caught that continuation before submitting it. The final position instead had Black rook, knight and six pawns against White's two rooks, knight and five pawns. I resigned on my practical assessment of that rook-for-pawn deficit, without a forced-loss certificate. White's Qxc3 was not the blunder my first material summary suggested.

Trial 05 finished two wins and four losses. The estimate moved from 1740 [1600, 1890] to 1720 [1590, 1860]; overlapping uncertainty does not support a precise decline claim, but there is no sustained improvement. Played failures in games 55, 56, 59 and 60 violate the declared process condition. Correct practice branches and occasional catches did not transfer reliably. Long candidate exploration repeatedly displaced the simplest immediate reply. Stop this method at its declared endpoint and carry out a revised learning trial before game 61. All moves used my own reasoning and the referee; no external advice, automated analysis or delegation was used.

## Trial 06 practice and game 61 — White, maximum strength, loss

Separate practice ran from the 09:38:03 planning reference through inspected results at 09:46:52 UTC. Four preselected older positions and two remembered recent failures produced 11 supplied branches and 35 legal plies, with all explicit capture/check/occupancy predictions matched. I rejected a newly considered Qxe5 in the remembered game-59 position after finding Nxc4+ forking the queen and king. The checker did not certify reply-set completeness or best play. Full limitations, inputs and results are in `trials/immediate-replies-06.md` and its associated JSON files. Games 61–66 are the declared evaluation, beginning at 1720 [1590, 1860].

Game 61 completed at 10:08:35 UTC by resignation after 33...a5 (66 plies), zero illegal submissions. Total record: 26 wins, one draw, 34 losses. Maximum-strength record: zero wins, one draw, 20 losses. The estimate remains 1720 [1590, 1860], with 40 rated games and 21 excluded maximum games. Observed cumulative active-goal usage afterward: 12,781,018 tokens, including all prior play, separate practice and associated reasoning.

The queen-pawn opening led through cxd5/cxd4/Nxd4/Nxd5/e4/Nxc3/bxc3/e5/Nf3/Qxd1+/Kxd1 to an equal-material queenless position. I developed Bc4/Be3, moved the king to c2 and put the h-rook on d1. Nd2 reinforced e4 and controlled c4, but also blocked the rook: the imagined Rxd5 recapture after ...Bxd5 was unavailable. I noticed the obstruction after the actual bishop capture and used exd5. ...Bb4 increased pressure on c3; Ne4 defended that pawn and reopened the rook. Kb2 unpinned c3, then d6 gained space with rook and knight support. Rac1 connected the rooks.

After ...f5 I returned the knight to d2 to meet ...Nc4+ with Nxc4. This again blocked the rook's d-file, and more seriously blocked Be3's retreat through d2. I omitted the effect of ...f4: Bd4 and Bf4 were capturable by e5, while Bc5 and Bxb6 had pawn recaptures. The bishop was trapped. I played Bxf4/exf4 and Ne4, losing the bishop for a pawn while restoring d6's defenses. This was a real played error caused by the selected knight retreat; a narrow count of immediate major-piece captures cannot turn it into successful play.

The later checking sequence exposed another incomplete response calculation. After ...Re8/f3/Re5/g3/Nc4+, I chose Kb3 with ...Rb5+ anticipated, but had not resolved what followed. After the actual rook check I found that Kc2 allowed ...Ne3+ to fork Rd1, while Ka4 allowed ...Nb2+ with the same rook target. I chose Kc2 knowing that concession, then answered the actual ...Ne3+ with Kd2 and ...Nxd1 with Rxd1. The fork was identified before the final king escape was submitted, but the defensive branch used for the preceding king move was incomplete. Do not call this a clean execution of the trial's reply-resolution step merely because the first check was named.

...Rb2+/Kd3/...Rxa2 and gxf4/...Rxh2 removed my flank pawns. Ra1 sought an eventual seventh-rank check to displace Kd7; ...a5 blocked the route. I rejected Rxa5 because b6 would capture the rook. The final material was White rook, knight and four pawns against two rooks, bishop and four pawns. I resigned on my practical assessment of this large deficit, with no forced-loss certificate. The passed d6 pawn had supplied activity but no concrete recovery.

The first trial-06 game is a loss. Some immediate checks and capture hazards were identified, but the bishop trap and incomplete checking sequence show that the execution change has not yet made play reliable. In particular the checking line lost a major piece despite the intended short recapture/rebuild step. Preserve those failures and continue games 62–66 at the declared endpoint; revision is required there rather than treating this game's narrow first-pass successes as improvement. No outside advice, automated chess analysis or delegation was used.

## Game 62 — Black, maximum strength, loss

Completed at 10:35:08 UTC on 2026-10-01 by resignation after 37.Re7, 73 plies, zero illegal submissions. Total record: 26 wins, one draw, 35 losses; maximum-strength record: zero wins, one draw, 21 losses. The fixed provisional estimate remains 1720 [1590, 1860], with 40 rated games and 22 excluded maximum games. Observed cumulative active-goal usage afterward was 12,910,927 tokens, covering the entire goal, including prior play, practice and associated reasoning.

The e-pawn opening reached a queenless position through ...Nxe4/d4/...Nd6/Bxc6/...dxc6/dxe5/...Nf5/Qxd8+/...Kxd8. I retreated the knight after g4, defended f7 with ...Be8, and exchanged ...Nd5/Nxd5/...cxd5. This removed the doubled c-pawns and retained both bishops. White's e5/f5 pawns restricted my pieces. ...h5/hxg4/hxg4 opened the h-file. The king excursion ...Kc7 was premature: Bf4 aligned with it behind e5, and I returned to c8. ...dxc4 temporarily won a pawn. I recognized that the doubled white rooks meant the king alone could not defend Bd7, added ...Rd8, and later retreated ...Be8. Rxd8+/...Bxd8 exchanged one rook pair. Ne4 introduced Nd6+, attacking both king and Be8; ...Be7 gave a concrete bishop capture against that check.

After Rh1/...Kd7/Rh7, I chose 29...g6. I had considered 30.e6+ but used an incomplete favorable continuation with ...fxe6/fxe6+/...Kxe6. Re-examining the actual check exposed the omitted alternative f6: moving the f7 pawn could leave Be7 pinned by Rh7 to Kd7, preventing the bishop from capturing or escaping. This is another failure to finish the response to an anticipated check. I played ...Kd8 and met exf7 with ...gxf5, attacking Ne4 and expecting a possible fxe8=Q+/...Kxe8 concession.

I then missed the immediate 32.Bc7+ from f4 through e5 and d6. After ...Kxc7, 33.f8=Q promoted safely because Be7 was pinned along the seventh rank and could not capture on f8. I recognized that mechanism after Bc7+ and before accepting the bishop, but it was absent from the candidate's immediate-reply pass. This is a played omission that enables a queen promotion and loss of the pinned bishop; do not excuse it because the narrow trial wording emphasized captures of existing major pieces. ...fxe4 recovered the knight, then Qxe7+ removed Be7. The king was driven through b6/a6/a5, with Qxb7+ taking another pawn. I resigned after Re7 with Black Ka5/Ra8/Be8 and four pawns against White Kg2/Qb7/Re7 and three pawns. This was a practical resignation, not a forced-loss certificate.

Trial 06 is now zero wins and two losses. Immediate-check enumeration was incomplete, and an anticipated checking branch was not resolved correctly. Useful catches around the doubled rooks and Nd6+ did not prevent these failures. Continue the remaining four declared games, then revise the method at the endpoint. No external chess advice, engine analysis outside the referee, automated chess analysis or delegation was used.

## Game 63 — White, skill 0, win

Completed at 10:54:22 UTC on 2026-10-01 by 34.Qb5#, 67 plies, zero illegal submissions. Total record: 27 wins, one draw, 35 losses; skill-0 record: 20 wins and one loss. The provisional estimate is 1730 [1590, 1860], with 41 rated games and 22 excluded maximum games. Observed cumulative active-goal usage afterward was 12,996,746 tokens, covering the entire goal and prior play, practice and reasoning.

The opening e4/c5/Nf3/Nc6/d4/Nf6/Nc3/d5 led to exd5/cxd4/dxc6/dxc3. I exchanged queens with Qxd8+/Kxd8 before cxb7/Bxb7/bxc3, leaving an extra pawn. I considered the alternative ...cxb2 and a bishop recapture of that pawn before choosing cxb7; the played bishop recapture produced the pawn gain. Bd2 defended c3 against ...Rc8. After the anticipated ...Ne4, c4 retained bishop support for the pawn, followed by Bd3 and castling. ...Nxd2/Nxd2 exchanged a bishop for the knight without losing a rook. Rab1 and Ne4 developed with threats against Black's bishops.

After ...Bb6, 17.c5/Bxc5/18.Nxc5/Rxc5/19.Rxb7 worked as calculated: the rook's recapture on c5 left the b7 bishop undefended. I emerged a bishop ahead with equal pawns. ...Rc3 attacked Bd3, but c2 still defended it; after Rxa7/...Rxd3, cxd3 won that rook for the bishop and retained the extra pawn. Ra8+ displaced the king to d7, allowing Rxf8 to remove Black's last rook. The two rooks were coordinated on b7/f7 so that ...Kxb7 was unavailable. The a-pawn advanced behind the b-file barrier and promoted. Qa5+ forced the king to d6; Rfd7+/Kc6/Qb5# completed the game, with the rooks defending the queen and covering the remaining king squares.

No played missed check or lower-valued capture of a major piece was identified in this game. Several recapture and king-capture hazards were checked before submission. This is a successful conversion against skill 0, not evidence that the trial's earlier failures have been repaired. Trial 06 stands at one win and two losses; continue through game 66 and revise as already required. All move selection was my own reasoning, using only the referee and pre-existing notes during play.

## Game 64 — Black, skill 0, win

Completed at 11:07:29 UTC on 2026-10-01 by 19...Qe2#, 38 plies, zero illegal submissions. Total record: 28 wins, one draw, 35 losses; skill-0 record: 21 wins and one loss. The provisional estimate is 1730 [1600, 1870], with 42 rated games and 22 excluded maximum games. Observed cumulative active-goal usage afterward was 13,049,345 tokens, covering the entire goal and prior play, practice and reasoning.

Against e4/c3/Qe2/Nh3, I developed both knights, challenged the center with ...d5 and recaptured exd5 with ...Nxd5. ...Be6, ...Be7 and castling completed development while White moved the queen again. ...Qd7 supported ...Bxh3; the proposed Bxh3 recapture would itself allow ...Qxh3. White instead played Na3/Nb5, allowing ...Bxh3 and ...Bxf1. When c4 attacked Nd5 I moved it to f6, expecting White could still recover the bishop. White pushed d4 instead, opening the bishop's retreat from f1 through e2/d3 to c4. ...Bxc4 captured that pawn and retained both bishops. After b3, ...Bxb5 removed White's remaining knight; ...Nxd4 then captured the central pawn.

Before trying a knight fork, I rejected the unsupported ...Nc2+ and ...Nf3+ ideas because Qxc2 or Qxf3 could capture the checker. ...Qf5 added the needed support on the f-file. After Be3, ...Nf3+ forced Qxf3: the king's candidate escapes were covered by the knight or Bb5, or occupied by White's pieces. ...Qxf3 won the queen, with no pawn on g2 or e2 able to capture it; the pawn on g3 attacks f4, not f3. White's h4 allowed ...Qe2#. Bb5 protected the queen through c4 and d3, and the queen covered the remaining adjacent king squares. The referee recorded checkmate.

No played missed check or immediate lower-valued capture of my major pieces was identified. The useful behavior was rejecting an unsupported fork before adding a concrete defender, then carrying the capture through. This easy-opponent result does not establish transfer against stronger play or repair the earlier trial failures. Trial 06 is two wins and two losses; games 65–66 against the unchanged 1800 setting remain before the declared review. No outside chess advice, automated analysis or delegation was used.

## Game 65 — White, 1800 setting, loss

Completed at 11:51:49 UTC on 2026-10-01 by resignation after 34...Qxd3+, 68 plies, zero illegal submissions. Total record: 28 wins, one draw, 36 losses; the 1800-setting record is seven wins and 14 losses. The provisional estimate is 1720 [1590, 1850], with 43 rated games and 22 excluded maximum games. Observed cumulative active-goal usage during the subsequent record work was 13,242,101 tokens, including all previous play, practice and reasoning. Roughly 44 minutes of play did not prevent the decisive elementary omission.

The Scandinavian opening gave White an extra central pawn and active pieces. I caught several concrete hazards: after ...Kh7 the imagined Bxh6/Bxh6/Qxh6+ would allow ...Kxh6; later Rd4 moved the rook off Bb7's diagonal before a contemplated e6/fxe6/dxe6 sequence. After ...Ne6 forked Rd4 and Bf4, I chose Rxc8 to remove the checking rook before resolving the knight. The actual ...Nxd4/Rxe8/...Nxb3 was an omitted intermediate capture: the knight took Bb3 and attacked Qd2 while Qd7 still attacked Re8. Qc3/...Nc1 then threatened ...Ne2+, forking king and queen. I saw that threat before playing Rxe7, and the supplied ...Ne2+/Kf1/...Qxe7/Kxe2 line occurred, leaving White queen, bishop and two extra pawns against queen and bishop.

After ...Qd7/d6/...Qxa4/Be3/...Bxg2, I greedily chose Bxb6. I had considered ...Qb5+ as a check but missed that it also attacked the loose bishop on b6. The actual check forced another concession. My 33.Qd3 interposition then omitted the immediate 33...Bf1+, which displaced the king from its defense of the queen on d3. I accepted the bishop with Kxf1; ...Qxd3+ won my queen. This is an exact recurrence of the trial's targeted error: the new queen candidate was submitted without identifying a bishop check that removed its only defender. Recognizing the tactic after the actual check did not repair the earlier move.

I resigned with bishop and five pawns against queen and four pawns, with legal king escapes still available; this was a practical decision, not a forced-loss certificate. Trial 06 is two wins and three losses. Its process condition has failed repeatedly and its rounded estimate has not risen from the 1720 baseline. Finish game 66, then replace the ineffective method. All decisions were my own; no external chess advice, automated analysis or delegation was used.

## Game 66 — Black, 1800 setting, loss; trial 06 endpoint

Completed at 12:42:10 UTC on 2026-10-01 by resignation after 74.Rxa1, 147 plies, zero illegal submissions. Total record: 28 wins, one draw, 37 losses. The 1800-setting record is seven wins and 15 losses. The provisional estimate is 1710 [1580, 1840], with 44 rated games and 22 excluded maximum games. Observed cumulative active-goal usage afterward was 13,471,012 tokens, covering the entire goal, earlier play, practice and reasoning.

The Vienna opening reached equal material after a knight exchange and the queen trade on d3. I developed, castled and prepared ...e4 with ...Bf6 and ...Bd5; I rejected the earlier unsupported advance because dxe4/fxe4/Bxe4 would win White a pawn. The played ...e4/dxe4/...fxe4/Nh2/...Ne5/Ng4/...Nd3+/Bxd3/...exd3/Nxf6+/...Rxf6 sequence produced a passed d3 pawn and equal material. ...Re6+ and bishop checks restricted the king. I corrected several imagined continuations before submission, including an impossible ...Re2 route through White's bishop on e3. These corrections did not establish accurate positional handling.

...Re5 and ...Rb5 chased b2 into b4. Bc5+ then restricted the rook's exits. After ...Kd7/Rh4/...Be6/Rf4 I recognized that c4 would leave no satisfactory retreat I could find. ...Kc6 prepared the practical concession ...Rxc5/bxc5/...Kxc5, which occurred after 35.c4. This exchanged my rook for bishop and pawn. The trap was identified before that final concession, but not avoided during the preceding maneuver. Moving the king onto d7 had also blocked the supposed d8-rook defense of d3 until it moved away. This game adds a real rook-mobility and defender-line failure; it is not a successful trial merely because I did not overlook the final pawn attack when submitting the exchange.

...Rd4/Rxd4/...Kxd4/Rxd3+/...Kxc4 simplified to bishop versus rook. The king recovered a5, while White took g7 and b7. I retained queenside counterplay with ...c5, ...Bd5 and king support. I rejected an immediate ...c4 while the king was on a5 because Rc5+ would also attack Bd5; moving the king to b4 first avoided that fork. White's h-pawn advanced. The bishop used the h7–c2 diagonal to limit promotion, but the rook eventually supported h7 and the bishop was lost after ...Bxh7, intervening checks, and Rxh7.

The a- and c-pawns reached the second rank with king support. White twice chose a new continuation instead of completing a repetition; no draw occurred. After ...c2+/Kc1/...a2/Ra7, I could not find a move preserving both pawns. ...g4/fxg4 and ...a1=Q+/Rxa1 left only Kb3 and Pc2 against Kc1, Ra1 and Pg4. The king on c1 blocked promotion. I resigned on my own assessment of that ending, without an engine or tablebase certificate.

Trial 06 finished two wins and four losses. Elo moved from 1720 [1590, 1860] to 1710 [1580, 1840]; the overlapping uncertainty does not establish a precise decline, but there is no sustained increase. Games 61, 62 and 65 already failed the targeted process condition. This game supplied useful catches but another material concession and a failed conversion of activity. Replace the ineffective rehearsed-line practice with recorded opponent drills before the next benchmark block.

During this game the operator authorized and installed selectable opponent/position practice, recorded as event 5512. I reread the updated AGENTS.md and GOAL.md, completed the active benchmark normally, and made no changes to operator files or records. Future practice uses the separate interface and remains excluded from benchmark Elo. All game-66 moves were my own decisions through the referee; no outside chess advice, automated analysis or delegation was used.

## Trial 07 practice — five recorded opponent replays before game 67

Planned at 12:45:02 UTC on 2026-10-01 with a 50-minute ceiling and the next measurement fixed at benchmark games 67–72. Finished all five drills by 13:14:34. The first four replayed remembered failures from games 65, 66, 60 and 61 at nominal 1800; the adaptive fifth repeated game 60 after reviewing those four. Each stopped after six learner moves and the opponent replies. All five are retained as unfinished, with no score, in the separate practice ledger: 60 plies and one illegal submission in total. Details and actual continuations are in `trials/opponent-replays-07.md`.

The first two retained their major and minor pieces apart from equal exchanges; the second also captured a pawn. The third avoided the old Ne7+ fork but lost its extra pawn, exposed the king to Rg3+/Bc5+, and included an illegal ...Kh8 despite my having identified Bd4's h8 diagonal. The fourth kept all material and retreated the bishop to e1, but omitted ...Nc4+ initially and temporarily blocked the rook's defense of d6 with Bd2. The original ...f4 trap was not played. These are unresolved execution failures, not clean passes.

For the adaptive replay I moved the queen to d7 before exchanging bishops. The actual opponent line allowed equal queen and bishop trades while Black retained its extra pawn and g7 cover. The final Nd5 attacked Rc7 and Nf6; ...Nxd5 is an unplayed response candidate, not an executed or verified continuation. That remembered local improvement does not establish stronger play or a winning ending.

Benchmark Elo is unchanged at 1710 [1580, 1840], 44 rated games; practice does not enter it. Observed cumulative active-goal usage after the drills was 13,620,442 tokens, including all earlier play, practice and reasoning. Continue with the declared six-game benchmark and assess transfer at game 72. All moves and assessments were my own; no automated chess analysis, external game advice or delegation was used.

## Game 67 — White, maximum strength, loss

Completed at 13:36:04 UTC on 2026-10-01 by resignation after 32...Rxg2+, 64 plies, zero illegal submissions. Total record: 28 wins, one draw, 38 losses; maximum-strength record: zero wins, one draw, 22 losses. Elo is unchanged at 1710 [1580, 1840], with 44 rated games and 23 excluded maximum games. Observed cumulative active-goal usage afterward was 13,712,381 tokens, covering the entire goal and previous play, practice and reasoning.

The d4/Nf3/c4 opening led to central pawn and knight exchanges, then ...Qxd1+/Kxd1. Bc4, Kc2, Be3 and Rhd1 completed development. Against ...Ba3 I used Rab1 and Bd5, then Kb3 attacked the bishop after its retreat line became usable without the earlier ...Na5+ fork of Bc4. The actual ...Bd6/Nd2/...Na5+/Kb2/...Be6 led to Bxe6/Kxe6, still with equal material. These individual checks did not establish overall safety.

After f3/...Rc6, I noticed that moving Nd2 to b3 would leave Be3 vulnerable to ...Nc4+ and ...Nxe3. Re1 supplied a real defender before Nb3. The opponent did play ...Nc4+, but after Kc2 it continued ...Na3+, forking king and Rb1. I had stopped at the anticipated ...Nxe3/Rxe3 branch and omitted the second knight check. Kd2/...Nxb1+/Rxb1 conceded a rook for knight. This is the decisive targeted failure, despite the correctly arranged defense of the bishop.

I anticipated the discovered rook check ...Bc5+ and answered Ke2, preserving the king's defense of Be3. ...Bxe3/Kxe3/...Rxc3+ nevertheless won c3. Kf2/...Rc2+/Kg3/...Rxa2 lost a2. I tried f4 for counterplay; ...Rd3+/Kg4/...Rxg2+ collected another pawn with check. The final material was White rook, knight and three pawns against two rooks and six pawns. I resigned with king escapes still available; this was a practical assessment, not a proved forced loss.

Trial 07 has one benchmark loss and a recurrence of the intended checking-sequence correction. The remembered practice improvements have not established transfer. Continue through the predeclared game 72 endpoint and revise on the full evidence. All decisions were my own through the referee, with no external chess advice, automated analysis or delegation.

## Game 68 — Black, maximum strength, loss

Completed at 13:56:21 UTC on 2026-10-01 by resignation after 21.Qa8, 41 plies, zero illegal submissions. Total record: 28 wins, one draw, 39 losses; maximum-strength record: zero wins, one draw, 23 losses. Elo remains 1710 [1580, 1840], with 44 rated games and 24 excluded maximum games. Observed cumulative active-goal usage afterward was 13,785,361 tokens, covering the whole goal and all earlier play, practice and reasoning.

I chose an Advance Caro–Kann: ...Bf5/...h5, the bishop exchange on d3, and ...e6/...c5. After dxc5/...Bxc5/c4/...Ne7/Nc3/...Nbc6/O-O, ...Ng6 challenged the center and blocked the queen's diagonal toward h7. The actual cxd5/...Ncxe5/Qb5+ was anticipated; ...Nd7 blocked check and supported Bc5. dxe6/...fxe6 retained equal material but left the king in the center and the d7 knight pinned.

After Rd1 I used ...Qe7 to support Bc5 and e6. Bg5 displaced the queen to f7. Against Ne4, I recognized that simply castling would not adequately protect Bc5 against both knight and queen, and that a bishop retreat to b6 would leave a contemplated Nd6+ king-and-queen fork. I chose ...Be7, but failed to apply the changed blocker: Be7 now obstructed Qf7's defense of Nd7. White's actual Qxd7+ won that knight. Kxd7 was illegal because Rd1 protected d7, and ...Qxd7 was unavailable through my own bishop. I recognized this after the capture and played ...Kf8.

Qxb7 took a pawn and attacked Ra8. ...Rd8/Rxd8+/...Bxd8/Qa8 then pinned Bd8 to Kf8 while Bg5 also attacked that bishop. I rejected the imagined ...Qxf3 counterplay before submission because g2 could capture the queen. I could not find an adequate defense to the actual position and resigned with queen, rook, bishop, knight and four pawns against queen, rook, bishop, two knights and five pawns. This is a practical resignation, not a proof of forced loss or exhaustive defense analysis.

Trial 07 is zero wins and two losses. The checked branches did not prevent a new defender obstruction, so reliable transfer has failed again. Complete the remaining four declared games and replace the method at the game-72 review; skill-0 wins alone cannot repair this finding. All game decisions were my own; no external chess advice, automated analysis or delegation was used.

## Game 69 — White, skill 0, win

Completed at 14:26:40 UTC on 2026-10-01 by 32.Ra8#, 63 plies, zero illegal submissions. Total record: 29 wins, one draw, 39 losses; skill-0 record: 22 wins and one loss. The rounded Elo estimate remains 1710 [1580, 1840], with 45 rated games and 24 excluded maximum games. Observed cumulative active-goal usage afterward was 13,911,172 tokens, including all prior play, practice and reasoning.

The e4/e5/Nf3/Nc6/Bc4 opening met ...d6 and ...Bg4. Be3 and Bxd4 recaptured the central pawn without moving the knight pinned to Qd1. Bb5 and Bxc6 exchanged a bishop for the c6 knight, then Nc3, castling and h3 completed development and displaced the pinning bishop. Re1, e5/e6, Qe2 and Rad1 built pressure while Black advanced kingside pawns and left the king central.

I kept Nf3 in place while Qc6 and Bb7 were aligned toward g2, rejecting speculative moves that would permit ...Qxg2 mate. Ne4 and Nxf6 took a pawn. After ...Nf5 attacked Bd4, Bc3 remained a usable retreat that still defended Nf6 through d4/e5. Against ...g4, hxg4 removed the pawn attack on Nf3. Black then played ...Qxc3; bxc3 won the queen for bishop. ...Ng3 attacked Qe2 but allowed fxg3 to remove that knight.

Nxh5 was supported by the actual g4 pawn; ...Rxh5/gxh5 won a rook for knight. The h- and e-pawns advanced. ...Bd4+ was not my predicted reply to e7, but cxd4 captured the checking bishop. After ...Ka7/e8=Q/...Bxf3, Qxf3 recovered the remaining bishop and vacated e2, preserving the promoted queen's defense through Re1. The played ...Rxe8/Rxe8 removed Black's last rook. Black's ...c5 left the Qf3–a8 diagonal clear, so Ra8# was protected and b7 was covered; a6 and b6 were occupied by Black's own pawns. The referee recorded checkmate.

No played missed check or defender obstruction causing material loss was identified. Several checks were resolved only after they occurred, and the queen blunder was decisive; do not describe this as exhaustive calculation or proof of transfer. Trial 07 is one win and two losses. Continue games 70–72, then revise the already-failed method using all outcomes. No external chess advice, automated analysis or delegation was used.


## Game 70 — Black, skill 0, win

Completed at 14:52:22 UTC on 2026-10-01 by 36...Rd1#, 72 plies, zero illegal submissions. Total record: 30 wins, one draw, 39 losses; skill-0 record: 23 wins and one loss. Elo remains 1710, with interval [1590, 1840], 46 rated games and 24 excluded maximum games. Observed cumulative active-goal usage afterward was 14,028,383 tokens, including all earlier play, practice and reasoning.

The opening gave Black development and a castled king against White's central king. After the bishop-for-knight exchange on c6, ...e4 displaced Nf3 before ...Nxd5 recaptured White's bishop. ...Bf5, ...Bb6 and ...Rc8 kept the center supported. ...Qg5/...Qxg2 and ...Bxh3 collected two pawns. I applied White's actual Nd2 as a new defender of Rf1 and rejected ...Qxf1+: the knight recapture would make the queen-and-bishop trade unfavorable.

I instead chose ...Nxe3, deliberately sacrificing the knight for a central pawn and checking play. The actual fxe3/...Qg3+/Rf2/...Qxe3+/Qe2 led to ...Qxe2+/Kxe2. Black had three extra pawns for a knight. I had not established that this sacrifice was better than retaining the extra pawn; the eventual win does not validate it. ...f5, ...Bc5 and ...b6 secured the center and answered a5/a6. I rejected an immediate ...f4 because both the bishop and rook could capture it, then prepared ...h6/...g5. Against Ng3, ...f4 attacked Be3 and Ng3. Bxf4/...gxf4 recovered the bishop and left Ng3 attacked.

White's Rh2 attacked Bh3 but left the knight. ...Bg4+/Kd2/...fxg3 won it while attacking the rook. Against Rg2, ...Rf2+ was protected by the actual g3 pawn. Ke1 allowed ...Rxg2. ...Bxd4 removed the remaining knight, and White's Ra3 allowed ...Bxc3+/Kf1. ...Rf2+/Kg1/...Rd8/Rb3/...Rd1# finished with a protected second-rank rook restricting the king and the d-rook covering the first rank. The referee confirmed mate.

No new played defender obstruction or omitted check causing material loss was identified; the knight concession was intentional but insufficiently justified. The decisive later gains relied on skill-0 mistakes. Trial 07 is two wins and two losses and has already failed its targeted process condition in 67–68. Continue the two nominal-1800 games and review at 72. All decisions were my own, with no external chess advice, automated analysis or delegation.


## Game 71 — White, nominal 1800, loss

Completed at 14:56:51 UTC on 2026-10-01 by resignation after 12...Rxh6, 24 plies, zero illegal submissions. Total record: 30 wins, one draw, 40 losses; nominal-1800 record: seven wins and 16 losses. Elo is 1700 [1580, 1830], with 47 rated games and 24 excluded maximum games. Observed cumulative active-goal usage afterward was 14,053,561 tokens, including the entire prior goal.

The opening was e4 c5, Nf3 d6, d4 Nd7, Nc3 g6, Be2 Ngf6, O-O Ng4, h3 Ngf6, Be3 cxd4, Nxd4 h6, Qd2 Rb8. White completed development and castled; Black retained an uncastled king. I then played 11.Bxh6 Bxh6 12.Qxh6 Rxh6. This lost the queen for a pawn after an equal bishop exchange.

The failure was direct and elementary. In calculating Bxh6 I had named the rook on h8 and its open line to h6, but treated Qxh6 as an attack that would force that rook to retreat. I failed to apply the reverse capture along the same file: the queen on h6 was undefended, and ...Rxh6 simply took it. This was not a hidden long combination, a legality problem, or an external fault. The selected-move check did not perform its intended function. Bxh6 was already an inadequately justified commitment; after ...Bxh6, Qxh6 compounded it instead of reassessing the actual capture.

The final position had equal rooks, bishop and two knights, with Black's additional queen against White's extra pawn. I resigned on that practical material assessment, without a forced-loss certificate. Trial 07 is two wins and three losses and has a third clear targeted calculation failure. Complete the declared final game 72, then revise the method. No external advice, automated analysis or delegation was used.


## Game 72 — Black, nominal 1800, loss

Completed at 15:47:46 UTC on 2026-10-01 by 66.Qg5#, 131 plies, zero illegal submissions. The PGN was read afterward to confirm the final move. Total record: 30 wins, one draw, 41 losses; nominal-1800 record: seven wins and 17 losses. Elo is 1700 [1570, 1820], with 48 rated games and 24 excluded maximum games. Observed cumulative active-goal usage afterward was 14,265,653 tokens, covering the entire goal.

Black castled early and developed against Nf3/e3/c4/d4. The central ...d4 sequence temporarily conceded a pawn after White's unanticipated Nxc6, but ...Bxd4/exd4/...Qxd4 restored equal material. I applied the queen attack exposed by Bf4 and exchanged queens. ...Rc2, ...b5, ...h6 and ...f5 led to ...Rxb2 after Be3 left that pawn. I recognized a possible back-rank problem after Rfe1 and supplied king space. ...Kf7/Rd7+/...Re7/Rxe7+/...Kxe7 left an extra pawn in a rook-and-minor ending.

Against 30.f3 I saw the danger of a discovered bishop check after moving Ne4. I chose ...Ng3 and anticipated Bf2+/...Ne2+, including Rb2's defense of e2. I failed to finish that line through Kf1: the knight on e2 remained pinned to Ke7, while White's king now supported Rxe2. Moving ...Kd6 did not save it; 33.Rxe2 took the knight. This is another actual failure to carry an identified checking line through the new recapture, not a successful check merely because the first interposition was legal. I retained the rook with ...Rb1+ instead of exchanging into a minor-piece deficit.

The queenside pawns supplied counterplay. I rejected an immediate ...Rxa3 while Kd6 allowed Bb4+ to fork king and rook, moved the king, and later captured a3. White collected g7 and h6. ...a5/...b4/...a4/...Rd3/...a3/...b3/...a2 produced 47...a1=Q. White declined the actual repetition route and eventually promoted on h8. I avoided immediate captures on e1 when the white king supported the final recapture. After the king moved to h1, ...Qc1, ...Rxe1+/Rxe1/...Qxe1+ removed White's bishop and exchanged the rooks, reaching queen and two pawns each.

...Qe2 supported the prospective b2 advance. White played Qd4+/...Kg5/Qg7+/...Kh5/65.f4. I considered continued checks and the pawn race but failed to apply the newly supplied pawn defense of g5. I played ...b2 and White answered 66.Qg5#: f4 defended the checking queen against Kxg5, and the queen covered the remaining king exits. This was an immediate missed mating threat, confirmed by the referee. I have not established whether an earlier position was objectively winning or what the first uniquely losing move was. The promotion and material recovery did not validate the earlier errors.

## Trial 07 endpoint — ineffective; revise before game 73

Games 67–72 finished two wins and four losses: both skill-0 games won, both maximum and both nominal-1800 games lost. Elo moved from 1710 [1580, 1840] to 1700 [1570, 1820]. The intervals overlap widely; no precise decline or sustained improvement is established. The targeted errors recurred in games 67, 68, 71 and 72, including a lost exchange, an obstructed defender, a direct queen loss, a pinned knight loss and an immediate mate.

The five short remembered opponent drills did not transfer reliably. Several correct catches coexisted with severe omissions, and extensive branching repeatedly ended in elementary mistakes. Replace this practice format before the next fixed benchmark. Retain the results and all separate practice records. All moves and assessments were my own; no automated chess analysis, external game advice or delegation was used.


## Trial 08 declared — fresh practice games

Replace trial 07 with two nominal-1600 practice sessions from the initial position, White then Black, capped at 45 learner moves each and 90 minutes combined. Declaration time 15:52:06 UTC; ceiling 17:22:06 UTC on 2026-10-01. Keep incomplete sessions explicitly unfinished and retain all outcomes. Details are in `trials/fresh-games-08.md`.

The change is longer exposure to unexpected replies in fresh games, with simpler supported play and a final opponent-turn check after choosing the move. It remains unproved and partly reuses an earlier safety requirement; do not describe restating it as learning. Benchmark games 73–78 are the next fixed evaluation, baseline 1700 [1570, 1820], 48 rated games. Practice wins cannot establish measured improvement.


### 2026-10-01 16:16 UTC — trial 08, practice 6 completed at its cap

Fresh White practice at nominal 1600 ended explicitly unfinished after 45 own moves / 90 plies, zero illegal attempts. Result `*`, no score; practice ledger seq 169, hash `fbaf9cba614e0e5dabff393a7353f752a9c227a6aad6cc7f71b0d8d58a0a46b0`. Referee PGN read back. This does not affect benchmark Elo 1700 [1570, 1820] through game 72.

The central exchange left a rook against two extra minor pieces with equal pawns, not the extra pawn I initially miscounted. Neither queen nor rook was lost by a direct unreciprocated capture, and no mate occurred. However, an existing target error recurred: after 41.Rd1, the reply sequence 42.axb6 Nxb6+ 43.Kd3 put my own king on the rook's line to d5. I still treated d5 as defended. Black captured it with 44...Kxd5 after 43...axb5 44.Rb3; 45.Rxb5+ Kd6 recovered only the other pawn. At the cap, White had 2R+3P against R+B+N+4P. No independent evaluation or claimed draw. Detailed assessment is in `trials/fresh-games-08.md`.

Observed whole-goal counter: 14,395,098 tokens, 152,755 elapsed seconds at 16:16:15 UTC, covering all goal activity rather than a fixed inference budget. Continue the already declared fresh Black session at nominal 1600, at most 45 own moves, combined deadline 17:22:06 UTC; then benchmarks 73–78. The longer practice format has not yet prevented changed-blocker mistakes.


### 2026-10-01 16:44 UTC — trial 08 practice complete; return to fixed benchmarks

Black practice 7 at nominal 1600 ended at the declared 45-own-move cap after White 46.gxf6+ en passant, 91 plies, one illegal submission. Result `*`, no score, practice seq 264, hash `5c6fbb2c711964736e8cff1303fc6375a846ce3432560d8f0c55c97186c2da3e`; PGN read back. Both fresh sessions are preserved unfinished: 90 learner moves / 181 plies in a combined 52m07s, within the 90-minute ceiling.

The targeted errors persisted. Practice 7: attempted ...Re1 through White's pawn on e3 (referee rejection); replacement 29...Re7 allowed 30.Nf5+ to fork king and rook, though White declined the capture after ...Ke6; retreating the king removed d5's defense before 34.Rxd5; a6 also fell in the rook exchange. The pawn recovered by 43...Nxh4 did not establish a sound position. I then omitted en passant after 45...f5, and the actual 46.gxf6+ left Black in check with R+N+3P against R+N+5P at the cap. No independent evaluation, forced-loss certificate, or scored practice result. Combined with practice 6's king blocking its own rook defense, this offers no evidence that longer fresh games solved the application weakness. Detailed assessment is in `trials/fresh-games-08.md`.

Observed cumulative counter: 14,513,989 tokens / 154,433 elapsed seconds for the whole goal, at 16:44:13 UTC. Continue with the already declared benchmark games 73–78, same settings and estimator. Elo baseline remains 1700 [1570, 1820], 48 rated games, overall 30W/1D/41L through 72. Evaluate at 78; do not extend practice to seek a favorable score or label these unfinished games wins/draws.


### Benchmark 73 — White versus maximum strength, loss

Completed at 17:16:14 UTC on 2026-10-01 by practical resignation after 41...b1=Q+, 82 plies, zero illegal attempts. Result seq 6075, SHA-256 `a5fa7af05fe53ee28a85c9dd01f9a510f0d99b9e973421ad852f7be69ed89c9f`, snapshot `af78f355dc7e40e1773db91ce166a900425e429d7f73ca391913c5e5bd420e72`. The saved PGN was read back. This is not a forced-mate certificate.

Ordinary development and the first central exchanges preserved material. The queenside plan 16.a3, 17.b4 and 18.bxc5 did not produce a sound hold of both weak pawns. After ...Rfc8, ...Qxc5 and 20.Qb2, Black took c3; 21.Qxc3 Rxc3 exchanged queens and left White a pawn down with a passive rook. No claim that this loss was forced or that a unique best alternative was identified. The later concrete sequence 29.f3 Bc6 30.Nxc6+ Rxc6 31.fxe4 removed the defender of e4 and actually restored equal pawn numbers. That did not establish a drawn rook ending: White's doubled pawns and the restricted rook/king left two separate defensive tasks.

After ...Ra4 and ...b4, 34.Rb2 Rxa3+ lost the a-pawn while permitting king activity. The chosen 36.Rb3 Rxb3 37.Kxb3 correctly recaptured the rook, but the resulting pawn ending was not adequately secured. The actual continuation ...Kd6, Ka4 Kc5, Kxa5 b3, Ka4 b2, Kb3 b1=Q+ demonstrated that Black's remaining passer promoted first. Resignation followed with a queen against unadvanced pawns and no concrete recovery. The endgame may have been lost earlier; no independent analysis establishes the first losing move.

No queen or rook was lost through a direct unreciprocated capture, and no immediate mate occurred. The observed failure was the strategic/pawn-race assessment during simplification, not a successful conversion or evidence that the practice method works. Correctly avoiding some candidate captures and counting the actual rook recapture did not establish the pawn ending's viability. Long branches still occurred during several decisions.

Through 73: total 30W/1D/42L; maximum strength 0W/1D/24L in 25 games. Elo remains 1700 [1570, 1820], 48 rated games, with maximum-strength games excluded as uncalibrated. Observed whole-goal counter at 17:16:14 UTC: 14,646,240 tokens and 156,355 elapsed seconds. Continue the same declared trial-08 benchmark block with game 74; evaluate at 78.


### Benchmark 74 — Black versus maximum strength, draw

Completed at 17:36:06 UTC on 2026-10-01 by the referee's automatic threefold-repetition claim after 24...Kg8, 48 plies, zero illegal attempts. Result seq 6126, SHA-256 `b601434f7dcc8fe88f826059fa4002ba0e3c41f712bb22a9a920f3a3c449ada5`, snapshot `29e155dc99791250eee2c343cd389dad8969a3955ea378136561639b337f0b46`. The saved PGN was read back.

The Caro-Kann development reached two knights versus bishop and knight after 14...Bxg5 15.Nxg5. I recognized the immediate Qh7 mate threat and chose 15...g6 after considering the knight fork on e6 and its actual pawn recapture. White played 16.Nxe6 fxe6 17.Qxg6+ Kh8, followed by repeated queen checks and 20.Qxh5+. Black's f-pawn survived on e6; the original e-, g- and h-pawns were captured. The final material was two knights and three pawns versus a bishop and six pawns, with queens and both rook pairs still present. White's actual checks supplied a repetition, and I used legal king escapes until the referee ended the game. No claim that this defense forced a draw against every White choice, that the opening was best, or that an unplayed alternative was sound.

No queen or rook was lost by a direct unreciprocated capture and no immediate mate was missed. Applying the immediate mating threat and calculating the fork recapture worked in this particular continuation. The draw is useful maximum-strength evidence, but a single result does not establish that the practice method transferred reliably or increased measured Elo. Maximum games remain excluded from the numerical estimator.

Through 74: overall 30W/2D/42L; maximum strength 0W/2D/24L in 26 games. Elo remains 1700 [1570, 1820], 48 rated games. Trial 08 benchmark so far is 0W/1D/1L. Observed whole-goal usage after the result: 14,740,191 tokens / 157,563 elapsed seconds. Continue the declared fixed block through 78 before its endpoint assessment.


### Benchmark 75 — White versus skill 0, win

Completed at 17:46:28 UTC on 2026-10-01 by 29.Qg7#, 57 plies, zero illegal attempts. Result seq 6186, SHA-256 `d2b69158b952e2c8c33c8d4ef43e79505cebf1c8bd4f332770a7a93b6fd7d164`, snapshot `f0bbd99ef404d1907d723cc17ffc3c1e8de50a7d5b0323b9caea26a093e5d16d`. Saved PGN read back.

White developed behind d4/e4, castled, and supported the center. The central captures preserved material. After 15.Bf4 Rb5, b3 removed the attacked b-pawn and a4 attacked the rook. Black's 17...Re5 allowed 18.Bxe5 Bxe5, winning the exchange. I moved the attacked bishop after ...Qf6, anticipated ...Bd4+ after f4, and used Kh1. Black then left the bishop on e3 undefended: 23.Qxe3 captured it. After 24.e5 Qxe5, I used 25.fxe5 to capture the queen rather than automatically exchanging queens. The final Rxf7, Qh6+ and Qg7# sequence applied the rook's real defense of g7 and the king's escape squares.

No direct unreciprocated queen/rook loss or missed immediate mate occurred for White. Large opponent blunders supplied the material advantage, and this result alone does not show improvement against nominal 1800 or reliable general transfer. Skill 0 is included in the fixed numerical estimator. Through 75: total 31W/2D/42L, skill-0 record 24W/0D/1L. Elo 1700 [1580, 1820], 49 rated games. Trial-08 benchmark so far 1W/1D/1L. Observed whole-goal usage: 14,791,453 tokens / 158,169 elapsed seconds. Continue to the declared endpoint at 78.


### Benchmark 76 — Black versus skill 0, loss

Completed at 18:14:51 UTC on 2026-10-01 by practical resignation after 49.Re5+, 97 plies, zero illegal attempts. Result seq 6286, SHA-256 `e2e3f57f79ac4b030766a552456d87466389c5fdc6da6768639c5c97fc31603a`, snapshot `b2f46b4c6ab18328ee0f7d5b2a780cc37772c809982db027839eac94c01f4471`. Saved PGN read back. The resignation is a practical assessment, not a forced-mate certificate.

Two targeted failures occurred. First, 14...Qb6 put the queen on a square attacked by White's knight on a4, a knight whose attack pattern I had previously used when retreating the bishop. I omitted that attack when selecting the queen move. Nxb6 would win the queen for a knight after ...axb6. White instead played Bxf6, c5 and Ne4; the queen remained exposed until I finally noticed and used 17...Qb5+. Those omissions by White do not validate the placement.

Second, after the queen trade and central pawn advances, White's king collected f5 and e4. I doubled rooks with 27...Rae8 and answered 28.exd4 with 28...Re3+. I explicitly relied on the other rook's protection against Kxe3, but failed to inspect the pawn on f2. The actual 29.fxe3 captured the checking rook. Recapturing with the remaining rook would then allow Kxe3 because the supporting rook had been removed. I recognized that only after the actual capture and did not compound the loss. This was a direct unreciprocated rook loss and another failure to finish the real recapture line. The long preceding branches did not prevent the elementary pawn omission.

White's 30.g4 allowed ...bxa4, recovering the knight on a4; Rxa4 recaptured the pawn. Later ...Rxg4 recovered a pawn, but White traded one rook pair and collected f7 and a7. At resignation Black had a knight and h-pawn against a rook and five pawns. 49.Re5+ checked the king on f5 and attacked Nd5; d4 defended the checking rook against Kxe5. No claim of an independently established first losing move. The main observed failures are established by the actual board and captures.

Through 76: overall 31W/2D/43L; skill 0 now 24W/0D/2L. Elo 1680 [1560, 1800], 50 rated games, 26 excluded maximum games. The rolling 50-game window is now full; each subsequent rated game replaces an older one. Trial 08 benchmark so far is 1W/1D/2L. The target failures have recurred, so this method has not solved the weakness even though the complete endpoint remains at 78. Observed cumulative whole-goal usage: 14,912,591 tokens / 159,883 elapsed seconds. Finish nominal-1800 games 77 and 78, then revise the method at the declared endpoint. No automated chess analysis, outside advice or delegation was used.


### Benchmark 77 — White versus nominal 1800, loss

Completed at 19:07:44 UTC on 2026-10-01 by practical resignation after 45...Qxf1, 90 plies, zero illegal attempts. Result seq 6379, SHA-256 `d2eb1cd9b1551baa110270816aa44361c2170967e19cfd54fc448f2b9a2f2644`, snapshot `b26422774039cd777061535e3d85004d5d64c4aacbcb9431e0d85f4fae5d69f0`. Saved PGN read back. No forced-mate certificate or independent first-losing-move claim.

White castled against a Dutch setup, developed, and exchanged Bxh6 for the knight. The later gxf4/Rxf4 sequence opened the king's shelter. Qe3, h3, Kh1 and Rg1 met immediate rook pressure, and b3 actually supported c4 before Nd2 moved to f3. Black left the knight capturable with 22...Ng4; hxg4 took it. Nxd4 then captured the bishop, while Black's queen and rook continued the attack. These material gains did not establish king safety.

I chose 28.Bxg4 after considering ...Qh4+, Kg2 and the rook capture, but did not finish the king escape through the real continuation. After 28...Qh4+ 29.Kg2 Rxg4+ 30.Kf1 Qh3+ 31.Ke1, Black played ...Rxe4. The rook now attacked Qe2 through e3 and pinned it to Ke1. I chose 32.Qxe4 Bxe4, conceding queen for rook. This was a material concession after the checking sequence, not a clean consolidation of the earlier extra pieces. I have not proved that it was forced or identified the best earlier king route.

Counterplay with the two rooks and knights captured the bishop by 38.Nxb7. After ...dxc4, I recognized that the c4-pawn removed the king's d3 escape and used Rf1 to reinforce f2. Black's ...Qc7 then exposed the knight's lack of a safe retreat in my calculation. I chose Nd8, accepted ...Qxd8, and recovered the c4-pawn with bxc4. The resulting knight-for-bishop exchange was real; I had not secured the knight's exit when taking on b7.

The final targeted failure was again a changed king defender. Ke2 had defended Rf1. Moving 43.Ke3 withdrew that defense, but I concentrated on Rd3 and Nc3. After ...Qh3+, Kd4 and ...Rd8+, I interposed Nd5 to avoid exposing Rd3 to both heavy pieces. Black instead played 45...Qxf1, directly capturing the undefended other rook along h3-g2-f1. I had not applied the king's departure to that rook. Resignation followed with R+N+3P against Q+R+4P. This is an actual unreciprocated rook loss, beyond the earlier queen-for-rook concession. Long speculative branches again failed to prevent the elementary omission.

Through 77: overall 31W/2D/44L; nominal 1800 now 7W/0D/18L. Elo 1670 [1550, 1790], 51 rated games total and the most recent 50 used, with 26 excluded maximum games. The rolling update replaces the oldest rated result; it is not a change to the estimator. Trial-08 benchmark so far is 1W/1D/3L. Observed cumulative whole-goal usage: 15,116,977 tokens / 163,061 elapsed seconds. Complete game 78 before the already declared endpoint assessment, then revise this ineffective method. No outside advice, engine analysis, automated move selection or delegation was used.


### Benchmark 78 — Black versus nominal 1800, win with a direct queen blunder

Completed at 19:41:21 UTC on 2026-10-01 by 59...Rh4#, 118 plies, one illegal submission. Result seq 6501, SHA-256 `c605fa57d85fd8cb8ba99e59a71e60859eea6ca2e1a61a454907441522d165be`, snapshot `036fbccc03b2d1f8cf09223a0ae315c8d568f94d6d0fccfe32d9ee81cd66c2e5`. Saved PGN read back. This win does not validate the move procedure.

The initial development and ...d4/...dxe3 central exchanges removed the isolated pawn. White's 17.Rxe6 Rxe6 conceded the exchange; 23.Qh6 gxf5 then lost a knight, and 25.Rd5 Nxd5 lost a rook. I answered the mating threat after Bxf5 with ...Nf6 and used ...Qf8/...Qg7 to strengthen h7's defense. The rook invasion and 34...Rxf2+ 35.Qxf2 Rxf2+ removed White's queen. White chose 36.Ke3 instead of taking the remaining rook. These large opponent concessions supplied the advantage.

The targeted failure followed immediately: 36...Qc5+ 37.bxc5 lost my queen to the pawn on b4. I calculated king replies and the queen's diagonal support for Rf2 but omitted the pawn's direct capture of the checking piece. There was no recapture or compensating combination. A check did not force a king move. This is the same basic failure class as game 76's ...Re3+/fxe3, despite the final opponent-turn requirement. No independent analysis or best-move claim is made for unplayed alternatives.

The remaining R+N versus B advantage allowed continued play. ...Ra2 saved the attacked rook; ...Rxa3 and ...Rxh3 took pawns, while ...bxc6 removed White's passer. At move 48 I tried ...Rh8 through my own h7-pawn; the referee rejected it. The replacement ...Rh6 then allowed 49.g5 to fork rook and knight. ...Nh5+ and ...Rg6 retained the rook. The knight on h5 was capturable by Kg4 after the rook left h6, and White declined that capture, eventually choosing 52.g6. I had calculated a promotion route if the knight was captured, but that is an unplayed own assessment, not a demonstrated forced conversion. The actual 52...Kxg6 took White's last pawn and supplied king protection to Nh5.

The rook then moved from the bishop's diagonal with ...Rc4+, the c-pawn promoted, and ...Qc3+/...Qxf3+ removed White's last piece. The final ...Qf2+ and ...Rh4# correctly used the queen's defense of h4 and the king's remaining exits. This concrete finish does not cancel the queen loss, the blocked rook attempt, or the allowed pawn fork.

Through 78: overall 32W/2D/44L. Each setting has 26 completed games: maximum 0W/2D/24L; skill 0 24W/0D/2L; nominal 1800 8W/0D/18L. Provisional engine-relative Elo 1680 [1560, 1800], 52 rated games total, most recent 50 used, 26 maximum games excluded. Observed cumulative whole-goal usage after completion: 15,275,535 tokens / 165,078 elapsed seconds. All choices and analysis were my own; no engine analysis, automated move selection, external game advice or delegation was used.


### Trial 08 endpoint — ineffective; replace the method before game 79

Games 73–78 finished 2W/1D/3L: 0W/1D/1L against maximum strength, 1W/0D/1L against skill 0, and 1W/0D/1L against nominal 1800. The rating moved from 1700 [1570, 1820] to 1680 [1560, 1800]. These widely overlapping intervals do not establish a precise decline or an increase. The estimator reached its 50-rated-game rolling window during this block, so the final two rated updates also replaced older results. No estimator or opponent change was made.

The process criterion failed in three of six fresh benchmark games. Game 76 left a queen capturable and then lost a checking rook to a pawn; game 77 lost a rook after withdrawing its king defender, beyond an earlier queen-for-rook concession; game 78 lost a checking queen to a pawn and added an illegal rook route and pawn fork. The maximum-strength draw and nominal-1800 win do not make these errors disappear. The two longer nominal-1600 practice sessions also contained changed-blocker and recapture failures.

Longer fresh practice plus the repeated final safety instruction did not produce reliable transfer. More speculative calculation repeatedly coexisted with simple omissions. Revise the actual practice and decision format now, after reviewing the earlier trials so that a renamed checklist is not mistaken for a new method. Preserve all practice and benchmark records. Choose and declare the next bounded learning period and fixed evaluation point before starting game 79. Sustained measured Elo improvement remains unachieved.


### Trial 09 declared — timed, shorter decisions

At 19:44:59 UTC on 2026-10-01, declared two fresh nominal-1800 practice sessions (White then Black), at most 40 learner moves each, combined ceiling 20:29:59 UTC. Next fixed evaluation is games 79–84; baseline 1680 [1560, 1800]. The change is a measured 20-second decision target with one short candidate/reply/answer, testing whether reduced branching prevents omitted board facts. Earlier capture and defender instructions are not relabeled as a new method. The helper records elapsed wall time and forwards only my supplied commands to ./play; it performs no chess analysis or move choice. Overtimes and illegal moves remain visible. Full plan in trials/short-decisions-09.md; prior procedure archived. No goal reset, model setting change or benchmark change.


### Practice 8 — White, nominal 1800, completed win

Finished at 19:58:45 UTC on 2026-10-01 by 31.Rh8#, 61 plies / 31 learner moves, zero illegal attempts. Practice result seq 327, SHA-256 `2ed8b8c997001de968ad86a9489dc50ce3b352bbc75478f9d20533f1c88a2e32`. Referee PGN read back. This is separate opponent practice and does not alter benchmark Elo or W/D/L.

The forcing 11.Bxf7+ Kxf7 12.Qxb4 won the queen for a bishop and pawn; later ...Ra8 and ...Rh5 allowed Qxa8 and Rxf8. I handled the actual a5 and d5 pawn attacks on the queen, blocked ...Bg4's attack on Rd1 with f3, and recaptured the checking bishop on c2 with the king. The last Qxf6+/Rh8# sequence used the queen's defense of the mating rook. No direct unreciprocated major-piece loss, illegal move or immediate mate omission was identified in the actual play. Opponent concessions supplied the advantage, and unplayed candidate lines were not independently evaluated.

The clock criterion failed: all 31 submissions were timed, but only 18 were within 20 seconds (58.1%); 13 exceeded it. Median 18.464 seconds, mean 21.431, maximum 59.837. The longest decision was Bxf7+, so that successful tactic cannot be credited to the specified short format. The log spans 19:47:00.362264 to 19:58:45.540629 UTC. Times include polling/tool/communication delays and are not pure inference time. Long branching returned during several attacking choices. A win does not establish that the duration intervention was implemented or caused improvement.

Continue the declared fresh Black session, same nominal strength and 20-second target, at most 40 own moves, unchanged combined 20:29:59 UTC ceiling. Use a longer initial tool wait to avoid an unnecessary extra polling round trip; preserve the original timing definition and every existing logged value. Do not exclude the first session's delays or failures. Fixed benchmark 79–84 remains due after the learning period.


### Practice 9 — Black, nominal 1800, loss by practical resignation

Finished at 20:11:55 UTC on 2026-10-01 after White 28.Qxf8, 55 plies / 27 learner moves, zero illegal attempts. Practice result seq 384, SHA-256 `9312567c86e4b4125217aed5e3330d986ab669233125dd918af4f2a427e64148`. Referee PGN read back. The resignation is a practical assessment, not a forced-loss certificate, and this result is excluded from benchmark Elo.

The first short calculation failed. After 10...Nxe5 11.dxe5 Bxb5 12.exf6 Bxf6, I had not carried the line through 13.Nxb5. Black lost both knights and the b5 bishop against White's knight, other bishop and d-pawn, leaving a minor-piece deficit for a pawn. Considering Nxb5 as an alternative earlier reply did not account for it after the pawn exchanges. The familiar final-capture omission returned under the shallow decision format.

I recovered White's remaining knight with 14...axb5 and explicitly accepted 15.Bxf8 Qxf8. That actual sequence left an exchange deficit with an extra pawn; it did not erase the original mistake. The queenside exchange and ...Rxc2 supplied activity, while White collected b7 and invaded with Ra8. I used ...Bd8 between the rook and queen, but Qd7 added a second attacker. The subsequent ...Be7 again left Qf8 capturable by Ra8; White instead played Qb7. I then chose 24...Qxa8 25.Qxa8+ Bf8, making an actual queen-for-rook concession. I have not proved that this was forced or established the best earlier defense. These difficult decisions again expanded into long branches.

The last error was a changed king defender: after ...h6, 27...Kh7 removed Kg8's protection of Bf8, and 28.Qxf8 directly captured the bishop. I concentrated on giving the king an exit while failing to apply the departure to the defended piece. At resignation Black had R+5P against Q+R+4P. There was no concrete recovery in my assessment. This is further adverse evidence for the intended procedure.

All 27 submissions were timed: 18 within 20 seconds (66.7%) and nine over. Median 14.553 seconds, mean 24.388, maximum 146.645. Session log: 20:00:00.171579 to 20:11:56.026722 UTC. Reducing polling round trips improved some routine timings, but did not prevent the long overruns when the defense became difficult. No timing values or failed moves were removed or redefined.

### Trial 09 practice endpoint — return to the declared benchmark

The two sessions ended naturally or by practical resignation within the 45-minute ceiling: one win and one loss, 58 learner moves / 116 plies, zero illegal attempts. Combined completion was 26 minutes 56 seconds after the declaration, including setup and reviews. All 58 moves have elapsed-time records; 36 were within 20 seconds (62.1%) and 22 exceeded it. Both sessions failed the 90% implementation criterion. The short central exchange in practice 9 was incomplete, and long defensive branches and changed-defender errors persisted. There is no basis to claim that the duration intervention worked, even though practice 8 ended in mate.

Follow the predeclared evaluation: fixed benchmark games 79–84 with the same observed timing target and unchanged chess rules, settings and estimator. Do not add practice until a favorable result appears or reinterpret the target afterward. Keep trying the shorter decision format, while recording noncompliance and errors honestly; any outcome attribution is limited by that noncompliance. At game 84 review all six results and the unchanged rating interval, then revise if needed. Baseline remains 1680 [1560, 1800] through benchmark 78, since practice does not enter the estimator. Sustained Elo improvement remains unachieved.

Observed cumulative whole-goal counter after both sessions: 15,431,410 tokens / 166,919 elapsed seconds. All moves and assessments were my own. The clock helper only forwards supplied referee commands and records elapsed time; no engine analysis, automated chess search, scoring, move selection, external game advice or delegation was used.


### Benchmark 79 — White versus maximum strength, loss

Completed at 20:23:39 UTC on 2026-10-01 by practical resignation after 23...Qxe3+, 46 plies, zero illegal attempts. Result seq 6551, SHA-256 `30ebdfcd7aae4bc2088f5fd3ad42be7d1c4a069e21df198f3b6ac28b5e8132e5`, result snapshot `9eea8115c7c833f0b0a47919dd5004283b20711b1eaa218c3f0da34ea3bfe6da`. Saved PGN read back. No forced-loss certificate or independently established first losing move.

The Italian development reached 8...Ng4. I used d4 to interrupt Bc5's line and then h3, but Black played ...Nxf2. I counted the actual Kxf2/dxc3+/Kf1/cxd2/Bxd2 continuation: the discovered bishop check let the pawn take Nd2, leaving equal pieces but two fewer White pawns and an exposed king. The initial blocking argument did not neutralize this full sequence. Bxe6 and Be3/Bxe3/Rxe3 removed the bishops; the second rook was saved from ...Qg5 with Rd3. Qe2 supplied e4 and Rd3 support, and Re3 answered the ...Ne5 fork with the queen still defending e3.

The next checking sequence was not completed correctly before committing. After ...Qh2, Ke1/Nxf3+ and 22.gxf3, Black used ...Qg1+. My earlier imagined Kd2 response omitted that leaving e1 would uncover Qg1's full rank against Ra1. When the check actually appeared, I identified that problem. I instead played 23.Qf1, knowing by then that it withdrew Qe2's defense of Re3, and Black captured that rook with ...Qxe3+. The loss was not a surprise at move 23; the failed anticipation was in the earlier recapture/king-escape plan. No alternative has been independently proved sound. Resignation followed with Q+R+5P against Q+2R+7P. This is another actual major-piece loss after an incomplete forcing-line assessment.

All 23 move submissions have timing records. Eleven were within 20 seconds (47.8%), twelve exceeded it; median 21.590 seconds, mean 23.734, maximum 71.405. Session log spans 20:13:29.093528 to 20:23:39.689174 UTC. The duration intervention again failed its 90% implementation condition; long branches persisted. Early quiet moves meeting the target do not validate the later defense or support attributing the result to uniformly short decisions.

Through 79: overall 32W/2D/45L; maximum strength 0W/2D/25L in 27 games. The provisional Elo remains 1680 [1560, 1800], 52 rated games total / latest 50 used, since maximum games are excluded (27). Skill 0 remains 24W/0D/2L and nominal 1800 8W/0D/18L, each in 26 games. Trial-09 benchmark so far is one loss. Continue the declared block through game 84, preserving the same target and every timing miss. Observed cumulative whole-goal usage: 15,481,414 tokens / 167,630 elapsed seconds. No engine analysis, external game advice, automated chess analysis or delegation was used.


### Benchmark 80 — Black versus maximum strength, loss by checkmate

Completed 2026-10-01 at 20:31:51 UTC after 17...Nh6 18.Qxe7#, 35 plies, one rejected move. Result seq 6590, SHA-256 `b65a029204bf3c7345b935a6830b19647f906b5dd4a7d0178993b579fd0c7d98`, result snapshot `e595ad8efae1c6a42794eb1f9e68fe15c5326d3f9f602dacf2167123fe959d31`. Saved PGN read back. The terminal mate is referee-confirmed; no earlier best defense or first losing move is independently established.

The advance Caro–Kann reached a central exchange with Black still uncastled. I rejected ...exd5 in my own reasoning because it would remove e6's protection of Nf5 while Qd3 attacked that knight; ...cxd4 kept that defender. However, after Qb3 I attempted 14...O-O-O without checking Bg5's diagonal through f6/e7 to d8. The referee rejected castling through attack. I then played ...Be7, moved the attacked Qc7 to b8, and answered dxe6 with ...fxe6; Qxe6 took the remaining central pawn.

The decisive error was another removed defender, now of a mating square. I focused on Qe6's threats to the knights, eventually recognized that Ke8 defended Nd7, and moved Nf5 to h6. I omitted that Nf5 was defending e7. With that knight gone, Qxe7 was mate: Bg5 protected the queen and Black had no legal response. Concern about the attacked knight displaced the opponent's immediate checking capture. This is an actual missed mate and failed transfer, not a sound defense made unlucky by opponent strength.

The timing record contains 18 submissions: 17 accepted moves and the rejected castling attempt. Fifteen accepted moves met 20 seconds (88.2%), two exceeded it; median 7.533 seconds, mean 10.221, maximum 31.636. The illegal castling submission was at 16.454 seconds; the replacement ...Be7 was at 28.00 seconds from the original response, with no clock reset. Session 20:28:30.939488–20:31:52.021011 UTC. This is closer to the timing target, but still fails the declared 90% legal-move criterion. The final mate-allowing move also exceeded the target. No attribution to uniformly short work is justified.

Through 80: overall 32W/2D/46L. Maximum strength 0W/2D/26L in 28; skill 0 24W/0D/2L and nominal 1800 8W/0D/18L, each in 26. Provisional Elo remains 1680 [1560, 1800], 52 rated total / latest 50 used, 28 maximum-strength exclusions. Trial 09 benchmark currently two losses; continue 81–84 as declared before revising. Actual cumulative whole-goal counter: 15,534,236 tokens / 168,110 elapsed seconds. Every move was my own; no external or automated chess advice, engine analysis, or delegation.


### Benchmark 81 — White versus skill 0, win

Completed 2026-10-01 at 20:37:08 UTC by 23.Qe7#, 45 plies, zero illegal submissions. Result seq 6638, SHA-256 `5397fea666b7c5e47d8d07387c8ccea73a1e65e4d146ffa93ea217709883ea51`, result snapshot `6ad067288cafef7a0cff90952865542b14182ede713a6b4e9082f73898e7d98f`. Saved PGN read back.

Black declined to recapture after 7.Bxe4, giving an extra knight; Bd3 preserved that bishop, and a3/Nxd3/Qxd3 exchanged the remaining black knight. The exposed Ke7 allowed Bg5+/Ke8/Bxd8, winning the queen by a king–queen skewer. Black again declined a recapture, letting Bf6 escape. I retreated Ng5 when ...h6 attacked it, took Be7 when offered and preserved that bishop after another declined recapture. Qxh6 followed only after Bf8's defender had been removed. Qh7/Rg7/Qxg7 took the rook, and Qe7# used Bf6's protection. No actual targeted direct major-piece loss, illegal move, or missed immediate opponent mate was identified. Opponent concessions dominated the material result; unplayed alternatives have not been independently assessed.

All 23 legal move submissions met the 20-second target: 100%, zero overruns. Median 9.013 seconds, mean 9.265, maximum 18.399. Session 20:33:01.237988–20:37:08.852939 UTC. This game meets the implementation criterion; that is evidence of shorter decision work here, not by itself evidence of stronger chess or causation.

Through 81: overall 33W/2D/46L; skill 0 25W/0D/2L in 27; maximum strength unchanged 0W/2D/26L in 28, nominal 1800 unchanged 8W/0D/18L in 26. The unchanged rolling-50 estimator reports 1670 [1550, 1790], 53 rated games total and 28 excluded maximum games. Its estimate decreased despite the latest win; do not report a cumulative or human rating gain. Trial-09 benchmark so far 1W/0D/2L. Continue games 82–84 before the declared endpoint. Observed cumulative whole-goal usage 15,562,640 tokens / 168,428 elapsed seconds. All chess decisions and review were my own; no external advice, automated chess analysis, engine analysis, or delegation.


### Benchmark 82 — Black versus skill 0, win despite an actual queen loss

Completed 2026-10-01 at 20:59:31 UTC by 81...Qg3#, 162 plies / 81 learner moves, zero illegal submissions. Result seq 6803, SHA-256 `26dacc7f9a2f7710b46ac4a12e1f725a9644b2c0f26e4c2a8cadb961e6d1fc12`, result snapshot `51209075b4487085994a823e2553e4140e8cc04ca08b0165ab49f65d2570e7be`. Saved PGN read back. The win is not a clean tactical performance.

Central exchanges and development initially kept material level. I moved the c8 rook when Bg4 attacked it. However, 19...h5 conceded a pawn: after Bxh5, Qe2 protected h5 along f3/g4, so ...Qxh5 would lose the queen to Qxh5. I recognized that only after the pawn capture and used ...Qh7. Further exchanges left Black a pawn behind.

The main target failure was 27...Ne6 28.Bxh6. I had put Qh6 behind Ng5 on Be3's e3–f4–g5–h6 diagonal, and even noted that blocker when choosing the queen square. When I later moved Ng5 to e6 to attack Rd4, I failed to carry forward the line it would uncover. White captured the queen, and ...gxh6 recovered only the bishop. This is a direct queen-for-bishop loss through a vacated line, not a forced tactical concession. The ...Ne6 submission was within the timing target (10.87 seconds displayed), so the clock format did not prevent the targeted error.

White then played h4 and allowed ...Nxd4, followed by b4 instead of a recapture. That returned a whole rook without taking the knight. I preserved the knight, later used ...Nf3+ gxf3 ...Rxh3 to exchange it for the bishop after removing g2's defense, and traded one rook pair. In the resulting R+B versus Q ending, rook activity collected the f4, b4, a2 and f2 pawns while I kept the rook and bishop defended through many checks. These actual defensive choices were useful, but they do not prove that every intervening position was sound or undo the earlier queen loss.

After 70...Rf2+ 71.Kg4 I missed the immediate ...Rxf1 queen capture and instead played ...f5+. White left the queen on f1 again, and 72...Rxf1 took it. I promoted the f-pawn, then used Qg5/Rg1/Qg3# with the rook protecting the mating queen. Opponent concessions rescued the result. The missed queen capture one move earlier is an additional immediate-opportunity omission.

All 81 legal submissions were timed: 66 within 20 seconds (81.5%), 15 over; median 12.481 seconds, mean 14.508, maximum 39.809. Session 20:38:01.627519–20:59:31.625568 UTC. The game fails the 90% implementation criterion; long branches returned in defense and even during the final mating conversion. Preserve every overrun and do not infer uniformly short decisions from the mean.

Through 82: overall 34W/2D/46L; maximum strength 0W/2D/26L in 28, skill 0 26W/0D/2L in 28, nominal 1800 8W/0D/18L in 26. Elo is 1680 [1560, 1800], exactly the trial baseline, with 54 rated games total / latest 50 used and 28 maximum exclusions. Trial-09 benchmark so far 2W/0D/2L, including major-piece/forcing-line failures in 79 and 82 and an immediate mate omission in 80. Games 83–84 remain before the endpoint. Actual cumulative whole-goal usage: 15,681,347 tokens / 169,769 elapsed seconds. No external chess advice, automated chess analysis, engine analysis or delegation was used.


### Benchmark 83 — White versus nominal 1800, win with a missed king fork

Completed 2026-10-01 at 21:13:13 UTC by 47.Qg7#, 93 plies / 47 learner moves, zero illegal submissions. Result seq 6899, SHA-256 `6180e8e51d022a2f5bd0df6dde07d2778fdb1997a08967fcf2830937c21c332b`, result snapshot `21080a5738f4f8c57ded7ea230638af5742a186a65b67251349c98d78d5fb1b8`. Saved PGN read back.

The open Sicilian center initially left equal material. After ...Ne4 attacked Qd2, 15.Nxe4 captured that knight. Black chose ...f6 rather than recapturing; Nxc5/Qxc5 traded for the bishop, Nd3 saved the other attacked knight while attacking the queen, and ...Nxe2+/Qxe2 finished the short exchange with White an extra knight. A commentary phrase mistakenly described a checking threat; I corrected it during play: the queen had been attacked, and White was not then in check. No external move assessment was used.

Be3 supplied support for Nc5, which attacked Qd7 and Be6; Nxe6/Qxe6 simplified to an extra bishop. I explicitly noticed that moving Be3 would uncover Black Qe6 against my Qe2, so Rfe1 first supplied a recapture. Bd4/Qxe2/Rxe2 then traded queens as intended. Bxf6 and Rxd5 collected pawns. After 28.Rxf5, Black played ...Re8 instead of recapturing the rook; Rfe5 preserved it and supported the bishop. These opponent concessions materially contributed to the win.

I then missed a king fork during further simplification. The line Re8+/Rxe8/Rxe8+ allowed ...Kf7, attacking both Re8 and Bf6. Once the fork appeared I saw the problem and used Re7+; ...Kxf6 took the bishop. I had not anticipated that loss before exchanging rooks. This is a real minor-piece oversight, though it left a large rook-and-pawn advantage. No earlier best defense or independently proved first error is claimed. I found no actual direct unreciprocated queen/rook loss, illegal blocked move, or immediate opponent mate in this game; the absence of those particular failures is not a claim of perfect play.

Rxb7/Ra7/Rxa4 removed the queenside pawns. The b-pawn promoted, Kxh2 answered the checking pawn capture, and Qf4/Ra6+/Qf6+/Ra7+/Qg7# completed the rook-supported mate. Black still had an h-pawn, so no stalemate was claimed or inferred during the conversion.

All 47 legal submissions were timed: 39 within 20 seconds (83.0%), eight over. Median 12.707 seconds, mean 14.272, maximum 51.146 (the response to the king fork). Session 21:00:57.449338–21:13:13.999020 UTC. Again the 90% implementation criterion fails, and several final mating decisions also exceeded the target. Useful handling of the earlier vacated queen line in this one position does not establish general transfer.

Through 83: overall 35W/2D/46L; nominal 1800 9W/0D/18L in 27, skill 0 26W/0D/2L in 28, maximum strength 0W/2D/26L in 28. Provisional Elo rises to 1710 [1590, 1830], 55 rated games total / latest 50 used, 28 exclusions. Trial-09 benchmark so far 3W/0D/2L. This temporary 30-point rise over baseline has broadly overlapping uncertainty and is not sustained improvement. Finish game 84 as declared before the trial assessment. Actual cumulative whole-goal usage: 15,749,717 tokens / 170,602 elapsed seconds. All chess decisions and review were my own; no automated chess analysis, external advice, engine analysis or delegation.


### Benchmark 84 — Black versus nominal 1800, loss; trial-09 endpoint

Completed 2026-10-01 21:43:25 UTC by practical resignation after 65.h6, 129 plies, 64 learner moves, zero illegal submissions. Result seq 7031, SHA-256 `0ecc6eb26cf3e49ed03a7b76ba8875be99adf2240066e18fde8612ca08d85856`, result snapshot `8deb9533e8064b29a8870c1a78a2d6706f116030575693813df8b0f2d8e29f4d`. Saved PGN read back. This is a practical resignation, not an engine-certified first losing move.

The middlegame traded all knights and queens. White collected queenside pawns while Black advanced the h-pawn and obtained g3. After ...Re6/Rxe6/fxe6 and ...Bxc6/bxc6, Black had a rook and central/kingside pawns against the rook and dangerous a/c passers. The bishop concession and later rook-for-promoted-queen exchange were deliberate; no soundness claim is made. I have not independently established the best defense at any of these points.

The late race exposed two concrete calculation failures. After 54.Rc3+, ...Kf2 left d2 unprotected and White took it. ...Ra2+ did not force the rook interposition I hoped for: Kd3 preserved both rook and passer. ...Ra8/c8=Q/Rxc8/Rxc8 gave up the rook for the promoted pawn, leaving my connected f/g pawns as compensation. Their apparent proximity to promotion was insufficient. At 62...g2 I allowed Rxf2: although Kg1 geometrically touches f2, White Ke2 prevents Kxf2. The earlier analysis considered promotion continuations without resolving this legal recapture problem. After ...Kh2, Rxg2+ sacrificed the rook to remove the last advanced pawn, and ...Kxg2/h6 left White's h-pawn beyond the black king's reach. No alternative is asserted to win or draw. This is failed pawn-race and king-legality reasoning even though it is not a direct unexplained queen/rook hang.

All 64 legal submissions were logged: 42 within 20 seconds (65.6%), 22 over; median 15.711 seconds, mean 25.552, maximum 396.060. Session 21:14:27.879244–21:43:25.982821 UTC. The long interruption before 54...Kf2 stays included, as the original definition requires; times are elapsed wall time, not pure thought. No rejected moves were recorded.

Through 84: overall 35W/2D/47L. Maximum strength 0W/2D/26L; skill 0 26W/0D/2L; nominal 1800 9W/0D/19L, each over 28 games. Elo 1700 [1580, 1820], 56 rated total / latest 50 used, 28 maximum exclusions. No external chess advice, engine analysis, automated chess analysis or delegation was used.

Trial 09 endpoint: fixed games 79–84 scored 3W/0D/3L. Elo changed 1680 [1560, 1800] to 1700 [1580, 1820]; the broadly overlapping uncertainty and single block do not establish improvement. Target failures recurred in 79 (rook lost after incomplete forcing sequence), 80 (withdrawn knight defender allowed mate; illegal castling), and 82 (vacated bishop line lost queen). Game 83 lost a bishop to a king fork; 84 failed the endgame race. Opponent concessions rescued wins, especially 82. Across the block 196/255 legal moves met 20 seconds (76.86%); only game 81 met the per-game 90% implementation criterion. One additional illegal submission in 80 is retained separately. Both practice sessions also failed the timing criterion. Decision: discontinue the 20-second target, preserve all clock data, and change the content of training to endgame races rather than claim the timing method worked.


Trial 10 declared after 84: bounded endgame race practice, then benchmarks 85–90. Full plan/review in trials/endgame-races-10.md. Practice 10 lost after two promotions were both exchanged away and the h-pawn escaped; no Elo change, no claimed theoretical verdict. Two declared sessions remain. Trial-09 clock target discontinued. Actual whole-goal counter observed: 16,135,991 tokens / 172,232 elapsed seconds.


## Practice 11 — sole remembered repetition, loss by checkmate

Completed 2026-10-01 21:49:24 UTC, 13 session plies, six learner moves, zero illegal submissions. Result seq 416, hash `00d2eaf8c36ed49557a6254dd43fdd841e6502051b588fb44e9feac3ae3c20a2`. PGN read back. Same benchmark-84 ply-116 starting position; opponent chose Rd8 instead of Rc1.

Actual line: 59.Rd8 Kh3 60.Ke4 Kxh4 61.Rh8+ Kg4 62.Rb8 f3 63.Rg8+ Kh3 64.Kxf3 e5 65.Rh8#. The alternative king route removed the h-pawn, but ...f3 and the checking rook drove the king away from that pawn, letting Kxf3 capture it. I then considered an e-pawn advance to draw the white king away from the g-pawn, and missed the immediate mating threat. Rh8# confines Kh3 because White Kf3 controls g2/g3/g4 and my own g3 pawn blocks that square. This is an actual missed mate, referee-confirmed, and another example of a longer race idea displacing the immediate opponent reply. No claim that the earlier position was defensible or that ...e5 was the first losing move.

Both remembered drills lost. No extra repetition will be added; finish the declared third new-position session, then benchmark 85–90 regardless of its outcome. These six own moves finished below the cap. Practice remains excluded from Elo.


## Practice 12 — new constructed rook ending, draw; practice phase complete

Completed 2026-10-01 21:53:04 UTC by referee automatic threefold-repetition claim after 21...Ra6+, 41 session plies, 21 learner moves, zero illegal submissions. Result seq 459, hash `b8812c8df1920c209bdad33e6599634e1f6ced724c37e4d9f2908ab82a1da042`. PGN read back. The position was the declared constructed FEN, not an independently evaluated theoretical exercise.

After ...Ke5, Rc5+ drove the king away and Rxf5 took the f-pawn. ...h4/...g3 and ...Rh8 preserved the remaining pawns temporarily. White advanced b5/a6/a7; I used ...Kc5/...Kxb5 and ...Ra8/...Rxa7 to remove both passers without giving up the rook. Leaving h8 conceded h4 to Rxh4. ...Ra3+ defended g3 while checking; I brought the king through c5/d5/d4. White eventually used Rxg3 with Kf4 protecting that rook. I declined the rook exchange because the resulting pawn ending looked unfavorable, preserving my rook with ...Ra1. This is my own assessment, not a proved endgame value.

With rook against rook and g/h pawns, ...Ra5+/...Ra6+ kept checking the exposed white king from the side. White alternated among g6, f5 and e6 and the referee claimed repetition. The recorded draw does not prove a forced draw against every defense, and the earlier pawn losses are not erased. No direct unreciprocated major-piece loss, illegal move, or actual missed immediate mate was identified in this session.

Trial-10 practice total: 0W/1D/2L, 34 learner moves, 69 session plies, zero illegal submissions. All three finished below their 25-own-move caps and by 21:53:04, before the 22:29 combined ceiling. The two remembered drills retained the same starting position and every loss; the new exercise was not repeated. Practice 11's missed rook mate is a clear failure, while practice 12's side-check draw is one useful defensive result, not established transfer. No further practice is added before the declared fixed benchmark 85–90. Continue that block with the trial-10 endgame focus and ordinary referee commands; the trial-09 20-second target remains discontinued.

Elo remains the benchmark-84 value 1700 [1580, 1820], with 56 rated games total / latest 50 used. No sustained improvement is established. All moves and reviews were my own, without external chess advice, automated chess analysis, engine evaluation, or delegation. Actual observed cumulative whole-goal usage after these sessions: 16,173,564 tokens / 172,631 elapsed seconds.


## Benchmark 85 — White versus maximum strength, loss

Completed 2026-10-01 22:00:50 UTC by practical resignation after 26...Bxb7; 52 plies, 26 own moves, zero illegal submissions. Result seq 7087, hash `3440787a1b3e65dd2a8f4367691b251e9265fc6d1abf6e048900d9775261bded`, snapshot `a23ef28ba03d5e1a54afb2429f03f3c4152d5250de0477e0aaa37193e4d8ed35`. Saved PGN read back. No best-defense or first-losing-move certificate is claimed.

The queen-pawn opening exchanged the central pawns and then queens. ...Qd5 attacked Rh1; Nf3 blocked that diagonal and allowed Qxd1+/Kxd1. Black's subsequent bishop checks and rook development kept my king moving. ...Bb4 pinned c3, so Bd2 supplied a blocker before the knight exchange; ...Nxd4/cxd4/Rxd4/Bxb4/Rxb4 left me a pawn down. The recapture on b4 was understood, not a surprise piece loss. Black's active rook then took a2 and e2 while my rooks and king moved into exposed positions.

After ...Re5, 24.Rhb1 enabled ...Bc6+, skewering Kf3 and Bg2. I recognized the bishop loss once the check occurred, but had not accounted for it before Rhb1. Kg4/Bxg2 lost that bishop. The final 26.Rxb7+ was a separate direct rook blunder: I considered king replies and follow-up checking sequences but omitted the checking rook's capture by Bg2 along f3/e4/d5/c6/b7. Black played ...Bxb7. Rb1's protection did not rescue the tactic because Kb8 defended b7, so Rxb7+ would allow Kxb7. Resignation followed with R+3P against 2R+B+5P. A check being answerable by capture remains an actual recurring failure.

No pawn-promotion race occurred, so this game does not directly test the trial-10 race exercise. It does show another failed transfer of the broader immediate-capture discipline, with an actual major-piece loss. The result is preserved; no extra practice or altered benchmark opponent is introduced mid-block.

Through 85: overall 35W/2D/48L. Maximum strength 0W/2D/27L in 29 games; skill 0 26W/0D/2L and nominal 1800 9W/0D/19L, each in 28. Elo remains 1700 [1580, 1820], 56 rated total / latest 50 used, 29 maximum exclusions. Trial-10 benchmark currently one loss; finish 86–90 before its endpoint. No short-decision timing target applies. Observed cumulative whole-goal usage 16,298,116 tokens / 173,091 elapsed seconds. All decisions and review were my own; no external chess advice, automated chess analysis, engine evaluation or delegation was used.


## Benchmark 86 — Black versus maximum strength, loss

Completed 2026-10-01 22:09:44 UTC by practical resignation after 27.Qxa8+, 53 plies, 26 own moves, zero illegal submissions. Result seq 7143, hash `61e7175ba05b0409b11e5c062b254b2a231cbfc4c90b4210823a0d52081928e4`, snapshot `d1b0ff3a430dadbed97736ff21299a2347eee0b6e8818a6312be4f0d7ad44d14`. Saved PGN read back. No independent first-losing-move or optimal-defense claim.

The closed king-pawn opening reached ...c4/b4 and sent Na5 to b7. The ...a5/axb5/axb4 sequence opened the a-file, but White's b6 pawn attacked Qc7 and constrained my queen and knight. I moved Qc8 and recaptured Rxa8 with Qxa8; cxb4 left White an extra pawn. ...Qa2 attacked Bc2 but Qc1 defended it; Nc3 then attacked the queen. I chose ...Qa6 without foreseeing how Ra1 would confine it. After Qb2/f5/Ra1 I recognized that the direct queen retreat squares were occupied or attacked and chose ...Qxa1+/Qxa1 as a queen-for-rook concession. I considered interpositions but did not establish a sound saving line; this is not a claim that the concession was objectively forced.

The last move was an additional direct rook blunder, separate from the queen problem. After ...f4/Bc1 I played 26...Ra8 to attack Qa1, imagining queen retreats. I failed to apply the reciprocal attack along that same open file: the rook had no defender and White simply played 27.Qxa8+. This was not an intended exchange or a surprise remote tactic. I resigned with no major pieces against White's queen, in addition to the pawn deficit. Both the confined queen and the undefended rook are concrete failures preserved in the record.

White's advanced pawn mattered to the queen's confinement, but no promotion race or rook-only ending occurred. Thus the bounded endgame practice has not supplied positive transfer evidence in either maximum-strength game. The direct-capture failure recurred despite prior explicit notes; do not call the new trial effective.

Through 86: overall 35W/2D/49L. Maximum strength 0W/2D/28L in 30 games; skill 0 26W/0D/2L and nominal 1800 9W/0D/19L, each in 28. Elo unchanged at 1700 [1580, 1820], 56 rated total / latest 50 used and 30 maximum exclusions. Trial-10 benchmark currently 0W/0D/2L; finish 87–90 before the declared endpoint. Observed cumulative whole-goal usage: 16,475,357 tokens / 173,625 elapsed seconds. All chess decisions and review were my own; no external advice, automated chess analysis, engine evaluation or delegation.


## Benchmark 87 — White versus skill 0, win

Completed 2026-10-01 22:19:35 UTC by 25.Qa8#, 49 plies, 25 own moves, zero illegal submissions. Result seq 7195, hash `6b0cf96f954febb186a77e4fc51b63e88e1bcbc6524d563e2b75a87188cb113d`, snapshot `8464d4e26ce1ef5b896ebbf26a2beba06a99dae99e3433a2223304ee5dd06f1e`. Saved PGN read back; terminal mate is referee-confirmed.

Black's ...Nxe4 and ...Nd6 allowed Qe2/Nc6+, a discovered check with a queen fork. After ...Qe7, Nxe7 captured the queen. Black chose ...a6 rather than recapturing; Nd5+ preserved the knight. I moved that knight when ...c6 attacked it, took the undefended Nc4 with Qxc4, and answered ...d5 by moving the attacked queen to d3. ...g5 attacked Bf4, so Be5 preserved it while attacking Rh8. ...Bf5 attacked Qd3 but was itself capturable; Qxf5 removed that bishop, followed by Bxh8.

Nd2 cleared the queenside castling path, and O-O-O completed castling legally. Qxf7 collected a pawn; Bd3 and Rhe1 completed development. Be5 offered a supported exchange, but ...Kc8 allowed Bxd6 without an immediate recapture. Qxa7 took the remaining rook. Re7 covered the king's escape along the seventh rank, and Qa8# completed the mate with Bd6 also controlling c7/b8. No actual direct unreciprocated queen/rook loss, illegal move, or missed immediate opponent mate was identified in the played line. Unplayed branches were not independently evaluated, and this is not a claim of optimal play.

Opponent concessions supplied the decisive advantage. This was not a promotion-race test, and an easy material conversion after winning a queen does not establish endgame transfer or stronger general play. Preserve the favorable result alongside the two previous maximum-strength losses.

Through 87: overall 36W/2D/49L. Skill 0 27W/0D/2L in 29; maximum strength 0W/2D/28L in 30; nominal 1800 9W/0D/19L in 28. Elo 1710 [1590, 1830], 57 rated total / latest 50 used, 30 maximum exclusions. Trial-10 benchmark so far 1W/0D/2L; games 88–90 remain. The 10-point increase from baseline has broadly overlapping uncertainty and is not sustained improvement. Observed cumulative whole-goal usage: 16,517,983 tokens / 174,216 elapsed seconds. All decisions and review were my own; no external chess advice, engine evaluation, automated chess analysis or delegation.


## Benchmark 88 — Black versus skill 0, win

Completed 2026-10-01 22:35:06 UTC by 41...Rd1#, 82 plies, 41 own moves, zero illegal submissions. Result seq 7280, hash `d826034ec6f9b700b4f5a35de34218d6889e920fbf4361e8acae63316539f02d`, snapshot `b5b3a6af516f9b1671d9a9c00dbe1a5a6217281d64df500fc5fd9245f5bacb48`. Saved PGN read back. The mate is referee-confirmed; no optimal-play claim.

White declined to recapture after ...exd4. ...Bc5 both supported that pawn and removed the potential e5 pawn fork of Bd6/Nf6. I answered the later queen, knight and bishop attacks with ...Qg6, ...Nf6 and ...Bb6. White's Ne5 removed Nf3's defense of Bg5, so ...Qxg5 captured it. ...Qxf4 answered the f-pawn attack by taking that pawn; ...fxg6 captured the knight that subsequently attacked the queen. Opponent concessions supplied a large advantage.

After ...Qxh3+/Nh2, the pinned knight could not take ...Bxg4. I chose ...Bf3+ after explicitly considering both Kg1 and Qxf3. White took the bishop; ...Qxf3+/Nxf3 traded queens, intentionally leaving the bishop unrecovered. This was a material concession for simplification from a large lead, not an unexpected loss or a proved necessity. The subsequent ...Nxe4/Ne5/...Rxe5/Rxe4/...Rxe4 exchanged the knights and won a rook. ...Rf8 was defended by Kg8; Rxf8+/Kxf8 removed White's final rook as intended. This differs from game 86's undefended reciprocal-file error.

The passed d-pawn then supplied a relevant, limited endgame instance. After ...d3+/Kf1 I placed the rook on d4 behind the pawn before advancing ...d2+. The king blockaded d1, so I brought my king forward and removed White's remaining pawns. When White moved Kc2, ...d1=Q+ was protected along the d-file by Rd4, preventing Kxd1. Qb3+ was protected by c4; ...Rd1# was protected by Qb3. I identified the own c4 pawn as a blocker before considering a rook capture along the fourth rank and made no illegal submission.

No unanticipated direct queen/rook loss or actual missed immediate mate was identified. The defended promotion is one correctly handled case, but White had already lost all pieces and posed no competing promotion threat by then. It does not validate performance in a contested race like game 84 or establish general improvement.

Through 88: overall 37W/2D/49L. Skill 0 28W/0D/2L in 30; maximum strength 0W/2D/28L in 30; nominal 1800 9W/0D/19L in 28. Elo 1720 [1600, 1850], 58 rated total / latest 50 used, 30 maximum exclusions. Trial-10 benchmark 2W/0D/2L; complete nominal-1800 games 89–90 before the endpoint. The small rating rise is provisional, with overlapping uncertainty. Observed whole-goal usage: 16,677,847 tokens / 175,147 elapsed seconds. All chess decisions and review were my own; no external advice, engine evaluation, automated chess analysis or delegation.


## Benchmark 89 — White versus nominal 1800, loss

Completed 2026-10-01 22:54:44 UTC by practical resignation after 33...Bh2+, 66 plies, 33 own moves, zero illegal submissions. Result seq 7349, hash `c1c106cc2d3263a13504d49790bcf1306a5e3724b2992b5f4b9d14a98460df14`, snapshot `4603afda667191547db7500d414371d195a0f680781f05020d6b4a5d58672ce0`. PGN read back. No independent optimal-defense or first-losing-move claim.

The Scandinavian opening reached d5/Nb4/Bc4/Bf5. Nd4 supplied a defender for c2 while attacking the bishop. I castled, but ...Bxd5/Nxd5/Nbxd5 removed the advanced pawn, leaving a pawn deficit. Further development and the ...Nxe3/Qxe3 exchange left B+N each with queens and rooks. I answered ...Bb4's attack on Re1 with c3 and moved the queen when ...h6 attacked it.

The f-pawn advance failed to produce a sufficient attack. After f4/...Nd7/f5/...Bd6, Ne5 was pinned to Qg3 and attacked twice. I explicitly rejected knight retreats that would expose the queen. The chosen f6 threatened the king but ...Nxf6 took that pawn; I then moved Qe3 to unpin, now two pawns down. This was a considered concession, not a claimed sound or forced sacrifice.

The queen was then driven through Qe4 and Qd4. After ...b4, Nc4, ...Bg3, Rf1, ...bxc3, bxc3 and ...c5, I found its direct retreats occupied or attacked. My own Nc4, Bd3 and c3 pawn restricted its movement, while Nd5, Bg3 and f5 covered key remaining squares. I had not anticipated that confinement when selecting Qd4 and Nc4. I chose 32.Qe3 knowing ...Nxe3 would capture it; 33.Nxe3 recovered the knight, and ...Bh2+ preceded resignation. Final material was 2R+B+N+4P against Q+2R+B+6P. A sound alternative at move 32 has not been independently ruled out, so do not call the concession objectively forced.

This is another actual queen-for-minor-piece loss after failing to anticipate confinement, alongside game 86. No promotion race occurred. The endgame practice does not establish improvement in these middlegame decisions, and the trial already contains major-piece failures in 85, 86 and 89.

Through 89: overall 37W/2D/50L. Nominal 1800 9W/0D/20L in 29; skill 0 28W/0D/2L and maximum strength 0W/2D/28L, each in 30. Elo 1710 [1590, 1830], 59 rated total / latest 50 used, 30 maximum exclusions. Trial-10 benchmark 2W/0D/3L, with game 90 still due before its endpoint. Observed cumulative whole-goal usage 16,848,644 tokens / 176,325 elapsed seconds. Every move and review was my own; no external chess advice, engine evaluation, automated chess analysis or delegation.


## Benchmark 90 — Black versus nominal 1800, win

Completed 2026-10-01 23:09:28 UTC by 41...Rc1#, 82 plies, 41 own moves, zero illegal submissions. Result seq 7434, hash `308b2fdd9e2c6e99b0c594eec3d6324ec9c408398aaa70d904a8b9b3aa17339a`, snapshot `7da82978c232c844c59ae9e879d6b614905db72b2fcbab5695cea03d5302be66`. Saved PGN read back; mate is referee-confirmed. No optimal-play or first-losing-move certificate.

Against e3/Be2 I developed with ...d5, ...Nf6, ...e6, ...c5, ...Nc6 and castled. White's knight retreats allowed ...e5 and normal development. The c4/d4/exd4/exd4 sequence produced a passed d-pawn. I exchanged the blockading Nd3 with ...Bxd3 and the dark bishops with ...Bd6/Bxd6/Qxd6. ...Ne5 attacked the queen; ...Nxf3+/gxf3 weakened the white king's cover.

The central sequence was a useful calculation success: ...d3/Bxd3/Rxe1, followed by White's c5 instead of recapturing, permitted ...Rxf1+/Kg2/...Qxd3/Qxd3/...Rxd3. I carried the queen exchange through the rook recapture and emerged with two rooks and a knight against pawns. White's refusal to recapture the first rook and subsequent king move supplied a much larger gain than the initially considered line; this is not proof that all defenses lose the same amount.

The conversion then contained an actual unanticipated rook loss. Rf1 was within White Kg2's capture reach. While concentrating on pawn captures and avoiding other king attacks, I left that rook loose through ...Rc3 and ...Rxa3; 28.Kxf1 captured it. Neither Rd3/Ra3 nor Nf6 defended f1. This was not a deliberate sacrifice for simplification. The remaining rook, knight and pawns still supplied a large advantage, but the win does not erase the failure to inspect the unmoved rook.

I removed b4, f4, f3 and c5, then promoted the a-pawn with the white king far away. White's lone h-pawn could not produce a competing promotion. ...Qe5+/Kh1/...Qg3 left h5 as the pawn move before ...Rc1#. This was an easy promotion/conversion after overwhelming material gain, not evidence of solving a contested race. All moves and review were my own, without external chess advice, engine evaluation, automated chess analysis or delegation.

Through 90: overall 38W/2D/50L. Maximum strength 0W/2D/28L; skill 0 28W/0D/2L; nominal 1800 10W/0D/20L, each in 30 games. Elo 1720 [1600, 1840], 60 rated total / latest 50 used, 30 maximum exclusions. Observed cumulative whole-goal usage 16,938,003 tokens / 177,221 elapsed seconds.


## Trial 10 endpoint — revise; no sustained improvement established

The declared benchmark block 85–90 finished 3W/0D/3L: both maximum games lost, both skill-0 games won, nominal 1800 split 1–1. Elo moved from 1700 [1580, 1820] to 1720 [1600, 1840], with broadly overlapping intervals. The trial does not establish sustained improvement. Practice was 0W/1D/2L, with a missed mate in practice 11. Benchmark games 88 and 90 contained correctly completed promotions against opponents already without pieces; neither tested a contested rook-sacrifice race like game 84.

Substantial safety failures remained in four of the six benchmark games: 85's bishop skewer and captured checking rook, 86's queen confinement and undefended rook, 89's queen confinement, and 90's missed king capture of an unmoved rook. The central exchange calculation in 90 was better handled, but did not generalize even to preserving the resulting material. Retire the race-focused trial as the main intervention; preserve its notes and all results. The next bounded trial will target recognizing the opposing king as an active attacker during sparse-board conversions, with recorded practice followed by another fixed six-game evaluation. No success claim is made from this choice itself.


## Practice 13 — remembered king-capture position; win with another rook error

Completed 2026-10-01 23:19:06 UTC by 40...Qf2#, 29 session plies, 15 own moves exactly at the declared cap, zero illegal submissions. Result seq 490, hash `d74bbd8089aa97714f8b509d8c650f64c0e90191a854d98eda32bd4fe30b8dc0`. PGN read back. This was the declared benchmark-90 ply-51 position, against practice skill 20, excluded from Elo.

26...Re1 corrected the remembered exposure to Kg2. White's c6/b5/a4 advances allowed ...bxc6/...cxb5/...bxa4. I then tried to connect the rooks on the third rank with 30...Ree3, and missed f2's direct capture onto e3. 31.fxe3 took the rook; ...Rxe3 recovered only the pawn. This was an unanticipated major-piece loss despite the king-focused cue, not an intended sacrifice. It is evidence that the narrow cue is insufficient for overall safety.

I did respond to later actual king attacks: Kf2 attacked Re3, prompting ...Rc3; Kd2 attacked Rc3, prompting ...Rc8. The c-file cutoff prevented the king from reaching the a-pawn, which promoted. ...Rc2+/Kg3/...Qe5+/f4/...Qe1+/Kf3/...Qf2# finished within the move cap. Rc2 protected the final queen on f2 from Kxf2, while Nf6 covered e4/g4. No king captured a major piece in this drill, but the rook lost to a pawn remains a failure. This remembered-position win is not benchmark transfer. Two declared new-position drills remain; no extra repetition is added.


## Practice 14 — first constructed conversion, win without a major-piece loss

Completed 2026-10-01 23:23:56 UTC by 11.Rb8#, 21 session plies, 11 own moves, zero illegal submissions. Result seq 513, hash `585208e824b3061481751961e01bda2b12b8bc59fcf2f7daa82e10bab6b3a4fd`. PGN read back. Used the declared White-to-move constructed FEN against practice skill 20; no repeat or benchmark score.

Rh8 moved the initially exposed Rd8 away from Kc7. Rh5/Rxe5+ removed the e-pawn. Rbxb5 removed the other pawn while Re5 defended b5 against Kc6. After ...Kd6, I kept the two rooks' mutual protection in view: immediately moving the other rook to give a check could leave the nearer rook capturable. Rh5 and Rbf5 moved them away from the approaching king. Rh6 cut off the sixth rank; Ra5/Ra7 cut off the seventh. Against Kg8 I chose Rb6 before Rb8#, avoiding the adjacent, undefended Rh8 check.

Both rooks survived and the referee confirmed mate. No unexpected king capture, pawn capture of a major piece or other direct major-piece loss was identified. This is a successful deliberately simple constructed drill, not a result from a full game or proof of benchmark transfer. The earlier rook error in practice 13 remains. Finish the third declared drill, then return to benchmark 91–96 without adding favorable repetitions.


## Practice 15 — second constructed conversion, win; practice phase complete

Completed 2026-10-01 23:28:06 UTC by 12...Rg1#, 23 session plies, 12 own moves, zero illegal submissions. Result seq 538, hash `f11a6f28c154a997eabd682a3d5f0da91d5e358d9c4f2961678594b30ae9a42b`. PGN read back. Used the declared Black-to-move constructed FEN against practice skill 20, without repetition.

...Ree6 moved the initially exposed Re1 away from Kf2. When d5 attacked Re6, ...Re5 preserved it before ...Rxd5. I played ...Rd4 before ...Rgxg4 so the capturing rook had support from the other rook. Against Ke3 and Kf3, ...Ra4 and ...Rgb4 preserved the mutual defense while relocating the rook nearest the king. ...Ra3 cut off the third rank; ...Rh4/...Rh2+ cut off the second. Against Kb1, ...Rg3 moved the remaining rook away from the king before ...Rg1#. Both rooks survived. No unexpected king capture, pawn capture of a major piece or other direct major-piece loss was identified in the played line; mate is referee-confirmed.

Trial-11 practice total: 3W/0D/0L, 38 own moves and 73 session plies, zero illegal submissions. All sessions finished within their 15-own-move caps and by 23:28:06, before the combined 23:43 ceiling. There were no extra repetitions. The two new, deliberately simple constructed conversions were completed with both rooks intact. The remembered drill still lost a rook to fxe3, so the narrow king-focused cue did not ensure overall safety. These heavily favorable starting positions and practice wins do not establish improved full-game play.

Return now to the declared benchmark block 91–96 with no extra practice before its endpoint. Elo remains 1720 [1600, 1840], 60 rated total / latest 50 used, 30 maximum exclusions. The previous trial remains unsuccessful at establishing sustained improvement. Observed cumulative whole-goal usage after practice: 17,021,115 tokens / 178,327 elapsed seconds. All moves, constructions and assessments were my own; no external chess advice, delegated analysis, engine evaluations or automated chess analysis were used.


## Benchmark 91 — White versus maximum strength, loss

Completed 2026-10-02 01:58:03 UTC by practical resignation after 36...Kh7; 72 plies, 36 own moves, zero illegal submissions. Result seq 7510, hash `d5a4ead4b4ae3c8b6b35212bdc25171ce8fc0a53b7b9bbeb16d65ea98dc05bf3`, snapshot `4f4c0abbeb24571239781300e0a70f8df313ef78c3074dfb1dbaee174a8a132c`. Saved PGN read back. The game resumed from its existing position after the user's Continue; elapsed wall time includes that interruption. No independent best-defense, forced-promotion or first-losing-move certificate is claimed.

The London-style opening reached a developed, materially level position. I exchanged the e5 knight, defended Nf3 with Be2/Qe2, and challenged the center with c4/cxd5. The concrete pawn error was 20.a4: I considered ...b5 reactions but omitted Bc6's direct capture along b5/a4. ...Bxa4 took the pawn and also attacked Rd1 along b3/c2/d1. Rxd8/Rxd8 answered that rook attack without an additional material loss. The second pair of rooks was exchanged with Rd1/Rxd1+/Qxd1.

After ...Qe6, Bc2 defended b3. Qa1 sought activity, but ...Nb4 attacked the bishop and guarded a6. Qc3 supported Bc2 and b3, while leaving Nf3 without the queen's former protection. ...Bxf3/gxf3 and ...Nxc2/Qxc2 traded the remaining minor pieces and left my king exposed with doubled f-pawns. These were recaptured exchanges, not lost minor pieces, but the king shelter deteriorated.

The queen ending remained one pawn down. ...c4/bxc4/Qxc4 left Black with a and b passers. I declined Qxc4/bxc4 because my own calculation judged the pawn ending dangerous; that is not a proved theoretical loss. After Qd2/...b4/Kg2/...b3/f4, ...Qc2 attacked my queen while b3 protected the black queen and c2 controlled the promotion square. Qd8+/Kh7 did not yield a continuation I could hold or a perpetual check I could establish. I resigned with Q+4P against Q+5P. The resignation is a practical decision, not proof that every defense fails or that f4 was the first decisive error.

No direct queen/rook loss or actual king capture of a major piece occurred. The specific two-rook conversion skill from practice was not tested. The a4 capture omission and failed queen-ending defense remain concrete weaknesses; this loss does not establish transfer.

Through 91: overall 38W/2D/51L. Maximum strength 0W/2D/29L in 31; skill 0 28W/0D/2L and nominal 1800 10W/0D/20L, each in 30. Elo remains 1720 [1600, 1840], 60 rated total / latest 50 used, 31 maximum exclusions. Trial-11 benchmark is 0W/0D/1L; complete games 92–96 before the declared endpoint. All decisions and review were my own; no external chess advice, delegated analysis, engine evaluation or automated chess analysis.

Usage bookkeeping: the goal tool currently reports blocked and an older counter of 17,035,946 tokens / 178,558 seconds (updated at 2026-10-01 23:31:57 UTC), rather than accounting for the resumed work. No new cumulative usage entry is submitted from that stale counter. The user's Continue remains the authorization to continue the chess task; the measurement files and estimator are unchanged.


## Benchmark 92 — Black versus maximum strength, loss

Completed 2026-10-02 02:16:52 UTC by practical resignation after 27.Qxh7+; 53 plies, 26 own moves, zero illegal submissions. Result seq 7565, hash `6f3802cdfa2d6883deaabe90a45864adebe97f0027f642a64a5cf520af1facda`, snapshot `3173a17bab5a33ea8163ec7191d26d0d6f66492b736e4786d4d8c305caa2cd78`. Saved PGN read back. No independently established first losing move or forced-loss certificate is claimed.

The advance Caro-Kann reached a developed position with both kings castled. Against Neg5, ...Bxg5/Nxg5 and ...g6 answered the threat on h7. After 16.Nxe6 forked Qd8/Rf8, I chose ...Nxe5, attacking Qd3, followed by Qh3/...fxe6/Qxe6+/...Rf7/Qxe5. This was my own calculated exchange sequence and left me one pawn down; I do not claim it was best defense.

The clear minor-piece loss was a vacated defender: 19...Nf6 left the knight protected by Qd8 and Rf7. 20...Rg7 defended g6 but removed the rook's protection of Nf6. After Be3, 21...Qc7 intended to remove the queen from the pin while forgetting that the queen was now the knight's remaining defender. 22.Qxf6 took the knight. This was an unanticipated loss, not a sacrifice.

...Rf8 and ...Rf5 chased the queen; Qh6/...Qc6/Rad1 followed. I then played 25...Rh7 to attack Qh6 while overlooking the checking interruption 26.Rd8+. Moving the rook away from g7 also opened Qh6's diagonal to f8, so an imagined ...Rf8/Rxf8+/Kxf8 recapture was illegal: the king could not capture onto f8 under the queen's attack. I recognized this only after the check. 26...Kf7 left Rh7 undefended, and 27.Qxh7+ actually captured it. I resigned down a rook, bishop and pawn: Q+R+4P against Q+2R+B+5P.

There was no direct opposing-king capture of a major piece and no two-rook conversion. Nevertheless, the actual rook loss after a checking reply displaced its defending king, and the illegal imagined king recapture, show that the narrow practice did not transfer to general piece safety. Both this rook loss and the earlier knight loss count against the trial.

Through 92: overall 38W/2D/52L. Maximum strength 0W/2D/30L in 32; skill 0 28W/0D/2L and nominal 1800 10W/0D/20L, each in 30. Elo remains 1720 [1600, 1840], 60 rated total / latest 50 used, 32 maximum exclusions. Trial-11 benchmark is 0W/0D/2L; games 93–96 remain before its declared endpoint. All play and review used my own reasoning and the referee; no external move advice, delegated analysis, engine evaluations or automated chess analysis.


## Benchmark 93 — White versus skill 0, win

Completed 2026-10-02 02:25:03 UTC by 29.Qh7#, 57 plies, 29 own moves, zero illegal submissions. Result seq 7624, hash `2f273cc6e149699a88698d7b0f9a5265a8de058a448e5910662d82911f6313ad`, snapshot `d99f57f58748300d3e1732295c06ac5636408081f9c14d0b6e18a61c698052af`. Saved PGN read back.

After the intended ...Nxg3/hxg3 exchange, ...dxc4/Bxc4 and the queenside advances, I relocated the bishop to c2 and the attacked c3 knight through d1 to e3. Rad1 and d5/dxe6 opened the d-file; ...fxe6 left an isolated e6 pawn. Nd4, f4 and e5 gained tempi against the queen. 24.Nxe6 won that pawn while attacking Qf8. After ...Qf7 attacked the knight, 25.f5 provided a pawn defender. Black nevertheless played ...Qxe6, and fxe6 took the queen. ...Bf3 then lost the bishop to Qxf3. Qe4 answered ...Rf8 and established the queen/bishop battery; after ...h6, Qh7# was referee-confirmed. Bc2 protected the queen from the king, e6 covered f7, and Black's own rook occupied f8.

No direct queen/rook loss or unexpected opposing-king capture occurred. The g3 bishop was exchanged for a knight, and the e6 knight was exchanged for Black's queen; neither was an unreciprocated piece loss. The win relied on major skill-0 errors and never reached the sparse conversion targeted by the trial. It does not validate that specific skill or establish sustained improvement.

Through 93: overall 39W/2D/52L; maximum 0W/2D/30L in 32, skill 0 29W/0D/2L in 31, nominal 1800 10W/0D/20L in 30. Current Elo 1710 [1590, 1830], 61 rated total / latest 50 used, 32 maximum exclusions. The estimate fell despite this win because the fixed rating window changes its contents; the estimator is unchanged. Trial-11 benchmark 1W/0D/2L; games 94–96 remain. All moves and review were my own, using the referee and no external chess assistance or automated analysis.


## Benchmark 94 — Black versus skill 0, win

Completed 2026-10-02 02:31:53 UTC by 26...Qc2#, 52 plies, 26 own moves, zero illegal submissions. Result seq 7678, hash `646bdbe7bc50082dc17487a86a24924f639abc39c669857749f232896d6b9526`, snapshot `2fe009f032a703576ec828f3c0d757ec2510d6429c055bf7d83f18be8bda4e35`. Saved PGN read back.

...a5/...axb4/...bxc3 undermined White's attempt to hold c5, and ...Bxc5 recovered the central pawn. After ...O-O, Nxc6/...bxc6 and Nxc3 left me one pawn ahead. ...Ba6/...Bxd3 and ...Bxa3 won both bishops when White declined recaptures. ...Bb4 saved the attacked bishop; after Kd2 attacked Bd3, ...Bc4 moved it to a square protected by d5. ...Ne4+ and ...Nxc3 took the remaining knight. Qd4 allowed ...Ne2+/...Nxd4+, the king/queen fork. I moved the knight away from the e3 pawn with ...Nb3, took Ra1 with ...Nxa1, and took the other rook after Rd3 with ...Bxd3. ...Qf6+/...Qc3+/...Qc2# finished against a pieceless opponent. Bd3 and Na1 both protected the final queen from Kxc2.

No direct queen/rook loss or unexpected king capture occurred. All black major pieces survived, but this was not a contested two-rook conversion: White's repeated failures to recapture and the queen fork supplied a very large advantage. Moving Bd3 from the king's attack and protecting the final queen were relevant local decisions, not proof that trial 11 improves full-game strength.

Through 94: overall 40W/2D/52L; maximum 0W/2D/30L, skill 0 30W/0D/2L (32 each), nominal 1800 10W/0D/20L in 30. Elo 1720 [1600, 1850], 62 rated total / latest 50 used, 32 maximum exclusions. Trial-11 benchmark 2W/0D/2L; finish 95–96 before reviewing the trial. No external chess assistance, delegated moves, engine evaluations or automated chess analysis.


## Benchmark 95 — White versus nominal 1800, loss by mate

Completed 2026-10-02 02:45:17 UTC by 32...Qf1#, 64 plies, 32 own accepted moves, one illegal submission. Result seq 7745, hash `d934545a92c7ec4da0e6b14cae03b5c73b19eebc6f4f53733fc65c51081905ba`, snapshot `7211c14b9ac73aefc083a0b0aa1827cefaf6b2d484ed4a06016cca53862217d7`. Saved PGN read back. Before 10.Rd1, I submitted illegal queenside castling: Qd8 controlled the transit square d1. The referee rejected it, and I corrected the move without a second illegal submission.

The early central exchanges won a pawn. After completing development and castling kingside, Nd5/Nxf6+ and e5 gained tempi against the queen. Bxc6/bxc6 left doubled c-pawns. Nd4/...c5/Nc6/...Qe6/Qxc5 won the advanced pawn, and Nd4 answered the double attack after ...Bb7. ...Qg4 threatened mate on g2; g3 delayed it, ...Qh3 renewed it, and f3 blocked the bishop diagonal with knight support. Re3 added a defender to f3.

Qb5 attacked the loose bishop. After ...c5, Qxb7 took it, but ...Rcd8 attacked and pinned Nd4. Red3 arranged rook recaptures while removing the rook's protection of e5; ...Rxe5 actually took that pawn. I then calculated Nc6/...Rxd3/Rxd3/...Re1+/Kf2 and incorrectly treated the king's first escape as sufficient. I failed to continue to ...Qf1#. The rook on e1 protected the mating queen and covered e3; my own f3/g3 pawns occupied potential king escapes. I recognized this continuation only once ...Re1+ was on the board. Kf2 was followed by referee-confirmed ...Qf1#.

I was still a knight and pawn ahead at mate. This was a failure to finish a forcing checking line, not an unavoidable consequence of being materially behind. No independent first-losing-move or best-defense claim is made. The rook on d3 was exchanged and recaptured, not lost without compensation; no opposing king captured a major piece. Nevertheless, the checking sequence defeated the conversion, and the trial's narrow king-capture practice did not address it. The material gain and earlier defensive moves do not count as successful transfer.

Through 95: overall 40W/2D/53L; maximum 0W/2D/30L and skill 0 30W/0D/2L (32 each), nominal 1800 10W/0D/21L in 31. Elo 1710 [1590, 1830], 63 rated total / latest 50 used, 32 maximum exclusions. Trial-11 benchmark 2W/0D/3L. Finish game 96 before the declared review. All play and review used my own reasoning and the referee, without external chess advice, delegated analysis or automated chess analysis.


## Benchmark 96 — Black versus nominal 1800, loss by mate

Completed 2026-10-02 02:59:15 UTC by 32.g6#, 63 plies, 31 own moves, zero illegal submissions. Result seq 7810, hash `40d01b845aacae9b18bc620b71a19e8a162a079d11dc4601d204b82962901990`, snapshot `b7f950ba31d505eb28584533c93af6a68b7a0763b6760c7701ff348e2ffa1aec`. Saved PGN read back.

The opening bishop/knight exchange on g6 and the central pawn exchanges were recaptured normally. ...Ne4/Nxe4/...dxe4 was also a recaptured knight exchange. After White's h-pawn advance and ...gxh5/g5/...Qg6/Rxh5, I played 20...Ne5 to seek ...Nd3+ against the king and rook. I overlooked the White pawn still on d4. 21.dxe5 took the knight; ...Bxe5 recovered only the pawn. The bishop/rook support of e5 did not make this a favorable exchange. This was an unanticipated minor-piece loss, not an intended sacrifice.

...Rac8/Rxc8/...Rxc8 exchanged one rook each. ...f5 defended e4 and opened f7; ...Bxb2 won a pawn. After Qb5 attacked the bishop, ...Bd4 allowed Qd5+, checking the king and attacking that bishop. ...Qf7 answered the check but left the queen dependent on Kg8. White instead played Bxe4; my ...fxe4 captured that bishop while overlooking the stronger checking continuation. 29.Rh8+ forced my legal ...Kxh8, displaced the queen's defending king, and 30.Qxf7 actually took the queen. I recognized the deflection only after Rh8+ was played. This queen-for-rook loss was not an intended concession in the earlier calculation.

...Rc7 chased the queen but vacated the back rank. Qe8+/...Kh7/g6# followed. Qe8 supported the mating pawn on g6, the newly opened Bd2–h6 diagonal removed h6, and my own g7 pawn occupied another escape square. The mate is referee-confirmed; no claim is made about the first losing move or a proved earlier defense.

There was an actual king capture of a major piece, but it was my king taking the sacrificed enemy rook and thereby exposing my queen. The direct pawn capture of my knight, checking fork, defender displacement and final mate are all failures; none is erased by the pawn or bishop recovered later.

Through 96: overall 40W/2D/54L. All settings have 32 games: maximum 0W/2D/30L, skill 0 30W/0D/2L, nominal 1800 10W/0D/22L. Elo 1700 [1580, 1820], 64 rated total / latest 50 used, 32 maximum exclusions. All decisions were my own, with no external chess advice, engine evaluations, delegated play or automated chess analysis.


## Trial 11 endpoint — no established improvement; retire the intervention

The declared practice and all benchmarks 91–96 are complete. Practice was 3W/0D/0L from deliberately favorable positions, but practice 13 still lost a rook to a pawn. Benchmarks were 2W/0D/4L: both skill-0 wins, both maximum losses and both nominal-1800 losses. Endpoint Elo 1700 [1580, 1820] versus baseline 1720 [1600, 1840]; the intervals overlap and the point estimate declined. Overall strength remains stagnant. The practice wins do not establish transfer.

There was no contested two-rook conversion in the benchmark block. The narrow king-capture cue is therefore not positively validated. More broadly, game 92 lost a rook after a check displaced its defending king, game 95 was mated while materially ahead after an incompletely calculated checking line, and game 96 lost a knight to a direct pawn capture and a queen after a rook sacrifice displaced its defending king. Game 95 also had one rejected castling attempt. These are substantive failures, not just an absence of a favorable rating result.

Decision: end trial 11. The older destination audit and breadth-first trials also failed, so merely restating their instructions will not be called a new success. The next trial will specifically test execution of the pawn-origin check on quiet minor-piece moves, with brief per-move records during practice and benchmarks. This revisits an unsuccessful principle with a narrower observable behavior; it is not claimed to solve the separate checking-line failures.

Usage remains unavailable for resumed work: the goal tool still reports the same blocked status and stale 17,035,946-token / 178,558-second counter dated 2026-10-01 23:31:57 UTC. No new usage entry was submitted from it. The user-authorized work continues, with unchanged measurement files, opponents and estimator.


# Trial 12 — record pawn origins for minor-piece moves

Declared 2026-10-02 03:02 UTC after trial 11 and benchmark 96. Baseline: 1700 [1580, 1820], 40W/2D/54L; no sustained improvement. Fixed benchmark endpoint: games 97–102. Opponents, estimator, model and fair-play rules remain unchanged.

Target: the omitted d4 pawn in game 96's ...Ne5. I pursued a future knight fork and counted defenders of e5 without noticing that a pawn could take the knight immediately. Trial 03 already taught this principle for major-piece moves and captures, and later broader reply checks failed. This is not a new chess principle and not evidence of learning by itself.

Execution change: immediately before submitting every knight or bishop move, identify the two enemy pawn origin squares that could capture its destination and their actual occupants. Include a short factual record in the referee move note, even on a capture or checking move. For Black moving to e5 these origins are d4/f4; for White moving to e5 they are d6/f6. A friendly defender of the destination does not prevent a lower-value pawn capture. If a pawn can capture, reject a gratuitous minor-for-pawn loss or explicitly account for the concrete compensation. Then submit the chosen move, without treating this narrow pass as a complete safety check. All other checks, king safety and legality still require ordinary own reasoning.

Bounded practice: three recorded max-strength sessions, each at most 15 own moves, with a combined ceiling of 03:32 UTC on 2026-10-02 including reviews. Session 16: Black from benchmark 96 ply 39, the explicitly remembered position before ...Ne5. Session 17: White from benchmark 85 ply 30. Session 18: White from benchmark 89 ply 30. The latter two are preselected older own-game positions; they may be familiar and are not independent blind tests. Do not inspect later historical moves before these replays. Preserve any session stopped at a cap as unfinished, and add no repetitions to seek favorable results.

Practice assessment: count actual bishop/knight moves and whether each had the stated two-square record. Record rejected candidates as limited self-corrections, every unexpected pawn capture or other material loss, illegal submissions and mates. Successful notes or remembered corrections show implementation only, not stronger play. A replay win does not affect Elo. The king-deflection and checking-line failures from games 92/95/96 remain unresolved.

After all three sessions, return to the fixed benchmark rotation for 97–102 using the same brief notes on every minor-piece move. Review implementation separately from Elo and all substantive failures. A skipped note or another omitted immediate pawn capture is adverse process evidence; a clean block still requires later measured confirmation. Revise at the endpoint rather than extending the trial indefinitely.

Use only my own move decisions and the referee during play. No outside move advice, automated chess analysis, attack enumeration, engines as analysts or delegated chess work.


## Practice 16 — remembered position, loss after a rook skewer

Finished 2026-10-02 03:08:20 UTC by practical resignation after 30.Rxa8, 20 session plies / 10 own moves, zero illegal submissions. Result seq 560, hash `31aa9ad01542af8136de2617dbb869e00b5ae794af99cc8356c8cdc81235b1e7`. Referee PGN read back. This is the declared benchmark-96 ply-39 replay against maximum strength, excluded from Elo.

All three minor-piece moves had the two-origin note: ...Ne7 (d6 black bishop/f6 empty), ...Nf5 (e4 black pawn/g4 empty), ...Nxe3 (d2 empty/f2 white pawn). The last deliberately exchanged the knight for Be3 with fxe3 as the anticipated recapture. The remembered ...Ne5 was rejected because d4 held a white pawn. No unexpected pawn capture of a minor piece occurred in this short replay. This is 3/3 implementation in a remembered setting, not independent accuracy or improved strength.

...f6/gxf6/...Qxg4/Bxg4/...gxf6 traded queens and reached equal material. ...Re7 was intended to cover h7, but 27...Kf7 put my own king between that rook and h7. White's Rh7+ exposed the changed blocker. I then chose ...Kf8 while considering the rook exchange, and missed Rh8+, which checked and skewered Ra8 behind the king. ...Kg7/Rxa8 actually lost the rook. At resignation Black had R+B+4P against 2R+B+4P. This is a practical loss assessment, not a theoretical certificate.

The new pawn-origin record was implemented, but a king obstruction and an unfinished checking-line calculation still caused a direct major-piece loss. The narrow behavior did not ensure successful play. No repeat is added. Continue the two predeclared older-position sessions, then benchmarks 97–102.


## Practice 17 — older game-85 replay, unfinished at the move cap

Stopped explicitly at 2026-10-02 03:17:10 UTC after 30...a5, exactly 15 own moves / 30 session plies, zero illegal submissions. Result is `*`, not a draw. Result seq 593, hash `87cc9f55d7ad529673f1954e225bb9769e7811501d01c3a8716fe14043f97c35`. Referee PGN read back. Used the predeclared game-85 ply-30 position against maximum strength, with no later historical moves consulted.

The starting position was a knight down. cxd4/...Rxd4 removed the knight while losing the c-pawn; Bxb4/...Rxb4 exchanged bishops, leaving a one-pawn deficit. Both bishop moves had the recorded pawn origins: Bxb4 (a5/c5 empty) and Bf3 (e4/g4 empty). Bf3 added a defender to e2; its later capture by ...Bxf3 was recaptured with exf3. There were no omitted pawn captures of a minor piece in the played line. This is only 2/2 implementation opportunities.

My passive rook/king arrangement did not hold the pawn ending. ...Rb2 and ...Rdd2 occupied the second rank. After the bishop trade, ...Rxf2+ and ...Rxf3 took both f-pawns. I answered the subsequent rook checks without a direct unreciprocated rook loss, but ...Rxh2 took another pawn. Rxe6 recovered e6 at the cap. Final material was 2R+2P against 2R+5P; the position remains unproved and unfinished, with a clear material deterioration.

No queen or rook was lost without recapture and no illegal move occurred. The narrow note behavior was implemented, but this poor defense is not evidence of stronger play. Continue only the third declared session, then benchmarks 97–102.


## Practice 18 — older game-89 replay, unfinished at the move cap

Stopped explicitly at 2026-10-02 03:30:48 UTC after 30...Rd2, exactly 15 own moves / 30 session plies, zero illegal submissions. Result is `*`, not a draw. Result seq 626, hash `07211060f3729005af1582b2f2d00dc210eb0dffb20397cbb7aa90084cbb235b`. Referee PGN read back. Used the predeclared game-89 ply-30 position against maximum strength, with no later historical moves consulted.

All five minor-piece moves had both enemy pawn origins recorded: Nd4 (c5/e5 empty), Ne2 (d3 empty/f3 white queen), Nf4 (e5/g5 empty), Nd3 (c4 white bishop/e4 empty), Nf2 (e3/g3 empty). No unexpected pawn capture of a minor piece occurred. The audit did not establish broader safety: Nd4 removed Nf3's defense of h2, allowing ...Bxh2+. Ne2 later vacated the diagonal through d4, and ...Bxb2 took another pawn after the rook exchange. These were actual concessions from a position already one pawn down.

Qf3 answered the bishop attack on the queen. ...Rxd1/Rxd1 exchanged one rook each. The later knight relocations, Rh3 and Nf2 avoided a direct major-piece loss in the played line, but did not recover the pawns. The session ended with Q+R+B+N+4P against Q+R+B+N+7P, and ...Rd2 attacking my queen. No completed defense, theoretical evaluation or successful conversion is claimed.

## Trial-12 practice endpoint

All three declared sessions and reviews finished before the combined 03:32 UTC ceiling, with no extra repetitions. Total: one practical loss and two explicitly unfinished sessions, 40 own moves / 80 session plies, zero illegal submissions. All 10 bishop/knight moves had the brief two-origin record (3 + 2 + 5). The remembered ...Ne5 was rejected; the intended ...Nxe3/fxe3 exchanged a knight for a bishop rather than overlooking a pawn capture.

This establishes implementation in these selected replays only. Practice 16 still lost a rook after a king obstruction and checking skewer; practice 17 deteriorated to a three-pawn deficit; practice 18 conceded h2 and b2 through changed defenses. There is no practice evidence of stronger overall play. Do not turn the absence of one narrow error into a learning claim.

Return now to the fixed benchmark block 97–102, using the same notes on every minor-piece move, and assess all errors as well as the unchanged Elo. Baseline remains 1700 [1580, 1820] through 96, with 40W/2D/54L overall. No valid new cumulative usage counter is available. All practice moves and reviews were my own, using only the referee during play and no external advice, engine evaluations, automated chess analysis or delegation.


## Benchmark 97 — White versus maximum strength, pawn-ending loss

Finished 2026-10-02 03:51:05 UTC by practical resignation after 39...Qxd7, 78 plies / 39 own moves, zero illegal submissions. Result seq 7890, hash `c295062be389f16cf6531db81a0210a1afcb687c7f3fb367e0ed9dab9573728c`; snapshot `fbf8a859567d6e604a2ef966f324703eb17509b3d77d68cd2bb93af2ebcae5b6`. Referee PGN read back.

All eight bishop/knight moves had the two-origin record: Nf3 (e4 white pawn/g4 empty), Bb5 (a6 empty/c6 black knight), Bxc6 (b7 and d7 black pawns, with an intended knight-for-bishop exchange), Nc3 (b4/d4 empty), Bf4 (e5 white pawn/g5 empty), Be3 (d4 empty/f4 moving white bishop), Ne1 (d2 empty/f2 white king), Nd3 (c4/e4 empty). The Be3/...Nxe3/fxe3 and Nd3/...Bxd3/cxd3 sequences were accounted minor exchanges. Nd4 was rejected while c5 held a black pawn. No omitted immediate pawn capture of a minor occurred; 8/8 notes show execution only.

The queen and rook exchanges were materially balanced. Rd2 protected c2 from Bf5; h4 removed h3 from the same bishop's attack; after exchanging the remaining rooks, Ne1 defended c2 and Nd3 defended e5. The resulting pawn ending remained equal in pawn count but was not established as equal in value. Black's ...c5 undermined d4; ...cxd4+/cxd4 left my king tied to the central chain. I chose g4/g5 and the h-pawn exchange while Black developed the queenside majority. ...g6 fixed my g5 pawn. After ...Ke4, a4/...bxa4 produced an outside passer. My d5/d6/d7 counterplay was too slow: ...a1=Q, ...Qa4+, and ...Qxd7 actually stopped it.

At resignation White had two pawns against Q+3P. This is a practical loss assessment, not a first-losing-move or theoretical endgame certificate. No queen or rook was lost without recapture; the decisive failure was an unfavorable pawn-ending transition/plan and the lost promotion race. The narrow trial behavior did not ensure overall strength.

After 97: 40W/2D/55L overall; maximum strength 0W/2D/31L. Elo remains 1700 [1580, 1820], with 64 rated games total and the latest 50 used; 33 maximum-strength games excluded. Continue the predeclared block through 102 without extra practice or changing the method.


## Benchmark 98 — Black versus maximum strength, knight loss and fork

Finished 2026-10-02 04:01:25 UTC by practical resignation after 29.Qh5, 57 plies / 28 own moves, zero illegal submissions. Result seq 7949, hash `da4ddba9f53d6134e8cb6dae6bb93357275204a2d1f0e6305448f808a19a6021`; snapshot `00687d60c0c6928c72216ff8a75ddf10863d7b50034b96341dbaf0a8913c6df5`. Referee PGN read back.

All ten minor-piece moves had the origin note: Nc6 (b5/d5 empty), Nf6 (e5 black pawn/g5 empty), Be7 (d6 empty/f6 black knight), Na5 (b4 empty/other origin off board), Bd7 (c6/e6 empty), Nb7 (a6 black pawn/c6 empty), Bxb5 (a4 empty/c4 black pawn), Bd7 (c6/e6 empty), Nh5 (g4 empty/other origin off board), Bxf5 (e4/g4 empty). There was no omitted immediate pawn capture of a minor. However, 20...Nh5 simply hung the knight to 21.Qxh5 along the clear d1-e2-f3-g4-h5 diagonal. I considered future knight activity and the pawn origins but omitted this direct queen capture. This is an actual piece loss, not a compensated sacrifice.

The closed Spanish position had produced a passed c3 pawn after ...axb4/cxb4/...c3. White's Ndc4 blocked Qc7's support of c3, limiting that pawn's usefulness. ...f5/exf5/...Bxf5 recaptured the exchanged pawn but vacated the bishop's control of b5, allowing Nb5 with tempo on Qc7. ...Qd7 answered that attack but placed the queen where the next fork could hit it. Rxa8/...Rxa8 was a balanced rook trade, followed by 26.Nb6 attacking both Qd7 and Ra8. ...Qd8/Nxa8/...Qxa8 conceded rook for knight. Bxf5/...gxf5 then traded bishops.

Final material: Black Q+B+N+5P against White Q+R+B+N+5P. The resignation is practical, not a theoretical certificate. The direct queen capture of Nh5 and the subsequent queen/rook fork were both broader tactical failures despite 10/10 recorded pawn-origin checks. No first-losing-move claim is made.

After 98: 40W/2D/56L overall; maximum strength 0W/2D/32L. Elo remains 1700 [1580, 1820], 64 rated total/latest 50 used, 34 maximum-strength games excluded. Trial-12 benchmark notes are 18/18 so far, but both games were losses and the method has not demonstrated stronger play. Continue the fixed block 99–102, with no added practice mid-block.


## Benchmark 99 — White versus skill 0, win despite a queen blunder

Finished 2026-10-02 04:24:11 UTC by 56.Nf2#, 111 plies / 56 own moves, zero illegal submissions. Result seq 8062, hash `9661a0ea7c447cc719fc165c20169333c76adb75cf03df4616fadcdecd39ee19`; snapshot `ac33f9a6f2eb1ee6f0a3d5d41a604c2ea718b3bba27e6d956967d578a27c94cb`. Referee PGN read back.

All 24 minor moves had the two-origin record: 3.Nc3, 4.Nf3, 5.Be2, 8.Be3, 11.Ne5, 12.Nxd7, 13.Bg4, 14.Nxe4, 15.Bxh5, 16.Bg4, 17.Nc5, 18.Bf3, 19.Bxf4, 20.Bxh6, 21.Be3, 22.Bg2, 26.Ne6+, 41.Nf4, 42.Nxd5+, 43.Nxe7+, 44.Ng6, 45.Nf4, 46.Nd3+, 56.Nf2#. Bxh5 explicitly accounted for ...gxh5 as a bishop-for-knight exchange, but Black declined the recapture. At ...f5's fork of Ne4/Bg4, Nc5 attacked the queen and Bf3 then saved the bishop. No omitted immediate pawn capture on the destination of an own bishop/knight occurred.

The weak opponent gave up Bh5, Nh5 and Bh6; ...Qxe3 then gave up the queen for a bishop. fxe3/...Rxf1+/Qxf1 completed the anticipated rook trade. This large advantage did not produce a sound conversion: after ...g5, I played 29.Qh4+ and calculated king escapes while omitting the immediate ...gxh4. The queen was actually lost to the g5 pawn. I had even recognized the analogous capture risk earlier, then failed to retain it in the final check calculation. This repeats the basic major-piece pawn-capture failure outside the narrow trial scope; it is not a successful sacrifice or a safe mating sequence.

...h3 then attacked Bg2 while Rg8 pinned it to Kg1. Rook checks did not resolve that threat. Kh2 unpinned the bishop but allowed ...hxg2, an additional actual bishop loss. Kg1 blocked promotion; Rf2, Rxg2/...Rxg2+/Kxg2 removed the passer and traded rooks. The position had deteriorated to N+4P against 5P. Nxd5+ and Nxe7+ captured both central black pawns; the e-pawn then promoted while Black's king was too far away. The final Qf4+, Kf3, Nf2# coordinated queen, king and knight. In that final position Kf3 covered g2/g3/g4, Qf4 covered h2/h4, and Nf2 checked h3.

The win does not erase the queen drop, trapped-bishop loss, or the very poor conversion of the earlier overwhelming material advantage. Notes were 24/24, but broader tactical control again failed. Trial benchmark implementation is now 42/42; no strength improvement is established.

After 99: 41W/2D/56L overall; skill 0 is 31W/0D/2L. Provisional Elo is 1690 [1570, 1810], 65 rated total/latest 50 used, 34 maximum-strength exclusions. The rolling estimate fell despite this win as the fixed window changed. Continue benchmark 100, then 101–102, without changing the declared trial mid-block.


## Benchmark 100 — Black versus skill 0, win after an unreciprocated rook loss

Finished 2026-10-02 04:43:47 UTC by 47...Rd1#, 94 plies / 47 own moves, zero illegal submissions. Result seq 8158, hash `b66ca357eeeaaf00fbd71841dabda144fe855e4fa6521392fb6aa2876b272be6`; snapshot `d92f55a923f3f45951c50fe0d2cfb56804d27611065269de0627d316390996c8`. Referee PGN read back.

All 17 minor-piece moves had the two-origin note: ...Nc6, ...Nf6, ...Be7, ...Bf5, ...Bxd3, ...Nxe4, ...Bxg5, ...Nd8, ...Ne6, ...Bf6, ...Nc5, ...Nxd7, ...Nc5, ...Nd3, ...Nxb2, ...Bxc3, ...Nc4. No unexpected pawn capture of a minor on its submitted destination occurred. The ...Bxd3/Bxd3/...Rxd3 and ...Nxe4/Rxe4 sequences were accounted minor exchanges. Implementation totals through 100 are 59/59; this does not imply overall safety.

An early queen exchange and pressure on d3 won that pawn. ...hxg5 captured White's exposed knight; ...Bxg5 later took the remaining bishop. However, 18...Rd1+ was a direct rook blunder. My expected line used a rook block on e1, but White's bishop had already left c1, so Ra1 could play 19.Rxd1 directly. There was no recapture. I failed to update the opened first-rank path after Bxg5, substantially dissipating the material advantage. This is the same broader changed-blocker/checking-line failure seen in earlier trials, not a successful rook sacrifice.

...Nd8 moved the attacked c6 knight to a rook-defended square; ...Ne6 defended c7. After ...Bf6 and Ra4, ...Nc5 forked both Rd7 and Ra4. White's Rxa7 allowed ...Nxd7 to win a rook. Later ...Rd8 blocked Ra8+ with Bf6 available to recapture on d8; White instead played Rc8 and lost the last rook to ...Rxc8. These were fresh opponent concessions, not proof that the earlier rook blunder was harmless.

...Nxb2 and ...Bxc3 removed the defended pawn chain in order, and ...cxb6 removed the remaining queenside pawn. The passed b-pawn promoted with the d-file rook restricting the white king's route. ...Kxf7 answered the checking pawn capture; the final ...Qe2+ forced Kg1, and ...Rd1# used the queen to cover the second-rank exits and defend d1. No further major piece was lost after the first-rank error.

After 100: 42W/2D/56L overall; skill 0 is 32W/0D/2L. Provisional Elo is 1680 [1560, 1800], 66 rated total/latest 50 used, 34 maximum-strength exclusions. The rolling estimate again declined despite a skill-0 win. Trial block 97–100 is 2W/0D/2L, with material failures in three of the four games. Continue the declared endpoint games 101–102 against nominal 1800, with the same method and no extra practice mid-block.


## Benchmark 101 — White versus nominal 1800, failed promotion compensation

Finished 2026-10-02 05:08:13 UTC by practical resignation after 37...Rh2, 74 plies / 37 own moves, zero illegal submissions. Result seq 8234, hash `470c6bab624ccfd102d675999eeec9f46d46fb5eb9544989d19e452c86cb46b4`; snapshot `fee25fa4d8bc65d60768f27d667ddb2b642f8be7329ae866785b4c302ae6d1a6`. Referee PGN read back in the preceding continuation.

All 12 minor moves had the pawn-origin record: Nf3, Bf4, Bg3, Nc3, Bd3, Na4, Nd2, Nb3, Be2, Bxg4, Nac5 and Nd7. Bxg4 deliberately exchanged bishop for the checking knight, with ...Bxg4 as recapture. No omitted immediate pawn capture of a minor on its submitted destination occurred. Trial benchmark implementation is 71/71, without demonstrated strength improvement.

The queenside plan supported c5 and produced a passed c6 pawn, but Black's h-pawn advance and rook battery created a serious attack on the castled king. 31.d6 pursued promotion while ...Rah8 completed the battery. 32.Rf3 was a consciously material-conceding defensive block, and ...Bxf3 actually took the rook. Nd7 attacked Qf6; ...Qe6 removed its f-file control, allowing Kf2 and Kxf3 to recover the bishop while retaining the g2 pawn as a barrier. After ...cxd6, White was an exchange and a pawn down.

36.c7 vacated c6's defense of Nd7 and deliberately allowed ...Qxd7 in the expectation that promotion would recover a rook. That calculation failed: the queen on d7 itself defends c8, in addition to Rh8. A heavy-piece recapture on c8 could therefore be followed by the other black heavy piece taking White's queen. The knight was actually lost without the expected promotion compensation. 37.g4 attacked Rh5, but ...Rh2 retained pressure. At resignation White had Q+R+N+5P against Q+2R+B+6P, nominally a rook and a pawn down. This is a practical resignation, not a proven forced loss or a first-losing-move certificate.

The narrow notes were implemented, but king-attack defense and the changed defenders in a promotion sequence were not controlled. Long speculative calculation did not prevent the false compensation claim. After 101: 42W/2D/57L overall; nominal 1800 is 10W/0D/23L. Provisional Elo is 1670 [1550, 1790], 67 rated total/latest 50 used, 34 maximum-strength exclusions. Finish the predeclared block with benchmark 102 before assessing trial 12; no extra practice is added mid-block.


## Benchmark 102 — Black versus nominal 1800, rook capture of an undefended knight

Finished 2026-10-02 05:30:44 UTC by practical resignation after 52.Rxe4, 103 plies / 51 own moves, zero illegal submissions. Result seq 8339, hash `94c84474fb73aaeeeea14dd747ed574878a8e22941e3b8ec4e62833704c0b16e`; snapshot `75e6f2b9291a4ac44c8d468e278c60450272773db4746d65f185759c2a41b947`. Referee PGN read back.

All 17 minor moves had the pawn-origin record: ...Nc6, ...Nf6, ...Nxd5, ...Bc5, ...Bg4, ...Bxf3, ...Nb4, ...Nd5, ...Bb6, ...Ne7, ...Nc6, ...Nd4, ...Nxb3, ...Na5, ...Nxc4, ...Nd2 and ...Ne4. The ...Bxf3 note contained a contradictory phrase saying there was no attacking pawn while also identifying the white pawn on g2. The next move note explicitly corrected that phrase: g2 could recapture, as part of the accounted bishop-for-knight trade. This is 17/17 recorded opportunities, with one wording defect and correction, not perfect note accuracy. No omitted pawn capture of a submitted minor occurred.

The opening exchanges left equal material but doubled c- and f-pawns. The queen and first rook trades were balanced. A long passive defense kept material equal until ...Ne7 dislodged the attacking rook but gave up f4 to 37.Rxf4. I chose 37...Re6+ and then ...Nc6, overlooking 39.Bg4's pin of Re6 to Kd7. ...Ke7 removed the pin; White declined Bxe6 and played a4, allowing ...Rd6 to save the rook. This was a real offered exchange loss, but not an actual captured rook. One commentary sentence incorrectly referred to an earlier claim of a safe conversion; no such conversion had been established.

...Nd4, ...Nxb3, ...Na5 and ...Nxc4 recovered both queenside pawns and briefly put Black one pawn ahead. ...Nd2 gained a tempo on the rook. After a5, Bb6 was trapped by a7/c7/c5 and the defended white a5 pawn. I chose 51...Ne4 while calculating ...Nxc3 and ...Nxf2+ forks, but failed to inspect the rook's immediate horizontal capture from g4 through f4 to e4. White played 52.Rxe4, and there was no recapture. This was a direct uncompensated knight loss to a rook, not a sound counterattack or sacrifice.

At resignation Black had R+B+5P against R+2B+4P, a minor piece down for a pawn, with Bb6 still trapped and threatened. The bishop had not yet been captured. The resignation is practical; no forced-loss certificate or first-losing-move claim is made. After 102: 42W/2D/58L overall; nominal 1800 is 10W/0D/24L. Provisional Elo is 1660 [1540, 1780], 68 rated games total/latest 50 used, 34 maximum-strength exclusions. Storage reported 22,604,928 bytes.

## Trial-12 endpoint — implementation without improvement

Benchmarks 97–102 finished as predeclared: 2W/0D/4L, with both wins against skill 0 and both losses against each stronger setting. Total 258 own moves / 517 plies, zero illegal submissions. All 88 bishop/knight moves included the two-origin note; the wording defect and correction in game 102 remain part of that record. There was no omitted immediate pawn capture on a submitted minor-piece destination in this block.

This narrow implementation did not transfer to sounder overall play. Game 98 lost a knight to the queen and later suffered a queen/rook fork. Game 99 dropped the queen to a pawn and subsequently lost a bishop despite eventually winning. Game 100 dropped a rook after forgetting an opened first-rank path. Game 101 conceded material under a king attack and miscalculated promotion compensation. Game 102 offered an exchange through a pin, then actually lost a knight to the rook while pursuing a future fork. Game 97 lost a pawn-ending promotion race. The two skill-0 wins do not validate the method.

Elo moved from 1700 [1580, 1820] after 96 to 1660 [1540, 1780] after 102. These overlapping intervals and the rolling window do not establish a quantified decline, but there is plainly no evidence of improvement at this endpoint or sustained improvement across trials. Retire the minor-only record as the main intervention. The next learning period must change the practice task, not claim that longer notes or more games themselves improve chess. Preserve every result and the fixed benchmark rotation. No valid new cumulative usage counter is available, and no invented usage entry is submitted.


# Trial 13 — play the capturing side before returning to defense

Declared 2026-10-02 05:33 UTC after benchmark 102. Baseline: 1660 [1540, 1780], 42W/2D/58L, 68 rated total/latest 50 used. Trial 12 failed despite 88/88 minor-piece pawn-origin notes. Next fixed benchmark endpoint: games 103–108. No change to opponent rotation, estimator, model, or fair-play rules.

Target: speculative threats displaced a direct capture of the moving piece. The latest examples are ...Nh5/Qxh5 in 98 and ...Ne4/Rxe4 in 102. Trial 03 and trial 06 already attempted destination and immediate-reply audits. This is not a new chess principle and a longer checklist is not learning evidence.

Change the practice task: take the opponent's side in four short recorded sessions against maximum strength. The first two deliberately rehearse remembered captures; the latter two are older own-game positions selected before inspection, with all later historical moves withheld. None is an independently blind test. Play beyond the first capture against actual replies, retaining concrete blockers and recaptures rather than merely recognizing the first move.

Predeclared sessions, in this order:

1. White from game 102, ply 102, before Rxe4. Remembered. The capture is supplied by my own preceding game, not a fresh solution.
2. White from game 98, ply 40, before Qxh5. Remembered.
3. Black from game 87, ply 41. Older position; do not inspect later moves before the session.
4. White from game 90, ply 40. Older position; do not inspect later moves before the session.

Each ends naturally or explicitly unfinished after six own moves and the last opponent reply. Combined ceiling: 06:03 UTC on 2026-10-02, including reviews. If a preselected ply is unavailable, record the failed setup and omit that drill rather than substitute a favorable position. No extra repeats. If the ceiling arrives, end the active drill explicitly and record omissions. Practice results stay outside benchmark Elo.

Execution change for practice and benchmarks: after selecting a move, reconstruct its destination on the actual board and inspect direct captures of the moved piece by every enemy piece type before following its intended threat. In particular, read rook/queen lines as well as pawn origins; Ne4 in 102 must fail this pass because Rg4 reaches e4 through the empty f4 square. If a capture is available, count the actual immediate recapture rather than assume a defender exists. A brief factual move note may record a relevant capture, blocker or accounted exchange; a note saying no capture was identified is not a certificate of completeness. Recheck the final replacement candidate. Retire the mandatory minor-only pawn note. Ordinary king safety, checks and vacated defenders still matter; this targeted step does not certify them.

For each drill record the actual line, material changes, direct captures missed/offered, illegal attempts, and whether an intended recapture was real. Remembered first captures count only as rehearsal. In games 103–108, record all unaccounted immediate captures, including captures of minor pieces by queens or rooks; opponent declines remain offered losses, distinct from actual ones. Compare the full block, nominal-1800 results, and unchanged Elo interval. Any recurrence rejects reliable transfer; a clean block or rating rise would still require repeated evaluations before a sustained-improvement claim. End or revise at 108 rather than study or benchmark indefinitely without assessment.

Only own chess decisions and referee during play. No external advice, automated chess search/scoring/attack enumeration/move selection, engine analysis, tablebases, or delegation. No valid new cumulative usage counter is available.


## Practice 19 — remembered capturing side, failed execution after the capture

Stopped explicitly unfinished at 2026-10-02 05:35:12 UTC after six own moves / 12 plies, zero illegal submissions. Result seq 641, hash `b44e813df7b81c4a1793bcd92a34e065e3ce11e38e1240a5e3968ac1c298595b`. Referee PGN read back. Actual line: 52.Rxe4 Bxa5 53.Bxa5 Rd5 54.Bg4 h5 55.Bf3 c6 56.Re8+ Kxe8 57.Bxd5 cxd5.

The remembered rook capture took the undefended knight; Bxa5 then took the trapped bishop. Bg4 and Bf3 responded to actual rook/pawn attacks. However, 56.Re8+ was submitted even though its move note recognized that the supposed bishop support was wrong and said the candidate required revision. Ba5 controls d8, not e8. Black legally played Kxe8. This is an explicit failure to apply a recognized correction before committing, not just failure to discover it. The direct-capture intervention failed within the first drill.

Bxd5 recovered Black's rook, and cxd5 took that bishop. Initial material was R+2B+4P versus R+B+N+5P; final material B+3P versus 5P. The two remembered piece captures had produced a much larger advantage that the rook submission dissipated. No endgame win or draw is claimed. Keep the remaining three predeclared drills and the fixed benchmark endpoint; do not add repetitions or redefine this as a success. The immediate operational correction is to finalize the actual UCI move after rejecting a candidate, before constructing the command; the submitted note is not a safe place to leave an unresolved replacement.


## Practice 20 — remembered queen capture, extra knight retained at the cap

Stopped explicitly unfinished at 2026-10-02 05:37:52 UTC, six own moves / 12 plies, zero illegal submissions. Result seq 656, hash `f11aae3c2726170864a1b1a77e54eff3853276206e85ab9488232ce90b51c0e1`. PGN read back. Line: 21.Qxh5 g6 22.Qe2 f5 23.exf5 gxf5 24.Be3 f4 25.Bc1 Rab8 26.Rd1 Nd8.

Qxh5 rehearsed the known undefended-knight capture, and Qe2 escaped the actual pawn attack. Black diverged from the benchmark with ...gxf5, retaining Bd7; I rejected the old Nb5 idea because that bishop still controlled b5. Be3 allowed ...f4 with tempo and returned to c1. Bd2 and Bd4 were rejected because c3 and e5 respectively could capture the bishop. Rd1 supported d5. These are limited self-corrections, not a certified solution.

The intended pawn exchange was the only own material removed. Starting Q+2R+2B+2N+6P versus Q+2R+2B+2N+6P became Q+2R+2B+2N+5P versus Q+2R+2B+N+5P. The extra knight was retained, but conversion was not completed, the bishop lost development time, and Black's c3/f4 pawns remained active. No win or Elo effect is claimed. Continue the two preselected older positions without looking at their later historical moves.


## Practice 21 — older reversed position, loss by Qe5 mate

Finished naturally at 2026-10-02 05:40:19 UTC by 26.Qe5#, five own moves / 10 plies, zero illegal submissions. Result seq 668, hash `31299845c13acdf839eee6bc1437a33e7ef9bce9d8fa2e68b9ad4599d8b67a65`. PGN read back. Later historical game-87 moves were not consulted. Actual line: 21...Bxe5 22.Rxe5 Kb8 23.Qe8+ Kc7 24.Re7 Kd6 25.Rxd7+ Rxd7 26.Qe5#.

The preselected Black position began with R+B+N+6P against Q+2R+2B+2N+7P, already an enormous material deficit. Thus this was a poor selection for testing conversion; it remains in the record with no replacement. ...Bxe5/Rxe5 traded bishops. I recognized Nd7's pin to Kc7 and used ...Kb8; the queen check and Re7 renewed the pressure. ...Kd6 let Rxd7+ take the knight, then ...Rxd7 took that rook. The proposed Qxd7 recapture could have been answered by Kxd7, but White instead played the immediate mate I had omitted.

Qe5 was supported by the d4 pawn; it checked Kd6 while the pawn and queen covered the exits, with c6/d5/d7 occupied by Black. This is the referee-confirmed terminal result, not a claim that the initially lost position could have been saved or that one particular earlier move was the first loss. The narrow capture accounting did not supply a complete check/mate assessment. No extra repetition is added. Continue only the fourth declared drill, then the fixed benchmarks.


## Practice 22 — older reversed position, equal material at the cap

Stopped explicitly unfinished at 2026-10-02 05:43:44 UTC, six own moves / 12 plies, zero illegal submissions. Result seq 683, hash `6408787d2fe34cac0461457eb5e4e809fb3cae1ade0bacf5aefbb44124baf056`. PGN read back. No later historical game-90 moves were consulted. Actual line: 21.Bxf3 Rxe1 22.Rxe1 d3 23.b4 b6 24.h3 Qd4 25.Rc1 Nd7 26.Bd5 b5.

Bxf3 removed the checking knight and its king/queen/rook fork. Vacating e2 allowed ...Rxe1/Rxe1, a balanced rook exchange that was accounted before submission. Qd2 then blockaded d3. Rc1 protected c4 from Qd4, and Bd5 was supported by c4, making an immediate ...Qxd5 answerable by cxd5. No further piece or pawn was lost in the played line.

Initial material was Q+2R+B+6P against Q+2R+2N+6P; final material Q+R+B+6P against Q+R+N+6P. The inherited extra black knight was captured, restoring nominal equality. Black's final ...b5 attacks c4, the bishop's defender, while the d3 passer remains heavily supported. Those problems are unresolved at the cap; this is neither a completed defense nor a proved equal position.

## Trial-13 practice endpoint

All four predeclared sessions finished by 05:43:44 UTC, before the 06:03 ceiling, with no extra repetitions: 23 own moves / 46 plies, zero illegal submissions, one checkmate loss and three explicitly unfinished drills. Two remembered captures were executed. Practice 19 then failed severely: a rejected rook candidate was nevertheless sent, allowing Kxe8. Practice 21 began far behind materially and ended in an omitted immediate mate. Practices 20 and 22 retained their material gains over their short continuations but did not complete a conversion or defense.

There is no practice basis for claiming the new method works. The first drill already refutes reliable execution, and the third demonstrates that destination capture checks alone omit other forcing replies. Preserve the selected examples, including the unsuitable starting deficit. Return now to fixed benchmarks 103–108 as declared and assess all errors, rather than extend practice until it looks favorable. Baseline remains 1660 [1540, 1780]; practice has no Elo effect.

Operational correction after practice 19: finish choosing the actual UCI move before constructing the referee command. If the destination audit rejects it, change the move itself before submission; a note acknowledging its flaw does not undo a submitted move. This is a correction prompted by an observed failure, not validated learning. No timing requirement, automated chess help, external advice or delegation is introduced.


## Benchmark 103 — White versus maximum strength, skewer and obstructed recapture

Finished 2026-10-02 06:02:00 UTC by practical resignation after 33...Bxc1+, 66 plies / 33 own moves, zero illegal submissions. Result seq 8407, hash `4b8cf8f1baa23a798f2a9276076dc159bba6e361e648b2c419774c1a509324a5`; snapshot `82399ad759956de93c724de3c9e5dc5d904e95aa0a947746fcc36cf4df8b79ff`. Saved PGN read back.

The central pawn, knight and queen exchanges were balanced. Kxd1 was legal, and subsequent development retained equal material. ...Bxd5/exd5 produced a passed d-pawn; I explicitly avoided treating Rd1 as its defender while Nd2 blocked the file. Black's rooks and knight gained activity. Kb2 temporarily removed the c3 pin, and later Kc2 supplied a new defender for Bd2 after both Rd1 and Nb3 had moved. ...Nxd2/Kxd2 then completed an equal bishop-for-knight exchange. These local corrections did not establish a sound defense.

30.Rec1 genuinely added support to c3 while the king was on d2. After ...e4 attacked Nd3, I chose 31.Nb4 and counted ...Bxb4/cxb4, but omitted 31...Bf4+. That check also exposed Rc1 behind the king. I then played 32.Kc2 expecting an exchange concession, while failing to apply the king's new obstruction of Rc1's c-file. Black used 32...Raxc3+: Rc1 could not recapture through Kc2, and Kxc3 was barred by Rc8. 33.Kb2 then allowed ...Bxc1+, an actual rook loss. Thus the immediate checking reply and a changed own-king blocker again defeated the broader defensive line.

At resignation White had R+N+5P against 2R+B+6P, nominally a rook and a pawn down. Black's bishop remained on c1; I did not play the further Rxc1/...Rxc1 sequence, which would lose the remaining rook. This is a practical resignation, not a forced-loss certificate or first-losing-move proof. No illegal attempt was made to execute the blocked recapture.

After 103: 42W/2D/59L overall; maximum strength 0W/2D/33L in 35 games. Elo stays 1660 [1540, 1780], 68 rated total/latest 50 used, with 35 maximum exclusions. The new trial has already failed to provide reliable tactical control in practice and in its first benchmark. Complete the declared 103–108 block without added practice or changing opponents; preserve these failures in the endpoint assessment. No valid new cumulative usage counter is available.


## Benchmark 104 — Black versus maximum strength, discovered check and promotion

Finished 2026-10-02 06:23:26 UTC by practical resignation after 33.h8=Q+, 65 plies / 32 own moves, zero illegal submissions. Result seq 8474, hash `35f54938702a51749f15826a013db645d1e3fb3909d587e68ddca17ad8164f7c`; snapshot `0ca5facd83f7c4483e5fb606d5f5cc916967d6220c5aea3fb7b0d880092d847e`. PGN read back.

The Berlin exchanges preserved nominal material equality. ...Ne7 avoided an unsupported ...Nh4/Nxh4, and ...fxe6 answered the checking knight capture. ...Bc5 escaped c3; ...Bd6 was rejected because e5 could capture it. ...Kd7 guarded c6/e6, and ...a6 supported b5 while opening a7 as a future bishop retreat. These were local applications, not evidence of a successful overall defense.

...Nb6 and 24...Nxa4 won a pawn. I had considered a bishop departure from d2 uncovering Rd1, but failed to resolve the stronger 25.Bxh6+ continuation: the check prevented ...gxh6, and ...Ke7 allowed Bxg7 to take a second kingside pawn and attack Rf8. I then chose 26...Kf7, deliberately allowing Bxf8/Kxf8 to avoid the checking lines I saw after rook retreats. The rook concession was anticipated at that point, not an unnoticed one-move rook drop; its necessity and best earlier defense were not independently established. My move note incorrectly wrote Bxf8 with a check suffix; the next note corrected that it was not check against Kf7.

After the exchange concession White was an exchange and a pawn ahead, with an outside h-passer. ...Kg8/...Kh8 blockaded it initially, but Rh1 supported h7 and Ng5/Nf7+ drove the king off h8. The returning knight on b6/d7 was too late. ...Kg7 was followed by the actual promotion, 33.h8=Q+. Final material was B+N+5P against Q+R+N+5P. This is a practical resignation, not a forced-loss certificate or proof that every earlier alternative failed.

The principal failure was incomplete anticipation of the discovered checking capture and the resulting king/rook defense, followed by inability to stop the supported passer. A safe immediate destination for ...Nxa4 did not make the pawn grab sound. After 104: 42W/2D/60L overall; maximum strength 0W/2D/34L in 36 games. Elo remains 1660 [1540, 1780], 68 rated total/latest 50 used, 36 maximum exclusions. Trial 13 is 0W/0D/2L so far. Continue fixed games 105–108 without additional practice; no sustained improvement or valid new cumulative usage count is claimed.


## Benchmark 105 — White versus skill 0, win despite an omitted king capture

Finished 2026-10-02 06:44:29 UTC by 44.Qb6#, 87 plies / 44 own moves, zero illegal submissions. Result seq 8563, hash `dca8f5256f69390139db4ef8ebe413b4ab8b9c4441edf1b24dcf56a9b75bedd5`; snapshot `d210a9cc41d1bae1bf8e1480ff5f15945c9337628694b83379c913206ca8812e`. PGN read back.

The opening queen sortie won b5, and bxc4 followed by a queen exchange retained two extra pawns. Black then offered both knights with ...Nxe5 and ...Nxd4; Nxe5 and cxd4 captured them. Vacating the c-file allowed ...Rxc1/Rxc1, an accounted rook exchange. After ...fxe6, White had two extra knights and a pawn. Rxb7 gained another pawn.

26.Nc6+ forked the king and Be7. However, after the actual ...Kc8 I focused on Nxe7+ and the possible ...Rxe7/Rxe7 exchange, omitting that the king now attacked the undefended Rb7. 27.Nxe7+ Kxb7 was an actual unanticipated rook loss. The checking capture did not prevent the king from escaping with material. This was a capture of another piece, outside the narrow moved-piece destination audit, and another failure of the broader tactical defense. White retained B+2N+5P against R+3P; the advantage remained because of earlier opponent losses, not because the rook sacrifice was planned.

Ng6/Ne5 escaped the rook attack. The king centralized and Bxg5 took another pawn. I kept Ne5 defending Nc4 against ...Rb4, and ...Rxc4/Nxc4 deliberately exchanged Black's final rook for a knight. The h-pawn then promoted. The final queen approach preserved real support: Qc5 was supported by d4, and Qb6 mate by Nc4. No additional own material loss was missed in that continuation.

After 105: 43W/2D/60L overall; skill 0 is 33W/0D/2L in 35 games. Trial 13 is 1W/0D/2L. The rolling estimator reports 1650 [1530, 1770], 69 rated total/latest 50 used, 36 maximum exclusions. The estimate fell despite this win as the fixed rolling dataset changed; this is not evidence that winning itself reduced playing strength. No sustained improvement is established. Continue the declared block through 108, retaining the rook blunder in the assessment. No valid new cumulative usage counter is available.


## Benchmark 106 — Black versus skill 0, central fork and completed conversion

Finished 2026-10-02 06:56:21 UTC by 33...Rh1#, 66 plies / 33 own moves, zero illegal submissions. Result seq 8631, hash `47ef33d24109327d5cca6da79878464d7ed6d17d93fec39cdbbe490ff8861c38`; snapshot `823616f26f51b99287d04907728afb255e41603e3337afb096faf49dfe31364a`. PGN read back.

The supported ...e5/...e4 advance forked Bd3 and Nf3, and ...exd3 won the bishop. White's Nxd5 was then answerable by ...Nxd5 because the d3 pawn blocked Qd1's file. ...Nb6 escaped c4. White offered its second bishop with Bc7, and ...Qxc7 captured it. ...Bf5/...Bxe4 retained support for d3 and took another pawn.

I moved the queen off the e-file after Re1 and accounted for captures on e4. ...Nxc4 was supported by Qd4; ...Qe5 escaped Nb3 while defending Bc5. ...Ne3 forked Qd1 and Rf1, with f2 initially pinned by Bc5. The actual 24.Rxc5 was not the reply I had calculated before ...Ne3: it removed that bishop and attacked Qe5. I then chose and accounted for the forcing simplification ...Nxd1 Rxe5 ...Rxe5 Rxd1. Both queens and a rook were exchanged, with Black conceding that knight as anticipated in this line; the resulting extra rook, bishop and pawn were retained. Do not present the whole sequence as a fully predicted variation from move 23.

...Rd8, ...Bf3 and ...Re2 supported the passer without assuming Rd8 could see through Nd4. White's final knight was captured by ...Nxd4. ...d2/...Re1 used the pawn's actual support of e1; after Kh2, ...Rxf1 took the final rook and ...Rh1# finished with bishop support through g2. Final Black material was 2R+B+N+6P against 5P. No rejected candidate was submitted, and no unnoticed direct capture of the moved piece was identified in this game. This is a skill-0 conversion, not proof of reliable transfer or sustained improvement.

After 106: 44W/2D/60L overall; skill 0 is 34W/0D/2L in 36 games. Trial 13 is 2W/0D/2L, with both wins at skill 0. Elo is 1660 [1540, 1780], 70 rated total/latest 50 used, 36 maximum exclusions. Continue the two nominal-1800 games to the declared endpoint. No valid new cumulative usage counter is available.


## Benchmark 107 — White versus nominal 1800, win after a pawn loss and declined recaptures

Finished 2026-10-02 07:18:29 UTC by 49.Qg8#, 97 plies / 49 own moves, zero illegal submissions. Result seq 8730, hash `b13e038094f897b2954369736ab976528216490f3790ba3ac2c8b9b2745aa0e2`; snapshot `19008aa75c371bfc36bc2e056b931e13e7acb47beade1df18c35f56855543145`. PGN read back.

Balanced opening exchanges produced a supported d5 passer. I cleared Qd1's file before taking on c5, then used c4 and Rd1 to defend d5. However, 22.d6 was too optimistic: I counted Ne4 and Rd1 as defenders and recognized ...Bxe4/Qxe4, but did not carry the removal of Ne4 into the subsequent ...Bxd6 calculation before advancing. After the actual bishop exchange, I recognized the changed defenders and avoided the losing Rxd6/Qxd6 recapture. Black took d6, a real pawn loss caused by incomplete defender-removal accounting.

The rooks gained activity on the d-file, queens were exchanged, and Rd2 defended b2. Bxc5 recovered the pawn, restoring equal material. On 33.Bxf8 I anticipated an equal bishop exchange, but Black played ...Rbb8. I saved the bishop with Bc5, supported by Rd5. After both rooks attacked it, Be3 withdrew while the possible ...Rxd5/Rxd5 exchange remained accounted. The supported c5 advance followed.

Black then declined further legal recaptures: after 37.R5xd4 it played ...Kh7 instead of ...exd4, and after 41.Rxe6 it played ...a4 instead of ...fxe6. In each case I moved the rook away from the pawn attack on the next turn, retaining the extra rook. I removed the advancing a-pawn before promoting c6-c7-c8. Rh8+ was supported by Qc8 after Rd8 vacated the queen's line; Bd4+ forced ...f6 and Qg8 mate was supported by Rh8. Final White material was Q+2R+B+4P against 4P.

This is a completed nominal-1800 win, with no illegal attempts or unnoticed own piece drop identified. It still includes the failed d6 advance, and the large winning margin depended on explicit opponent errors, including three declined recaptures. Do not treat it as evidence that the whole tactical process is reliable.

After 107: 45W/2D/60L overall; nominal 1800 is 11W/0D/24L in 35 games. Trial 13 is 3W/0D/2L. Elo is 1670 [1550, 1790], 71 rated total/latest 50 used, 36 maximum exclusions. The ten-point rise from the trial baseline is small within the wide interval and does not establish sustained improvement. Complete game 108 before the declared endpoint assessment. No valid new cumulative usage counter is available.


## Benchmark 108 — Black versus nominal 1800, king move pins the needed defender

Finished 2026-10-02 07:30:54 UTC by 26.Qxf8#, 51 plies / 25 own moves, zero illegal submissions. Result seq 8783, hash `fda1d73ff685a5a97b3822881a8a8fd2745da0255d4c4f3405d7c171cb60dd52`; snapshot `874f4d48c86ebccd8316bd773ab833cfca6d750124abf16d3b00665c7d7ca117`. PGN read back.

Opening bishop/knight and central pawn exchanges preserved nominal equality. ...Qc7 unpinned Nf6, and ...Rfe8 allowed an accounted rook exchange before ...gxf6 recaptured Bf6. That recapture left doubled f-pawns and an exposed king. Qf5, Nh5+ and Qxh7 developed the attack; h7 was actually lost after the king moved toward f8.

22...Be7 defended f6 while Qc7 supported the bishop against Rxe7. I then played 23...Ke8 to move away from the h-file attack, treating Be7 as a useful blocker but failing to apply the new absolute pin on the e-file. 24.Nxf6+ captured the pawn with check; ...Bxf6 was illegal because it would leave Re1 checking Ke8. I recognized that only after submitting the king move. ...Kd8 then left c8/c7 occupied by my rook/queen, d7/e8 controlled by Nf6, and e7 occupied by the bishop. Qh8+ forced ...Bf8, followed by the referee-confirmed Qxf8 mate. The prior king move was legal but made the needed defender unusable. No illegal recapture was submitted.

This is a direct recurrence of changed king/blocker geometry defeating an assumed defense. It is not evidence that every earlier defense failed or that a particular alternative is best. Final Black material was Q+R+4P against Q+R+N+6P, with the king checkmated. No valid new cumulative usage counter is available.

## Trial-13 endpoint — no sustained improvement; replace the focus

Games 103–108: 3W/0D/3L, 216 own moves / 432 plies, zero illegal submissions. Maximum strength 0/2, skill 0 2/2, nominal 1800 1/2. Elo is 1660 [1540, 1780], exactly the baseline point estimate and interval; 72 rated total/latest 50 used, 36 maximum exclusions. Overall 45W/2D/61L in 108 completed games. Skill 0: 34W/0D/2L; nominal 1800: 11W/0D/25L; maximum: 0W/2D/34L. Storage reported 25,164,460 bytes.

The four role-reversed drills had already failed reliable execution in practice 19. The benchmark block retained serious errors: 103's checking skewer and own-king obstruction; 104's missed discovered checking capture and subsequent exchange concession; 105's omitted ...Kxb7 rook capture; 107's removal of Ne4 before ...Bxd6; and 108's self-imposed bishop pin followed by mate. In 106, the actual Rxc5 was not anticipated before ...Ne3, although the subsequent exchange was correctly rebuilt and converted. The wins, including 107 against nominal 1800, do not erase these failures. The wins assisted by large opponent errors are not independent evidence of reliable tactical control.

End trial 13 here. Do not extend the same practice or interpret the flat estimate as improvement. The next bounded trial will practice defending the attacked king from the learner's own side, specifically keeping a necessary defender movable and reducing the attack. Earlier trials 04 and 05 already addressed changed lines and exchanged defenders and failed transfer; their full plans and outcomes were reread at this endpoint. Thus the next trial revisits a known failure with a different opponent-practice task, not a newly discovered principle or a longer-checklist success claim.


# Trial 14 — keep the king's defenders usable

Declared after benchmark 108, reference clock 2026-10-02 07:34:42 UTC. Baseline 1660 [1540, 1780], 45W/2D/61L; 72 rated total/latest 50 used, 36 maximum exclusions. Next fixed benchmark endpoint: games 109–114. Opponent rotation, estimator, model and fair-play rules remain unchanged.

Target: a legal king move can pin or obstruct the very piece needed against the next check. In 108, ...Ke8 put Be7 between Re1 and the king; Nxf6+ then made the intended bishop capture illegal. In 104, the checking bishop departure from d2 changed the king/rook defense. Trials 04 and 05 already studied changed lines and defenders and failed. This trial is a focused rehearsal of an old weakness, not a claim of novelty or a longer checklist proving learning.

Practice change: defend from my own side against maximum strength for a longer short continuation, instead of the six-move role-reversed captures in trial 13. Exactly two recorded sessions, in order:

1. Black from game 108 after ply 45, before the failed ...Ke8. Remembered. Manually consider ...Qc6 as an unverified alternative: it would defend f6 with the queen while keeping the king off the e-file. The actual opponent may choose a different attack; this is not a supplied engine answer.
2. Black from game 104 after ply 49, in check after Bxh6+. Remembered. Reconstruct the checking line and choose the defense on the actual starting board. Do not presume that an earlier imagined king square is legal or safe.

Each session ends naturally or explicitly unfinished after twelve own moves and the final opponent reply. Combined practice-and-review ceiling: 2026-10-02 08:04:42 UTC. No extra repeats, no replacements for an unfavorable starting position, and no later historical move lookup during either session. End any active drill at the ceiling and record omissions. Both are remembered own failures, so even a clean continuation is rehearsal, not independent proof of transfer or a completed defense unless the game actually ends.

The immediate practice objective is to reduce the attack while preserving legal recaptures and king exits. Before a selected king move, reconstruct the new rook/bishop/queen line through the king, including any own blocker now pinned; then inspect the next forcing check using that resulting board. A piece geometrically reaching a capture square is not a usable defender if moving it exposes its king. When an opponent exchanges a defender, discard that defender from the next branch. Keep direct destination captures and ordinary checks in view, but use only brief factual notes when useful, without mandatory per-move audit claims.

Record the actual lines, material changes, illegal attempts, newly imposed pins or obstructions, and whether the attack was resolved at the cap. For benchmarks 109–114, retain every analogous recurrence and the full W/D/L/Elo outcome. A recurrence rejects reliable execution; a clean block or small rating rise still requires later repeated evaluations before sustained improvement can be claimed. Revise at 114 rather than continuing this method indefinitely.

Only own chess reasoning, own existing notes and the referee during play. No external move advice, engine analysis, automated move search/scoring/attack enumeration, tablebases or delegated chess work. No valid new cumulative usage counter is available.


## Practice 23 — remembered 108 defense, immediate mate

Finished naturally at 2026-10-02 07:36:14 UTC, one own move / two plies, zero illegal submissions. Result seq 687, hash `09189acc28a4f90e59ca78a1439a7e38594543c9817e0e9ff074bff8b5fa6c60`. PGN read back. Actual line: 23...Qc6 24.Qh8#.

The proposed ...Qc6 did add queen support to f6 while leaving Kf8 off the e-file, but it failed to answer the immediate mating threat. In the manual assessment I incorrectly treated e8 as an escape after Qh8+, focusing on Be7 blocking Re1; the queen on h8 itself controls e8 along h8-g8-f8-e8 once the king leaves f8. Be7 occupied e7, f7 was occupied, and the queen covered g7/g8. The referee confirmed mate on the next move. This is an omitted immediate check and a wrong king-exit assessment, not a successful alternative to ...Ke8.

The starting position may already require an earlier defensive improvement, but no claim that every legal defense loses has been proved. The late remembered selection cannot test recovery from a sound position merely by being called practice. Retain it, with no replacement or extra repeat. The first session already refutes reliable execution of this trial's immediate objective. Complete only the second predeclared session and preserve the benchmark endpoint 109–114; practice has no Elo effect.


## Practice 24 — remembered 104 defense, rook saved and then lost to promotion

Finished naturally at 2026-10-02 07:47:26 UTC by 37.h8=R#, twelve own moves / 24 plies, zero illegal submissions. Result seq 713, hash `65012f1d5663213d1ca35b1259a20cbf74be11c74a2d3bfd66369bdf03ad07a3`. PGN read back. Line: 25...Kc8 26.Bxg7 Rf7 27.h6 Bf8 28.Bxf8 Rxf8 29.g5 Rh8 30.Rh1 Nb6 31.g6 Nd5 32.g7 Ne7 33.gxh8=Q+ Kd7 34.Rd1+ Nd5 35.h7 Ke7 36.Qg7+ Ke8 37.h8=R#.

The starting board showed c6/c7 occupied by my own pawns and d6 attacked by e5; I chose ...Kc8 without an illegal attempt. ...Rf7 escaped Bg7 while attacking it. After h6 defended the bishop, I avoided ...Rxg7/hxg7 and instead used ...Bf8, genuinely supported by Rf7. Bxf8/Rxf8 traded bishops while retaining the rook, unlike the measured game's exchange concession.

That limited improvement did not hold the defense. ...Rh8 and the knight route a4-b6-d5-e7 focused on blockading g8/h8. I explicitly rejected ...Nf6 because e5 could capture there, but then omitted the most immediate consequence of 32.g7: the pawn now directly attacked Rh8. 32...Ne7 covered g8 but did nothing against 33.gxh8=Q+, an actual unanticipated rook loss with promotion. This repeats the direct pawn-capture failure despite the narrower king/defender focus. The later checks drove the king back; the actual final promotion was to a rook, not the queen I had anticipated, and the referee confirmed mate.

Initial material was R+B+N+6P each. After Bxg7 and the bishop exchange, Black had R+N+5P against R+N+6P. Final Black material was N+5P against Q+2R+N+4P. The saved rook in the early continuation is limited rehearsal evidence; the whole drill failed. Neither the starting position's objective evaluation nor an earlier best defense has been established.

## Trial-14 practice endpoint

Both predeclared sessions completed by 07:47:26 UTC, before the 08:04:42 ceiling, with no repeats or replacements: thirteen own moves / 26 plies, two checkmate losses, zero illegal submissions. Practice 23 missed an immediate queen mate and misread the eighth-rank king escape. Practice 24 initially kept the rook, then missed a direct pawn capture and promotion. The first objective has already failed reliable execution; the second demonstrates that concentrating on king lines can still displace an elementary capture threat elsewhere.

No improvement is claimed from these drills, and practice does not enter Elo. Return to fixed games 109–114 as declared, preserving these failures. Keep the modest cue about newly pinned defenders without treating it as a complete safety certificate or adding successful-audit counts. The benchmark baseline remains 1660 [1540, 1780], 45W/2D/61L through 108. No valid new cumulative usage counter is available.


## Benchmark 109 — White versus maximum strength, defender exchange and e-file loss

Finished 2026-10-02 08:04:50 UTC by practical resignation after 22...Qxe1+, 44 plies / 22 own moves, zero illegal submissions. Result seq 8829, hash `438a919b5e48bb48494437394e51d6828e8571f731ae45d85f2ff674726298a3`; snapshot `ebf48a6171d6dbc8fc02e1be6026c815096e938cdb14b9d580b93e0f3a5ac79f`. PGN read back.

The early d4 advance removed d3's support of e4, which Re1 restored. Qd3 unpinned Nf3, but the ensuing ...Bxf3/Qxf3/...exd4/cxd4/...Bxd4 sequence lost the central pawn. Bb5 avoided the additional Ne5 fork of Qf3 and Bc4. After Nc3 and Be3, however, I failed to carry ...Bxc3/bxc3 into the new e4 defense: Nc3 had departed and Be3 blocked Re1, leaving only the queen against ...Nxe4 supported by Re8. Black took a second pawn. Bd4 subsequently restored the rook and queen lines, but the earlier pawn loss remained.

The bishop-for-knight exchange on e5 was accounted. Qf3 defended c3, then 20.Rad1 was followed by the omitted ...Ng5: the knight attacked the queen while clearing the e-file between Re5 and Re1. With Qe7 behind the rook and White's king boxed by its pawns, the actual Qf4/Rxe1+/Rxe1/Qxe1+ sequence lost both white rooks for one black rook. I recognized this danger after ...Ng5 and deliberately chose that continuation; it was not an unexpected final queen capture, nor a proof that all earlier alternatives lost. The failure to prevent the forcing sequence belongs to the earlier position assessment.

At resignation White had Q+B+5P against Q+R+N+7P, nominally a rook and two pawns down. Bf1 remained a legal block of the current queen check; this was not checkmate and I did not claim a forced-loss certificate. The practical resignation retained the material loss and every played move.

After 109: 45W/2D/62L overall; maximum strength 0W/2D/35L in 37 games. Elo remains 1660 [1540, 1780], 72 rated total/latest 50 used, 37 maximum exclusions. Trial 14 has one benchmark loss following its two practice checkmates; no sustained improvement is established. Continue the declared block through 114 without adding practice mid-block.

The goal tracker was queried again at this checkpoint. It still returned the obsolete two-100-game maximum-strength objective with status blocked and the same stale 17,035,946-token / 178,558-second values, last updated before this continuation. This does not provide a valid new cumulative usage counter. No usage entry, goal reset, completion claim or status change was made. The latest user Continue and current local GOAL.md authorize continuing the revised measured-Elo experiment.


## Benchmark 110 — Black versus maximum strength, blocked king exit and exchanged rook defender

Finished 2026-10-02 08:23:00 UTC by practical resignation after 17.Qxh7, 33 plies / 16 own moves, zero illegal submissions. Result seq 8864, hash `3643b832b5c7a6cd1f50c252454f83aada36808619ee48b8d411360a742b45d3`; snapshot `2c162ef9d565d6ec363ef226a13ba22e448dc8984ac3b17b4f538aeb5238b375`. PGN read back.

The Caro-Kann pawn advance sequence led to ...fxe6 and an extra pawn, followed by Bxh7/Rxh7. I recognized the Qd3-g6-h7 danger and used ...Ne4 to block the diagonal, with d5 supporting that knight. After Nc3 I played 11...Nd7, intending ...Nf6 to defend Rh7 following an exchange on e4. This omitted White's 12.f3, and Nd7 also occupied the king's d7 escape square. In my subsequent manual calculation, immediately moving Ne4 to f6 or c3 would allow Qg6 with no identified legal answer. That is an unverified limited branch assessment, not a proof that every defense lost.

I chose 12...Ndf6 knowing the e4-knight remained exposed. The actual fxe4/dxe4/Nxe4 sequence left Black a knight down for one extra pawn. ...Qa5+ cleared d8, but Bd2 attacked the queen and required ...Qb6. White then played Nxf6+: the knight I had counted as Rh7's defender was exchanged. I had considered ...gxf6 opening the seventh rank for a possible ...Rf7 against Qg6+, but overlooked the simpler direct Qxh7 until the checking knight had already arrived. After ...gxf6, White captured the rook immediately along d3-e4-f5-g6-h7. No such extra defensive tempo was available.

At resignation Black had Q+R+B+7P against Q+2R+B+N+6P, a rook and knight down for one pawn. Black was not in check; this was practical resignation, not checkmate or an established forced-loss proof. The same departed-defender mistake recurred, while the narrower king-move cue did not prevent an own knight from obstructing a needed king exit.

After 110: 45W/2D/63L overall; maximum strength 0W/2D/36L in 38 games. Elo remains 1660 [1540, 1780], 72 rated total/latest 50 used, 38 maximum exclusions. Trial 14 is 0W/0D/2L in benchmarks so far, with its practice failures retained. No sustained improvement is established. Continue the predeclared block through 114; do not add practice or reset results mid-block. No valid new cumulative usage counter is available.


## Benchmark 111 — White versus skill 0, retained material and a completed pin-based mate

Finished 2026-10-02 08:36:00 UTC by 31.Qg7#, 61 plies / 31 own moves, zero illegal submissions. Result seq 8927, hash `963d596c6bc7114f3e71ad18aba6f155ca196993c87aa8480cae4d7315015ce8`; snapshot `a607c9d0bf73a3853ab7008ead1fd5d9abaa4015d5bfd7195eeff4419162d8bf`. PGN read back.

Development and castling preceded e5. Qd2 supported Bf4 against ...Nh5, and exd6 attacked Qc7, making an immediate ...Nxf4 inappropriate. After exd6/Bxd6/Bxd6, Black played ...Qc8 instead of recapturing. Later ...Rf8 allowed Bxf8, and ...b5 again declined a recapture; Bd6 saved the bishop. Bxh5 won the other knight. I moved the bishop away from ...g6 and ...f5, and moved Nc3 to e2 after ...b4 rather than onto the pawn-controlled e4 or d5 squares.

Bxd5 offered a bishop-for-knight exchange, but Black instead played ...Qd7, permitting Nxd7. ...Kf7 declined that recapture too. Bb3 then saved the bishop from c6/e6 pawn attacks. The enormous advantage therefore arose largely from the opponent's repeated missed recaptures and queen loss, not from forcing those concessions. White retained every non-pawn piece through the game.

I did not play Qxe6 once ...Re8 defended the pawn. Nc5/Nxb7 removed Black's last bishop. After ...f4 attacked Qe3, the actual finish was Qe5+ Kf7, Qf5+ Kg7, Be5+ Kg8, Qg6+ Kf8, Qg7#. Qf5+ correctly relied on Bb3 absolutely pinning e6 to Kf7, so ...exf5 was unavailable. Be5 then supplied the final queen's protection and covered h8. The last four checking moves and this actual king route were calculated before Qf5+ and confirmed by the referee's mate result. This is a successful local tactical calculation in an already overwhelmingly won position, not sustained benchmark improvement.

Final material: White Q+2R+2B+2N+7P against R+7P. No actual unanticipated material loss or king-exit error was identified in this game. One earlier note called a hypothetical ...Nc4 fork a fork of the queen and bishops; the actual contemplated targets were Qd2, Bd6 and Ne5, with Ne5 able to capture Nc4. That branch did not occur.

After 111: 46W/2D/63L overall; skill 0 is 35W/0D/2L in 37 games. Elo 1670 [1550, 1790], 73 rated total/latest 50 used, 38 maximum exclusions. Trial 14 benchmarks are 1W/0D/2L so far. The small rating rise and this skill-0 conversion do not undo the two maximum-strength losses or practice failures. Continue the fixed endpoint through 114; no valid new cumulative usage counter is available.


## Benchmark 112 — Black versus skill 0, a large material lead lost to a forced king chase

Finished 2026-10-02 08:53:33 UTC by 27.Rh5#, 53 plies / 26 own moves, zero illegal submissions. Result seq 8982, hash `94722255bfe7c3bfff5cf3256a2bc3ef7288f8b282fe671f21f615341b018628`; snapshot `f08966b795508f8deedab3c774f20213366a71c58509662d05063e19718c4a43`. PGN read back.

Early development and castling were followed by ...Nd4 and ...h6. After Nxd4/exd4, White moved Bg5-d2 instead of resolving both pawn attacks, allowing ...dxc3. Bxh6/gxh6 then lost White another bishop. ...cxb2/Qxb2 removed a further pawn with a queen/rook fork, and ...Rb8 defended b7. The ...a6/...b5 preparation avoided relying on an unsupported rook recapture on b5 in front of White's queen. ...Kh7 defended h6 before ...bxc4 took the central pawn.

Against d5 I used ...Nxe4 to attack Qd2, then met Qd4 with ...Bf5, both saving the bishop and defending Ne4. Bg4/Bxg4/hxg4 removed that defender, and I explicitly moved the knight rather than continuing to count the departed bishop. ...Ng5 was genuinely defended by Be7; I also correctly identified that h6 was pinned to Kh7 by the now-open h-file and could not capture off that file. These local recognitions did not make the subsequent king defense sound.

The actual losing finish was 22...Ng5 23.Rxh6+ Kxh6 24.Rh1+ Kg6 25.f4 Nh7 26.f5+ Kg5 27.Rh5#. The rook on h6 was not defended by Qd4 or White's pawns, but the remaining rook could immediately transfer from g1 to h1 and continue checking. I treated safe immediate capture squares as sufficient while failing to resolve the continuation. After f4, I rejected ...Ne6 because d5 could capture the knight and chose ...Nh7, relying on Kg6 to defend it against Rxh7. This omitted the forcing f5+: the knight itself then occupied the king's h7 exit, while Qd4 covered f6/g7, Rh1 covered the h-file, and f7 was occupied by my pawn. I identified only ...Kg5 manually and saw Rh5 mate before submitting it; the actual next move confirmed mate. No all-defenses proof for earlier positions is claimed.

At mate Black still had Q+2R+B+N+5P against Q+R+5P, a rook, bishop and knight ahead with equal pawn counts. Rh5 was protected by g4, and the queen, pawn and rook coverage left no king escape. This is a clear recurrence of an own piece obstructing the needed king route, and of stopping a defensive calculation before the opponent's next forcing check. It defeats any claim that the narrowly correct pin/defender observations constituted reliable execution. Zero illegal submissions did not prevent the tactical failure.

After 112: 46W/2D/64L overall; skill 0 is 35W/0D/3L in 38 games. Elo 1660 [1540, 1780], 74 rated total/latest 50 used, 38 maximum exclusions. Trial 14 benchmarks are 1W/0D/3L so far. The target has failed again, now against skill 0 despite a large lead. Preserve the result and finish the declared nominal-1800 pair 113–114 before the trial assessment and revision. No valid new cumulative usage counter is available.


## Benchmark 113 — White versus nominal 1800, queen concession and an undefended last rook

Finished 2026-10-02 09:35:35 UTC by practical resignation after 39...Qxe1+, 78 plies / 39 own moves, zero illegal submissions. Result seq 9062, hash `1fdb541991c793aea943923915d01d865b7a092e8365bf0c00bebb3da6714794`; snapshot `5bba03f7f26e132ca9eb51a8d6161aa944836a73a9ddfe33c4a3763f74b33cd4`. PGN read back.

Black's kingside pawn advance induced hxg4/Bxg4, pinning Nf3 to Qe2. I withheld the central d4 advance after recognizing that pin changed the available recaptures. Bxc5 was followed by ...Nh5 instead of ...dxc5, so Ba3 preserved an extra bishop and pinned d6 along a3-f8. Qe3/Bxf3/Qxf3 removed the original bishop pin without damaging f2/g2. Black's two knights nevertheless drove the queen back, and ...Qg5 threatened mate on g2.

17.g3 blocked that immediate line. Before attempting gxf4 I recognized that g3 was now absolutely pinned to Kg1, so the pawn could not actually capture Nf4 off the g-file. I chose 18.Nd5 to challenge the knight instead. I had considered ...Nde2+ but stopped the king-retreat analysis too soon. After that check arrived, I manually found ...Qh5 mate after either Kh1 or Kh2: the knights covered the exits, g3 blocked Qe3-h3, and the available pieces could not answer the h-file check. I chose 19.Qxe2, knowingly allowing ...Nxe2+, rather than submit that mating line. This was a deliberate queen concession following an earlier tactical failure, not an unexpected knight capture and not a proof that every earlier defense lost.

The king then escaped through g2-f3-e3-d2-c1-b1. Rfe1 had cleared f1, but ...Nxg3 subsequently attacked f1, which I recognized before selecting Kf3. Bxb5 recovered a pawn. Against ...Nf5+ I used exf5/Qxf5 to remove the last black knight, while recognizing that e4 would no longer defend Nd5. Ne3 forked Qf5/Rg2, but ...Qxf2+ escaped with tempo. ...Qf4 then absolutely pinned Ne3 to Kc1; I did not submit Nxg2 and used Kb1 to remove the pin. These were locally correct changed-board observations amid an already compromised game.

After moving the knight away from repeated attacks, I exchanged rooks with Rxf4/exf4 and placed the remaining rook on f1. I rejected an immediate second Rxf4 because ...Qg1+ could exploit the boxed king, then played c3 with tempo against Qd4 and opened c2. Black answered ...Qe3, defending f4. The decisive new blunder was 39.Re1: I treated attacking the queen and supporting Ne4 as sufficient, but the rook on e1 was now undefended. The second white rook, which had supported it earlier in the game, had been exchanged. Black simply played ...Qxe1+. This was an actual unanticipated rook loss, repeating the missing-defender failure despite recognizing several other pins and king routes correctly.

At resignation White had 2B+N+4P against Q+R+6P, nominally a rook and two pawns down. Kc2 remained legal; this was not checkmate. The remaining rook loss and the failed king-retreat calculation outweigh the successful local observations and the opponent's earlier missed bishop recapture. No reliable transfer is established.

After 113: 46W/2D/65L overall; nominal 1800 is 11W/0D/26L in 37 games. Elo 1650 [1530, 1770], 75 rated total/latest 50 used, 38 maximum exclusions. Trial 14 benchmarks are 1W/0D/4L, with the final paired Black game 114 still required before the declared assessment. Continue that game without adding a new practice period mid-block. No valid new cumulative usage counter is available.


## Benchmark 114 — Black versus nominal 1800, incomplete exchanges and a failed pawn defense

Finished 2026-10-02 10:50:16 UTC by practical resignation after 80.g8=Q; 159 plies / 79 own moves, zero illegal submissions. Result seq 9223, hash `99930f83f49f7f7098cb34651939341e2a9842f25ca7170de04862b329a13cec`; snapshot `ffee30592cbe953df1c69dfa1654ccb9576cae1f130136f1d9230d4642ae4f67`. PGN and status read back.

The first material error was 11...Re8 12.Bxg4 Nxg4 13.Qxg4. I counted Nf6 as the bishop's defender but omitted Qa4's clear fourth-rank line to g4 after the recapture. Black lost a knight. The subsequent ...e4/...Ne5 and pawn advances drove the queen back, and ...e3/...exf2+ created counterplay. Later ...Ne3/Nxe3/Bxe3 and ...Bxc1/Rxc1 removed the remaining minor pieces. ...Qxe2 allowed Qxd5+, and White's Kg2 made Rxf2 possible despite queen support of f2: ...Qxf2 would allow Kxf2. I recognized that limitation before 32.Rxf2. Black then had equal pawns but one fewer knight.

Active rooks and the queen pin on Nf3 recovered a5. Qc6 saved the attacked queen while still defending Re8 and Rd5. White's 41.Qxf6+ allowed ...Qxf6/Rxe8+, exchanging White's queen for a rook and pawn. Black now had Q+R against 2R+N, with equal pawns; ...Qxc3 briefly added a pawn. This opponent concession supplied the new opportunity. ...g4 maintained a pawn chain, and ...Qf3/...Rd2 threatened the pinned Ng2. White checked repeatedly and then played 53.Rxf3, which I had not included in the selected king-route continuation. After ...gxf3/Re6+/...Kf5/Re8/...Rxg2+, however, the actual sequence recovered the knight and reached equal rook-and-three-pawn material. The unanticipated queen capture is a calculation omission, but calling it a queen loss with no subsequent compensation would misstate the completed exchange.

I correctly avoided immediately pushing f3 while Rg2 depended on that pawn against Kh3, and used ...Rg1 first. The next failure was 57...Ke4 58.Kg4 Ke3 59.Rxf3+: I had counted my king's support of f3 without applying the opposing king's protection of the capturing rook. Kxf3 would put the kings adjacent. The passer was lost and Black entered R+2P against R+3P. No best earlier defense is established.

The queenside king route and ...a5/bxa5 created an a-passer. Supported advances to a3 induced 73.Rxa3/Kxa3, leaving Black's rook against the connected g/h pawns with the black king on a3. I did not establish that this position was winning; the later result must not be described as losing a proved win. While the king returned through b4/c5/d6, White advanced g5/g6/g7. ...Rg1 stopped an unsupported promotion, but Kh7 supported g8 and h6 retained the second passer. ...Rg5 and ...Ke7 were too late in the actual continuation: 80.g8=Q.

Final position: Black Ke7/Rg5 against White Kh7/Qg8/h6. Black was not in check and Kf6 remained legal. The considered rook-for-queen exchange left a further h-pawn promotion threat; the actual result was practical resignation, not checkmate or a complete proof of every defense. Zero illegal submissions did not prevent the errors in exchange completion, king-protected captures, or pawn timing.

After 114: 46W/2D/66L overall. Maximum strength 0W/2D/36L, skill 0 35W/0D/3L, nominal 1800 11W/0D/27L, each over 38 completed games. Provisional engine-relative Elo 1640 [1520, 1760], 76 rated total/latest 50 used, 38 maximum exclusions; storage 27,422,576 bytes. No valid new cumulative usage counter is available.

## Trial 14 endpoint — failed; revise the intervention

Fixed benchmarks 109–114 finished 1W/0D/5L, 213 own moves / 428 plies, zero illegal submissions. Both maximum-strength games and both nominal-1800 games were lost; skill 0 split 1–1. The only win relied heavily on declined opponent recaptures. The two predeclared remembered practices also ended in checkmate losses, thirteen own moves / 26 plies in total, without repeats or replacements.

Elo declined from 1660 [1540, 1780] through 108 to 1640 [1520, 1760] through 114. The intervals overlap broadly; the result supplies no sustained-improvement evidence. The king/defender focus failed its stated execution objective: 112 obstructed a needed king exit and was mated despite a large material lead; 113 lost its remaining undefended rook after forgetting the other rook had departed; 114 again stopped an exchange too early and later relied on a king recapture forbidden by the opposing king. The practice mates and 109–110 supply further failures. Isolated correct recognition of pins and departing defenders does not overturn those results.

Retire trial 14 as the main intervention. Long branching, short timed decisions (trial 09), static reconstruction, and remembered defensive continuations have all already failed to establish transfer. The next intervention must declare a bounded learning activity and fixed new evaluation endpoint; do not claim novelty from restating these same safety cues or improvement from completing another worksheet. Preserve every record.

The goal tracker was read again after 114. It still has the superseded two-100-game maximum-strength objective, status blocked, and unchanged stale 17,035,946-token / 178,558-second values. No new usage entry, reset, completion claim, or status change was made. Current GOAL.md and the user's Continue still authorize the measured-Elo experiment.


# Trial 15 — complete development before exposing pieces

Declared 2026-10-02 10:53:39 UTC after benchmark 114 and the completed trial-14 assessment. Baseline provisional engine-relative Elo 1640 [1520, 1760], 46W/2D/66L; 76 rated total/latest 50 used, 38 maximum exclusions. Next fixed evaluation: benchmarks 115–120 in the unchanged paired-color rotation. No sustained improvement is established.

Intervention: change the opening positions I seek, rather than add another tactical checklist or repeat late defensive rescues. In 114, repeated bishop moves and the incomplete g4 exchange lost a knight before move 14. In 110, the early exposed rook and king prevented straightforward development. Earlier fresh full-game practice (08/09) did not test this particular opening choice; it also failed to establish improvement. The present choice may concede activity and is not a claim of theoretically best opening play.

White: start with 1.d4. Aim for Nf3, e3, Be2 and castling, followed by c4/Nc3 when the actual center permits it. Develop the remaining bishop through a real available route instead of rushing it onto an exposed advanced square. These are priorities, not a move script; checks, pawn attacks and concrete captures can require a different order.

Black: against 1.e4 try ...e6 and ...d5. If White advances e5, consider the central ...c5 break before putting a knight on f6 where the pawn would immediately attack it. If Nc3/Nd2 defends e4, ...dxe4 followed by development is a simplifying candidate, not an automatic move. Against d4/Nf3/c4 starts, seek ...d5/...e6, ...Nf6, ...Be7 and castling before an unsupported bishop sortie. Apply the actual position and finish exchanges; no opening preference overrides a direct threat.

Short own study before practice: identify the costs of these choices. e3/e6 restricts the queen bishop, so its development still needs a route; castling alone does not complete development. Moving a center pawn may remove a knight's defender or open a queen/rook line. A quiet bishop square is not automatically safe. Avoid unnecessary early queen moves and repeated piece moves, but retreat an attacked piece when needed. Do not mechanically copy a remembered sequence after the opponent diverges. These observations are own unverified preparation, not external opening advice or an independent evaluation.

Exactly two recorded opening sessions at nominal 1800:
1. White from the standard initial position.
2. Black from the standard position after White's 1.e4: FEN `rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1`.

Neither session is a replay of a measured continuation. They are selected opening rehearsals, not blind accuracy tests. Cap each at twelve own moves plus the final opponent reply, or finish naturally sooner. Combined setup, play and review ceiling: 11:23:39 UTC on 2026-10-02. At the ceiling end any active drill explicitly unfinished and record any unstarted session; no extensions, replacements or repeats to obtain favorable results.

At each cap record actual material, development, king location, and any unanticipated piece loss, direct mating sequence, or newly unusable recapture. An unfinished opening is neither a win nor a draw. A clean opening against this opponent does not establish stronger play. During the fixed block 115–120, retain the same opening priorities and specifically record unanticipated piece losses within the first fifteen moves, alongside every later tactical failure and full W/D/L/Elo result. Fewer early losses would be limited evidence about the opening intervention only; later losses still determine overall performance. Compare the whole block at 120 and revise if it fails.

Only own reasoning, pre-existing notes and the referee during play. No engines except the referee opponent, no opening explorers, external position advice, tablebases, automated chess analysis/search/attack enumeration, or delegation. No decision-clock target or invented token counter. All practice results stay outside benchmark Elo.


## Practice 25 — White opening rehearsal, stopped at the cap

Stopped 2026-10-02 10:59:24 UTC after exactly twelve own moves and the final reply, 24 session plies, zero illegal submissions. Unfinished result `*`, not a win or draw. Result seq 740, hash `4e193b28864ce3db687c53918cd4b0682f3bbd331a3c099a668ba1477f2b79db`. PGN read back.

Actual line: 1.d4 d5 2.Nf3 Nf6 3.e3 e6 4.Be2 c6 5.O-O Bd6 6.c4 Nbd7 7.Nc3 Ne4 8.Bd2 O-O 9.Rc1 Qe7 10.cxd5 Nxd2 11.Qxd2 exd5 12.Rfd1 Nf6.

Castling finished on move five and all four minor pieces had developed by move eight. Bd2 was offered for Ne4 with Qxd2 available; the actual central exchange completed without an unanticipated loss. Final White material Q+2R+B+2N+7P, Black Q+2R+2B+N+7P. White's remaining minor pieces and both rooks were developed. I rejected b3 while Nc3 still relied on b2, then chose a real bishop route. This local catch is not transfer evidence.

No actual direct major-piece loss, missed mate, or unusable recapture was identified in these twelve moves. The middlegame and eventual result are untested, and no position evaluation or optimal-play claim is made. Preserve this unfinished record and proceed to the one declared Black rehearsal without repetition.


## Practice 26 — Black opening rehearsal, stopped during a planned exchange

Stopped 2026-10-02 11:04:01 UTC after exactly twelve own moves and White's final reply, 24 session plies, zero illegal submissions. Unfinished result `*`, not a win or draw. Result seq 767, hash `4adf6e306d618ef2be4a9b3dbef9e685beb7b9c1ad38af83051b71a11a2a12d7`. PGN read back. The starting FEN already contained White's 1.e4; it is not an additional session ply.

Actual line: 1...e6 2.Nf3 d5 3.Nc3 dxe4 4.Ne5 Nd7 5.Nxd7 Bxd7 6.Nxe4 Nf6 7.Nxf6+ Qxf6 8.Qf3 Qxf3 9.gxf3 Be7 10.Rg1 O-O 11.d4 c5 12.Be3 Rac8 13.dxc5.

White declined the first immediate pawn recapture, and both knight pairs were then exchanged. Bxd7 developed the queen bishop; Qxf6 preserved the kingside pawns. The queen exchange induced doubled White f-pawns but does not establish a positional advantage. Black castled on move ten, which also supplied Kg8 as g7's defender against Rg1. Both surviving bishops and the a-rook developed.

At the cap Black had 2R+2B+6P against 2R+2B+7P: White had just taken c5. Before ...Rac8 I considered ...Bxc5/Bxc5/...Rxc5, with the c-rook supporting the bishop after the d-pawn vacated d4. That recapture and continuation were not played because the fixed cap had been reached. Do not silently credit equal final material or a completed exchange. No unanticipated piece loss, mate, or unusable recapture occurred in the played twelve-move segment, but the final position and future defense remain untested.

## Trial 15 practice endpoint

The two declared rehearsals ended by 11:04:01 UTC, 10 minutes 22 seconds after declaration and before the 11:23:39 ceiling. Total 24 own moves / 48 session plies, zero illegal submissions, two explicitly unfinished sessions and no W/D/L scores. No extra sessions, repeats or cap extensions were added.

Both sessions implemented the intended development priorities locally. White reached equal material with development complete; Black's final central capture awaits the planned recapture. Neither short segment establishes an opening advantage, full-game safety, benchmark transfer, or sustained improvement. In particular, the absence of a tactical failure in 24 own practice moves does not erase the repeated failures in earlier full games.

Return now to fixed benchmarks 115–120 with the declared opening choices. Assess early piece losses within the first fifteen moves and retain all later failures and full results. Baseline remains 1640 [1520, 1760]; practice has no Elo effect. No valid new cumulative usage counter is available.


## Benchmark 115 — White versus maximum strength, clean opening segment but lost ending

Finished 2026-10-02 11:30:38 UTC by practical resignation after 37...Kc7, 74 plies / 37 own moves, zero illegal submissions. Result seq 9299, hash `781254b64db39af51c5338d0307220db4c8db29ec7cb036bdac5dba3edb97785`; snapshot `c2391a5c945b8b86f9ba43b0d34c2cbee89ff0fa7c134d93325b52d060e4c566`. PGN and status read back.

The declared 1.d4/Nf3/e3/Be2 approach reached castling on move six, all four minor pieces developed by move ten, and equal material through move fifteen. cxd4/exd4 and dxc4/Bxc4 completed the central pawn exchanges. Against ...Na5, Bd3 was supported by Qe2; Bxd3/Qxd3 exchanged bishops, and Nxd5/Qxd5 exchanged knights. No unanticipated piece loss occurred within the trial's first-fifteen-move window. This is a local opening observation, not an evaluation that the resulting isolated-d-pawn position was equal or best played.

Black's ...Ba3/...Nb4 displaced the rook and queen. b3 had blocked Qd5's route to a2 and controlled c4, but ...Rc2 forced Qe1 and ...Nxa2 took a pawn. Ra1 avoided a prospective Nc3 fork of both rooks; it also withdrew Rb1's support of b3. Following ...Rfc8, Rd2/Rc1/Rd1/Rxa1/Rxa1, Black took b3 as well. These are actual pawn losses from the invasion and changed defense, not an unexplained material count.

After Nd2/Qb2/Ne4, ...Nc1 blocked Qe1's defense of Ra1. I had not resolved that maneuver before Ne4. Once it appeared, I explicitly calculated the whole c1 exchange before starting it: Rxc1/Rxc1/Qxc1/Qxc1+/Bxc1/Bxc1. The actual continuation left Ne4 against Bc1, with four White pawns versus six Black pawns, exactly the counted result. It was a deliberate simplification after an earlier positional failure, not a surprise loss of a queen or rook at the end of the chain.

Bb2 then attacked the undefended d4 pawn. Nd6/Bxd4/Nxb7 exchanged that pawn for b7, leaving three White pawns against five. Recovering b7 failed to account for the knight's confinement. ...Bb6 covered a5, c5 and d8, while the king's approach covered d6. Ke5 tried to support d6, but ...f6+ forced the king back. After ...Kc7, Nb7 was attacked by the king: a5/c5 were covered by Bb6, d6/d8 by Kc7, and d8 also lay on the bishop's diagonal. No saving forcing continuation was identified. The knight was still on the board at resignation; do not record an actual knight capture or call this checkmate.

A further missed defense change occurred with 35.Ke4: the king left f2's protection while Bb6 still attacked f2. Black chose the king approach instead of Bxf2. The absence of that pawn capture does not make the move a complete safety success.

Final material remained N+3P against B+5P, with the knight trapped in my manual assessment. This was practical resignation, not an independently proved full-position result. The opening intervention was implemented and avoided an early piece loss in this one game, but the later invasion, pawn losses and restricted knight still produced a loss. No sustained improvement is established.

After 115: 46W/2D/67L overall; maximum strength 0W/2D/37L in 39 games. Elo unchanged at 1640 [1520, 1760], 76 rated total/latest 50 used, 39 maximum exclusions. Trial 15 benchmark record is 0W/0D/1L, 37 own moves / 74 plies, zero illegal submissions. Continue the fixed block through 120 without adding practice mid-block. No valid new cumulative usage counter is available.


## Benchmark 116 — Black versus maximum strength, queen loss inside the opening window

Finished 2026-10-02 12:03:00 UTC by 31.Qxf8# after 30...Nf8: 61 plies / 30 own moves, zero illegal submissions. Result seq 9362, hash `e0a8b9c769e13cb89043d544c3dd83935ca8bbb2c7dad7a496203262bf05a0e5`; snapshot `e3abcd2338df785b4f47e067c6f2fb2bfd50d63b17ae41de13dee67393249049`. PGN and status read back.

The declared ...e6/...d5 approach led to an early central exchange and one knight-pair exchange. Black castled on move eight and developed the queen bishop with ...b6/...Bb7 by move ten. ...Rc8 supplied support for a later bishop recapture on c5. These development milestones did not prevent an early queen loss.

After 13.dxc5, I noticed that Bd3 could leave the d-file with Bxh7+, exposing the queen to Rd1. I nevertheless played 13...Qd5 and falsely described it as moving the queen off the d-file. It remained on that same file. Actual play was 14.Bxh7+ Nxh7 15.Rxd5 Bxd5. The incorrect historical note remains intact; I acknowledged and corrected the factual error immediately after Bxh7+. The capture with ...Nxh7 and the final bishop recapture knowingly accepted the queen-for-rook-and-bishop concession, but that does not excuse the unanticipated loss created by ...Qd5. This is a clear failure within the trial's first-fifteen-move window. The later thought of ...Qc7 was an unplayed, unverified alternative, not a demonstrated solution.

After ...Bxc5 and a bishop exchange, ...f6 had removed f7's defense of e6 while Bd5 still defended that pawn. 21...Bb7 saved the bishop from c4 but forgot its remaining defensive role; 22.Qxe6+ took the pawn and pinned the rook after ...Rf7. I avoided the prospective Ne7+ fork of Kg8/Rc8 by ...Rd8. Against Nh8, ...Rd7 added a real rook recapture on f7, and 25.Nxf7 Rxf7 completed that exchange as intended. Kxf7 was unavailable while Qe6 protected f7. These local catches did not repair the earlier material loss.

26...Kf8 tried to unpin the rook but allowed Rd1 with a direct back-rank threat. I had to return with ...Kg8. White instead chose Rd7, combining the rook and queen against f7. ...Be4+ was answered by fxe4, removing the bishop without disrupting the attack. After ...Kh8 Qxf7 I anticipated a mate on g7; the actual finish after ...Nf8 was the shorter 31.Qxf8#. Record the actual knight capture and mate, not the predicted Qg7 line.

The opening changed but the geometric error and removal of a pawn's last defender recurred. No tactical or overall improvement is established. After 116: 46W/2D/68L overall; maximum strength 0W/2D/38L in 40 games. Elo remains 1640 [1520, 1760], 76 rated total/latest 50 used, 40 maximum exclusions. Storage reported 28,609,547 bytes. Trial 15 benchmarks so far: 0W/0D/2L, 67 own moves / 135 plies, zero illegal submissions. Continue the declared block through 120; no new practice or changed trial criteria mid-block. No valid new cumulative usage counter is available.


## Benchmark 117 — White versus skill 0, win with opening and middlegame oversights

Finished 2026-10-02 12:22:15 UTC by 41.Rd8#, 81 plies / 41 own moves, zero illegal submissions. Result seq 9445, hash `8527a297fc5ccf06a2bea14e604758a7e7c18c15a677d6a032f692a299b0a861`; snapshot `5292c11aa84161c89f37621214ad893f1b52f77055a27ba143b051a8854094e1`. PGN and status read back.

Castling finished on move five, all minor pieces developed by move nine, and both rooks developed by move thirteen. However, 13...Nb4 cleared the c-file from Rc8 to my undefended Bc4. I answered with 14.a3 without noticing ...Rxc4; Nc3 blocked Rc1's recapture. Actual 14...Rxc4 15.axb4 Bxb4 exchanged my bishop for the knight and lost the a-pawn. This was an unanticipated bishop capture inside the first-fifteen-move window, although axb4 recovered an equivalent minor piece rather than leaving an uncompensated piece deficit. Do not count the opening as entirely clean merely because material was only one pawn down afterward.

Qd3 unpinned Nc3 and attacked the c4 rook. Ne5 attacked Rc6/Bd7, and Nxd7/Nxd7 completed a knight-for-bishop exchange. After Ne4/Rd5, 20.Rc4 overlooked 20...Ne5, which forked Qd3/Rc4. d4 could not capture that knight without exposing Qd3 to Rd5. I moved the queen to e2, allowing Nxc4/Qxc4 to cost the exchange, but Black instead played ...Nc6. That opponent omission saved the rook; it is not a successful tactical check by me.

After the remaining knight/bishop exchange, bxc3 strengthened d4. Rc5/Rxb5 recovered the pawn and Rxd5/Qxd5 exchanged a rook pair. The central advance c4/d5 gained space. Before Bxa7 I noticed that Be3 blocked Qe4's attack on Qe2 and first played f3. Only after ...Qf5 did Bxa7 take the pawn. dxe6/fxe6 then made c5 possible with bishop support. Bb6 kept the bishop and c5 pawn mutually defended while attacking Na5.

Black's 34...Rxc5 35.Bxc5 Qxc5+ deliberately allowed the previously considered exchange of the c-pawn and bishop for the rook. This left Q+R+3P against Q+N+3P. Qe4 offered a queen exchange with f3 as recapture support; after ...Nb3, Qxf5+ could be met by ...exf5. Black instead played ...g6, declining the available queen recapture and leaving my queen intact. Qxe6 saved it and took another pawn. This major opponent error sharply increased the advantage; do not credit it as learned conversion of the intended rook-versus-knight ending.

After ...Nc5 attacked Qe6, I calculated Qf7+/Kh8/Rd8# before playing Qf7+. The referee confirmed that exact two-move finish. This local mating sequence was correct, but the opening file oversight, the omitted Ne5 fork, and the opponent's refusal to take the rook and later the queen remain part of the win. No sustained improvement is established.

After 117: 47W/2D/68L overall; skill 0 is 36W/0D/3L in 39 games. The reported rolling estimate is now 1620 [1500, 1750], 77 rated total/latest 50 used, 40 maximum exclusions; preserve the actual decrease despite this win. Storage 28,913,619 bytes. Trial 15 so far: 1W/0D/2L, 108 own moves / 216 plies, zero illegal submissions. Continue unchanged through 120. No valid new cumulative usage counter is available.


## Benchmark 118 — Black versus skill 0, opening bishop loss and late queen blunder

Finished 2026-10-02 13:26:08 UTC by practical resignation after 64.fxe3, 127 plies / 63 own moves, zero illegal submissions. Result seq 9574, hash `7d95f429a821ba40ddd6b3879d7929fe6c8b592215b83b039933188e79c9fe06`; snapshot `0d9b2291184ca6a82c5fb79b5040e2d20cb5cd94172e212755fad66b85adcc39`. PGN and status read back.

Black castled on move five and completed minor-piece development by move nine. The central cxd4/Nxd4/Nxd4/exd4 sequence exchanged one pawn and knight pair. Nevertheless, 13...Bd6 offered the bishop while I falsely claimed Qd8 could recapture on d6. My own Bd7 blocked that file. White played 14.Bxd6; I recognized the obstruction before attempting the illegal recapture and saved the attacked f8 rook with ...Re8. The bishop was lost without compensation inside the first-fifteen-move window. The original wrong note remains; the next note corrected it. This is another direct failure of the opening intervention despite completion of development.

...Nd7/Nxe5/dxe5 exchanged the remaining knight for White's other advanced bishop. The d-pawn break and ...Qd5/...Qxg2 gave activity against the uncastled king. ...Qh1+ forced Nf1; ...Bg2/Kd2/Red8 put pressure on Bd3. However, 25...Rd7 left that rook undefended while intending a future doubling that was never completed. After ...Rxc3, 28.Bh7+ vacated d3 with check, exposing both Rd7 to Rd1 and Rc3 to Re3. I noticed the d7 loss before ...Kxh7, but White actually chose 29.Rxc3, taking the other rook. Record the actual rook capture, not the predicted Rxd7.

...Qb4 tried to pin Rc3; 30.Qc2+ both defended it and checked. ...Be4 blocked and attacked the queen but could have been captured; White instead chose Qb3. ...Rxd1+/Kxd1 completed the remaining rook exchange, and ...Qd4+/...Qxe5 recovered a pawn. Black then had queen, bishop and six pawns against queen, rook, knight and three pawns. The pawn compensation did not establish equality or a forced recovery.

I tried to prepare ...b5 with ...a6/...Bc6. When Rc1 attacked the bishop along the c-file, I correctly avoided moving b7 and leaving Bc6 undefended, but ...Bd7 removed the bishop's protection of b7 itself. White's 38.Qxb7 took that pawn. A local defender check thus missed the other changed defense. ...Qd6 held Bd7/a6 and ...Qe7 held f7 during subsequent checks.

The central pawns advanced with actual support: ...f5 was supported by e6; ...f4 by Qd6; ...e5 added pawn support; ...e4 was supported by the bishop and cleared a king escape; ...f3 was supported by e4. The king escaped repeated checks through f7/e6/f6/e5/f5/g4/h4. I explicitly avoided several imagined captures where a final recapture or blocked line would fail, but these catches are not improvement evidence. White saved Rc1 by Rc2 before the queen could capture it. The bishop retreated to a8 while keeping e4 defended. ...Kxh5 took the h-pawn, but 62.Qe8+ attacked both king and Ba8; after ...Kg5, 63.Qxa8 took the bishop.

The decisive final error was 63...Qe3+. I explored king moves and knight interpositions while omitting the immediate 64.fxe3 from the still-present f2 pawn. That ordinary pawn capture took the unsupported queen. Final Black material was king plus a6/e4/f3/g7/h6, against White queen, rook, knight and two pawns. The position was not checkmate; I resigned practically with legal moves still available. No claim of an independently proved full-position result is made.

The repeated opening obstruction, discovered rook attacks, removed pawn defender, and final missed pawn capture are retained. No sustained improvement is established. After 118: 47W/2D/69L overall; skill 0 is 36W/0D/4L in 40 games. Elo is 1590 [1470, 1710], 78 rated total/latest 50 used, 40 maximum exclusions. Storage 29,235,021 bytes. Trial 15 so far: 1W/0D/3L, 171 own moves / 343 plies, zero illegal submissions. Finish the declared 119–120 pair before revising the trial. No valid new cumulative usage counter is available.

## Benchmark 119 — White, nominal 1800; loss (2026-10-02 14:12 UTC)

Result: practical resignation after 50...Rxb2, 100 plies / 50 own moves / 0 illegal attempts. Result seq 9676, sha256 f38043afb6214daf37f166f1cc8000b0bbb83a80a84d4a0067518bf96d7fa6b6; snapshot 7d077e87f8c885d99685729627a1ced274eeb7cc88a5dc5857bcd6c7f4041123. The final position was not mate: White Ke3 Bd3, pawns d4/e5/f4/f2; Black Kg7 Ra3 Rb2, pawns e6/f7/g6.

Castled on move 5, developed all four minors by 8 and both rooks by 13. No unanticipated material loss in the first fifteen moves. 16.Bxb4 Bxb4 exchanged bishop for knight, preventing the Nb4-d3 fork of the two rooks. 17.Re2 correctly escaped the bishop's newly opened diagonal. 21.Rxc6 won an undefended pawn; 22.Rc1 escaped ...Bb7 and 23.Ne4 avoided the unfavorable ...Bxf6/exf6/Qxf6 sequence. These were local successes, not a successful full game.

25.Qd3 missed ...Ba6, skewering Qd3 and Re2. 26.Rc4 interposed with a calculated exchange concession, but Black played ...axb3, 27.axb3 Qd5, 28.Qc2 Nxc4, 29.bxc4 Qxc4, 30.Qxc4 Bxc4. The actual capture on c4 was first by the knight, then the queen; do not replace it with the anticipated bishop line. 31.Re1 saved the other rook. White was then down the exchange with equal pawn counts.

The ending included some explicit defender checks: Nd3 guarded b2; Ke2 avoided a future bishop pin; Re1 avoided ...b2 forking a rook on c1; Bd3/Be4 guarded Rb1; 40.g3 was safe for Nf3 because Ke2 could recapture ...Bxf3+; Kd2 avoided blocking the Be4-d3-c2-b1 diagonal. 45...hxg3 46.hxg3 restored protection of Nf4, and ...Bxf4+ 47.gxf4 completed an equal minor exchange.

These did not prevent the decisive late failures. 48.Ke3 defended d4 and 49.Bd3 met ...Ra3+, but ...Rbb3 added a second rook behind the attack on the pinned bishop. My earlier claim that the king could protect Bd3 was insufficient against the doubled rooks. I recognized that ...Rxd3+ would be protected by the other rook, then chose 50.Rxb2 while concentrating on that bishop-capture reply. I omitted the immediate 50...Rxb2, which simply won White's last rook for the pawn. The bishop was not captured. This is another failure to check the destination's ordinary recapture, and is worse than the anticipated bishop loss. Resigned with bishop versus two rooks and only one extra pawn.

After 119: 47W/2D/70L; nominal 1800 11W/0D/28L from 39. Elo 1580 [1460,1700], 95% Bayesian equal-tail interval, 79 rated total / latest 50 / 40 uncalibrated MAX exclusions; storage 29,574,673 bytes. Trial 15 so far: 1W/0D/4L, 221 own moves / 443 plies / 0 illegal attempts. No improvement established. Finish the already declared endpoint at 120 before revising the learning trial. No new cumulative token counter is available.

## Benchmark 120 — Black, nominal 1800; win (2026-10-02 15:31 UTC)

Result: 81...Rh8#, 162 plies / 81 own moves / 0 illegal attempts. Referee result seq 9840, sha256 baa3872b9fccb66258a949cda730deac2ff297078ec23e108b33de83629e93d3; snapshot 771991d9bd9aa59db1910de10f6b988b44fa355759f336ca2dd04cd63d952366.

Castled on move 5, developed all four minors by 10 and both rooks by 12. The first fifteen moves had no unanticipated material loss. ...Nxd4/exd4 and ...Nxc3/Rxc3 traded both knight pairs. 17...Rf8 escaped Bb5; ...Rxc3/Qxc3 traded a rook pair, and 20...Qc7 21.Qxc7 Bxc7 exchanged queens with a real bishop recapture. White gained activity with Ba3, Bd7, Re7, Bc6 and Be8. 24...Bc8 did not produce the offered bishop exchange: White declined with Bc6. 25...Bf4 saved the attacked bishop. I considered long speculative alternatives and avoided some back-rank mating lines, but this was still slow and passive play, not a demonstrated best defense. 27.Bxf7 won a pawn after ...Kf8.

27...Bd6 28.Bxd6 Rxd6 29.Re8+ Kxf7 30.Rxc8 removed both remaining bishop pairs. Before Kxf7 I explicitly corrected the apparent bishop gain: White's rook also attacked Bc8 and then captured it. The resulting rook ending had Black five pawns versus White six.

The active king and rook eventually obtained counterplay. Rc3 attacked b3; 47...Rxb3 recovered that pawn. Rb4 protected itself with a5 and attacked d4; 54...Rxd4+ and 55...Rxh4 won pawns before White's ...Rxg6+ reply could occur. Actual further captures were 56.Rxg6+ Kf7 57.Rxb6 Rxa4. Do not omit the b6 loss when counting the pawn advantage.

...d4+ and the a-pawn advance produced three separate passers against White's connected f/g pawns. 64...Rb2 deliberately released d4 to 65.Kxd4 while protecting a2. The h-pawn then advanced. After 69.Kf5 I detected the immediate Rh6 mating threat and played ...Kh4 instead of continuing the pawn script. 70...Rg2 used h3 as an actual defender, released a2, and stopped 71.g7 with ...Rxg7. White then took a2. ...Rg2, ...h2 and ...Rg1 supported promotion; ...Kg3 answered Rh7+ and protected h2. The exact conversion was 76...h1=Q 77.Rxh1 Rxh1, leaving rook versus f-pawn.

White's 79.Kg7 left f5 undefended; ...Kxf5 captured it. This opponent error is part of the win and is not proof that every rook-versus-pawn continuation was winning. The final mating line was calculated before execution: 80...Kf6 forced 81.Kf8, then ...Rh8#; the referee confirmed mate. No engine evaluation, legal-move menu, or delegated chess advice was used.

After 120: 48W/2D/70L. MAX 0W/2D/38L from 40; skill 0 36W/0D/4L from 40; nominal 1800 12W/0D/28L from 40. Elo 1590 [1470,1710], 95% Bayesian equal-tail interval, 80 rated total / latest 50 / 40 uncalibrated MAX exclusions; storage 29,966,880 bytes.

## Trial 15 endpoint — failed transfer (after benchmark 120)

Fixed six-game block 115–120: 2W/0D/4L, 302 own moves / 605 plies / 0 illegal attempts. MAX 0/2, skill 0 1/2, nominal 1800 1/2. The declared baseline was 1640 [1520,1760]; endpoint 1590 [1470,1710]. The wide overlapping intervals and the lower endpoint establish no sustained improvement.

Opening observations: 115, 119 and 120 had no unanticipated material loss through the first fifteen moves. 116 lost the queen after the d-file clearance error; 118 lost Bd6 because Bd7 blocked its supposed queen defender. 117 missed ...Rxc4, with a later knight capture compensating the bishop but leaving a pawn loss. Its win also depended on major later gifts. The two short opening rehearsals did not transfer reliably to the benchmark block.

Later failures remained decisive: 119 missed the queen/rook skewer, then the final ...Rxb2 recapture; 118 omitted f2xe3 when giving a queen check. Game 120 supplies a positive example of coordinated defense and conversion, with explicit king-safety catches and a verified mate, but cannot erase the other results. The opening intervention is not accepted as an effective learning method. Revise the next trial rather than extend this block or merely lengthen the cue sheet.

Goal tracker was read again at 2026-10-02 15:31:50 UTC. It still reports the obsolete two-100-game-MAX objective with status blocked and the unchanged historical counter 17,035,946 tokens / 178,558 seconds. I did not change that status or report these values as new usage. GOAL.md's clarified Elo objective remains unmet; no current cumulative token counter is available.


## Trial 16 declared — safe queen exchanges

Declared 2026-10-02 15:36:16 UTC after the failed trial-15 endpoint. Baseline 1590 [1470,1710], 48W/2D/70L. Change position choice toward concretely safe equal queen exchanges at comparable material, retaining the development-first opening fallback. Full plan and own-game contrasts are in trials/queen-exchanges-16.md. Exactly two fresh standard-start nominal-1800 practices, White then Black, at most 20 own moves each with the final reply; combined ceiling 16:21:16 UTC. No repeats or extensions. Fixed evaluation is benchmarks 121–126. Track actual exchanges, all piece-loss failures, complete W/D/L and Elo uncertainty; no improvement claim from practice or one win. Trial-09 timing remains discontinued. No new valid token counter.

## Practice 27 — fresh White opening; no queen-exchange exposure

Ended at 2026-10-02 15:48:18 UTC after exactly 20 own moves / 40 plies, zero illegal attempts, explicitly unfinished with no score. Result seq 810, sha256 a12d9ab4000d16c709d0b78fcef595b2be7774c95e62d44da0af0c40132f0cb2. PGN read back.

1.d4 d5 2.Nf3 c6 3.e3 e6 4.Be2 Be7 5.O-O Nf6 6.c4 O-O 7.Nc3 b6 8.Bd2 Nbd7 9.Rc1 dxc4 10.Bxc4 Nd5 11.Re1 Re8 12.e4 Nxc3 13.Bxc3 Bd6 14.e5 Bc7 15.b3 a5 16.Qd2 Ba6 17.Bxa6 Rxa6 18.Bb2 Nb8 19.Red1 Qd5 20.h3 Ra8.

Castled on 5, all minors developed by 8, both rooks by 11. Pawn, knight and bishop exchanges completed as anticipated; final material equal, Q/2R/B/N/7 pawns each. No unanticipated material loss in this stopped session. b3 protected Bc4 while Rc1 retained Bc3 protection; Bb2 later cleared the c-file while Nf3 still defended Qd2. ...Nb8 defended c6, so no Rxc6 raid was attempted.

Actual queen offers: zero; completed queen exchanges: zero. The d4 pawn continued to separate Qd2 and Qd5. No safe immediate offer was identified, and the session was not extended to manufacture one. This is clean short development but does not test the new exchange preference, demonstrate stronger full-game play, or alter Elo.

One declared fresh Black session remains, at most 20 own moves with the final reply; unchanged combined deadline 16:21:16 UTC. No repetitions or extra White session. Return to fixed benchmarks 121–126 after it.


## Practice 28 — fresh Black; queen exchange followed by knight loss

Ended at 2026-10-02 15:59:51 UTC after exactly 20 own moves / 41 plies including White's final reply, one illegal attempt, explicitly unfinished with no score. Result seq 855, sha256 3961bf9097f5cc3f492d6e41aa786d6fd313dfd878e653f26f9bcb49111404f5. PGN read back.

1.e4 e6 2.Nc3 d5 3.exd5 exd5 4.Nf3 Nf6 5.Qe2+ Qe7 6.a3 Qxe2+ 7.Bxe2 Bd6 8.Nb5 O-O 9.Nxd6 cxd6 10.h3 Nc6 11.g4 Be6 12.b4 Rfe8 13.d3 Rac8 14.Kd1 Ne5 15.Nd4 Bd7 16.g5 Nfg4 17.hxg4 Nxg4 18.Kd2 Nxf2 19.Re1 Nh3 20.a4 Nxg5 21.a5.

The queen offer 5...Qe7 blocked check with Bf8 available to recapture; 6.a3 declined immediate acceptance but left the exchange available. 6...Qxe2+ 7.Bxe2 completed an equal exchange with the actual White bishop recapture. One offer, one completed exchange, queens removed on White move 7, comparable material. Castled on 8, remaining minors developed by 11, both rooks by 13. Nxd6/cxd6 was an anticipated equal bishop-for-knight exchange but left doubled central pawns.

The later failure matters: 15...Bd7 blocked d7 before 16.g5 attacked Nf6. The proposed 16...Ng8 was illegal because Black's king already occupied g8; the referee rejected it once. Other nearby squares were occupied or capturable. 16...Nfg4 knowingly allowed 17.hxg4, and ...Nxg4 recovered only the pawn. This was a knight loss caused by the earlier retreat/development choices, not successful simplification. Subsequent ...Nxf2 and ...Nxg5 recovered two more pawns. Final Black 2R/B/N/7 pawns versus White 2R/2B/N/4 pawns; do not describe the material pattern as a proved favorable ending or erase the lost piece.

Both prescribed practices are now finished before the unchanged 16:21:16 deadline, with no repeat or extension. White had no queen-exchange exposure; Black implemented the exchange preference but still mishandled a minor piece. This does not establish improvement. Proceed to the predeclared fixed benchmarks 121–126 with the same conditional queen-exchange policy and development fallback. Practice remains excluded from Elo and W/D/L; baseline stays 1590 [1470,1710], 48W/2D/70L.


## Benchmark 121 — White versus MAX, loss

Finished 2026-10-02 16:18:10 UTC by practical resignation after 33...gxh4, 66 plies / 33 own moves, zero illegal attempts. Result seq 9908, sha256 d84e5877dac3a4f5c3de37b69b8a8653f965507d1d0d8fbf3c21ee4583ebbc60; snapshot aac54a90b8bdebaf3624afeff8514cf961e66d5904f96d27301399aa9af59a42. PGN read back.

1.d4 Nf6 2.Nf3 d5 3.e3 c5 4.Be2 cxd4 5.exd4 Nc6 6.O-O Bf5 7.c4 dxc4 8.Bxc4 e6 9.Nc3 Be7 10.Bf4 O-O 11.Re1 Qb6 12.Qb3 Nxd4 13.Qxb6 Nxf3+ 14.gxf3 axb6 15.Rad1 Rfc8 16.Bb3 Bh3 17.Bd6 Kf8 18.Bxe7+ Kxe7 19.Nd5+ Nxd5 20.Bxd5 Rc2 21.Bxb7 Rxa2 22.Rd4 Raxb2 23.Rh4 Bf5 24.Rf1 Bd3 25.Be4 Bxf1 26.Bxc2 Be2 27.Be4 h6 28.Kg2 b5 29.Kg3 f5 30.Bc6 Kd6 31.Be8 Kc5 32.Kf4 g5+ 33.Ke5 gxh4.

Castled on 6, all minors by 10, both rooks by 15. However the first 15 were not materially clean. 12.Qb3 offered a queen trade while overlooking ...Nxd4. The actual knight capture attacked Qb3 and Nf3; Nxd4/Qxd4 would also leave the pawn lost. 13.Qxb6 allowed the anticipated intervening 13...Nxf3+ before 14.gxf3 axb6. Thus one offer was answered by a tactical pawn capture, and one queen exchange completed on Black move 14 with a-pawn recapture. No net queen loss, but White was a pawn down with damaged pawns; this was not a safe equal-material implementation.

18.Bxe7+/Kxe7 and 19.Nd5+/Nxd5/20.Bxd5 used the genuine e6 pin to Re1 and exchanged equal minor pieces. Black's second-rank invasion then won a2 and b2 while Bxb7 recovered one pawn, leaving White two pawns down. Rh4 chased Bh3 to f5, which made Rf1 legal without immediate bishop capture on that diagonal. 25.Be4/Bxf1/26.Bxc2 exchanged equal rooks. The opponent chose 26...Be2, not the projected ...Rxc2/Kxf1; 27.Be4 therefore saved the still-present bishop and defended f3. Retain this actual continuation, with R+B remaining on both sides.

The decisive later failure was 32.Kf4 g5+: the two-square pawn push forked Kf4 and Rh4. 33.Ke5 answered check and the actual 33...gxh4 took the rook. Final White Ke5/Be8/f2,f3,h2 versus Black Kc5/Rb2/Be2/b5,e6,f5,h6,h4. This was a practical resignation after a real rook loss, not checkmate. Earlier correct local exchanges did not prevent a basic pawn fork in the queenless ending. Sustained improvement remains unshown.

Trial 16 so far: 0W/0D/1L. Overall 48W/2D/71L; MAX 0W/2D/39L (41), skill 0 36W/0D/4L (40), nominal 1800 12W/0D/28L (40). Elo unchanged at 1590 [1470,1710] because MAX is excluded; 80 rated games total, latest 50, 41 MAX exclusions. Storage 30,908,306 bytes. Continue the unchanged declared 121–126 block; next 122 Black MAX, no additional drill or policy change before its endpoint.


## Benchmark 122 — Black versus MAX, checkmate loss

Finished 2026-10-02 16:33:33 UTC with 27.Qf7#, 53 plies / 26 own moves, zero illegal attempts. Result seq 9963, sha256 f1e6c64b0cd18681845f2f63d76f65f9f190f5b002128ad50bfd33451cc62fc7; snapshot f8a1370212857409fd31c2f71412bb49ea7faa8b9bc46a4821a41a2b2485d1a8. PGN read back.

1.e4 e6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Nf3 Ngf6 6.Nxf6+ Nxf6 7.Be3 Be7 8.Bd3 O-O 9.Qe2 b6 10.O-O-O Bb7 11.Kb1 c5 12.dxc5 Nd5 13.c4 Nxe3 14.Bxh7+ Kxh7 15.Rxd8 Raxd8 16.Qxe3 bxc5 17.Qe2 Rd6 18.Rd1 Kg8 19.Rxd6 Bxd6 20.Ng5 Bc8 21.Qh5 Rd8 22.Qxf7+ Kh8 23.Qh5+ Kg8 24.Qh7+ Kf8 25.Qh8+ Ke7 26.Qxg7+ Ke8 27.Qf7#.

Castled on 8 and developed remaining minors by 10, but the first 15 again contained a queen loss. After 12.dxc5 I explicitly recognized the Bd3/Rd1 line toward Qd8. 12...Nd5 blocked it temporarily; 13.c4 attacked the knight. 13...Nxe3 removed the blocker while assuming the knight would be recaptured first. White instead inserted 14.Bxh7+ before Qxe3, then 15.Rxd8 won the queen. 14...Kxh7 and 15...Raxd8 captured the checking bishop and rook, but 16.Qxe3 removed the remaining knight. After 16...bxc5 the actual balance was Black 2R/2B/5 pawns versus White Q/R/N/6 pawns. Recognition of the line did not prevent the move-order failure.

Queen offers: zero; equal queen exchanges: zero. This was a queen lost in an unequal transaction, not implementation of the trial preference. 19.Rxd6/Bxd6 traded a rook pair, leaving R/2B versus Q/N. 20...Bc8 reinforced e6 and 21...Rd8 defended Bd6 while clearing f8. The escape square was actually used at 24...Kf8, but the queen checks drove the king through e7 to e8. White captured f7 and g7, then the referee confirmed 27.Qf7#; do not substitute the earlier imagined Ng5-f7 fork line for the actual mate.

Trial 16 so far: 0W/0D/2L, 59 own moves / 119 plies, zero benchmark illegal attempts. Overall 48W/2D/72L; MAX 0W/2D/40L (42), skill 0 36W/0D/4L (40), nominal 1800 12W/0D/28L (40). Elo remains 1590 [1470,1710], 80 rated total/latest 50, 42 MAX exclusions. Storage 31,222,136 bytes. These two losses are retained as adverse evidence; continue the same declared block through 126, next 123 White skill 0. No additional practice or changed stopping point.


## Benchmark 123 — White versus skill 0, repetition draw

Finished 2026-10-02 18:00:30 UTC after 93 own moves / 185 plies, zero illegal attempts. The referee automatically recorded threefold repetition after 93.Kh6. Result seq 10150, sha256 b1614c4473122378e7a0d1cc50532bbed52760378adf1fde13d00ddbd9db21b2; snapshot fa8e0d121c7d89a98b71931ac4b07ec2d8b02f3692d48daf169d2f6721bdca6d. Complete PGN read back.

Castled on 5, all minors by 9, both rooks by 15; nevertheless the first 15 were not materially clean. 9.Bd2 cxd4 attacked Nc3 while vacating c5 and exposing Bc4 to Qc7. Bd2 also obstructed the d-file recapture. 10.Bxe6 dxc3 11.Bxc8 cxd2 12.Bf5 Nc6 13.Qxd2 left White down a minor for a pawn: both Nc3 and Bd2 were lost, while Black lost Bc8. The attempted damage limitation did not repair the opening oversight.

24.Qe3 offered an exchange with f2 available to recapture; Black counteroffered 24...Qd3. 25.Qxd3 Rxd3 completed an equal queen-for-queen exchange with the actual rook recapture. One own offer, one opponent counteroffer, one completed exchange on Black move 25, no net queen loss. White was already down a minor for a pawn, so this was not implementation at comparable material. 26.Ra1 attacked the restricted Na2; 27.Kf1 provided king mobility before 28.Rxa2 recovered that knight after Black chose ...f5. This recovery depended on the opponent allowing it.

31.Rd2 Rxd2+ 32.Kxd2 traded the remaining rooks, but 32...Bxa3 captured the pawn that had lost rook protection. The resulting equal-material minor-piece ending was then mishandled: 36.g4 fxg4 37.Bxg4 Ne5+ forked Kd3 and Bg4; 38.Ke4 Nxg4 actually lost the bishop. Retain both this loss and the separate opening piece-loss episode despite the eventual draw.

Later 54.Kxh5 and 55.Nxg3 removed Black's kingside pawns. f5 supported e6, and Nc2 guarded a1 against the passed a-pawn. Earlier repetition attempts were broken by ...g4 and ...Be5; they were not draws. Black eventually played 82...a1=R 83.Nxa1 Bxa1, exchanging its passed pawn for White's last knight. White then had only king and four pawns against king, bishop, knight and b-pawn. The h7 pawn kept a promotion threat while the bishop covered h8. King shuffling preserved the formation, and the actual final sequence was 88.Kg6 Nc7 89.Kh6 Nd5 90.Kg6 Kf8 91.Kh6 Ke7 92.Kg6 Nc7 93.Kh6, when the referee claimed repetition. This is a practical save against skill 0, not a proved fortress or evidence that the preceding errors were sound.

Trial 16 through 123: 0W/1D/2L, 152 own moves / 304 plies, zero benchmark illegal attempts. Overall 48W/3D/72L in 123 games; MAX 0W/2D/40L (42), skill 0 36W/1D/4L (41), nominal 1800 12W/0D/28L (40). Elo remains 1590 [1470,1710], 81 rated games total/latest 50, 42 MAX exclusions; storage 31,652,318 bytes. The draw does not establish improvement. Continue the unchanged 121–126 block with 124 Black skill 0, then the two nominal-1800 games. No extra practice or endpoint change.


## Benchmark 124 — Black versus skill 0, checkmate win

Finished 2026-10-02 18:14:07 UTC with 30...Qf2#, 30 own moves / 60 plies, one illegal attempt. Result seq 10213, sha256 61145e8099f5e57bba9b0cdae20551f4169f1f03cc5c740006c5103d0c93da29; snapshot ee57e87a2736ad3ceecc0aa58cc44a8ac34e50f60aae2cdfa71929cb4226dff0. Complete PGN read back.

1.Nf3 d5 2.d4 Nf6 3.c3 Bf5 4.Bf4 e6 5.Nh4 Bg6 6.Qb3 Qc8 7.Nd2 Bd6 8.Qa4+ Nbd7 9.Nxg6 hxg6 10.g3 O-O 11.e3 Bxf4 12.exf4 c5 13.h4 Qc6 14.Qb3 Rac8 15.Bd3 Rfe8 16.Nf3 c4 17.Ne5 Nxe5 18.Bb1 cxb3 19.Ke2 Nc4 20.a3 Ne4 21.Bxe4 dxe4 22.h5 gxh5 23.Rh3 Qd5 24.Rah1 Qf5 25.a4 Qg4+ 26.Kf1 Nd2+ 27.Kg2 e3 28.fxe3 Qf3+ 29.Kg1 Qf1+ 30.Kh2 Qf2#.

Castled on 10, all minors developed by 8, both rooks by 15. First 15 materially clean. Qc8 defended b7; Nxg6/hxg6 and Bxf4/exf4 completed equal minor exchanges. The c-pawn moved only after exchanging Bd6, which had relied on c7 for protection.

13...Qc6 offered an equal queen exchange with b7 available to recapture, at comparable material. White declined with 14.Qb3. One offer, zero completed queen exchanges, no own queen loss. 16...c4 attacked Qb3 and Bd3 together. White's 17.Ne5 attacked Qc6, but 17...Nxe5 removed that knight while retaining the pawn attack. White then chose 18.Bb1 and left its queen to 18...cxb3. Retain this major opponent error when attributing the win.

19...Nc4 moved the attacked knight to a d5-supported square; 20...Ne4 21.Bxe4 dxe4 exchanged another equal minor pair. No unanticipated own piece loss occurred. The proposed 25...Qf3 was nevertheless illegal because White's f4 pawn blocked the queen's route from f5; the referee rejected it once. 25...Qg4+ was the legal correction. After ...Nd2+, 27...e3 28.fxe3 cleared f2. The actual supported queen checks ...Qf3+, ...Qf1+, ...Qf2# completed the conversion; Nd2 protected f3 and f1.

Trial 16 through 124: 1W/1D/2L, 182 own moves / 364 plies, one benchmark illegal attempt. Overall 49W/3D/72L; MAX 0W/2D/40L (42), skill 0 37W/1D/4L (42), nominal 1800 12W/0D/28L (40). Elo 1600 [1480,1720], 82 rated total/latest 50, 42 MAX exclusions; storage 31,950,181 bytes. The 10-point increase from baseline has broad overlapping uncertainty and follows an opponent queen blunder; it is not sustained improvement. Complete the unchanged endpoint with 125 White and 126 Black against nominal 1800.


## Benchmark 125 — White versus nominal 1800, loss after two late piece failures

Finished 2026-10-02 19:18:56 UTC by resignation after the actual 87...Rxf7, 87 own moves / 174 plies, zero illegal attempts. Result seq 10389, sha256 c2959f8d0c3ca71b035ce8d5c08e5e1ed8b117efe147f20c630a7abd955b5b22; snapshot 43dbdf292b46d7027bbaa7e9bdb2a1fcee99b0aeb535ed3afabba22975e10f61. Complete PGN read back. Final White bare Ke6 versus Black Kg8/Rf7/g6,h5; Kxf7 was unavailable because Kg8 protected f7. This was resignation, not checkmate or a repetition draw.

Castled on 5, all minors by 8, both rooks by 10. Early exchanges were anticipated and no minor or queen was lost in the first 15. 15.f4 exf3 en passant 16.Nxf3 completed the planned pawn transaction and moved the threatened knight. However 17.c5/18.Qb3 allowed 18...Nxc5 with tempo against the queen. I had overstated the security of c5: Black's Qc7 and Be7 also supported the knight capture, and the imagined easy recapture chain omitted the final queen capture. Qc3 saved the queen but did not recover the pawn.

22.Bxf6 Ne4 inserted a knight attack on Qc3 before 23.Qe5 Nxf6 completed the equal bishop exchange. 24.Rc7 Qb8 25.Rc6 uncovered the b8-e5 queen line, with Nf3 able to recapture on e5. Black declined immediate capture with ...h6, but 26.Qxb8 Rxb8 completed the available equal queen-for-queen exchange, with the actual a8-rook recapture. One direct offer and one completed exchange on Black move 26; no queen loss. White was already one pawn down, so queen removal did not itself restore material parity.

31.Bxg4 fxg4+ traded equal minor pieces and opened the f-file with the anticipated check. 34.Nxg4 recovered that pawn; 35.Rxe6 captured the pawn left without bishop protection. 36.Re5 Rxe5 37.Nxe5 completed an equal rook trade, but 37...Bxa2 restored pawn equality. 38.Nc6 Bb3 attacked Rd1 in reply to the knight attack on Rb8; 39.Rd6 saved the rook. 44.Nxb5 and 47.Nxa4 captured both remaining queenside pawns, leaving White two pawns ahead. After 50.Kd4 Re4+ 51.Kc5 Rxe3, the central pawn was lost and only a one-pawn advantage remained.

The decisive minor-piece error was 56.Kd6. After 54.Nc4 Rc3 55.Rd4 Bf1, Nc4 had two attackers and depended on both rook and king for the final exchange. Moving Kc5 to d6 removed that final c4 recapture. Black actually played 56...Bxc4. Rxc4/Rxc4 would leave the last black rook out of the king's reach, so the knight was lost. The move was incorrectly praised as removing a pin while its essential defensive role was missed.

The b-pawn still supplied practical counterplay. It reached b7 with king and rook support. 63...Bc6 pinned it to Ka8, so immediate promotion was not legal; no illegal promotion was submitted. Ra6/Kb8/Ka7 cleared that pin and prepared promotion. The actual 66...Bxb7 67.Kxb7 exchanged Black's bishop for the passed pawn. This recovered material balance in a rook ending with two pawns each; it was not a promotion or a proved winning conversion. Black subsequently captured g2 on 68 and h4 on 77, leaving White a bare rook.

The final failure was the supported-rook assessment around 82.Rf7+ Kg8 83.Kf6 Ra6+ 84.Ke7 Ra7+. After the king left e7, the black rook could take Rf7, and Kg8 prevented the supposed king recapture. Black first repeated checks with 85...Ra6+ 86.Ke7 Ra7+ but then actually captured 87...Rxf7. No draw was recorded and no earlier hypothetical capture replaces the actual finish. Both the c4 defender error and the f7 recapture error remain adverse evidence against the queenless-play hypothesis.

Trial 16 through 125: 1W/1D/3L, 269 own moves / 538 plies, one benchmark illegal attempt (from 124). Overall 49W/3D/73L; MAX 0W/2D/40L (42), skill 0 37W/1D/4L (42), nominal 1800 12W/0D/29L (41). Elo returns to 1590 [1470,1710], 83 rated total/latest 50, 42 MAX exclusions; storage 32,367,456 bytes. Sustained improvement is unshown. Complete the unchanged endpoint with 126 Black nominal 1800 before the full assessment and next learning revision.


## Benchmark 126 — Black versus nominal 1800, rook confinement and missed knight support

Finished 2026-10-02 19:45:38 UTC by practical resignation after 30.Rf8, 29 own moves / 59 plies, zero illegal attempts. Result seq 10450, sha256 6ead8756c4dfefd5f62d6cab631fbe5fc066768acb23ebf0f6d9811b43bc7237; snapshot db5a0ae0f14e8f32aab41abad0f4e66b23f4280617635d734ab9f601f1ea39a6. PGN read back. Final Black Kc6/Bf5/Nf7/b5,c7,d5,e6,h7 versus White Kf1/Rf8/Bf6/Be2/b4,e3,f3,g2,h2: a full rook deficit at equal pawn count. Black had legal continuations; this is resignation, not checkmate or a proved forced loss.

Castled on 6, all minors developed by 7, and the first 15 remained materially clean. ...axb4/axb4 and ...Rxa1/Qxa1 completed equal pawn and rook exchanges. 12...Qa8 offered a supported equal queen exchange; White declined immediate capture with 13.O-O, but 13...Qxa1 14.Rxa1 completed it with the actual f1-rook recapture. One direct offer, one completed queen exchange on White move 14, comparable material, no queen loss. ...Rb8 defended b7 against Ra7. 17...Nxe5 18.dxe5 completed an equal knight trade.

...Bd8 defended c7 before ...b6. White advanced c6 instead of exchanging on b6; ...b5 stopped b4-b5, but it also occupied the rook's downward escape route. 21...Rb6 attacked the then-undefended c6 pawn while retaining b5's protection. 22.f3 restricted Ne4 severely; ...Ng5 was followed by 23.Na5 rather than the h-pawn chase I feared. ...f6 then cleared f7 as a retreat square. These are actual moves, not a claim that the knight placement was sound.

24.Ra8 attacked Bd8, and ...Ke7 supplied king support. 25.exf6+ gxf6 preserved that support. But 26.Bd4 attacked Rb6, whose routes were confined by b5/c6 and White's rook and minor pieces. I chose 26...Rxc6 expecting to limit the cost to an exchange. 27.Nxc6+ forked king and bishop, and after ...Kd7 White played 28.Rxd8+: Nc6 protected d8, so the intended king defense was unusable. 28...Kxc6 recovered the knight while leaving White's rook, and 29.Bxf6 removed the extra pawn. ...Nf7 attacked Rd8; White moved to f8. The actual loss was a full rook, not the initially described exchange concession. No best alternative or earliest forced-loss move is certified.

This repeats the failed king-recapture/defender assessment while also exposing a rook-mobility problem. Equal queen removal and a clean opening did not prevent it.

## Trial-16 endpoint — discontinue the queen-exchange preference

Fixed games 121–126 finished 1W/1D/4L: MAX 0W/0D/2L, skill 0 1W/1D/0L, nominal 1800 0W/0D/2L. Total 298 own moves / 597 plies, one illegal benchmark submission (124's blocked queen path). No results or endpoint were changed.

Five own direct queen offers were recorded; four games completed equal queen-for-queen exchanges (121, 123, 125, 126). Only 126 completed its exchange at equal material; the other three were already behind, including 121's tactical pawn loss during the offer. Game 124's offer at comparable material was declined, and queens remained. Game 122 instead lost a queen in an unequal transaction. These counts describe implementation, not strength.

All four queenless games retained serious errors: 121 lost a rook to a pawn fork; 123 lost minors in two separate episodes and later salvaged a repetition against skill 0; 125 lost a knight after removing an essential defender and later a rook with an illegal imagined king recapture; 126 lost a rook through confinement and missed knight protection. The only win, 124, kept queens and depended on a large opponent queen error. This block does not support the hypothesis that the simplification preference improves play.

Elo moved from 1590 [1470,1710] to 1580 [1460,1700], with broadly overlapping 95% credible intervals. Overall 49W/3D/74L in 126 completed games; MAX 0W/2D/40L, skill 0 37W/1D/4L, nominal 1800 12W/0D/30L, 42 games in each category. Fixed estimator: 84 rated total/latest 50, 42 uncalibrated MAX exclusions; storage 32,684,435 bytes. The provisional scale is engine-relative, not human Elo. No valid new cumulative token counter is available.

Decision: end trial 16 at its declared endpoint. Retain ordinary sound exchanges and the development fallback, but remove the special queen-exchange preference. The next trial will revisit material preservation through sparse, equal-material rook-and-minor opponent practice rather than another remembered-position checklist. This is a change in practice format, not a newly discovered principle or a claim of learning. Its plan and next benchmark endpoint are recorded separately before practice.


# Trial 17 — rook activity in sparse positions

Declared after game 126 at 2026-10-02 19:48:02 UTC. Baseline 1580 [1460,1700], 49W/3D/74L; 84 rated total/latest 50, 42 MAX exclusions. Fixed next evaluation: benchmarks 127–132 in the unchanged paired-color rotation.

Trial 16 failed. Equal queen removal did not prevent rook confinement, forks, or unusable king recaptures. Earlier reconstruction and defender exercises (including trials 02, 03 and 14) also failed transfer. This revisits that old weakness using longer opponent continuations from sparse equal-material positions; it is not a novel checklist or an independent blind tactical test.

Learning task: activate a rook without losing its retreat routes or relying on a defender that becomes unusable after an exchange. Use the lower piece count to practise following the actual reply through its final capture. Rook activity remains useful; mere passivity and preserved material in a short drill do not prove a sound ending.

Exactly two recorded nominal-1800 practice sessions, in this order:
1. White, self-composed FEN: r5k1/pp3ppp/2b5/3n4/3N4/2B5/PP3PPP/R5K1 w - - 0 1
2. Black, distinct self-composed FEN: 2r3k1/pp4pp/2n1p3/5b2/5B2/2N1P3/PP4PP/2R3K1 b - - 0 1

Both have R+B+N+5 pawns per side. They are deliberately composed training positions with known starting geometry, not certified equal evaluations or unseen test items. Subsequent opponent moves are fresh. No engine advice or historical continuations are supplied.

Each ends naturally or explicitly unfinished after 20 own moves and the final opponent reply. Combined setup/play/review ceiling: 2026-10-02 20:33:02 UTC (45 minutes). At the ceiling finish any pending reply and end an active session. No repeats, replacement positions, or extensions after favorable or unfavorable results. Preserve all practice records separately from Elo.

Record actual exchanges, rook confinement or unsupported rook moves, any omitted check or capture, illegal attempts, final material and whether a game actually finished. A retained rook alone is not success if another piece or the game is lost. Short practice outcomes are not full-game results.

For full-game transfer, remove trial 16's special queen-exchange preference. Keep normal development and choose exchanges on their concrete merits. Before committing a rook to an advanced square, account for its usable retreat route after the opponent's immediate attack; at a capture sequence, use the actual resulting board and legally available final recapture. These are modest execution cues prompted by the practice, not a guarantee or a larger mandatory audit.

Return to fixed benchmarks 127–132 after the two sessions regardless of outcome. At 132 assess full W/D/L, Elo and uncertainty, all material errors, and specifically recurrence of rook confinement or invalid final recaptures. A recurrence rejects reliable execution; even a clean block or higher estimate requires repeated evaluations before sustained improvement is claimed. Revise again on failure.

Only own reasoning, pre-existing notes and the referee during games. No engine analysis, external move advice, automated chess search/scoring/attack analysis or move menus, and no delegation. No decision-time target, model change, estimator change or invented usage count.


## Practice 29 — White sparse position, unfinished at 20 moves

Ended 2026-10-02 19:53:55 UTC after 20 own moves / 40 plies, zero illegal submissions, explicitly unfinished and excluded from Elo. Result seq 898, sha256 ec324e92f0ceb6b50141034832a92a06dc1319093cc54de4d87073ae5e2fbd33. PGN read back.

1.Nxc6 bxc6 2.Rd1 a5 3.Bd4 Rc8 4.Kf1 Ra8 5.Ke2 a4 6.Rc1 a3 7.b3 Nb4 8.Ra1 h5 9.Bc5 Re8+ 10.Kd2 Re4 11.Bxb4 Rxb4 12.Kc3 Rb5 13.Rd1 Kf8 14.Rd7 g5 15.Ra7 Rf5 16.f3 Rc5+ 17.Kd3 Rc1 18.Rxa3 Rg1 19.g3 Rh1 20.h4 gxh4.

The initial knight-for-bishop exchange and later Bxb4/Rxb4 were counted correctly; both sides reached R+5P. Rc1 attacked c6, but ...Nb4 newly defended c6 and attacked a2, so Ra1 withdrew without trying the now-unsound pawn capture. Bc5 left the possible ...Nc2 fork of bishop and rook. After the equal minor exchange, Kc3 protected b3, allowing Rd1/Rd7/Ra7. The rook's d4 retreat was available while the king remained c3; no later position was assumed to retain that king defense automatically.

f3 answered ...Rf5 before Rxa3 captured the blocked pawn. ...Rg1/...Rh1 then attacked the kingside. g3 had h2 support until h4; the actual ...gxh4 removed White's h-pawn at the cap. The possible gxh4/Rxh4 continuation was anticipated but was not played and is not recorded as a completed exchange. Final actual material is R+4P each: White Kd3/Ra3/a2,b3,f3,g3; Black Kf8/Rh1/c6,f7,h5,h4. The g3 pawn remains attacked by h4 and the continuation is unresolved.

No rook or unanticipated minor loss occurred in this short session. The extra pawn was not retained, and rook activity did not establish a favorable ending. This is limited practice evidence only, with no full-game score, independent evaluation or Elo effect. No extension was made. Continue only the predeclared Black session, same 20-own-move cap and combined 20:33:02 deadline.


## Practice 30 — Black sparse position, rook exchange followed by pawn loss

Ended 2026-10-02 20:01:18 UTC after 20 own moves / 40 plies, zero illegal submissions, explicitly unfinished and excluded from Elo. Result seq 941, sha256 9f34b76bb18cbfc734b64c3a9be128102bde2ed9743a76a3f43b0c4cfbe67f73. PGN read back.

1...Rd8 2.h3 e5 3.Bg3 Rd3 4.Rd1 Rxe3 5.Be1 Kf7 6.Nb5 a6 7.Kf2 Rd3 8.Nd6+ Ke6 9.Rxd3 Bxd3 10.Nxb7 e4 11.Bc3 g6 12.Nc5+ Kd5 13.Nxd3 exd3 14.Kf3 Kc4 15.Bd2 Nd4+ 16.Ke4 Ne2 17.Ke3 Ng3 18.b3+ Kd5 19.Kxd3 Ne4 20.Bb4 h5 21.Be7.

The rook developed on d8 and entered d3 with Bf5 support. Rxe3 captured a pawn. When Kf2 attacked Re3, ...Rd3 used the planned bishop-supported retreat rather than capturing the attacked Nb5 while leaving the rook to Kxe3. Nd6+ was answered by ...Ke6, making f5 an actual king-recapture square. White instead played Rxd3, and ...Bxd3 completed the anticipated equal rook exchange. Nc6's d8 coverage was retained in the earlier rook-check considerations; no rook loss occurred.

10.Nxb7 recovered the extra pawn, returning material equality. ...e4 supported Bd3, which continued to defend a6. Nc5+/...Kd5/Nxd3/...exd3 completed an equal minor exchange. The resulting d3 passer depended on king support; ...Kc4 provided it. ...Nd4+ and ...Ne2 used real king and pawn support respectively.

The later plan failed to retain that pawn. After ...Ng3, 18.b3+ drove the king from c4 while Bd2 controlled c3 and b4 and Pa2 protected b3. ...Kd5 left d3 undefended, and 19.Kxd3 actually captured it. Recognizing that consequence after the check did not prevent the preceding defensive failure. No best earlier alternative or inevitable-pawn-loss claim has been established. ...Ne4 and ...h5 retained the remaining material through the cap.

Final Black Kd5/Ne4/a6,g6,h5 versus White Kd3/Be7/a2,b3,g2,h3: knight and three pawns against bishop and four pawns. This is an unfinished inferior-material ending, not a completed draw or successful defense. No unanticipated own rook/minor loss was identified, but the pawn failure remains adverse evidence.

## Trial-17 practice endpoint

Both predeclared sessions finished by 20:01:18 UTC, before the 20:33:02 ceiling, with no repeats or extensions: 40 own moves / 80 plies, zero illegal attempts, two explicitly unfinished drills. The White session ended at equal material with an unresolved pawn transaction; the Black session ended a pawn down after the king was driven off a defensive duty. Rook activation, retreat and equal exchange were handled locally, but this does not establish stronger full-game play or reliable overall defense.

Return now to the fixed benchmarks 127–132 exactly as declared, using the modest rook-mobility cue and ordinary concrete exchange choices. No additional practice, special queen-exchange preference, timing target, opponent change or rating change. Baseline remains 1580 [1460,1700], 49W/3D/74L through 126. Preserve all later errors and assess the full block at 132; no valid new cumulative token counter is available.


## Benchmark 127 — White versus MAX, bishop skewer and incomplete transaction

Finished 2026-10-02 20:10:14 UTC by practical resignation after 21...Bxa5, 21 own moves / 42 plies, zero illegal attempts. Result seq 10494, sha256 1ae4eb78aee93f2bed781e429a38d0d9f6493722ac5ab5a14b849275984c09e4; snapshot 41f4a9258efe81e9b6a1c740ccf15ff3977b474e690d552072237079c103e36d. PGN read back.

1.d4 Nf6 2.Nf3 d5 3.e3 c5 4.Be2 cxd4 5.exd4 Nc6 6.O-O Bf5 7.c4 dxc4 8.Bxc4 e6 9.Nc3 Be7 10.Bf4 O-O 11.Re1 Qb6 12.Qd2 Rfd8 13.Rad1 Bg4 14.Be3 Bxf3 15.gxf3 Qa5 16.d5 exd5 17.Nxd5 Bb4 18.Nxf6+ gxf6 19.Qd5 Rxd5 20.Rxd5 Bxe1 21.Rxa5 Bxa5.

Castled on 6, all minors by 10, both rooks by 13; first 15 materially clean. The opening repeated the familiar game-121 position through ...Qb6. Qd2 retained d4 defense while defending b2; Rad1 supplied a later d-file recapture, and Be3 added a real defender before ...Bxf3/gxf3 removed Nf3. These local corrections avoided the earlier ...Nxd4 pawn loss but left damaged king pawns.

The central break d5/exd5/Nxd5 was calculated incompletely. 17...Bb4 attacked Qd2 with Re1 behind it on b4-c3-d2-e1. 18.Nxf6+ gxf6 exchanged knights but also removed the d-file blocker. I then chose 19.Qd5 while overvaluing a nominal rook/queen recapture sequence. The actual ...Rxd5/Rxd5/...Bxe1 inserted the bishop capture of the other rook. 21.Rxa5 recovered the queen, but Black recaptured with 21...Bxa5 from e1 through d2/c3/b4, not the ...Nxa5 anticipated in the move note.

The complete actual transaction removed White's queen and both rooks for Black's queen and one rook: a full rook loss. The final position was White Kg1/Bc4/Be3/a2,b2,f2,f3,h2 versus Black Kg8/Ra8/Ba5/Nc6/a7,b7,f7,f6,h7. Legal play remained; this was practical resignation, not checkmate or a proof that every earlier defense lost. No best alternative is certified.

This is a recurrence of missing a forcing reply elsewhere while calculating a nominally supported capture. Sparse-practice rook handling has not supplied reliable full-position defense. The first benchmark already rejects a claim of reliable execution; preserve the rest of the declared block.

After 127: 49W/3D/75L overall; MAX 0W/2D/41L in 43 games, skill 0 37W/1D/4L in 42, nominal 1800 12W/0D/30L in 42. Elo unchanged at 1580 [1460,1700], 84 rated total/latest 50, 43 MAX exclusions; storage 33,673,572 bytes. Trial 17 is 0W/0D/1L. Continue unchanged through 132, next 128 Black MAX, with no extra practice or changed endpoint.


## Benchmark 128 — Black versus MAX, missed smothered mate

Finished 2026-10-02 20:15:30 UTC with referee-confirmed 19.Nf7#, 18 own moves / 37 plies, zero illegal attempts. Result seq 10533, sha256 96875cf502a12f201354391496436b883f36a81c355e81bbd3316e765d1f45ea; snapshot b5ad15af66642c4a82e7667a95a7bbf6a25f97246e1f3a06a13141699e6ad2b3. PGN read back.

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.a4 Bb7 10.d4 Re8 11.Nbd2 Bf8 12.Ng5 d5 13.axb5 axb5 14.exd5 Nxd5 15.Rxa8 Bxa8 16.Qh5 Nf6 17.Qxf7+ Kh8 18.Qg8+ Nxg8 19.Nf7#.

Castled on 7, all minors by 9, remaining rook activated on 10. Pawn exchanges through 14 preserved material. On 15.Rxa8 I changed the earlier proposed queen recapture to ...Bxa8 because Qd8 needed to keep defending Nd5; that equal rook exchange was correctly completed. This local defender check did not prevent the following mate.

16.Qh5 threatened h7. ...Nf6 attacked the queen and defended h7, but vacated d5 and reopened Bb3's diagonal. White captured f7 with check. After ...Kh8, I considered Qg8+ in advance but incorrectly treated ...Nxg8 as a favorable queen capture, overlooking 19.Nf7#. The king on h8, knight on g8 and pawns on g7/h7 formed the smothered-mate position. Bb3 protected g8, so Kxg8 was unavailable. The actual final sequence was played and confirmed, rather than replaced by resignation or a material-based success claim.

No rook was dropped, but there was a pawn loss and an immediate mating-pattern failure. This refutes adequate overall defense despite the isolated correct rook recapture. No best earlier alternative is certified.

Trial 17 through 128: 0W/0D/2L, 39 own moves / 79 plies, zero illegal submissions. Overall 49W/3D/76L; MAX 0W/2D/42L in 44, skill 0 37W/1D/4L in 42, nominal 1800 12W/0D/30L in 42. Elo unchanged at 1580 [1460,1700], 84 rated total/latest 50, 44 MAX exclusions; storage 33,980,540 bytes. Continue fixed games 129–132 without additional practice or an endpoint change.


## Benchmark 129 — White versus skill 0, mate with a retained recapture error

Finished 2026-10-02 20:21:15 UTC with 21.Qh7#, 21 own moves / 41 plies, zero illegal submissions. Result seq 10576, sha256 6e44c1f067edea34230a1a99612ba41515229e89478ba90d6dcfe506b9039ef6; snapshot e3c398e1428d481b625580ec5d412c8d45e5a6fbcfc09739e2c99ba40905aa40. PGN read back.

1.d4 e6 2.Nf3 Nf6 3.e3 d5 4.Be2 c6 5.O-O Bd6 6.c4 Qe7 7.Nc3 Nbd7 8.b3 O-O 9.Bb2 b6 10.Rc1 Re8 11.Re1 h6 12.Bd3 Bb7 13.e4 dxe4 14.Nxe4 c5 15.Nxd6 Bxf3 16.Qxf3 Rad8 17.Nxe8 Nd5 18.cxd5 Qf8 19.Nf6+ gxf6 20.Qe4 c4 21.Qh7#.

Castled on 5, all minors by 9, both rooks by 11. Bd3 cleared Re1's line before e4; Nxe4 recaptured with bishop and rook support. Nxd6 was intended as a knight-for-bishop exchange. Black inserted Bxf3, attacking Qd1, and Qxf3 answered that actual move. Black then declined Qxd6 with ...Rad8, allowing Nxe8; ...Nd5 declined another recapture and placed the other knight under cxd5. ...Qf8 again left Ne8. These are major opponent errors, not forced gains established by the opening.

19.Nf6+ retained a flaw in my analysis. I considered both recaptures but failed to retain Nd7 after the actual ...gxf6: the intended Qxf6 would lose the queen to Nxf6. I recognized that only after the knight had been captured and did not submit the queen capture. Thus the knight was conceded without the intended pawn recovery; this is a failed recapture plan, not a clean material-conversion claim.

20.Qe4 instead created the bishop-supported h7 threat while Re1 supported the queen. Black played ...c4 against Bd3, allowing the actual Qh7 mate before the bishop could be captured. Bd3 protected h7 along e4/f5/g6 after the queen left e4; the black queen occupied f8 and f7 was also occupied. The referee confirmed mate. No own rook was lost, but the earlier knight/recapture failure remains in the assessment.

After 129: 50W/3D/76L overall; skill 0 38W/1D/4L in 43, MAX 0W/2D/42L in 44, nominal 1800 12W/0D/30L in 42. Elo 1590 [1470,1710], 85 rated total/latest 50, 44 MAX exclusions; storage 34,294,662 bytes. Trial 17 is 1W/0D/2L, 60 own moves / 120 plies, zero illegal submissions. The ten-point rise from baseline is not sustained improvement. Continue unchanged with 130 Black skill 0, then both nominal-1800 games through 132.


## Benchmark 130 — Black versus skill 0, back-rank mate after a planned exchange

Finished 2026-10-02 20:32:54 UTC with referee-confirmed 32.Rxe8#, 31 own moves / 63 plies, zero illegal attempts. Result seq 10641, sha256 5a0ec13b0007542ea7a284dd2cc9f552184e3e16790ab6ef305d4f9a56f5d0ab; snapshot af77a78e4b9ecdc8918d0f3d689913204837fa22162d3aff19fa5b16fb7880de. PGN read back.

1.c4 Nf6 2.e3 e6 3.Nf3 d5 4.a3 Be7 5.Nc3 O-O 6.h3 c5 7.d4 Nc6 8.Be2 b6 9.O-O Bb7 10.cxd5 exd5 11.Re1 Re8 12.Bb5 a6 13.Bf1 Rc8 14.b3 Ne4 15.Bd2 Nxd2 16.Qxd2 Bf6 17.Rac1 Qd6 18.Ne2 cxd4 19.Nexd4 Qxa3 20.Ra1 Qd6 21.Bxa6 Bxa6 22.Rxa6 Nb4 23.Raa1 Re4 24.Nf5 Qd7 25.N5d4 Nc6 26.Rec1 Ne5 27.Nxe5 Bxe5 28.Rxc8+ Qxc8 29.Qc1 Qxc1+ 30.Rxc1 Bxd4 31.Rc8+ Re8 32.Rxe8#.

Castled on 5, all minors by 9, both rooks by 13. The central pawn exchange and Nxd2/Qxd2 were balanced; first 15 materially clean. Qxa3 won a pawn after the c-file pawn moved, and the planned a3-b4-c5-d6 queen retreat was actually used after Ra1. White recovered that pawn with Bxa6/Bxa6/Rxa6: bishop protection did not preserve a6 against this equal bishop exchange. Material returned to equality.

...Nb4 attacked Ra6 with queen support and cleared Qd6's line to b6. ...Re4 was supported by d5 and had an e-file retreat. Nf5 forced ...Qd7; after N5d4 blocked the rook's support of Nb4, ...Nc6 returned the knight to support before Qxb4. ...Ne5/Nxe5/...Bxe5 completed another equal minor exchange. Rxc8+/Qxc8 traded one rook pair; Qc1/Qxc1+/Rxc1 traded queens at equal material.

The decisive failure was 30...Bxd4. I planned exd4/Rxd4 to gain a pawn and considered an intervening Rc8+, but did not verify the king escapes. With Kg8 and pawns f7/g7/h7 still on their original squares, f8 and h8 lay on the checking rook's rank, while f7/g7/h7 were occupied. White actually played Rc8+, forcing the rook block ...Re8, and Rxe8 was mate. No exd4 or Rxd4 occurred. The bishop capture removed White's knight but did not make the line safe against a forcing check.

This game contains several locally correct defender updates and no earlier unexpected rook drop, yet it ended in a basic back-rank mate against skill 0. Those local successes do not establish stronger play or excuse the omitted king-safety consequence.

After 130: 50W/3D/77L overall; MAX 0W/2D/42L in 44, skill 0 38W/1D/5L in 44, nominal 1800 12W/0D/30L in 42. Elo 1580 [1460,1700], back to the trial baseline; 86 rated total/latest 50, 44 MAX exclusions; storage 34,602,925 bytes. Trial 17 is 1W/0D/3L, 91 own moves / 183 plies, zero illegal submissions. Complete the fixed endpoint with 131 White and 132 Black against nominal 1800 before revising the method.


## Benchmark 131 — White versus nominal 1800, successful endgame conversion with retained errors

Finished 2026-10-02 21:21:16 UTC with referee-confirmed 90.Qc2#, 90 own moves / 179 plies, zero illegal attempts. Result seq 10823, sha256 c504fabc72133724e8e16bc63910ca7154a81ec7c2237df4dda903063742c96b; snapshot 38bf0303fa12f64f014ecc9abc28545b016106c5b659c442fd080a2f97ab941b. Complete PGN read back.

Castled on 5, all minors by 8, both rooks by 11; first 15 materially clean. Bd2 supplied a recapturer behind Nc3 before the b-pawn moved. a3 chased Bb4 before Re1, avoiding game 127's specific arrangement. After Nxb5/Ne4, Bf1 retained the diagonal recapture on b5 while escaping the knight attack on Bd2. Bxb5/Bxb5 and Nxd2/Qxd2 were equal minor trades; Bxa3 recovered Black's pawn deficit. Rc2 escaped Ba3, and Rd1 removed the other rook from the possible bishop skewer behind Qd2. These were concrete local corrections, not proof of a generally sound opening.

The central exchanges through 29.fxe4 Bb8 retained equality. fxe4 exchanged knights while leaving d4 as a blocker on the b6-e3 queen diagonal. Qd2 attacked Rc3, answered by ...Qb4; e5 then closed the bishop route to h2. The material error came with 32.Rf1 Rxb3. I counted Ba4 as a recapturer but failed to account for the discovered Qb4-c3-d2 attack after the rook moved. Rf1 had removed Qd2's rook defender. Bxb3 would therefore lose the queen; Qxb4/Rxb4/Bc2 instead retained a one-pawn deficit. The subsequent ...a4/...Rb8 allowed Ra1/Rxa4 to recover the pawn. The recovery does not erase the earlier missed combined threat.

In the sparse ending I preserved the rook while improving king and bishop placement, completed e4/dxe4+/Bxe4 and the legal en-passant exchange, and kept d4 supported before Ra6. After ...Rd8 I chose Rxe6, explicitly rejecting an illegal Kxd4 recapture if ...Rxd4+ followed and planning Ke3 instead. Black actually played ...Be7 and left the extra pawn. After d5/Rd6, Re5 retreated with pawn support; ...g6 removed f5 as a safe rook retreat, so Bf3 freed e4. Ke4 then occupied that square, and against ...Bf6 I used the separately defended Re6. Rxe6+/dxe6 completed the actual equal rook exchange. No unanticipated rook loss occurred in this game.

Bg4 protected the passed e6 pawn while the king won g6 and h4. The h-pawn advanced with king support. At 69.e7 I deliberately offered the central pawn to divert Kf6: ...Kxe7 made Kg7 legal, keeping h6 defended while clearing its advance. h7/Bf6+/Kg8/Ba1/h8=Q/Bxh8/Kxh8 executed the planned transaction and removed Black's bishop. This is an actual successful longer continuation, although it relies on the opponent's played defenses rather than certifying the best defense or a forced win from earlier positions.

A later oversight remains: after Bf3/g4/g5, ...Kf4 attacked both g5 and Bf3. My preceding note tracked only the pawn attack. Before playing 79.g6 I recognized the bishop loss and calculated that ...Kxf3/Kh7/g7/g8=Q would promote first. That capture and promotion actually occurred. Thus the bishop was lost after an incompletely anticipated king fork, followed by a successful promotion calculation; do not describe the entire conversion as error-free. The final queen-and-king sequence preserved legal black moves until 90.Qc2#.

After 131: 51W/3D/77L overall in 131 scored games; MAX 0W/2D/42L in 44, skill 0 38W/1D/5L in 44, nominal 1800 13W/0D/30L in 43. Elo 1590 [1470,1710], 87 rated total/latest 50, 44 MAX exclusions; storage 35,047,830 bytes. Trial 17 is 2W/0D/3L, 181 own moves / 362 plies, zero illegal submissions. This supplies a successful endgame example, not sustained Elo improvement. Complete game 132 before the declared endpoint assessment.


## User endpoint update — 2 October 2026, during game 131

Read the updated bounded-run sections of AGENTS.md and GOAL.md after the user's direction. The existing run ends at exactly 200 scored benchmark games, including all prior scored results. Practice and unfinished safety-limit games do not count. Continue autonomous study/practice and the unchanged fixed benchmark rotation until that endpoint; then stop benchmarks, report measured Elo/per-opponent results and honest learning evidence, and mark the bounded experiment complete regardless of achieved Elo. Do not inspect other learners or shared comparison material. No move rules, opponents, estimator, past results or curriculum were changed. Trial 17's existing endpoint remains 132; no extra practice was added to its block.


## Benchmark 132 — Black versus nominal 1800, rook pin and false king recapture

Finished 2026-10-02 22:03:13 UTC by practical resignation after 54.Rxb6, 53 own moves / 107 plies, zero illegal submissions. Result seq 10932, sha256 e1dea53e93bbe5b3f566f6e8ba0a13e7f69ecf8e3abd41a6772fc8e5594c6b37; snapshot 7ba38559c6b7a547ff85c9db9cbbe9de992e999cfb652b3a43168a363b6b7b7c. Complete PGN read back.

Castled on 6, all minors by 7, both rooks by 13; first 15 materially clean. Nxg6/hxg6, dxc5/Nxc5, Bxc5/Bxc5 and cxd5/Nxd5 completed the intended equal exchanges. Red8 escaped Bb5's attack with rook and queen support. Against 22.Bc4, ...Nf6 avoided Bxd5/Rxd5/Qxd5: moving the white bishop would expose Qb3's line to the nominal rook recapturer. Rxd1+/Rxd1 then exchanged one rook pair at equality.

The remaining rook went Rc6, answered Qa4 with the supported Rd6, then Re6 behind e4. Moving Nd7 and retreating Bb4-c5 after a3 were locally supported. However ...f6 and ...fxg5 vacated f7 while Re6 and Kg8 remained on c4-d5-e6-f7-g8. After 33...gxh5 White played 34.Bc4, pinning and attacking Re6. I had counted on Bxh5 instead and failed to preserve the changed king line. ...Kf8 unpinned the rook but did not prevent 35.Bxe6/Qxe6, an exchange loss. 36.Qxe4 recovered the central pawn as its rook defender was gone. Qg4+/Qxg4/hxg4 completed a sound queen exchange afterward; it did not repair the earlier loss.

The ending was Black bishop/knight/five pawns versus White rook/knight/four pawns. I centralized the king and retained Nf6's defense of g4. Several specific checks were handled correctly: Ng3+ excluded f5, Nc4+ reopened the d-file, and Nc4 controlled b6. After ...b5/Nb2/...b4/Nc4, I used ...Bb6 to defend a5, with Kc6 behind the bishop. This was still only a nominal defender arrangement.

53.Rd6+ was protected by Nc4, so Kxd6 was unavailable; I correctly recognized that and played ...Kc5. But 54.Rxb6 captured the bishop on another square still protected by Nc4. Kxb6 was therefore illegal as well. Before Rd6, the imagined Nxb6/Kxb6 exchange would remove the c4 knight; the actual rook capture left that knight in place. After Rd6, even a knight capture on b6 would leave Rd6 guarding b6. The specific capturing piece and the newly occupied rook rank changed the recapture. I recognized the failed king capture after the bishop was lost, did not submit it, and resigned.

Final position: White Kg2/Rb6/Nc4/a4,b3,e3,f2 versus Black Kc5/Nf6/a5,b4,g4,g5,g7. This is a rook deficit for one pawn. Legal continuations remained; resignation was practical, not checkmate or a proof that every defense from earlier positions lost. No engine analysis or certified best alternative was used.

After 132: 51W/3D/78L overall in 132 scored games. MAX 0W/2D/42L in 44; skill 0 38W/1D/5L in 44; nominal 1800 13W/0D/31L in 44. Elo 1580 [1460,1700], 88 rated total/latest 50, 44 MAX exclusions; storage 35,444,837 bytes.

## Trial 17 endpoint assessment — 132

The predeclared six-game block is complete: 2W/0D/4L, 234 own moves / 469 plies, zero illegal submissions. MAX 0/2, skill 0 1/2, nominal 1800 1/2. Elo returned to the exact 1580 [1460,1700] baseline after transient 1590 readings. No sustained rating improvement is shown.

The two 20-move sparse-position practices were unfinished and avoided unexpected rook/minor loss, but did not demonstrate complete defense or conversion. Transfer was inadequate: 127 lost a rook through an incomplete forcing transaction; 128 missed smothered mate; 130 missed back-rank mate; 132 lost the exchange through a new bishop pin and then lost a bishop through an illegal king-recapture assumption. Game 129 won despite an erroneous recapture plan. Game 131 supplied genuine positive evidence of successful rook preservation, king activity, a played pawn-deflection sequence, promotion and mate, while retaining its earlier pawn loss and late missed bishop attack.

Normal development was consistently completed without first-15 material loss in this block. That modest process result is not a substitute for tactical reliability. The trial's focused rook cue did not generalize reliably even to another rook/king-defender position. Stop treating this intervention as effective; revise the next bounded learning trial while retaining ordinary development and all losses. No extra practice or selective benchmark extension was added, and no valid cumulative token counter was available.

The user endpoint remains exactly 200 scored benchmark games. There are 68 scored games remaining; practice does not count.


# Trial 18 — forcing king safety and recapture contrasts

Declared 2026-10-02 22:07 UTC after game 132, with no active game. Baseline: 1580 [1460,1700], 51W/3D/78L in 132 scored games; MAX 0W/2D/42L, skill 0 38W/1D/5L, nominal 1800 13W/0D/31L (44 each). The user endpoint is exactly 200 scored games. This trial's fixed benchmark block is 133–138 in the unchanged paired-color rotation.

## Weakness and method

Trial 17 did not transfer reliably: the material calculation repeatedly stopped before a forcing check or treated a nearby king as a recapturer without retaining the opponent's surviving defender. Revisit this already-failed skill explicitly; this is not a novel checklist or a claim that recalling a diagram is improvement.

First make and mechanically check eight manually specified contrast cases from our own games 128, 130 and 132. Only board reconstruction and legality of the specified moves are allowed. No generated move menu, attack-map analysis, search, engine evaluation or external source. The remembered positions are training examples, not held-out tests.

Then play exactly two fresh self-composed opponent-practice positions at nominal 1800, White then Black, at most 20 own moves plus the reply in each. Unlike trial 17's sparse rook drills, both positions retain queens, rook, bishop, knight and six pawns per side, including constrained castled kings and diagonals that can open when blockers move. These are equal-material constructions, not certified equal evaluations.

Combined study/practice deadline: 2026-10-02 22:52:05 UTC, 45 minutes from the post-132 review clock. End any ongoing practice at its move cap or this deadline; record early results or unfinished sessions and add no replacement practice. Return to benchmarks after both sessions, even if the exercises fail.

Position A, White:
5rk1/p1pq1ppp/1b2p3/3n4/3N4/1B2P3/P1PQ1PPP/5RK1 w - - 0 1

Position B, Black:
6rk/pp2qppp/3bpn2/8/8/3BPN2/PP2QPPP/6RK b - - 0 1

## Predictions written before legality checks

1. Game 132 after ply 104 (...Bb6): Nxb6/Kxb6 is legal because the knight leaves c4 and Rd1 does not guard b6.
2. From that same position, Rd6+/Kc5/Rxb6 is legal, but Kxb6 is illegal: Nc4 survives and protects b6.
3. From that same position, Rd6+/Kc5/Nxb6 is legal, but Kxb6 is illegal: Rd6 now protects b6.
4. Immediately after Rd6+, Kxd6 is illegal because Nc4 protects d6.
5. Game 130 after ply 61 (Rc8+): Kh7 is illegal because h7 is occupied; Kf8 is illegal because the checking rook controls f8. Re8/Rxe8 are legal and the recorded result is mate.
6. Counterfactual to case 5 with only the black h7 pawn placed on h6: Kh7 is legal. This demonstrates an actual escape square, not a certified best earlier plan.
7. Game 128 after ply 35 (Qg8+): Kxg8 is illegal while Bb3 protects g8. Nxg8/Nf7 are legal; the recorded result is mate, so winning the queen did not make the capture safe.
8. Counterfactual to case 7 with Bb3 removed: Kxg8 is legal. This deliberately changes material and is only a geometry contrast.

## Evaluation and decision

The practice target is to preserve a usable king response through checking continuations and to reject false king recaptures in the actual final board. Track actual mating losses, newly opened pins, unsupported material losses and illegal submissions; retain all other errors as well. Success on remembered cases is diagnosis/retention only. Fresh practice is still training, not Elo evidence.

Use ordinary development in games. A short cue replaces trial 17's special rook focus: when a capture gives or permits check, resolve the king response before counting the gain; a king recapture must be legal with every surviving enemy defender still present. Do not expand the cue into an exhaustive move checklist or assume a king-adjacent piece is secure.

At game 138 report the whole block's W/D/L, per-opponent results, Elo and uncertainty, along with recurrence of the targeted errors. A recurrence rejects reliable execution and requires another revision. No single win, clean drill or transient rating rise establishes sustained progress. No opponent, estimator, decision-time target or token counter is changed.


## Contrast study completed — before opponent practice

Eight predeclared case groups were checked as eleven supplied branches, 21 specified plies: 15 legal continuations and six deliberately illegal king moves. Every starting board was valid and all predictions matched. Inputs, the supplied-move-only verifier, and results are saved in king-safety-18-inputs.json, king-safety-18-verify.py and king-safety-18-legality.json.

The check used only the existing vendored board module, with bytecode writes disabled and the shared t3-job wrapper. It reconstructed our recorded SAN moves and checked the explicitly supplied UCI moves. No engine interface, search, generated move menu, attack map or evaluation was used. The two mating outcomes are from the recorded referee results, not a new automated evaluation.

The 132 contrasts distinguish Nxb6 before Rd6 (king recapture legal), Rxb6 after Rd6 (Nc4 survives), and Nxb6 after Rd6 (Rd6 survives). Both later king recaptures are illegal. The 130 counterfactual makes h7 available only by actually vacating h7; merely naming it did not create an escape. The 128 contrast confirms Bb3's role in preventing Kxg8, while the recorded Nxg8/Nf7 sequence shows that a legal queen capture can still allow mate.

These were known failures with written predictions, so passing them is diagnosis/retention only. Proceed to the two declared fresh positions without extra examples or changed limits.


## Practice 31 — fresh White position A

Stopped at the declared cap on 2026-10-02 22:27:15 UTC: 20 own moves / 40 plies, zero illegal submissions, unfinished rather than a win or draw. Result seq 984, sha256 5654baa3c792f9e85a54a85bce6174723c175e7cc1858ad2bc0652ff8c982b70. PGN read back.

1.h3 Nf6 2.Rd1 c5 3.Nf3 Qb5 4.c4 Qc6 5.Qc2 Rb8 6.Nd2 Qc7 7.e4 Nd7 8.Nf3 Ne5 9.Nxe5 Qxe5 10.Rd7 Bc7 11.g3 Ba5 12.Kh2 h5 13.f4 Qf6 14.e5 Qh6 15.h4 g6 16.Rxa7 Bb6 17.Ra6 Qf8 18.a3 Qe8 19.Ba4 Qd8 20.Bb5 Ra8.

h3 created an initial h2 escape. Rd1 supplied a real queen defender before Nf3 opened the d-file; c4 stopped a pawn advance that would restrict Bb3 behind a2/c2. Nd2 added e4 support before the pawn advanced. After Qc7 and later Qxe5, I explicitly stopped treating h2 as safe. Bc7 created the queen-bishop battery; g3 blocked it with f2 support, and Kh2 was chosen only after checking the actual diagonal. f4/e5 gained queen tempi with pawn support, and h4 closed the pawn contact.

The knight exchange completed at equality. Rxa7 won the pawn only after its bishop defender left b6, and the planned Ra6 retreat was actually used after ...Bb6. I kept a4 clear by a3 rather than a4. Ba4 forced the queen off e8, then Bb5 restored the rook exit and put the bishop on a c4-supported square protecting Ra6.

Final board: White Kh2/Qc2/Ra6/Bb5/a3,c4,e5,f4,g3,h4 versus Black Kg8/Qd8/Ra8/Bb6/c5,e6,f7,g6,h5. White has one extra pawn. No unexpected material loss, mating loss or illegal move occurred within the cap. Black's final ...Ra8 attacks Ra6. The bishop-support geometry was planned, but no further rook exchange or recapture was played; do not report a completed defense, conversion or practice win. This is positive training execution, not measured Elo evidence.

## Trial 18 practice B and training endpoint — 2026-10-02 22:43 UTC

Practice 32, Black, nominal 1800, fresh self-composed FEN `6rk/pp2qppp/3bpn2/8/8/3BPN2/PP2QPPP/6RK b - - 0 1`, ended exactly at the declared 20 own moves plus final opponent reply (40 plies). Referee result is unfinished, not a win/draw/loss; zero illegal submissions. Result seq 1027, hash `1cfdca0761e4e96e4333a5db074df29aee2173b957c74864f9691116bd4afdef`, timestamp 22:43:06. PGN read back in full.

Actual moves:
1...Rf8 2.a3 e5 3.Bb1 e4 4.Nd4 Qe5 5.f4 exf3 6.Nxf3 Qh5 7.g3 Re8 8.b4 Ne4 9.Bxe4 Rxe4 10.Kg2 f5 11.Qd3 Be7 12.Rc1 h6 13.Kf2 g5 14.Qd7 g4 15.Rc8+ Kh7 16.Nh4 Qf7 17.Nxf5 Re5 18.Rc5 Rxc5 19.bxc5 Qa2+ 20.Kg1 Qb1+ 21.Kf2.

Observed useful execution:
- Rf8 opened g8 while Qe7 guarded f8; no assumed king recapture from h8 to f8.
- e4 blocked Bb1-h7. The actual f4/exf3 en-passant/Nxf3 sequence exchanged pawns and changed the queen attack and h2 defense; no pawn win was claimed.
- Bxe4/Rxe4 was an actual equal minor exchange. White Kg2 ended the earlier h-pawn pin.
- Once White Rc1 made Rc8+ concrete, h6 created h7. White's bishop had gone; later Qd7 was blocked by Be7. The actual Rc8+/Kh7 response was legal.
- Recognized the bishop pin on the seventh rank and inserted Qf7 as a second blocker.

Errors and limits retained:
- The claims that f5 was defended were materially incomplete. White Qd7 and Nh4 jointly attacked it, and 17.Nxf5 won the pawn. Qxf5+ would allow Qd7xf5+, so queen protection was not an adequate recapture. This repeats the effective-defender weakness.
- Rxc5/bxc5 was an equal rook trade. An immediate Bxc5 would open Qd7's attack on Qf7. Qa2+ moved the queen with check, but my initial planned bishop recovery still failed: Be7 was again the sole blocker between Qd7 and Kh7, so Bxc5 would be illegal. This was recognized before submission. The final Qb1+ bought another king response but did not solve the bishop problem.
- Final Black Kh7/Qb1/Be7 with a7,b7,g4,h6 versus White Kf2/Qd7/Nf5 with a3,c5,e3,g3,h2. One pawn down, bishop pinned and attacked, no resolved defense or conversion. No illegal move was submitted.

Both declared practices are now complete, both unfinished at 20 own moves and zero illegal attempts, before the shared 22:52:05 deadline. Practice A ended one pawn up with a final rook attack still unresolved; B ended one pawn down with an unresolved bishop pin. Eight remembered contrast groups passed their specified legality predictions, but that is retention, not transfer. Fresh B already reproduced an inadequate recapture assumption, so these drills do not establish reliable king-safety execution or improved playing strength.

No extra practice or selective extension. Proceed with the predeclared unchanged fixed benchmark block 133–138, assessing all six results at 138. Baseline remains 1580 [1460,1700], 51W/3D/78L after 132; training is excluded from ratings. The run stops at 200 scored benchmarks regardless of Elo. No valid new cumulative token counter is available. The tool goal still contains the obsolete win-based objective and old blocked status; the explicit user endpoint and current AGENTS/GOAL govern this continuation.

## Benchmark 133 — White versus maximum strength — loss, 2026-10-02 23:00 UTC

41 own moves, 82 plies, zero illegal submissions. Practical resignation after 41...Kxa4 with N+2P versus N+5P and connected Black a/b passers; legal continuations remained, not checkmate or a proved forced win. Result seq 11016, hash `90194b603881f7e1a8f6924809e1f44a584d2ae27bfdd10e5d759ae196517515`; snapshot `a84f8d5f14e518687af2594d20dc7cba511e8549ba6c9f5ab5038e365973a7cb`. Full PGN read back.

Normal development: castled move6, all minors developed move8, first rook move11 and second13, first15 moves without material loss. h3 created a currently legal h2 escape; no later back-rank mate occurred. c4/dxc4/Nxc4 exchanged central pawns, leaving isolated d4. Nce5 deliberately retained Nf3 as a d4 defender.

Error: 18.Bd3 was annotated as retaining Qd1 and Nf3 on d4, but Bd3 itself blocked the queen line. This was noticed at 19.Qxc1 after ...Rxc1, not before the bishop move. ...Bxd3/Nxd3 and ...Nf5 left d4 under three-piece pressure. Qf4 did not restore a sufficient defense; ...Nxd4/Nxd4/Qxd4/Qxd4/Rxd4 cost the pawn while otherwise exchanging material equally. This is another blocked/effective-defender failure, not a new mating failure.

The rook sequence Ne5/Re4/Nf3/Rxe1+/Nxe1 was handled with an actual knight recapture; Kg1 could not recapture e1. Endgame: a4 avoided an undefended-a2 fork, and after Kf3/f5, Nb2 was played before the actual ...e4+, avoiding a check-and-knight fork. Kxe4 was correctly rejected because f5 guarded it. Nd3+ later was rejected because e4 could capture the checking knight. These are local observed/identified tactics, not evidence that the ending was held.

Black's checks drove the king backward, then Kc5–b4–xb3 and ...Kxa4 took both queenside pawns. f3/exf3/gxf3 exchanged the central pawn, and h4 saved h3 from the knight attack, but no adequate defense of the queenside was found. Final: White Kd2/Ne3/f3,h4; Black Ka4/Nf4/a5,b6,f5,g6,h6.

Cumulative 51W/3D/79L from133; MAX 0W/2D/43L from45. MAX remains excluded from the nominal rating, so the displayed baseline estimate remains1580 [1460,1700]. Trial18 block133–138 continues as declared; one loss alone is not its full endpoint assessment. No additional practice inserted.

## Benchmark 134 — Black versus maximum strength — loss, 2026-10-02 23:14 UTC

27 own moves, 55 plies, zero illegal submissions. Practical resignation after 28.Qxd5, a bishop and two pawns down with the central counterplay gone; legal defensive continuations remained, not a mate or proved forced loss. Result seq11073, hash `f2983dc23209582c25bedb212b9f7dee26aaf292af5eec514481bfd6fbc06b36`, snapshot `d1ea746beb9902d73a338d175a7ec6e20cb6aa5fd1fc019f82e0ec42f00f662a`. Full PGN read back.

Ruy Lopez development: castled7, all minors developed9. Bb7 cleared c8 so the queen could recapture on a8 if the a-file opened. Na5/c5/c4 gained space; Nd7/f5 attempted a central break. No claim that the resulting position was objectively good.

Decisive failure: after 15.exf5 I recognized that the promised Rxf5 was unsound because White's e-pawn departure had opened Bc2-d3-e4-f5. But the replacement 15...Bxd5 overlooked Qd1-d2-d3-d4-d5. Actual 16.Qxd5+ won the undefended bishop and checked along the newly open d5-e6-f7-g8 diagonal. Kh8 was a legal reply. Catching the first bad candidate did not make the replacement sound.

Nf6 chased the queen, axb5 restored pawn parity, and the actual Rxa8/Qxa8 exchange was correctly recaptured. Another effective-defender error followed: d5 removed the d6 pawn's defense of e5. Nc6 alone did not hold it against Nf3 and Re1; Nxe5/Nxe5/Rxe5 cost another pawn. Bd6/Re6/Qc6/Bf4 created a relative pin of Bd6 to Qc6. Ne8 added a rook-supported defender, and the actual Bxd6/Nxd6 exchanged bishops without a further piece loss. Qd7 moved out of that alignment but White Qxd5 took the remaining center pawn and supported Re6.

Final Black Kh8/Qd7/Rf8/Nd6/b5,c4,g7,h7 versus White Kg1/Qd5/Re6/Bc2/Nf3/b2,c3,f2,f5,g2,h3. No material recovery or reliable forcing-safety transfer established.

Cumulative51W/3D/80L from134; MAX0W/2D/44L from46. The nominal rating remains1580 [1460,1700] because MAX is excluded. Trial18 is0W/0D/2L so far, with its complete assessment still fixed at138. Continue135–138 in unchanged rotation, without extra practice.

## Benchmark 135 — White versus skill0 — checkmated, 2026-10-02 23:34 UTC

37 own moves, 74 plies, zero illegal submissions; actual 37...R8e3#. Result seq11149, hash `cd31c0e66a41e3760331ffd2b159f6ca57244a4d22465829af5cdfbe2d24ca4d`, snapshot `b5750b9dbae119a8e9e301218596d6ee452862479d9b5372f98c699e67350e2b`. Full PGN read back and status verified.

Castled5, developed all minors9, rooks10 and14. First15 moves material-clean. Bd3 was explicitly assessed as blocking Qd1's d4 defense this time, with e3/Nf3 remaining. Equal bishop and queenside-pawn exchanges; Ne2-f4 and Nf3-e5 improved activity. After h4/Nxe5/dxe5, the cleared Bb2 diagonal did protect e5 as planned.

Missed threats:
- ...Qb7 directly attacked Bb2. I annotated hxg5 as a knight-for-pawn gain while looking at other queen lines, overlooking the actual ...Qxb2. This was a knight/bishop exchange, not a won piece. gxh6/Qxe5 subsequently exchanged pawns equally while retaining an advanced h-pawn.
- Nd3 attacked Qe5, but I overlooked ...Qxe3+ before the queen exchange. Qxe3/Rxe3 left White one pawn down. Nd3 also blocked the Rd1-d4 defense of the queen; simply moving the king would not have preserved that queen.
- Rh1 correctly guarded h6; Black Kh7 could not capture it while the rook line remained clear. Kf2 and later f4/g3/Rce1 were legal defensive/activation moves, but the claimed safety of Kf3 was only a current-square check, not a check of the opponent's forcing reply.

Decisive mate: after ...Re2+, 37.Kf3 allowed ...R8e3#. Re2 protected the checking Re3 and controlled f2/g2; White's own f4 and g3 pawns occupied escapes, Black f5 controlled g4, and the e-file/central pawns covered the remaining exits. Re2 also blocked Re1 from capturing the checking rook on e3. No king capture of Re3 was legal while Re2 survived. I had considered a rook exchange but chose king activity without recognizing this mate. This is direct recurrence of trial18's forcing-king-safety target, despite legal move submissions and some correctly identified individual recaptures.

Actual ending had White Kf3/Re1/Rh1/Nd3/a4,c5,f4,g3,h6 versus Black Kh7/Re2/Re3/Bc7/a5,c6,d5,f5,f6,g6. No conversion or improved strength established.

Cumulative51W/3D/81L after135. MAX0W/2D/44L (46); skill0 38W/1D/6L (45); nominal1800 13W/0D/31L (44). Elo1570 [1450,1690], 95% Bayesian equal-tail interval,89 rated games total/latest50,46 MAX excluded. Storage37,248,796bytes. Trial18 now0W/0D/3L; finish the predeclared136–138 before its full endpoint review. No extra practice or changed opponent settings.

## Benchmark 136 — Black versus skill0 — win, 2026-10-03 00:01 UTC

57 own moves,114 plies,zero illegal submissions; actual57...Ra1#. Result seq11265, hash `aed2703c3b4b98a288233bb33a2870713b5a53fec3bc3497de0aad9b6a075395`; snapshot `1c03cbc0806d91580dbe392afc43fc3e8a3c123280dda474dafb2241ad0eb237`. Full PGN and status read back.

Castled5, all minors developed8. First15 own moves had equal material transactions without unexpected loss. Rxa8/Qxa8 and Nxe4/fxe4 were correctly recaptured; fxe4 opened the f-file and drove Nf3 back. Ba6 was protected by Qa8, and Bxa6/Qxa6 later exchanged bishops equally. h6 created a currently safe h7 escape, explicitly conditional on e4 still blocking Qc2-h7. Qe6 restored d5 defense after e6-e5; Qg4's g3 pin was explicitly dropped from the assessment when Qh5 moved away. Queens exchanged25...Qxe2/Nxe2.

White's c6 advance attacked Nd7. Nb8 attacked that pawn; after White Rd1 failed to defend it, Nxc6 won it. Rb8 pressured Bb2; dxe5/Nxe5/Bxe5/Bxe5 was an actual equal minor/pawn exchange leaving R+B versus R+N and a pawn extra. Be5 guarded c7. Kf7-e6-d6 activated the king and kept d5 defended while facing rook/knight checks.

Concrete forcing-safety execution:
- Rb7 blocked Ra7+ with Kc7 support. After Ne6+, Kd6 would have abandoned Rb7; Kb6 was chosen instead, retaining that support.
- White39.Ra6+ left the checking rook unprotected by Ne6. Actual39...Kxa6 was legal and won it; all remaining White defenders were considered, rather than proximity alone.
- White40.Nxc5+ forked king and Rb7. Kb6 retained a legal recapture after a possible Nxb7. White instead continued Na4+, met by Kc6.
- Rb4 attacked Na4 while covering b2/b6, Be5 covered c3 and Kc6 covered c5. White g4 left the knight, and actual Rxa4 won it.

The decisive rook and knight losses were opponent blunders. Correctly taking them and preserving material is observed execution, not independent proof of increased strength. Conversion: hxg5/hxg5/g6 blocked the pawn; ...exf3+ en passant removed the attacking f-pawn with an explicitly allowed Kxf3 recapture. The remaining pawns were captured, the rook cut off ranks, the king advanced, and Ra2-a1# was completed with Ke3 covering d2/e2/f2. No claimed conversion was left hypothetical.

Cumulative52W/3D/81L after136. MAX0W/2D/44L from46; skill0 39W/1D/6L from46; nominal1800 13W/0D/31L from44. Elo1580 [1460,1700],95% Bayesian equal-tail interval,90 rated total/latest50,46 MAX excluded. Storage37,661,248bytes. Trial18 is1W/0D/3L through four games; finish the unchanged137–138 nominal1800 pair before full assessment. The prior checkmate in135 and defender errors remain in the trial record.


## Benchmark 137 — 2026-10-03 00:22 UTC
White versus nominal 1800; loss by resignation after 53...Rg2. 53 own moves, 106 plies, zero illegal submissions. Full saved PGN read. Result seq 11373; hash b20c02b1fe0703b412366ca9b86abeffc9880be69d01e2438b0b29672685c4bc; snapshot 034181d05c880a08d61abe15a206114af281b142d9e151116f78ad6dcae4d898.

Castled on 5, last minor developed/exchanged by 10, rooks activated on 11 and 15; first 15 moves had no unexpected material loss. The supported Nd6 outpost and Rc5 activity won the a-pawn. Qd3 retained Bb3 and d6 defenses; R1c3 added a lower-value bishop defender against Qb6/Rb8, correctly avoiding an insufficient queen-only recapture. Rxc6 won a second pawn and d7 created a serious passer. However, the proposed queen-exchange/Rc8 conversion omitted 36...Ne2+, a checking fork of king and supporting rook. 37.Kh2 Nxc3 38.Rxc3 left rook and bishop versus two rooks, with two extra pawns. This was an unanticipated exchange loss, not an independently validated sacrifice.

Ba4, Rd3 and b3 retained the passer/bishop; the king reached e4. The specific break 47.f5 gxf5+ 48.gxf5 exf5+ 49.Kxf5 actually occurred, and the king capture was legal only after both adjacent pawn defenders had left. 51.Kxh5 was also legal and gained another pawn. Then 52.Rg3 was a decisive fresh blunder: after ...Rxg3 I had imagined h3xg3, a sideways pawn capture. The pawn could only capture g4. No illegal attempt was submitted, but the rook was lost for nothing. This repeats elementary capture-origin failure despite earlier practice on related geometry. Final position after Kh4/Rg2: White Kh4/Ba4 with b3,d7,e5,h3 against Black Ke7/Rd8/Rg2/f7. I resigned as a practical assessment with legal continuations remaining; no forced loss was proved.

Cumulative 52W/3D/82L in 137; nominal 1800 13W/0D/32L in 45. MAX 0W/2D/44L in 46; skill 0 39W/1D/6L in 46. Elo 1570 [1450,1690], 91 rated total/latest 50 and 46 MAX excluded. Storage 38,068,679 bytes. Trial 18 through 133–137: 1W/0D/4L, 215 own moves/431 plies, zero illegal submissions. Actual positive king-capture evidence did not prevent a forcing-check miss or a basic impossible recapture plan. No sustained improvement claim; finish predeclared game 138 before assessment.


## Benchmark 138 — 2026-10-03 00:46 UTC
Black versus nominal 1800; loss by resignation after 54.Kg6. 53 own moves, 107 plies, zero illegal submissions. Full saved PGN read. Result seq 11482; hash 470daa651f1a6f73320e06eb0ff9d69da9572f0a7ebc15f04930c9972c3d3e2e; snapshot 2262911ee3f21c3bfad8fc2c616ce53fcd3c47bdc0beb7838a023cbda3a752fa.

Castled on 6, minors developed by 10, rooks active on 9/14; first 15 moves were material-clean. Queens exchanged on 12. Nxd3/cxd3 was an equal minor exchange; c6 retained the attacked c-pawn. Nxc3/Rxb7 exchanged pawns, then Nxe6/Rxe6/Rxe6/fxe6 exchanged minors and rooks equally. The f7-to-e6 pawn capture was actually legal and executed. Rxd3 won a pawn. After Be5, I recognized that the bishop made a king capture of a rook on g7 illegal; Nf5 added an effective defender. Rd5 supported a5, but Bc3 added a second attacker, so I did not assume Rxa5 would be a safe recapture. The king became active; 36...Kxd5 after Rxd5+ was an actual legal rook recapture, with surviving bishop/pawn controls checked.

The minor-piece ending deteriorated despite these local successes. After Kf2 I recognized that Nxf3 no longer won a pawn because the king defended it. ...g5 supported the restricted Nh4, Bxa5 returned material to equality, Kxa4 gained a pawn, and fxg5/hxg5 preserved the knight's pawn defender. White's Ke3 allowed the actual escape ...Ng2+ and ...Nf4. However, king activity and pawn grabs did not produce a coordinated conversion: Kxe5 removed the central pawn; Nxg4+/Kxg5 left one pawn each. White's bishop and king dominated the knight's route to the h-pawn. Several proposed knight routes were rejected mentally because the bishop or king could capture; Nd7/Bg7 also closed the f8 route. The c-pawn did not advance in time. Final: Black Kc4/Ne4/c6 against White Kg6/Bg7/h6. I resigned because I could not find a viable promotion defense; no tablebase/engine evaluation or exhaustive forced-loss proof was used. This is an endgame coordination and race failure, not a checkmate or illegal submission.

Cumulative 52W/3D/83L in 138. Each opponent has 46 games: MAX 0W/2D/44L; skill 0 39W/1D/6L; nominal 1800 13W/0D/33L. Elo 1560 [1440,1680], 92 rated total/latest 50; 46 MAX excluded. Storage 38,470,080 bytes.

## Trial 18 fixed endpoint — 138
All predeclared study and practice bounds were respected; no extra practice was added after the failed fresh practice. Benchmarks 133–138: 1W/0D/5L, 268 own moves/538 plies, zero illegal submissions. MAX 0/2, skill 0 1/2, nominal 1800 0/2; White 0W/3L, Black 1W/2L. All six had material-clean first 15 moves. Baseline 1580 [1460,1700] became 1560 [1440,1680]. Intervals overlap; this is not a statistical proof of decline, but there is no measured improvement.

Remembered contrast predictions matched mechanical legality, which is retention evidence only. The two fresh practices were unfinished: one pawn up with an unresolved rook attack, one pawn down with an unresolved pinned bishop. Benchmark positives include the actual Kxa6 capture and conversion in 136, Kxf5/Kxh5 in 137, effective g7 defense and Kxd5 in 138. They do not establish reliable transfer: 135 ended in the targeted forcing-check mate, 137 omitted ...Ne2+ and then lost a rook through an impossible sideways pawn-recapture assumption, while 133/134 retained defender and exchange errors. 138 added an unresolved knight-versus-bishop pawn-race weakness. Decision: discontinue the current king-safety cue as a successful intervention; retain ordinary development, acknowledge prior material-geometry methods also failed, and predeclare a revised bounded learning period before games 139–144. The 200-scored-game endpoint remains unchanged; 62 scored games remain.


# Trial 19 — minor-piece mobility and passed-pawn defense

Declared 2026-10-03 00:50 UTC after benchmark 138. Baseline 1560 [1440,1680], 52W/3D/83L, 92 rated games total/latest 50; each opponent has 46 scored games. Fixed next benchmark endpoint: games 139–144. Preserve rotation, settings, estimator and every record. The entire run ends at 200 scored games.

Trial 18 failed (1W/0D/5L). Trials 02, 12 and 13 already attempted explicit reconstruction, pawn origins and destination captures; their records show played failures despite implemented notes. Trial 10 already studied races with rooks. This is not a new general principle or a claim that another checklist will work. I am changing the material and practical task: recognize when a minor piece is being denied access to an opposing passer, before relying on distant king activity or pawn collection. In 138, the knight escaped h4 locally but the later bishop/king blockade of its routes defeated the h-pawn defense. The 137 sideways recapture and missed forcing check remain unresolved general weaknesses.

Bounded learning: a short mechanical check of five prewritten remembered/contrast branches below, then exactly two new self-composed nominal-1800 opponent practices, White then Black. Each practice ends naturally or explicitly unfinished after at most 16 own moves and the final opponent reply. Combined setup/study/practice/review ceiling: 2026-10-03 01:20:12 UTC. Add no repeats or replacement examples to improve the result. If the ceiling arrives, end an active drill and record any omitted work. Composed positions are not independently blind tests or certified equal positions; the mechanisms are known, and the opponent supplies fresh replies.

Practice A (White knight, Black bishop), FEN: `8/8/1p1k1b2/6p1/2K4p/P4NP1/5P2/8 w - - 0 1`.
White Kc4/Nf3/a3/f2/g3; Black Kd6/Bf6/b6/g5/h4. Both have a minor and three pawns. Decide how to handle the kingside pawn tension while preserving the knight's access; account for real captures rather than inventing a blockade result.

Practice B (Black knight, White bishop), FEN: `8/1p5p/2n2kp1/P7/1PB4P/4K3/8/8 b - - 0 1`.
Black Kf6/Nc6/b7/g6/h7; White Ke3/Bc4/a5/b4/h4. Both have a minor and three pawns. Deal with the advanced queenside pawn and bishop controls while retaining useful king/knight routes. This is a different composition, not a color-swapped copy of A.

Remembered/contrast predictions, recorded before mechanical checking (legality/check status only; no search, evaluation, attack map or move menu):
1. Game 137 after ply 104: h3g3 is illegal. The h3 pawn cannot recapture sideways after ...Rxg3. This is a remembered failure, not a fresh solution.
2. Game 138 after ply 73 (37.Kf2): h4f3 is a legal knight capture, and f2f3 is a legal king recapture. Thus Nxf3 is not a free pawn once the king has moved to f2.
3. Game 138 after ply 87 (44.Ke3): h4g2, e3f3, g2f4 are legal; Ng2 gives check. The proposed f3f4 king capture is illegal with the e5 and g5 pawn defenders surviving. This is the actual escape plus a supplied capture contrast.
4. Game 138 after ply 101 (51.Bf6): e5d7, h5h6, d7f8, h6h7, f8h7 are legal. The last knight capture gives check to Kg5. White cooperates in this deliberately supplied branch; it does not establish a hold against best play.
5. Game 138 after ply 103 (52.Bg7): d7f8 is still a legal knight move, but g7f8 is now a legal bishop capture. Legal mobility is not safe mobility; Bg7 changes the route used in branch 4.

Carry into practice and benchmarks: when an ending or exchange makes an enemy passed pawn urgent, identify the actual defender's route and the enemy king/bishop squares that bar it before choosing a distant pawn grab. Include the next capture and promotion response in that short line. Use ordinary development and ordinary capture/check reasoning; no special queen-trade preference, timing target, mandated move-note list or expanded general checklist. This targeted endgame cue is not a substitute for elementary legality or forcing-reply checks.

Assessment: record actual route obstructions, defender losses, legal recaptures, pawn promotions, successful stops, and all unrelated material/check errors. In capped practice an unresolved attack or race stays unresolved. A benchmark block with no relevant ending gives no direct transfer evidence. Compare the full fixed block and Elo interval at 144; do not claim a remembered legality match, a practice win or one benchmark win establishes learning. Revise again if the failures recur. All moves remain my own, without external chess advice, engines as analysts, automated move choice or delegation.


## Supplied-branch study result
Five branches / 14 supplied plies: 12 legal and two deliberately illegal; all predictions matched. The two predicted checking moves (Ng2 and Nxh7) were confirmed as checks. All starting positions were valid. The script checked only those prewritten moves using the vendored board module, with no engine, move menu, attack enumeration, scoring or search. Outputs: minor-mobility-19-legality.json. These are remembered/controlled contrasts; no fresh-solution accuracy or strength claim follows. The f8 branch explicitly demonstrates that move legality does not imply safe mobility. Proceed to the two predeclared new compositions only.


## Practice 33 — fresh composition A, unfinished
Stopped at the declared 16-own-move / 32-ply cap on 2026-10-03 01:01:52 UTC; zero illegal submissions. Result *, not a draw. Seq 1062; hash 5c345ed58b71c86e8a1c867279d7bfa573c75328403fbb35e9cb60a31d37b35a. Referee PGN read. Actual line: 1.Nd4 Ke5 2.Nf3+ Ke4 3.Nh2 Be5 4.f3+ Kf5 5.g4+ Kg6 6.Nf1 Kf6 7.Kd3 Bf4 8.Ke2 h3 9.Kf2 Ke5 10.Kg1 b5 11.Nh2 Kd5 12.Kh1 Kc4 13.Nf1 Kb3 14.Nh2 Kb2 15.Nf1 Kb3 16.Nh2 Kxa3.

After Ke5 I recognized that Bxd4 could no longer be answered safely by Kxd4 because the opposing king would guard d4. Nf3+ retained the knight, but allowed further king activity. f3+/g4+ moved the king back and kept the kingside pawns, yet vacating g3 opened Be5's line to Nh2; Nf1 escaped. I abandoned a knight-only blockade and brought the king through d3/e2/f2/g1/h1. The h3 pawn barred Kg2, so that route was not used. With Kg1 or Kh1 present, Nh2 had an actual king recapture after ...Bxh2; the h-pawn remained on h3. These are executed local defensive changes, not a proved hold.

Bf4 controlled the knight's alternatives d2/e3/g3/h2, while the king and knight were tied to the promotion corner. Black's king approached the other flank and captured a3 on the final reply. Final White Kh1/Nh2/f3/g4 against Black Ka3/Bf4/b5/g5/h3: one pawn down, no promotion or minor-piece loss, but the new b-pawn threat and restricted mobility remain unresolved. The starting composition was not objectively evaluated; no claim that these moves were best or that the position was initially drawable. No extra moves/repetition added; proceed to fresh composition B within the same deadline.


## Practice 34 — fresh composition B, draw after material errors
Ended naturally by insufficient material on 2026-10-03 01:09:44 UTC, 15 own moves / 29 plies, zero illegal submissions. Seq 1093; hash c22d6018447ba19c750ac45fe8b625e1ceb421cc2673934788839fe15f87f01f. Full referee PGN read. Actual line: 1...Nxb4 2.Kf4 h5 3.Be2 Nc6 4.Bc4 Nxa5 5.Bd3 Nc6 6.Be4 Ne5 7.Bxb7 Ke6 8.Kg3 Kf5 9.Ba6 Ke4 10.Bb5 Nf3 11.Be8 g5 12.Bxh5 Ne5 13.hxg5 Kf5 14.Bf7 Kxg5 15.Kh3 Nxf7 1/2-1/2.

The composition supplied an undefended b4 pawn, taken immediately. Nc6/Nxa5 also actually removed the advanced a-pawn when White left it undefended; this is an executed stop but an easy capture opportunity, not evidence of stronger defense against a well-supported passer. h5 fixed the other pawn. Then 6...Ne5 vacated c6 and opened Be4-d5-c6-b7: Bxb7 was an unanticipated pawn loss. I had noticed the attack on Nc6, but not the newly opened attack beyond it. The king/knight then reached Ke4/Nf3. Kxf3 by Kg3 was illegal while Ke4 guarded f3, but an immediate Nxh4 would still fail to the king on g3; that candidate was rejected.

11...g5 was intended to meet hxg5 with Nf3xg5. I omitted that vacating g6 both removed h5's defender and opened Be8-f7-g6-h5. White played Bxh5. The replacement 12...Ne5 then removed the knight's defense of g5, allowing 13.hxg5. All three original pawns were gone despite the earlier two-pawn gain. These are actual changed-line/defender failures, not a sound conversion. Kf5 approached the passer; White Bf7 left Pg5 undefended and the bishop itself attacked by Ne5. 14...Kxg5 was an actual legal king capture, and 15...Nxf7 removed the bishop. The referee drew with K+N against K. Opponent errors were decisive to this recovery; the draw does not erase the three pawn losses or demonstrate a forced defensive method.

## Trial 19 practice endpoint
Five remembered/controlled branches matched mechanical legality; two fresh composed practices then finished by 01:09:44, before the declared 01:20:12 ceiling. Combined 31 own moves / 61 plies, zero illegal submissions: one unfinished session one pawn down, one insufficient-material draw after surrendering a two-pawn advantage. No extra repetitions were added. A stopped the immediate h-pawn but tied down both pieces and conceded the other flank; B actually removed the a-pawn, then failed repeatedly on changed bishop lines and defenders before the opponent allowed simplification.

No practice evidence establishes improvement. Carry the predeclared minor-mobility/passers focus into fixed benchmarks 139–144, while retaining all capture, check and blocker errors. Do not expand the trial or treat the draw as a strength gain. Benchmark baseline remains 1560 [1440,1680], 52W/3D/83L in 138; practice does not enter Elo. No valid new cumulative token counter is available. All move choices and review were my own, with only the referee during active play and the declared limited mechanical checks between games.


## Benchmark 139 — 2026-10-03 01:24 UTC
White versus MAX; loss by resignation after 30...Rxa3. 30 own moves/60 plies, zero illegal submissions. Full PGN read. Result seq 11544; hash b670751a53bcfa942fe54cab2fa7cfd71e1290838c8512ebc17420637373c85a; snapshot 387312cd5f5f5a92c87a60a07b7b55546c831bf2c277b71adae5bcc6abd91f1b.

Castled on 6, minors developed by 8, rook activated on 11; first 15 moves material-clean. c3 retained a pawn defender of d4. Before Bf1 I rejected Bd3 because Nd2 would block Qd1's recapture after ...Bxd3; after Nf3 vacated d2, Bd3/Bxd3/Qxd3 was actually completed. Re5 could not retreat down the e-file with Be4 in the way; Rh5 preserved it when ...Nd7 attacked. Queens exchanged equally with ...bxc4, producing Black's queenside chain. Rb1 defended b2, while a speculative Rxf7 plan was invalid until Nf6 moved off the file; that blocker was noticed before an illegal submission. The rook activity did not yield a material gain.

After ...Rb3/...Ne4, I rejected Kf1 because ...Nd2+ would fork king and Rb1. However, 27.g3 allowed ...Nxc3, and 28.bxc3 was chosen while following ...Rxc3 in my own line. I omitted the decisive ...Rxb1+: vacating b2 opened the b-file from Rb3 to the rook behind it. Thus the apparent knight gain actually cost a rook and pawn, with check. This directly repeats the changed-blocker and incomplete-forcing-reply failures despite the practice period. Rf3 then protected c3 with Kg2 supporting the rook, but ...Rxa3 won another pawn; c3 blocked any Rf3-to-a3 recapture.

Final White Kg2/Rf3/Nc6/c3/d4/f2/g3/h3 against Black Kg8/Ra8/Ra3/a4/c4/d5/e6/f7/g7/h6. I resigned an exchange and two pawns down with an advanced supported a-pawn; legal continuations remained, and no forced-loss proof was used. No complete minor-piece-only ending or successful passed-pawn defense occurred, so there is no direct positive transfer evidence for trial 19. The older tactical weakness already recurred.

Cumulative 52W/3D/84L in 139. MAX 0W/2D/45L in 47; skill 0 39W/1D/6L and nominal 1800 13W/0D/33L, each 46. Elo stays 1560 [1440,1680], 92 rated total/latest 50; 47 MAX excluded. Storage 39,574,188 bytes. Trial 19 currently 0W/0D/1L; continue its fixed 139–144 block without extra practice. Sixty-one scored games remain to the 200-game endpoint.


## Benchmark 140 — 2026-10-03 01:34 UTC
Black versus MAX; loss by resignation after 23.Nxa1. 22 own moves/45 plies, zero illegal submissions. Referee PGN read. Result seq 11591; hash 42b9eb6e1f6851ea34492b935659048d5f2c5ee614efcfea0d2f89e59e60239f; snapshot 5fc4b03ed19e81069f079b6aa8c8cef2669cd895a403ed87b73bbdbae819cf91.

Castled on 7 and completed minor development on 9. The first 15 moves were not a material-clean opening: 13...c4 14.b4 restricted Na5. Nc6 was attacked by d5, b7 was occupied, and c4 held my own pawn. I chose 14...Nb3 15.Bxb3 cxb3 16.Qxb3, anticipating the pawn concession. The knight/bishop exchange was equal but the c-pawn was lost. Nd7 rerouted; I rejected Nc5 because b4 attacked it. After axb5/axb5 opened the a-file, Na3 temporarily blocked that file and attacked b5.

19...Qb6 defended b5 but 20.Be3 attacked the queen. 20...Qa6 retained that pawn defense while missing 21.Nc2: vacating a3 opened Ra1's attack on Qa6, and Nc2 also guarded a1. The queen obstructed my own Ra8. I found the queen's alternatives constrained by Be3, d5 and my own pieces, but did not prove a forced loss. The executed 21...Qxa1 22.Rxa1 Rxa1+ 23.Nxa1 traded my queen and one rook for both White rooks. It left a queen-for-rook deficit, not a favorable queen-for-two-rooks gain, because the knight recaptured the second rook.

Final Black Kg8/Rf8/Bb7/Be7/Nd7/b5/d6/e5/f7/g7/h6 versus White Kg1/Qb3/Be3/Na1/Nf3/b4/c3/d5/e4/f2/g2/h3. I resigned with the queen-for-rook deficit and one fewer pawn; legal continuations remained, and this was a practical decision without a forced-loss certificate. Both knight restriction and queen confinement were actual failures. There was no completed minor-piece ending or successful passer defense, and no positive transfer claim follows.

Cumulative 52W/3D/85L in 140. MAX 0W/2D/46L in 48; skill 0 39W/1D/6L and nominal 1800 13W/0D/33L, each 46. Elo 1560 [1440,1680], 92 rated total/latest 50; 48 MAX excluded. Storage 39,938,769 bytes. Trial 19 through 139–140: 0W/0D/2L, 52 own moves/105 plies, zero illegal submissions. Continue the fixed block through 144. Sixty scored games remain.


## Benchmark 141 — 2026-10-03 01:49 UTC
White versus skill 0; loss by resignation after 41...Kxg6. 41 own moves/82 plies, zero illegal submissions. Full PGN read. Result seq 11675; hash c5b74bd9609632708eea3f85b5104e50ad85d24001eff20c87b14273881bbfbf; snapshot 1d74d6e1b099f64af7a6226180a150ade5b4864a7a13b6bebadd5880963ff936.

Castled on 5, minors developed by 10, rook activated on 11; first 15 material-clean. Before Black castled, I rejected Bxh6/Bxh6/Qxh6 because Rh8 could then capture the queen. After castling moved that rook, 19.Bxh6 actually won the pawn; Bxg7/Kxg7 exchanged bishops equally. This local blocker recognition did not persist. 21.Qe3 put the queen on the e-file, and 22.Nd4 exd5 23.Nxd5 Bxd5 24.exd5 opened that file. I explicitly considered rook activity but omitted my own queen in the line: ...Rxe3 won it for a rook. 25.fxe3 retained a pawn defender of Nd4; Rxe3 would instead leave that knight vulnerable.

27.Nc6 attacked queen and rook, but ...Qxe3+ forced a king reply and ...Rf8 escaped. I had considered that checking interruption, so it was not an established material recovery. 29.Rce1 allowed the anticipated ...Ng3+/...Nxf1+ fork, losing another exchange before Rxf1. The d-pawn reached d6, but my own Rd7 obstructed its advance. Re7/Rxd7 did actually win Black's remaining knight. The queen checks briefly repeated; Black then broke the sequence with ...b4, so no draw occurred.

The final 41.Bxg6 correctly noticed that f7 was pinned to Kg7 by Rd7, but ignored the king itself: ...Kxg6 legally captured the undefended bishop. This is a direct recurrence of the defender/capture failure, despite the specific accurate pawn-pin note. Final White Kh2/Rd7/Nd4/a2/b2/d6/g2/h3 against Black Kg6/Qf1/Rh8/a6/b4/c4/f7. I resigned queen-versus-knight material down with one extra pawn; no forced-loss proof. No successful passed-pawn conversion or defense was completed. The errors, rather than the opening or isolated accurate pin observation, dominate this game's learning evidence.

Cumulative 52W/3D/86L in 141. MAX 0W/2D/46L in 48; skill 0 39W/1D/7L in 47; nominal 1800 13W/0D/33L in 46. Elo 1550 [1430,1670], 93 rated total/latest 50; 48 MAX excluded. Storage 40,318,387 bytes. Trial 19 currently 0W/0D/3L, 93 own moves/187 plies, zero illegal submissions. Continue unchanged fixed block through 144; 59 scored games remain to 200.


## Benchmark 142 — 2026-10-03 01:55 UTC
Black versus skill 0; win by 28...Rb1 checkmate. 28 own moves/56 plies, zero illegal submissions. Full PGN read. Result seq 11733; hash 86d96daf3a61a0b6867370b4c25f4c8939b3421b1af164898b7e0e18bef40992; snapshot b5fef939f17f3dcf88c172bb0c0994a7c79b121646a3cbdde21c011071264fc1.

Castled on 8, remaining minors developed by 9, rook activated on 10. 7...d6 blocked Qf4's added support of Nb5's c7 target. After the equal opening exchanges, 11...Nxd4 12.Qxf6 Qxf6 gave me White's queen for a knight. White then ignored ...Nxf3 and ...Nxd2, losing its remaining knight and a rook. These were major opponent errors. My 15...Qxb2+ was itself unsound: I considered other king responses but missed 16.Kxb2, which legally captured the undefended queen. The old Nd4 queen defender had long moved. The first-15 checkpoint is therefore not clean; the following reply exposes the loss. This is another direct king-capture/defender failure.

16...Nc4+ moved the knight with tempo, and 17...Re7 saved the rook attacked by Bb5. After ...c6 White left the bishop en prise; ...cxb5 actually won it. ...Nd2+ then forked king and the last rook, and ...Nxf1 won that rook. White had only pawns against both rooks, bishop and knight. I removed c4 and h6 pawns and finished an executed mating net: ...Rb4 cut off the b-file while vacating c4 opened Be6's line to a2; ...Nd2 defended b1; ...Rb1 was referee-confirmed mate. No promotion occurred. The huge opponent concessions, not a clean game or established intervention effect, explain the win. The successful final coordination does not cancel my queen loss.

Cumulative 53W/3D/86L in 142. MAX 0W/2D/46L in 48; skill 0 40W/1D/7L in 48; nominal 1800 13W/0D/33L in 46. Elo 1560 [1440,1680], 94 rated total/latest 50; 48 MAX excluded. Storage 40,665,398 bytes. Trial 19 currently 1W/0D/3L, 121 own moves/243 plies, zero illegal submissions. Complete 143–144 before assessment; 58 scored games remain.


## Benchmark 143 — 2026-10-03 02:14 UTC
White versus nominal 1800; loss by resignation after 69...Nxa7+. 69 own moves/138 plies, zero illegal submissions. Full PGN read. Result seq 11873; hash f5cf35c2998b20ed831de59e880c45b52741bec20a28d8f55a6181db599dc05c; snapshot 30d86c113ff7a50c55a6dabf3dd604906eda374b0202c5dac05b6f9538ded9c2.

Castled on 5, minors developed by 10, rook activated on 13; first 15 material-clean. The queen exchange Qd2/Qxd2/Nxd2 was equal and defended b2 while completing development. cxb6/Nxb6/Nc5 preserved a4 with the knight; Rb3 met the opened b-file. After ...Nb4, Bd1 saved the bishop. Ke3 defended d4 but allowed checking knight threats. I moved Rb3 to c3 specifically to avoid ...Nbd5+ opening the b-file against it; the other knight instead played 30...Nfd5+, forking Ke3 and Rc3. Ke4/Nxc3+/bxc3 left an exchange deficit. Addressing one line while overlooking a different forcing reply directly repeated the older failure.

The subsequent pawn and minor-piece structure held temporarily. c4/Bb3 retained the central pawns, Re3 added a bishop defender, and Black declined a repeated setup with ...Na8. I recognized that ...Nxd4 could be protected by Rd8 and fork Rf3/Bb3, so Rf2 removed the rook from that fork; Black chose ...gxh4, answered legally by gxh4. Rh2 protected h4. These local avoided losses did not recover the exchange. Once the black rook left the d-file, d5/cxd5/cxd5 opened the bishop's diagonal. Black's doubled b-file rooks forced Bc4. Rb3/Rxb3/Nxb3 traded rooks equally, choosing the knight recapture to retain Bc4's support of d5. ...exd5+/Bxd5 was then completed; no pawn was lost in that exchange.

...Ng3+/...f6+ pushed the king to d4, where Bd5 was pinned on the d-file. ...Kd6 added a king attacker to the rook attack. I could not find a way to preserve the bishop, but this was my own assessment, not a proof. Nxa5 did win a pawn. Black used ...Ne2+/...Rc8+; Bc6/Rxc6+/Nxc6/Kxc6 then actually exchanged both remaining white minor pieces for the black rook. The result was king and three pawns against king, knight and two pawns. The king on d6 made the final recapture legal; I had anticipated that last capture before Bc6.

I advanced f5 and escorted the outside a-pawn with Kb5/Ka6/Ka7. Black's king blocked the b-file route. The pawn reached a7 with Ka8 support, but my king was confined and the kingside pawns were frozen. ...Nd4/...Nc6+ forced the king away; 69.Kc8 Nxa7+ actually removed the passer. Final White Kc8/f5/h4 against Black Kb6/Na7/f6/h5, knight down with equal pawn counts. I resigned practically; legal continuations remained, and no engine/tablebase or forced-loss certificate was used. This is direct ending evidence: temporary coordination and a far-advanced passer did not yield a hold, and the enemy king/knight stopped it. No promotion or successful defense occurred.

Cumulative 53W/3D/87L in 143. MAX 0W/2D/46L in 48; skill 0 40W/1D/7L in 48; nominal 1800 13W/0D/34L in 47. Elo 1550 [1430,1670], 95 rated total/latest 50; 48 MAX excluded. Storage 41,117,580 bytes. Trial 19 through 143: 1W/0D/4L, 190 own moves/381 plies, zero illegal submissions. Finish 144 before assessment; 57 scored games remain.


## Benchmark 144 — 2026-10-03 02:35 UTC
Black versus nominal 1800; loss by resignation after 49.Qxd8+. 48 own moves/97 plies, zero illegal submissions. Full PGN read. Result seq 11972; hash a80252d89531a66328f00a2c663714ac2cdfe6fc2b46baadae736c86c57438a7; snapshot 71b0fda72222dd5afc18ec8720f64ea6ea96cb02657efb6e3d8e93d7b25cb400.

Castled on 6, minor development complete on 8, rooks activated on 10 and 14; first 15 material-clean. ...c4/...cxb3 gained a pawn temporarily. When Nce1 opened the c-file against Qc7, Qb6 moved the queen and defended the passer; ...Nc5 added support. White accumulated attacks with Nd4 and Qd1. I recognized that ...b2 could be met by captures involving the rook, bishop and queen, and did not claim the passer was safely promotable. After ...Bd6, Nxb3/Nxb3 returned the pawn and exchanged a knight; Bxf6 then captured my other knight and attacked Rd8.

25...Nxa1 was chosen around the legal imagined line Bxd8/Rxd8/Rxa1. Actual 26.Rxb6 instead captured my queen: moving Nb3 vacated the b-file between Rb1 and Qb6. I overlooked that direct capture while considering the bishop's alternative. This is the same changed-blocker failure as 139 and 141. ...gxf6 took the bishop, while Rxb7 won another pawn. The queen loss was not erased. Be5 protected the confined Na1; ...Bc3 attacked rook and knight. The actual ...Bxe1/Qxe1/...Nc2 exchange opened the c-file and let the knight escape under rook protection. ...Nxa3 won a pawn, then ...Nc2/...Nb4 preserved the knight with rook attacks and briefly defended a6. When Qe1 attacked Nb4, ...Nc6 avoided that capture, but Rxa6 lost the pawn.

I recognized that g4 and d3 restricted Bg6. ...Kg7 vacated h7 before f5, and ...Bh7 actually saved the bishop. This is local mobility evidence, not a solved position. ...d4 and ...Ne5 made the knight active, while the bishop stayed restricted. After Qh4 I rejected ...Rxe2 because Qxf6+ would fork king and Rd8. ...Rc1+/...Rd7 removed that particular rook target, but Qxf6+/...Kg8/Ra8+ still drove the king onto the back rank. ...Rc8/Rxc8+/...Rd8 lost both rooks. I expected Rxd8 mate, but White actually chose Qxd8+, leaving a legal king continuation (g7 now no longer controlled by Qf6). The referee remained active; the attempted completed-PGN read at that moment failed because there was no completed file yet. I corrected the outcome description and resigned. No checkmate claim, no illegal submission, and no external analysis occurred.

Final Black Kg8/Bh7/Ne5/d4/f7/h6 against White Kg2/Qd8/Rc8/Be2/d3/e4/f5/g4/h2. Resignation was a practical material decision, not a forced-mate certificate. The b-passer was returned, the knight escape and bishop retreat were executed, but the queen capture and later king attack decided the game. No successful conversion or defensive hold.

Cumulative 53W/3D/88L in 144. MAX 0W/2D/46L, skill 0 40W/1D/7L, nominal 1800 13W/0D/35L, each 48 scored games. Elo 1540 [1420,1660], 96 rated total/latest 50; 48 MAX excluded. Storage 41,545,300 bytes. Fifty-six scored games remain to the 200-game endpoint.

## Trial 19 endpoint — fixed 139–144 block
Result 1W/0D/5L, 238 own moves/478 plies, zero illegal submissions. MAX 0/2, skill 0 1/2, nominal 1800 0/2; White 0W/3L, Black 1W/2L. Four first-15 checkpoints were material-clean; 140 and 142 were not, including the next reply completing the loss. Baseline after 138 was 1560 [1440,1680], now 1540 [1420,1660]. The intervals overlap widely; the point estimate fell, and neither outcomes nor error recurrence demonstrate improvement.

The remembered mechanical checks matched predictions, but that was retention of supplied lines. Fresh composed practice produced one unfinished pawn-down position and one draw after three pawn losses and opponent errors. In benchmarks, 140 restricted its knight and then trapped its queen; 143 advanced a passer to a7 but lost it to the opposing king/knight; 144 had a temporary b-passer, a real knight escape and a real bishop retreat, but still lost. No complete successful passer defense or conversion validates the method. Older failures were decisive throughout: opened-line captures (139, 141, 144), omitted king captures (141, 142), a knight fork while solving a different threat (143), and king confinement (144). The only win depended on large skill-0 concessions and itself included my queen blunder.

Decision: discontinue trial 19 as an effective intervention. The next bounded trial will reduce the practice material to queens and rooks to work directly on changed lines and the next forcing capture, with explicit acknowledgement that prior reconstruction and king-safety trials also failed. No new larger checklist or claim that easier drills establish strength. Preserve the fixed rotation and evaluate the entire next block, 145–150. No valid new cumulative token counter is available.


# Trial 20 — queen-and-rook lines in sparse positions

Declared 2026-10-03 02:38 UTC after benchmark 144. Baseline 1540 [1420,1660], 53W/3D/88L in 144; 96 rated total/latest 50, 48 MAX excluded. Next fixed benchmark endpoint: games 145–150. The overall run stops at 200 scored games, with no strength prerequisite.

Trial 19 failed: 1W/0D/5L, repeated opened-line queen/rook losses and missed king captures. Earlier trials 02 (reconstruction), 04 (vacated lines), 11/14 (king captures/defenders), and 18 (forcing king safety) also failed to establish sustained transfer. This is not a new rule, a larger checklist, or a claim that another correct remembered answer constitutes improvement. Change the practice task: remove bishops and knights and work with queens, rooks, kings and three pawns per side, so the actual line-changing captures are the main practical problem.

Bounded learning: mechanically check the six prewritten remembered/contrast branches below, then exactly two new self-composed nominal-1800 practices, White then Black. Each ends naturally or explicitly unfinished after at most 16 own moves and the final opponent reply. Combined study/setup/practice/review ceiling: 2026-10-03 03:18:13 UTC. No repeats, replacement positions or extensions to improve the record. If the ceiling arrives, stop an active practice and record omitted work. A composed position is not objectively certified equal or an independent blind test; its intended mechanism is known, with fresh replies supplied by the opponent.

Remembered/contrast predictions (all moves below predicted legal; checks noted):
1. Game 141 after ply 47 (24.exd5): e8e3, f2e3. The first move takes the queen through the vacated e-file. The pawn recapture does not undo that loss.
2. Game 141 after ply 81 (41.Bxg6): g7g6. The king itself can capture, despite the separately correct f7-pin observation.
3. Game 142 after ply 30 (15...Qxb2+): c1b2. The king can take the undefended queen; a checking move is not automatically safe.
4. Game 143 after ply 59 (30.Rc3): f6d5, e3e4, d5c3, b2c3. Both black knight moves give check; this is the actual fork, not the different knight route I had focused on.
5. Game 144 after ply 49 (25.Bxf6), actual branch: b3a1, b1b6, g7f6. The knight's departure opens Rb1's capture of Qb6.
6. Same 144 position, my imagined cooperative branch: b3a1, f6d8, e8d8, b1a1. Its legality would not make it the opponent's best or actual reply. Compare it with branch 5, without a search or evaluation claim.

Practice A, White, FEN `2r3k1/5p1p/pq6/8/8/P7/3Q1P1P/4R1K1 w - - 0 1`: White Kg1/Qd2/Re1/a3/f2/h2; Black Kg8/Qb6/Rc8/a6/f7/h7.
Practice B, Black, FEN `2r3k1/pq3p2/7p/8/8/4Q2P/P4P2/3R2K1 b - - 0 1`: Black Kg8/Qb7/Rc8/a7/f7/h6; White Kg1/Qe3/Rd1/a2/f2/h3. Different placement, not a color-swapped replay of A.

Working focus: restart the short capture line from each actual referee reply. After a blocker leaves, consider the king and the opposing heavy pieces as possible capturers, including a forcing check that interrupts the intended recapture. A supplied alternative branch stays hypothetical until played. Use ordinary development in benchmarks; no special queen-exchange preference, timing target or mandatory expanded move checklist.

Assessment: preserve every actual major-piece loss, king capture, checking interruption, legal recapture, confined piece and unresolved attack. A capped practice stays unfinished; a legal remembered branch measures retention only. Judge the entire 145–150 block and interval at its fixed endpoint, including unrelated errors. A sparse-practice success alone cannot establish broader learning. All moves are my own; no agents, engine analysis, automated search, scoring, attack maps or move menus.


## Trial 20 supplied-branch study result
Six remembered/controlled branches, 15 supplied plies: all starting boards valid and all 15 legality predictions matched. Both specified checking knight moves in 143 were confirmed. The actual Rxb6 branch and my imagined Bxd8 branch in 144 are both legal; that does not make the imagined reply a sufficient account of the position. The output establishes only the supplied geometry, without search, evaluation, attack enumeration or a best-move claim. Files heavy-lines-20-inputs.json, heavy-lines-20-verify.py and heavy-lines-20-legality.json preserve the exact scope. No fresh-solution accuracy or improvement is inferred. Proceed to the two predeclared compositions, without adding cases.


## Practice 35 — fresh composition A, checkmated
Natural loss by checkmate at 2026-10-03 02:42:31 UTC, 6 own moves/12 plies, zero illegal submissions. Seq 1107; hash 3cf8dc1f49e741091db1913ff920d5955643c8150fe190bf3392119a86fcbd4f. Full referee PGN read. Actual line: 1.Rc1 Re8 2.Qd7 Re6 3.Qc8+ Kg7 4.h3 Rg6+ 5.Kh2 Qxf2+ 6.Kh1 Qg2#.

Rc1 was supported by Qd2 for a possible rook exchange; Black instead moved its rook. Qd7/Qc8+ advanced the queen, with Rc1 supporting c8. I rejected an imagined Qd8+ because Qb6 could capture along c7/d8, but that local caution did not prevent the actual failure. Moving Qd2 had removed the queen's protection of f2. I treated h3 as a useful flight-square move, then met ...Rg6+ with Kh2. The king had also stopped protecting f2, and ...Qxf2+ actually won that pawn with check. Kh1 followed; I considered a later ...Qf3+ but omitted the immediate ...Qg2 mate, protected by Rg6. The king could not capture the queen through the rook's g-file protection.

No major piece was directly blundered, but queen/rook coordination and king safety failed in a sparse new position. The composition was not independently evaluated as equal or drawable; no best-move or forced-loss claim about the starting position. This loss is direct adverse practice evidence, not a reason to repeat or replace the example. Proceed only to predeclared composition B; the 16-move cap was not a minimum.


## Practice 36 — fresh composition B, unfinished
Stopped at the declared 16-own-move/32-ply cap on 2026-10-03 02:52:17 UTC, with the last opponent reply included. One illegal submission. Result *, not a win or draw. Seq 1143; hash 1aaeb7fafd14f913b11a2cad5a5512485e29ac07e89f48d2d629df34253cb361. Full referee PGN read. Actual line: 1...Qc6 2.Qd3 Qf6 3.a4 Rc3 4.Qd5 Rxh3 5.Qg2+ Qg6 6.Qxg6+ fxg6 7.Rd4 Kf7 8.Rd6 Ke7 9.Ra6 Kf7 10.Rxa7+ Kf6 11.a5 Ra3 12.Ra6+ Kg5 13.Rc6 Rxa5 14.Rb6 h5 15.Rb3 h4 16.Rf3 Kg4 17.Rf8.

After Qc6/Qd3 I submitted c8c3 while my own queen still occupied c6. The referee rejected it as the first illegal attempt on that turn; the position was unchanged. I then played Qf6, and after a4 the c-file was actually clear, so ...Rc3 was legal and supported by Qf6's diagonal. This is direct blocker-tracking failure even with few pieces, not merely a missed optimal move.

...Rxh3 won a pawn, but I had not anticipated Qg2+ checking the king and attacking the rook. I selected ...Qg6 as an interposition and exchange offer, initially thinking Qxh3 remained an option. After the actual Qxg6+/fxg6 exchange, my own review recognized the g-file pin: Qg6 also pinned Qg2 to Kg1, so moving that queen off the file to h3 would expose its king. That full defensive mechanism was not foreseen in my choice. No extra mechanical branch or best-line analysis was added. The actual exchange preserved the rook and pawn gain; calling it an immediate rook loss or crediting a fully calculated pin would both be inaccurate.

Kf7/Ke7 approached the rook but left a7 undefended and removed g6's king defender. After Ra6 I returned to f7 to cover g6, and Rxa7+ returned the pawn count to equality. In the rook ending, ...Ra3 went behind White's a-passer. White Rc6 later removed its rook's protection of a5, allowing the actual ...Rxa5 capture. This removed the passer and restored a one-pawn advantage; it was an available opponent concession, not a proved forced stop. ...h5/...h4 advanced with king/pawn support, and ...Kg4 attacked Rf3; White chose Rf8 on the final reply.

Final Black Kg4/Ra5/g6/h4 versus White Kg1/Rf8/f2. One pawn up, but no promotion, conversion or established theoretical result. No extension or replacement practice was added.

## Trial 20 practice endpoint
All six remembered/controlled branches (15 supplied plies) matched legality predictions. The two fresh compositions then finished by 02:52:17, before the 03:18:13 ceiling. Combined 22 own moves/44 plies, one illegal submission: a six-move mating loss, and an unfinished rook ending one pawn up after losing the initial extra pawn and later capturing an abandoned passer. The illegal rook move and missed mating mechanism are adverse evidence; the queen exchange and later pawn capture are local executed outcomes with the limitations above. Sparse practice has not established improvement or resolved the old failures.

Return now to the predeclared fixed benchmark block 145–150. Baseline remains 1540 [1420,1660], 53W/3D/88L in 144; practice is excluded. Preserve rotation, settings, estimator and every record. Carry the actual-position capture focus as an unproved experiment and assess the complete block, including all recurrences. No new valid cumulative token counter is available. All decisions were my own; only the referee was used during active practice.


## Benchmark 145 — White versus MAX, loss
Resigned after 32...Rxh2+ at 2026-10-03 03:08:37 UTC: 32 own moves/64 plies, zero illegal submissions. Seq 12038; hash 5c9c23d09885370573a0e839146366580988b5f0551f1272fd76b0ce93c94fd3. Full referee PGN read. Cumulative 53W/3D/89L in 145; MAX 0W/2D/47L. Elo unchanged 1540 [1420,1660], with 96 rated total/latest 50 and 49 MAX excluded.

Castled on move 5, minor development complete by 9, first rook move 15; first 15 material-clean. Qxd2 and gxf3 made the actual recaptures, accepting doubled f-pawns. Qe3 defended f3 against Qf6. Bb5 pinned Nc6 while Ke8 remained, and Bxc6+/Rxc6 was an equal exchange. After c4/cxd5, ...Nxd5 attacked the queen; Qe4 moved it and retained f3 protection. I recognized that ...Kd7 removed the former e6-pawn pin, so did not rely on the old position for Qxd5.

Bc1/Bd2 let the doubled c-file rooks penetrate. Re2 defended the bishop but ...Rxa2 won a pawn. Qxf5/exf5 was an actual equal queen exchange, not a solution to the rook pressure. Re5 attacked Nd5 and f5, but ...Kd6 attacked the rook and defended the knight; I returned to e2. After ...Rcc2, Rd1 added a bishop defender but permitted the considered ...Nc3 fork of both rooks. Actual Bxc3/Rxe2 cost an exchange. Kg2 did not save f2: ...Rxf2+ was protected by the other rook, followed by ...Rg2+ and ...Rxh2+. Final White Kh3/Rd1/Bc3/b3/d4/f3 versus Black Kd6/Ra2/Rh2/a6/b7/f5/f7/g5/h6. An exchange and three pawns down; practical resignation, not a proved forced result or checkmate.

Local pin and recapture observations were correct, but confinement, double-rook pressure and the knight fork remained unresolved. Sparse heavy-piece practice did not establish transfer here. Continue the already declared 145–150 block without added study or a replacement game.


## Benchmark 146 — Black versus MAX, checkmated
Lost to 23.Qxf7# at 2026-10-03 03:13:50 UTC: 22 own moves/45 plies, zero illegal submissions. Seq 12085; hash 623ada10a32be18b1a4e7a31d126d0a75e273b2d71849e4fb6b7c0559fe46e88. Full referee PGN read. Cumulative 53W/3D/90L in 146; MAX 0W/2D/48L in 50. Elo remains 1540 [1420,1660], 96 rated total/latest 50, 50 MAX excluded.

Castled 8, developed all minors by 9, rook to e8 on 10. First 15 not material-clean: ...b4/White d5 drove Nc6 back to b8, and 15.cxb4 won the pawn. ...Nbd7 reorganized the knight but did not recover it. After ...c6, Nxd6 forked Re8/Bb7. Actual Bxd6/dxc6/Bxc6/Qxd6 traded the knight for the bishop through the opened d-file and left Black two pawns down. I anticipated Qxd6 before choosing the recapture; it was not a discovered after-the-fact queen route. ...Bxe4 recovered a pawn, then White Rxe4/Nxe4 deliberately gave a rook for a bishop; Qg6 created the king attack. I recognized the f7 pawn's bishop pin and the g7 pawn's queen pin, but that did not produce a working defense.

...Ndf6 defended Ne4. Bxh6 won another pawn. I chose ...Kf8 to leave the g-file/old g8 diagonal and considered Bxg7+ followed by a king escape. The actual reply was Qxf7 mate: Ba2 protected the queen and my king had no escape. I missed the immediate mating move and over-relied on an imagined different capture. The game ended by referee-confirmed checkmate, not resignation. This repeats the practice-35 immediate queen-mate failure and provides adverse transfer evidence. No new study is inserted; continue the fixed block with games 147–150.


## Benchmark 147 — White versus skill 0, win with three missed king captures
Won by 52.Qb7# at 2026-10-03 03:26:25 UTC: 52 own moves/103 plies, zero illegal submissions. Seq 12190; hash f8ee35ee3e444b4ff91a23f7322c0f3eb182b53513538e639d1baaeda028f275. Full referee PGN read. Cumulative 54W/3D/90L in 147; skill 0 41W/1D/7L in 49. Elo 1550 [1430,1670], 97 rated total/latest 50, 50 MAX excluded.

Castled 5, all remaining minors developed by 11, rooks activated 13/15; first 15 material-clean. Bxd3/Qxd3 and Nxe4/Qxe4 were actual equal recaptures. d5/exd5/cxd5 opened the center; Black then castled. d6 attacked the confined Be7. Actual Bxd6/Bxd6 won a bishop for a pawn, and ...Nd5 allowed Bxf8 to take a rook. ...Nf4 attacked my queen but also vacated d5, enabling Qxd8/Rxd8/Rxd8. ...Ne2+ was answered by Rxe2, removing Black's last piece. These major opponent errors created a huge advantage.

Conversion was poor, with three real unanticipated king captures. (1) Bxg7+ was a discovered rook check; I considered a king retreat and missed the direct Kxg7, losing the bishop. (2) Later ...Kd8 approached Re7. Rfxf7 correctly defended Re7 temporarily, but Rf8+ immediately removed that defender. I privately misidentified it as mate; actual Kxe7 took the rook. I did not report a completed mate in the move note and continued from the referee. (3) After bxc3/b4, I played cxb4 while Rf8 remained next to Ke7, permitting Kxf8. Both rooks and the bishop were lost to the king, despite the declared king/heavy-piece focus. Repeated correct partial observations did not prevent the failures.

The remaining knight and five pawns versus two pawns still offered a practical conversion. a4 supported b5; Black moved its king rather than capturing the pawn. Actual bxa6/Kd8/a7/Kd7/a8=Q promoted safely. Qe4/Qd5/Qd7 confined the king to a8/b8 while Nh4 blocked the final h-pawn. I then brought Kg1 via f1/e2/d3/c4/b5/c6, preserving legal king moves, and Qb7# was confirmed by the referee. This is an executed promotion and supported queen mate, but the win depended on abundant opponent concessions and does not establish learning or sound rook conversion. Continue games 148–150 as predeclared.


## Benchmark 148 — Black versus skill 0, checkmated
Lost to 50.Rc5# at 2026-10-03 03:38:54 UTC: 49 own moves/99 plies, zero illegal submissions. Seq 12291; hash afab2c94078ff0bdfe04c50d04f79b1824213d1a7f2f298f222dd31d5bc9e0cd. Full referee PGN read. Cumulative 54W/3D/91L in 148; skill 0 41W/1D/8L in 50. Elo 1540 [1420,1660], 98 rated total/latest 50, 50 MAX excluded.

Castled 8, remaining minors developed by 9, rook activated 12. First 15 not material-clean including White's completing reply: ...d4/exd4/cxd4 left the new d4 pawn unprotected and 16.Bxd4 won it. Bc5/Bxc5/Nxc5 exchanged bishops, and ...Nxd3 recovered the pawn with Rd8 support on the cleared d-file. ...Qc6 then exposed the queen to Bg2's diagonal; White Nb2 missed the capture, and I noticed the exposure and moved Qd6. The later Nxd3/Qxd3/Qxd3/Rxd3 sequence was an actual equal knight-and-queen exchange. Bxb7/Rxb3 traded pawns, and White Rfd1 left c4 available to ...Rxc4. Rc7 defended f7 against Rf8, and Ra7 defended both a6 and f7 after Bf1.

...Ng4/...Ne3 forked Rd1/Bf1; White Rd3 avoided the rook loss. I explicitly anticipated the king recapture when playing Nxf1, and actual Kxf1 made this an equal minor exchange, not a piece win. But after Re8, ...Re7 defended e6 by placing the rook directly under the enemy rook without a defender. Rxe7 simply won it. A local correct anticipated king capture did not fix direct heavy-piece safety.

The remaining rook captured a5 and the f-pawn captured g4. I advanced e5 with Ra5 protection. After Kh6/Rd8, I noticed that an immediate ...Kh5 would permit Rh8 mate; ...g5 vacated g6 first. Actual fxg5+/Kh5/Rc8 then allowed Kxh4 and Kxg5, eliminating White's remaining pawns. Kxg5 was legal because g7 still blocked Rg8's file. Kf6 defended e5/g7, Ra2 retained a6 support, and Rb6+/Kf5/Rc8 led to the final error: ...e4 kept the pawn king-protected but vacated e5, opening Rc8-c5's fifth-rank check. The actual Rc5 was mate, with Rb6 and Ke3 covering escapes and my pawns restricting my king. I was considering my own pawn/rook attack and omitted the immediate opponent mate.

Final result is a confirmed loss, despite recovering to rook plus four pawns versus two rooks. Neither the pawn recovery nor the earlier avoided h-file mating pattern establishes transfer. Direct rook loss and a vacated-line mate both recur in this reduced ending. Continue the already declared block with 149–150, then assess the complete six games.


## Benchmark 149 — White versus nominal 1800, loss
Resigned after 45...axb1=Q at 2026-10-03 03:56:24 UTC: 45 own moves/90 plies, zero illegal submissions. Seq 12383; hash c2732856e224da242274ace7f8aa08f2e80dc1c906e175d44e14a096d78b88d8. Full referee PGN read. Cumulative 54W/3D/92L in 149; nominal 1800 13W/0D/36L in 49. Elo 1530 [1410,1650], 99 rated total/latest 50, 50 MAX excluded.

Castled 5, all minors developed 7, rook activated 10; first 15 material-clean. Nh2/f4/Nf3 opened the f-pawn break. Central captures gained a temporary pawn. Qe2 supported Bc4/e4 before the rook exchange, and Rd1/Rxd1/Rxd1 was completed correctly. Bxe6/Nxe6 removed the last bishops. Rd6 was supported by Pe5, but Qb6+ followed by Qxb2 and Qxa3 turned the material balance to one pawn down; Nd1 saved the attacked knight with queen tempo without saving the a-pawn. Qd3/Qxd3/cxd3 exchanged queens. Nc4 attacked Ra5 and supported both e5 and Rd6; actual Nxf3+/gxf3/Ra8 completed the minor exchange without losing those pieces.

Rd7/b5/Nd6 put the knight on a supported square and Rxf7 recovered a pawn. f4 moved the pawn attacked by Nd4 and supported e5, but also obstructed the rook's f-file route toward the first rank. Black's a-pawn reached a2 while my pieces were far away. Nf5/Rxg7+ supplied a protected rook check, then Rg1 prepared to capture a promotion even at a rook cost. Black instead played Rg8, abandoning the a-file; I used the actual reply with Ra1 to block promotion. Nxf5/exf5 removed the last knights, and Black restored Ra8. This temporary blockade was executed, not a proved hold or forced rescue.

In the rook ending, e6 remained protected by f5 and Kg3/Kg4 defended f5 against Kf6. The b-pawn advance overloaded the blockade while Black's king stopped the central pawns. After d4/Rg8+/Kf3/b3, I chose Rb1 intending first-rank control and focused on a straight a1 promotion or a b-pawn push. I omitted the pawn's immediate diagonal capture: a2 could take the rook on b1 and promote in one move. Actual axb1=Q removed the only rook. I had mentioned the pawn's b1 attack in earlier private calculation but failed to apply it to the final destination, so this is direct failed transfer and board tracking, not missing knowledge of the rule. Final White Kf3/d4/e6/f4/f5/h3 versus Black Kf6/Qb1/Rg8/b3/c6/h6. Practical resignation after the material collapse, not mate.

Some exchanges, checking recaptures and supported placements were executed accurately; the final pawn capture and inability to handle connected passers are decisive adverse evidence. Continue only the final predeclared game 150 before the full trial assessment.


## Benchmark 150 — Black versus nominal 1800, checkmated
Lost to 31.Qxg7# at 2026-10-03 04:06:50 UTC: 30 own moves/61 plies, zero illegal submissions. Seq 12446; hash 2bc5b3bf89d2ebf287ae1a2f0984164de35db04d0730b36ce274a5c06069ea28. Full referee PGN read. Cumulative 54W/3D/93L in 150; nominal 1800 13W/0D/37L in 50. Elo 1540 [1420,1660], 100 rated total/latest 50, 50 MAX excluded. The estimate rose from 1530 after 149 despite another loss as the rolling window changed; that is not improvement from this loss.

Castled 5, all minors developed 9, rook activated 10; first 15 material-clean. ...c5/cxd5/exd5 and ...Ne4/Bxe7/Qxe7/Nxd7/Qxd7/Nxe4/dxe4 completed the central exchanges accurately. Bxd5 captured White's advanced pawn with Qd7 support. But after Bc4 I chose ...Bxc4, treating it as a bishop exchange and considering Qxc4. Moving Bd5 off the d-file exposed my own queen: White instead played Rxd7. This is exactly the vacated-blocker/imagined-recapture failure the trial targeted. Bd3 attacked White's queen and rook; after Qd2/Bxf1/Kxf1 the anticipated king recapture left two black rooks versus queen and rook, with one extra pawn.

Rfe8 defended e4 and connected the rooks. The supported c-/b-/a-pawn advances reached c2 with check, but the pawn was blocked by White Kc1. I first recognized the f7 attack and played Rf8 after Qd5. Later Qb3 preserved the same diagonal to f7. ...Rfd8 challenged Rd7 after the queen left the d-file but removed f7's defender. Actual Qxf7+/Kh8/Qxg7# completed the mating attack; after Qxf7+ I recognized the net and played the forced practical king move. Correct recognition of the threat several moves earlier did not survive the changed rook task. A passed pawn on c2 did not compensate or convert.

## Trial 20 complete assessment — benchmark 145–150
Entire predeclared block: 1W/0D/5L, 230 own moves/462 plies, zero illegal submissions. MAX 0/2, skill 0 1/2, nominal 1800 0/2; White 1W/2L, Black 0W/3L. Four of six first-15 phases were material-clean (145,147,149,150); 146 and 148 were not, including White's move-16 reply that completed 148's pawn loss. Baseline and endpoint are both 1540 [1420,1660], with a temporary 1550 after 147 and 1530 after 149. These wide, overlapping model-conditional intervals and the rolling-window behavior do not establish progress.

All six remembered/controlled branches (15 supplied plies) passed, but fresh sparse practice produced a six-move mating loss and an unfinished rook ending with one illegal rook-through-queen submission. The benchmark then included 145's knight fork and rook penetration; 146's immediate queen mate; 147's missed Kxg7/Kxe7/Kxf8 despite a win; 148's direct Rxe7 and vacated-rank mate; 149's axb1=Q capture of the rook; and 150's opened d-file queen loss and removal of f7's defender. The isolated correct recaptures, pins, pawn captures, one promotion, and final supported queen mate are real but do not generalize to the target failures. No intervention effect or sustained strength gain is claimed. Sparse queen-and-rook practice is discontinued as an effective method; choosing a narrower task next is an experiment, not evidence that it will work.

At 150 scored games: 54W/3D/93L; MAX 0W/2D/48L, skill 0 41W/1D/8L, nominal 1800 13W/0D/37L, each 50 games. Storage 44,805,635 bytes at this status. No unfinished benchmark games and no active game. The endpoint remains 200 scored games regardless of Elo; 50 remain. No new valid token counter is available.


# Trial 21 — keep the rooks safe while finishing

Declared 2026-10-03 04:09 UTC after benchmark 150. Baseline 1540 [1420,1660], 54W/3D/93L in 150; 100 rated total/latest 50, 50 MAX excluded. Next fixed benchmark endpoint: games 151–156, regardless of drill results. The entire run stops at 200 scored games.

Trial 20 failed: 1W/0D/5L with repeated direct captures and missed mates. Earlier capture, defender, rook-activity and king-safety trials also failed. Narrow this learning period to a concrete conversion skill that failed spectacularly in 147: two rooks driving back a king without handing either rook to it. This deliberately uses a large material advantage, so wins are not Elo evidence or proof of broad tactical learning. Stop treating a remembered correct line, an intended check, or a connected pair of rooks before a move as proof that the resulting position is safe.

Own study principle to test: the checking rook's move can remove the other rook's only defender. Before the next checking move, use the resulting position to see whether the opposing king can capture either rook. A king near one rook may require relocating that rook along the protected rank before giving the next check with the other. Bring the king up when needed. This is a short practical task, not a new mandatory checklist, timing target or externally supplied solution.

Bounded learning: check exactly seven prewritten remembered/controlled branches below, plus validity of two self-composed drill setups. Then exactly two fresh maximum-strength opponent practices, White and Black, each ending naturally or stopped after 18 own moves with the final opponent reply included. Combined setup/study/practice/review deadline: 2026-10-03 04:34:29 UTC. No repetitions, replacements or extensions to improve the record. Starting material and intended mechanism are known; these are not blind positions or independently evaluated starting positions.

Supplied branches, predicted legal throughout (17 total supplied plies):
1. 147 after ply 47 (24.Bxg7+): g8g7. The king captures the checking bishop.
2. 147 after ply 68 (34...c3): f7f8, d8e7. The check removes Re7's defender and the king captures it.
3. Same 147 start, a controlled alternative, not a forced/best line: e7a7, d8e8, f7h7, e8f8, a7a8. Relocate both rooks away from the king before the final checking move. I expect the final move to give check; this supplied route does not predict the opponent's actual choices.
4. 149 after ply 89 (45.Rb1): a2b1q. The pawn captures diagonally and promotes.
5. 150 after ply 35 (18.Bc4): d5c4, d1d7. Vacating d5 exposes the queen on d7.
6. 150 after ply 57 (29.Kc1): f8d8, b3f7, g8h8, f7g7. Removing f7's defender allows the actual queen attack.
7. 148 after ply 97 (49.Rc8): e5e4, c8c5. Moving e5 opens the fifth-rank check.

Fresh composition A, White: `8/1p4p1/4k3/8/R6R/8/8/6K1 w - - 0 1` (Kg1/Ra4/Rh4 versus Ke6/b7/g7).
Fresh composition B, Black: `7k/8/8/1r3r2/8/2K5/P5P1/8 b - - 0 1` (Kh8/Rb5/Rf5 versus Kc3/a2/g2). Different placements, not a color-swapped replay. The opponent may find captures or evasions I missed.

Practice observation: finish without losing a rook, avoid illegal submissions, and distinguish a check from an actual referee-confirmed mate. A capped drill is unfinished, never an assumed win. For transfer, record every direct capture, loss of a defender, mating error and promotion oversight in the entire 151–156 block, including losses outside this narrow focus. Preserve ordinary development and all measurement settings. Stop or revise the method at the fixed assessment point if failures continue. All moves remain my own; no agents, engine analysis, automated search, scoring, attack maps or move menus.


## Trial 21 supplied study result
Seven remembered/controlled branches, 17 supplied plies: every legality prediction matched, and the specified final/checking moves gave check. Both new composition boards passed validity checks. The output labels nine records as branches because it includes two setup-only records; there are seven move branches and two setups, not nine tactical tests. No move generation/menu, attack-map enumeration, search, scoring, engine analysis or best-move claim was used. The alternative rook route is a legal controlled example with stipulated king replies, not an independently solved fresh position or a forced line. No mate search was performed by the script; actual recorded benchmark mates retain their referee results. Proceed to the two declared practices without adding cases.


## Practice 37 — composition A, converted with both rooks intact
Referee-confirmed 11.Rd1# at 2026-10-03 04:15:05 UTC: 11 own moves/21 plies, zero illegal submissions. Seq 1166; hash 84d4f9cc2c27c7838c976e4ccec4cb7a9abbd16edd3102ac1499fc23a7b6f843. Full practice PGN read. Actual line: 1.Rh5 g6 2.Rh7 b6 3.Ra6 Kd5 4.Rxb6 Kc5 5.Rxg6 Kd5 6.Rh5+ Kd4 7.Rg4+ Kd3 8.Rh3+ Kc2 9.Rg2+ Kc1 10.Rd3 Kb1 11.Rd1#.

The fresh replies mattered: ...g6 attacked Rh5, so I moved it; I also rejected Ra6+ while the pawn still stood on b7 because b7xa6 would capture that rook. After ...b6, Ra6 no longer lay on that pawn's capture square. Rxb6 was safe from Kd5; the actual ...Kc5 then approached the rook, and Rxg6 both moved it away and removed the other pawn. Successive rook checks drove the king down the board while the other rook blocked the higher rank, with both rooks beyond immediate king capture. At the first rank, my own Kg1 would block an imagined Rh1 check, so I used Rd3/Kb1/Rd1# instead. Both rooks survived.

This is a successful execution of the narrow, known-advantage task against fresh maximum-strength replies, not a benchmark win or independent strength gain. No extra practice is added after success; proceed to predeclared composition B.


## Practice 38 — composition B, both rooks lost
Resigned at 2026-10-03 04:18:05 UTC after 6.Kxb2: 5 own moves/10 plies, zero illegal submissions. Seq 1178; hash a0c27a06daae8d1b81a6c23c1e4b03e0e3c43066667a7a2f784bd02b2893fec3. Full practice PGN read. Actual line: 1...Rf4 2.Kd3 Rb3+ 3.axb3 Rg4 4.Kc3 Rxg2 5.b4 Rb2 6.Kxb2.

...Rb3+ considered the king on d3 but omitted the a2 pawn's capture on b3. I even considered a straight a-pawn move as a possible response without considering axb3; the actual capture removed the first rook. After ...Rg4/...Rxg2 captured the g-pawn, I chose ...Rb2 to go behind the remaining b-pawn and reasoned about the b-file's restrictions. I omitted Kc3xb2, a direct diagonal king capture of the second rook. Final Black Kh8 versus White Kb2/b4; practical resignation, not a proved starting-position or theoretical result. No replacement or extension was added. The 18-move cap was a maximum, not a requirement to play on after resignation.

## Trial 21 practice endpoint
Completed by 04:18:05, before the 04:34:29 ceiling. Seven remembered/controlled branches (17 supplied plies) matched predictions; both composition setups were valid. Fresh practices combined 16 own moves/31 plies, zero illegal submissions: an 11-move two-rook checkmate with both rooks preserved, followed by a five-move practical resignation after both rooks were captured. The second case repeats both pawn-destination and king-destination failures despite the first success and exact remembered examples. This does not establish improvement or reliable mastery even of the narrow task.

Return to the predeclared 151–156 fixed benchmark block now, without another drill or added mechanical case. Keep the short resulting-position focus as unproved and preserve every recurrence. Baseline remains 1540 [1420,1660], 54W/3D/93L after 150; practices do not affect it. The overall endpoint is 200 scored games regardless of Elo. No new valid token counter is available.


## Benchmark 151 — White MAX, loss
Resigned after 26...Kh7 at 2026-10-03 04:31:04 UTC: 26 own moves/52 plies, zero illegal submissions. Seq 12500; result hash 61b64f52ff93fa646b79f9bed5ef8ee9c510c7d9ec34697314ffcbf78dbdf928. Full PGN and trimmed status read. Cumulative 54W/3D/94L in 151; MAX 0W/2D/49L. Elo unchanged 1540 [1420,1660], 100 rated total/latest 50; 51 MAX excluded.

Castled move 5; remaining minors developed by 13, rooks activated 16/18. First 15 were not clean. After ...Bxf3/Qxf3 removed the knight that had defended d4, 8.exd4 Nxd4 lost the central pawn. More decisively, 10.Nc3 allowed ...d4 to fork Qe3/Nc3; Qg3/dxc3/bxc3 left me a knight down. ...Nh5 subsequently attacked Qg3/Bf4; Qg4 defended the bishop while escaping, and Black did not capture it. Later Qf3 correctly moved off the e-file before possible central exchanges. The c5 advance nevertheless lost a pawn to ...Rd5/...Rxc5. Bb3 kept the queen's horizontal defense of Bc3 open, and Bxa5/Rxa5 was an anticipated equal minor exchange. Final White Q/2R/B/5P versus Black Q/2R/B/N/6P, with no concrete compensating attack found. Practical resignation, not a mate or proof that the final position is theoretically lost. Neither rook was directly lost here, but the opening fork and pawn losses are adverse whole-game evidence; the narrow rook practice did not prevent them. Continue the declared block with 152.


## Benchmark 152 — Black MAX, loss
Resigned after 29.Ng3 at 2026-10-03 04:37:13 UTC: 28 own moves/57 plies, zero illegal submissions. Seq 12559; hash 6835da20a0972a0e8260b08e6cf6ad2ed3db0fc1b0bad6284c3cd1dd457f8083. Full PGN/status read. Cumulative 54W/3D/95L in 152; MAX 0W/2D/50L. Elo stays 1540 [1420,1660], 100 rated total/latest 50, 52 MAX excluded.

Castled 8, minors developed 9, rook activated 10. First 15 not clean when including White's 16th reply: 15...c4 16.b4 trapped Na5 because c4 and b7 were occupied by my pieces and c6 was attacked by d5. ...Nb3 axb3 cxb3 Bxb3 Qxc3 recovered two white pawns while losing my knight and c-pawn: a knight for one net pawn. The queen's apparent attacks on both rooks did not win material; Bd2 attacked her and connected the first-rank defense. ...a5 bxa5 lost another pawn: I correctly rejected ...Rxa5 when I noticed Bd2 protected a5. ...Bg7 defended Nf6; ...Nxg4 hxg4 was an anticipated equal knight exchange. The ...f5/gxf5/gxf5/exf5 break then left another pawn deficit. I initially imagined ...Qxf5 but rejected it before submission because Qf3 could take the undefended queen; moving Re8-f8 instead did not restore material. Final White Q/2R/2B/N/5P versus Black Q/2R/2B/4P. Practical resignation, not a theoretical result. No rook was lost directly, but confinement, pawn transactions and an initially mistaken recapture idea remain failures beyond the narrow study. Continue 153–156 as declared.


## Benchmark 153 — White skill 0, loss
Resigned after 37...Bxe3 at 2026-10-03 04:48:25 UTC: 37 own moves/74 plies, zero illegal submissions. Seq 12635; hash 40d9f80c61221030b2967d0bf27e6f9993ef10370c937b1dcd82ad340fdcfac7. Full PGN/status read. Cumulative 54W/3D/96L; skill 0 41W/1D/9L in 51. Elo 1530 [1410,1650], 101 rated total/latest 50, 52 MAX excluded.

Castled 5, minors developed 12, rook activated 15; first 15 clean, including the anticipated ...Nxe3/fxe3 exchange. Local correct applications: Qc2 protected b2 before Be3; e5 cleared the queen's diagonal so Bxh7 was protected, and after ...f5 the en-passant capture restored that protection. Bd3 returned before Ne4 could block its defender. After ...cxd4 opened Rc8 against Qc2, I moved the queen rather than blindly taking Rf6. Qxb5 was protected by Bd3; after ...Bxe4 I exchanged queens first (Qxb6/Nxb6) before Bxe4, avoiding removal of my queen's defender. These are actual local successes, not general mastery.

The endgame still failed. ...Nxb2 forked Rd1/Bd3; Rd2 saved the rook while retaining bishop defense, but later ...Bc3 attacked that overloaded rook. Before that, 30.Ng4 removed d4's defender and allowed ...Bxd4+. I chose Rxb2/axb2 as an anticipated exchange concession, then Bb1 blockaded the passer. The king reached e4 and attacked Bd4 successfully, but 37.Ne3—intended to route toward c2—walked onto Ba7's diagonal. ...Bxe3 captured the knight, protected by Ra3 along the third rank, so Kxe3 was unavailable. I had explicitly noticed both that bishop diagonal and rook rank earlier, then failed to apply them to the candidate. Final White B/3P versus Black R/B/3P. Practical resignation. A rook exchange loss, defender-removal pawn loss and direct knight capture outweigh the earlier correct line checks; the trial has not transferred reliably. Continue 154–156 without added study.


## Benchmark 154 — Black skill 0, win
Referee-confirmed 26...Rh1# at 2026-10-03 04:58:05 UTC: 26 own moves/52 plies, zero illegal submissions. Seq 12689; hash 72663665c67738d183a33231d06b586e16e2d7d7caa5c890e6f61c219e1f8dde. Full PGN/status read. Cumulative 55W/3D/96L in 154; skill 0 42W/1D/9L in 52. Elo 1510 [1390,1640], 102 rated total/latest 50, 52 MAX excluded. It fell from 1530 despite this win as the rolling rated window changed; do not infer deterioration from this one game's update alone.

First 15 clean by the no-material-oversight criterion. No castling: ...Kxf7 captured an undefended knight after ...Nxd5 had removed its bishop defender, then ...Kg8 answered Qf3+. Remaining minors developed by 11 and ...Rf8 activated a rook on 14. White's 12.Qg5 simply left its queen capturable by Qd8; this major opponent error chiefly explains the advantage, not demonstrated strength improvement. ...Be6 interrupted Qb3's diagonal and supported d5; ...Nf4 protected Be6 after leaving that diagonal, and ...Bd6 defended Nf4. When Nf3 also uncovered Bc1 against Qg5, I moved the queen rather than taking the knight and allowing Bxg5. Later apparent Qxg5 captures remained rejected because Bc1 protected Ng5. Pawn attacks were met by queen retreats.

The final attack was executed without a major material loss: ...Bxe5 was protected by Nc6; ...Bd5 escaped b3 and supported f3; ...Nf3+/Nxf3/Rxf3 was anticipated. ...Rxh3 threatened the first rank. White's Re4 then blocked Bd5's protection of h1; I noticed that immediate ...Rh1+ would permit Kxh1, and played ...Bxe4 first. After Bf4, ...Rh1# was protected by Be4 and confirmed by the referee. Both rooks survived. This is a concrete successful defender/king-capture application in a game dominated by opponent blunders, contrasted with the failures in 151–153. It does not by itself establish improvement. Continue 155–156, then assess the full declared block.


## Benchmark 155 — White nominal 1800, loss
Resigned after 50...Rxa7 at 2026-10-03 05:20:22 UTC: 50 own moves/100 plies, zero illegal submissions. Seq 12791; hash d9841217f6872e2b53243c39c8b081a90eee739b26af2696c89aa23bd36a1e6b. Full PGN/status read. Cumulative 55W/3D/97L; nominal 1800 13W/0D/38L in 51. Elo 1500 [1380,1630], 103 rated total/latest 50, 52 MAX excluded.

Castled 5, minors developed 9, rooks activated 10/16; first 15 clean. Central captures ...Nxe4/Nxe4/dxe4/Bxe4 were anticipated. bxa4 was protected by Qd1's opened diagonal. After dxc6/Qxa4/Qxa4/Rxa4, I recognized that Bd3 had lost its queen defender and moved it to e2. Be5/c7 created a supported passer, but Rc8 blocked it. I correctly rejected immediate Rd8+ as a clean promotion win because Rc8 and Be7 both defended d8. Bd6/Bxd6/Rxd6 removed a bishop but also the passer's defender; ...Rxc7 took that pawn as anticipated. Rxb6 recovered a pawn.

The major failure was 27.Rxa6: I expected ...Rxe2 as an exchange of bishops, but overlooked ...Rxa6 from a2 along the entirely open a-file. I had incorrectly treated moving that rook from a5 to a2 as abandoning the bishop's defense, although it remained on the same file. This lost the exchange. The second c-pawn reached c7 with rook/knight support after king activation and checks, but the blockade ultimately captured it too. The attempted checking repetition was broken by ...Rd7, so no draw occurred. Later Ra7 depended on Nb5. ...Nc3+ forked my king, bishop and knight; Nxc3 answered it but removed Ra7's defender. ...f5+/Ke5/...Rxa7 then removed the last rook. Final White Ke5/Ba4/Nc3/f2/g2/h2 versus Black Kf8/Ra7/Rd8/e6/f5/g7/h5. Practical resignation with two minors against two rooks and a pawn deficit, not a theoretical proof. Both rooks were lost through failed defender/line accounting. Active play and some correctly handled captures did not preserve the advantage or prevent the targeted failures. Continue 156 before the fixed assessment.


## Benchmark 156 — Black nominal 1800, loss
Referee-confirmed 42.Re4# at 2026-10-03 05:44:05 UTC: 41 own moves/83 plies, zero illegal submissions. Seq 12876; hash 3dfb35aa77bc0a74ea28a39f4e5ea36797b72bdae8bc917d0ff6bac9eed87a1f. Full PGN/status read. Cumulative 55W/3D/98L in 156; nominal 1800 13W/0D/39L in 52. Elo 1500 [1370,1620], 104 rated total/latest 50, 52 MAX excluded.

Castled 6, remaining minors developed 9, rook activated 10; first 15 clean. ...Nxb6/axb6 and ...Nd4/Nxd4/exd4 were anticipated exchanges. The Nf8-g6 route was meant to avoid a bishop trap after f5 by clearing d7, but 17...Ng6 allowed 18.f5 to fork Be6/Ng6. I had considered the bishop retreat and overlooked the simultaneous attack on the knight. ...Bxc4/dxc4/Ne5 conceded a bishop for a pawn. The supported d-pawn reached d3, and the queen repeatedly escaped pawn/bishop attacks without restoring material.

A second major failure: ...Re6 and ...Qf5 were intended to protect Ne5, Re6 and d3. 33.Bxe5 also uncovered Rf1 against Qf5. The imagined ...dxe5 recapture would have allowed Rxf5; I caught that only after the knight had been captured, and chose ...Qxg5 to save the queen and obtain a pawn. This left both enemy bishops against no minor piece. ...Qxf6/Qxf6/Rxf6 correctly traded queens and removed the advanced pawn, then ...Rxf1+/Kxf1 traded the attacked rook. Black had seven pawns against four but White retained two extra bishops. King activation reached f5/e5; I correctly recognized that Be4 temporarily blocked Re1 when choosing ...Ke5, but Bxh7+ reopened the file and took h7. ...Kd4 defended d3 yet allowed Re4#, protected by Bh7. I considered a possible bishop check in the final position and missed the actual supported rook mate. Final R/6P versus R/2B/4P was checkmate, not merely a material evaluation. No repetition draw occurred. The final supported-rook pattern is especially adverse next to my correctly executed ...Rh1# in 154.

## Trial 21 fixed benchmark assessment — complete after 156
Games 151–156: 1W/0D/5L, 208 own moves/418 plies, zero illegal submissions. MAX 0/2, skill 0 1/2, nominal 1800 0/2. White 0W/3L; Black 1W/2L. First 15 clean in four of six (153–156); 151–152 failed. Baseline 1540 [1420,1660] after 150 -> 1500 [1370,1620] after 156, with intervening 1530/1510/1500 updates. These overlapping, model-conditional intervals do not establish an exact strength decrease, but there is no measured improvement. Rated total 104/latest 50; 52 MAX excluded. Cumulative 55W/3D/98L.

The seven remembered/controlled branches passed and practice 37 converted a known two-rook advantage, but practice 38 lost both rooks. Benchmark 154 executed a supported rook mate cleanly after huge opponent errors. Against that, 153 conceded a rook exchange and then a knight to a known bishop/rook line; 155 lost both rooks through line/defender failures; 156 lost two minor pieces to a pawn fork and an opened queen file, then missed a supported rook mate. 151–152 added opening pawn-fork and confinement failures. The narrow finishing method is not reliable, and its local successes do not establish transfer. Retire the two-rook-versus-king compositions as the next practice method. Choose a new bounded mixed-material test, preserving the original benchmark settings and endpoint 200. No valid new token counter is available.


# Trial 22 — direct capture lines in mixed rook/bishop endings

Declared 2026-10-03 05:46–05:49 UTC after benchmark 156. Baseline 1500 [1370,1620], 55W/3D/98L in 156. Next fixed evaluation: benchmarks 157–162, unchanged rotation regardless of practice outcome. Entire run ends at 200 scored games.

Trial 21 failed: one win and five losses, with major rook/defender failures despite a successful supported mate in 154. The earlier checklists, short-decision trial, capture drills and remembered cases also did not establish reliable improvement. Replace the large-advantage two-rook drills with mixed rook/bishop positions where the opposing rook, bishop, king and pawns can all make immediate captures. Equal starting material is known; positional equality is not independently established.

Own approach to test: before committing to a tactical capture or rook move, reconstruct its resulting occupancy and test a concrete immediate capture against the full line, rather than inferring that a distant piece stopped defending. For a rook, include the intervening squares: in 155, a2–a3–a4–a5–a6 remained an open defending file. For a pawn, use its two capture squares: f5 attacked both e6 and g6 in 156. Check the direct reply before spending time on a long continuation. This is an unproved change in attention, not a claim that more prose or another checklist constitutes learning; no mandatory timing target.

Bounded study: exactly six supplied remembered/controlled branches, 21 plies, all predicted legal, plus validity checks for the two new setups. The only controlled variation is the unplayed ...dxe5/Rxf5 branch in 156; it is a legal-refutation test, not a best-move or forced-line claim. Mate statements in the recorded lines come from the referee; the script checks supplied move legality and resulting check status only, without enumerating moves or performing mate search.

1. 155 after ply 52: b6a6, a2a6. The rook on a2 still protects a6.
2. 151 after ply 18: b1c3, d5d4, e3g3, d4c3, b2c3. A pawn fork costs the knight.
3. 156 after ply 33: f8g6, f4f5, e6c4, d3c4, g6e5. Clearing a bishop retreat did not prevent the f5 fork.
4. 156 after ply 64, controlled branch: f4e5, d6e5, f1f5. Moving Bf4 exposes Qf5 to the f1 rook; the imagined pawn recapture fails.
5. 156 after ply 81: e5d4, e1e4. The final rook check is protected by Bh7; the actual game ended in mate.
6. 154 after ply 48: e2e4, d5e4, c1f4, h3h1. Capturing the blocker preserves the bishop's protection of h1 in the actual winning line.

Then exactly two fresh maximum-strength opponent practices, one White and one Black, at most 16 own moves each, including the last opponent reply. Natural results or practical resignation are allowed. Stop a capped game explicitly as unfinished. Combined setup/study/practice/review ceiling: 2026-10-03 06:16:44 UTC. No added examples, repeats, replacements, or extensions to improve results. If time runs short, stop the current drill and still record the second setup briefly within the same deadline.

Composition A, White: `1r4k1/p3bp2/7p/8/2B5/7P/P4P2/3R2K1 w - - 0 1` — White Kg1/Rd1/Bc4/a2/f2/h3; Black Kg8/Rb8/Be7/a7/f7/h6.
Composition B, Black: `2k3r1/1p2p2p/3b4/8/8/4B3/1P2P2P/2K4R b - - 0 1` — Black Kc8/Rg8/Bd6/b7/e7/h7; White Kc1/Rh1/Be3/b2/e2/h2. Different geometry, not a color-swapped replay. These are self-composed, known-material tasks, not blind independently rated test positions.

Observe actual unexpected direct captures, failure to retain a defender, pawn forks, king safety, and illegal submissions. Keeping both pieces during a capped drill is only a local observation, not a win. For transfer, assess all six benchmark games and every major error, including errors outside the rook/bishop focus. No external advice, agent delegation, engine analysis, automated search/scoring, attack-map generation or move menus. No valid new token counter is available.


## Trial 22 supplied study result
Six remembered/controlled branches, 21 supplied plies: all legality predictions matched. The two recorded final rook checks were checks in the reconstructed boards; their mate results remain referee-established, not independently searched by this script. Both self-composed setups were valid. The output's eight records comprise six move branches plus two setup-only records, not eight tactical tests. The controlled ...dxe5/Rxf5 variation confirms a legal queen capture after the f-file opens; it does not claim a best reply or an independently solved new example. No move menu, search, scoring, attack-map enumeration or engine analysis was used. Proceed to the two declared practices without adding examples.


## Practice 39 — composition A, capped unfinished
Stopped at the declared 16-own-move cap after 16...f3, 32 plies, zero illegal submissions, 2026-10-03 05:55:40 UTC. Seq 1213; hash 9ae5f5bd7466bc2c5603cf283c4916392c69913fc18b416275e8a04340abd287. Full practice PGN read. No win/draw/loss score. Final White Kb5/Ra8/a7/h4 versus Black Kf2/Ra1/f3/h5.

1.Rd7 attacked Be7; ...Rb4 counterattacked Bc4. Rxe7/Rxc4 was an explicitly anticipated equal bishop exchange, followed by Rxa7. Kg2 defended h3 against Rc3. I advanced the a-pawn while keeping the rook on its file, and recognized that moving the rook away after a7 would let the rook behind it capture the pawn. The king's defense of f2 held until ...Ra1+ forced Kd2; Black delayed the capture with ...f5/...f4, then ...Kxf2 took it. My commentary initially predicted that loss too categorically before Black's intervening choices; the actual capture occurred at move 15. The final pawn race remains unresolved at the cap. I did not lose the rook or mistake an enemy rook's open file for an abandoned defense, but the bishops disappeared early and the rook-in-front blockade prevented an easy conversion. Equal final pawn count and an intact rook are local observations, not a proved draw, theoretical verdict, or Elo improvement. No extension or replacement. Proceed to the declared Black composition.


## Practice 40 — composition B, capped unfinished
Stopped after the declared 16 own moves and final reply 17.Rd2+, 32 plies, zero illegal submissions, 2026-10-03 06:06:36 UTC. Seq 1248; hash fffa71bed3e3cb583781244ed2d1083c964cad214a2a88bab92c4a4d36fa0a18. Full PGN read. Final Black Kd4/Rb1/e5 versus White Kf3/Rd2/b2/e4; Black in check. No scored result or theoretical verdict.

Rejected the initially imagined ...Rg1+ because Rh1 could capture the unprotected rook. ...Rg2/...Rxh2 won a pawn supported by Bd6; ...Bxf4+/Rxf4 intentionally exchanged bishops. The king defended b7 against Rb4, then e7 against Re4, but the rook switched back. ...h4 deliberately allowed Rxb7. The h-pawn reached h2 with Rg2 protecting it, but Rh5 blockaded from behind while Kf3 attacked Rg2. I recognized that moving the rook abandoned h2, played ...Rg1 to preserve the rook, and White captured the pawn after first giving Rh6+. The passer did not convert, and the final position was a pawn down. ...Rb1 attacked b2; e4+ and Rd2+ kept the king occupied. No rook was lost and no illegal move was submitted, but this is not a successful ending conversion.

## Trial 22 practice-stage assessment and return
The two fresh drills both reached their 16-own-move caps unfinished: 32 own moves / 64 plies combined, zero illegal submissions, no scored practice wins. Rooks survived and some concrete captures were anticipated correctly. Both games exchanged bishops early, so the intended mixed-piece coverage was brief. Neither promoted a pawn; A ended in an unresolved race and B ended a pawn down after losing the h-passer. The remembered/controlled legality passes and these local observations do not establish transferable learning. Completed before the 06:16:44 deadline with no repeats, replacements, or extensions. Return now to the predeclared fixed benchmark block 157–162. Verified baseline remains 55W/3D/98L after 156, provisional Elo 1500 [1370,1620]; benchmark storage 48,986,521 bytes including practice-stage growth. No valid new token counter.


## Benchmark 157 — White versus maximum strength, loss
Resigned after 29...Rxd4, 29 own moves / 58 plies, one illegal submission, 2026-10-03 06:15:18 UTC. Seq 12937; hash e96ed8337f7238a0ae1a269f56591f4012e22ee1b3bef982613a3afe564dc393; snapshot 856af38b46545b48f4b4001f0168b70584df670efe4bdd6d4e645b800507897d. Full PGN read. Cumulative 55W/3D/99L after 157; Elo unchanged 1500 [1370,1620] because MAX is excluded. Storage 49,415,455 bytes.

Castled on 5, all minor pieces developed by 7, rook on e1 by 12. First 15 moves had no unanticipated material loss. Both initial bishop/minor exchanges were intentional. Qd3 reinforced e4, and exd4 opened Re1's defensive file. I recognized that moving the e4 pawn would expose Qd3 to Bg6. Nd2 and the exchanges on e4 were calculated through a possible complete liquidation, but Black instead stopped with ...f5. Ne4 then had to move while also shielding the undefended Re1 from Re8. This second line was missed before the exchange. Nf6+ conceded the knight; I primarily considered ...gxf6 but Black used the direct ...Qxf6 from d8 through e7. Rxe8+/Rxe8 was an ordinary rook exchange, leaving me a bishop down without a pawn gain.

Later Qd2 defended b4 and d4, and Rd1 added a second d4 defender. ...Bh5 attacked Rd1. I attempted illegal Rd3 through my own queen on d2, despite explicitly noticing that square during reasoning: a repeated occupancy failure, not infrastructure trouble. Corrected to Re1, after which ...Rxd4 won the pawn. Final White QR/4 pawns versus Black QRB/5 pawns; practical resignation, not an independently proved forced loss. Trial focus failed on the overloaded e-file defender and own-queen obstruction. Some correct local checks did not prevent the loss. Continue the unchanged declared block with 158; no separate learning period or replacement game.


## Benchmark 158 — Black versus maximum strength, loss
Referee checkmate 26.Qg8#, 25 own moves / 51 plies, zero illegal submissions, 2026-10-03 06:22:27 UTC. Seq 12990; hash 2f5483fb23b3c86358243c287bdf47413e86ca1b6d11c1433412323029723e1a; snapshot e659387c832dbddd63b050cd931f3e85f31a21aafc02e32bfa2ad925871e5333. Full PGN read. Cumulative 55W/3D/100L in 158; Elo unchanged 1500 [1370,1620], MAX excluded. Storage 49,838,224 bytes.

Castled on 8, minors developed by 9, Re8 on 14; no unanticipated material loss in the first 15. Central ...exd4/...d5 and ...Ne4/...Nxc3 exchanges were intentional. Unlike 152, ...Na5 occurred after White's b-pawn had moved to c3, so the earlier b4 trapping mechanism was absent. That local distinction did not establish a good overall position: the knight remained far from the king.

After e6/fxe6, White chose Bc2 rather than the anticipated possible rook recapture. I blocked the h7 battery with ...g6 and then played ...Bf6, attacking Ne5 and opening Re8's defence of e6. I saw Nxg6/hxg6/Qxg6+ as a possible sacrifice and chose to accept, but my continuation mainly considered Bh6+ and a central king escape. Actual Ba3+ instead controlled e7, defeating that imagined route. ...c5/Bxc5+ and ...Be7 blocked the checks temporarily. Qh6+/...Kg8/Bh7+ followed. I chose ...Kf7 without adequately checking Qg6+, which forced my played retreat to f8 and the actual supported Qg8# (Bh7 protects g8). No claim that an alternative king move or earlier defence was independently established as saving. This is a king-safety and forcing-reply failure despite retained material; no transfer gain. Continue 159–162 as declared.


## Benchmark 159 — White versus skill 0, win
Referee checkmate 51.Rg8#, 51 own moves / 101 plies, zero illegal submissions, 2026-10-03 06:44:20 UTC. Seq 13093; hash 0b01076f7db55634821f545bb76006da4ebb87f65c94c651d9af42d16f0e0bd8; snapshot 987be4c0c0a3053c1adf9ebcbf2479d9047161bd400553c414d80b1613359819. Full PGN read. Cumulative 56W/3D/100L in 159; skill 0 now 43W/1D/9L. Elo 1480 [1360,1600], 105 rated / latest 50, 54 MAX excluded; storage 50,282,317 bytes. The rolling estimate fell despite this win as the window changed; this is not a claim that winning itself reduced strength.

Castled on 6, minors developed by 7, rook on d1 by 10. First 15 had no unanticipated material loss. My Qe2 comment was wrong: the queen remained on Bh5's diagonal through Nf3, and Be3 blocked its purported e4 defence. I caught and explicitly corrected both before the next move. Black then sacrificed Nf6 with ...Nxg4 and left Bh5 available to gxh5 instead of recapturing on g4. These opponent errors produced the initial large gain.

The gain was not converted cleanly. f3/gxf3/Qxf3 allowed ...Rg8+, with Qh4 covering the escape squares. Qg2 blocked but allowed a queen-for-rook capture; Black instead played ...Rg7. Bxf7+ was protected by Rf1 and won a pawn, but the queen remained pinned. I chose Qxg7/Bxg7, conceding the queen for the rook. Subsequent king moves and supported blocks met repeated queen checks. ...cxd4 forked Nc3/Be3; Nf3xd4 anticipated ...exd4/Bxd4, but Black did not take the knight. Nf5 forked Qh4/Bg7; ...Qg4+ escaped while still protecting the bishop, so it was not a won bishop. Nxd6 and Nxe5 captured pawns. I kept Rf5 defended by Nd6 while it was directly exposed to Qg4, later used king-protected Rd2 to attack the queen, and moved the king before ...Qa1+ could trap it. Black overlooked the available attack on Nc4 during that sequence.

After ...Ne5, Nd3xe5 captured the knight because Rc4 blocked Black's own queen diagonal. I then answered the discovered check when the rook moved. A later Nd3 block was king-protected; Black nevertheless played ...Qxd3+, allowing Rxd3. ...Rxc2+ took a pawn, Rd2 blocked, and Black then left Rc2 undefended for Rxc2. Nxf6 captured the remaining bishop. Thus the decisive fresh advantage again depended on major opponent errors, not a clean forced attack.

In the finish I recognized ...b3 attacked Rc2 and saved it with supported Rd2+. Rh4 was chosen with an incorrect initial clear-file description: h5/h6 still blocked that file. Caught before an illegal Rh8 submission; Rd7+ was protected by Nf6, then Rg4 used the actually clear g-file and Rg8# completed the rook finish with both rooks intact. These corrected/local capture checks are positive observations, but the queen concession, false line descriptions, and opponent blunders rule out describing this as reliable trial transfer. Continue the fixed block with 160–162.


## Benchmark 160 — Black versus skill 0, loss
Resigned after 35.fxe3, 34 own moves / 69 plies, zero illegal submissions, 2026-10-03 07:00:16 UTC. Seq 13164; hash 17468d5d2123141241f6dfd045a93585e387871f2f8553e3e6e8baf35b9958ee; snapshot 01c66470f529c513423ca0f86ec3f0377bf20d19e67be3b2f976876f59854899. Full PGN read. Cumulative 56W/3D/101L in 160. Skill 0: 43W/1D/10L. Elo 1470 [1350,1590], 106 rated / latest 50; storage 50,736,837 bytes.

Castled on 6, minors developed by 9, rook on b8 by 11. First 15 were NOT clean. Qd7 deliberately supported Bf5 before moving its blocking knight. However, after Nbd2 I treated c3 as capturable with ...Nxc3 and a queen attack, considering the relocated b1-knight but omitting the b2-pawn. bxc3 simply took the knight. ...d4/Bxd4/...Nxd4/Nxd4 and ...Qxb5/Bxb5 then exchanged a bishop/knight and the queens; I explicitly recognized Bf1's long recapture line, so this was not a queen win. Bg6 saved the attacked bishop after the queen defender disappeared.

The rook errors were worse. Rd3 was correctly supported by Bg6 and escaped Bc4 to d6, where Be7 supported it. But I omitted the white e5-pawn's direct capture of d6. White initially retreated Bb3, then exd6 took the rook after ...b5; ...Bxd6 recovered only the pawn. I continued with active bishops and the e-file pin. ...Bf4 attacked Rc1 while Ne2 could not legally capture it because of the king behind it. White Rxd3/cxd3/Bxd3 conceded an exchange. ...bxc3 exploited the pin, and ...Bd2 gave mutual bishop/pawn support. ...Kxh7 correctly captured the checking bishop because White's h4-pawn blocked Rh1's line to h7.

But ...Re3, intended to attack Bd3 and support c3, had another omitted pawn capture: f2xe3. White gave the bishop check first, then moved Kc2; I played ...Kg6 without noticing fxe3, losing the last rook. Final Black B/4 pawns versus White R/2N/4 pawns; practical resignation, not a forced-loss proof. Three basic pawn captures (b2xc3, e5xd6, f2xe3) defeated substantial calculation elsewhere. Correct local support checks and the opponent's concessions do not repair that failure. Trial 22 has plainly not produced reliable direct-capture awareness. Complete the predeclared evaluation with 161–162 before revising the learning trial.


## Benchmark 161 — White versus nominal 1800, loss
Resigned after 54...Rf6, 54 own moves / 108 plies, zero illegal submissions, 2026-10-03 07:19:10 UTC. Seq 13274; hash 0ed34ea5daa1e9d785f1a6763612874436ba05ca72891b7e7e51a510e314cc1a; snapshot 35a770951c53663df58064e203370a4af0114141387f90fc73c17f1d8063e4bd. Full PGN read. Cumulative 56W/3D/102L in 161; nominal 1800 13W/0D/40L. Elo 1460 [1340,1580], 107 rated / latest 50. Storage 51,218,490 bytes.

Castled on 5, surviving minors developed by 10, Re1 on 14. First 15 NOT clean: 6.c4 allowed ...e4 to fork Bd3/Nf3. Bxe4/Nxe4 conceded a bishop for a pawn; Nc3/Nxc3/bxc3 was an equal knight exchange afterward. Again an immediate pawn advance, not a subtle distant ending, caused the first loss. Ba3/Bb4 met the queen attack, then I developed the rooks and advanced centrally. Exd6/Bxd6 was anticipated. Nh4 was supported across the fourth rank by Re4; after ...g6 I returned the knight rather than jumping onto the pawn's f5 capture square. Ne4 and d6 produced a supported passer, which ...Bd8 and Nd7 blockaded.

...Be4 attacked Qd3 with Rb1 behind it. Rxe4/fxe4/Qxe4 conceded the exchange while removing the pawn fork of Qd3/Nf3. The queen returned to defend d6, Bb2 added c3 defence, and a3 stopped ...a3 against that bishop. I brought the rook behind h4 and moved Qd5 to support a potential rook recapture on h5; Black instead exchanged queens. The kingside pawn exchanges then created a passed h-pawn. It reached h7 with Rh1 behind it; Bc1/Bxg5 won a pawn, and Bxf6+/Nxf6 exchanged bishops. Ng5 added h7 protection.

No conversion followed. ...Nxd5 removed the rear doubled d-pawn, and rook/knight checks displaced my king while ...Nxd6 removed the other passer. I rejected Nf7+ as a forced win once I noticed the a7 rook could capture on f7; I also recognized that Ng5 could not move off the g-file while it shielded Kg4 from Rg7. With Kh5, the king itself blocked Rh1's protection of h7, leaving the knight as its defender. ...Rf6 prevented the hoped-for knight fork by directly controlling e6. Final White Kh5/Rh1/Ng5/a3/c3/g3/h7 versus Black Kh8/Rf6/Rg7/Nd6/a4/b5/c5. Practical resignation with a rook deficit and the central passers gone, not a proved mate or theoretical ending verdict. Some new line checks were correct, but the early fork and later exchange concession prevented recovery. Continue 162, then assess the declared trial in full.


## Benchmark 162 — Black versus nominal 1800, loss
Resigned after 57.Kd4, 56 own moves / 113 plies, zero illegal submissions, 2026-10-03 07:35:33 UTC. Seq 13389; hash f840530138b4b668b30ccaebd9583fe0e18706c5d0613fee92daf26013a78b95; snapshot 6408e096aced4b52e73e1d166653e5d1d26b77ed78894bd10babb85f79337571. Full PGN read. Cumulative 56W/3D/103L in 162; nominal 1800 13W/0D/41L. Elo 1450 [1330,1570], 108 rated / latest 50, 54 MAX excluded. Storage 51,702,014 bytes.

Castled on 5, minors developed by 9, Rb8 on 11. First 15 NOT clean: after Na4 I counted Be7 as a c5 defender but failed to count Qc2 behind the knight. Nxc5/Bxc5/Qxc5 lost the pawn. Qb6 defended a7/c6 and challenged the queen. Nd6 retreated from d3; ...c4/...cxd3 recovered the pawn temporarily. Bf5 defended d3 against Rd1, and Rfe8 freed the knight from shielding the rook against Ba3. Qf4 attacked both Nd6 and Bf5. After extensive but confused defensive calculation, Nb5 correctly attacked Ba3; Qxf5/Nxa3 exchanged bishops without losing a piece. Rxd3 then took the advanced pawn.

Qe6 challenged the queen and defended d5; Rbd8 added the second defender after Qh5 maintained the pressure. Qe5 escaped Nd4 while offering another queen trade. ...a6 supported the knight's b5 retreat, and Nxb5/axb5 exchanged knights. Qxd4/Rxd4 reached the double-rook ending one pawn down. ...h6 gave an escape square and ...Re5 defended d5. Against Rb4/a4, ...Rb8/...Re4 did not save b5: Rxb5 was supported by a4, so ...Rxb5/axb5 lost another pawn and exchanged rooks. ...Rb4/...Rxb3 then exchanged d5 for b3, leaving the two-pawn deficit.

The king reached e6 while the rook stayed behind b5. After e4, I played ...f5, seeing that exf5+ would abandon Rd5. I overlooked the other e4 capture square: Rxf5 was itself protected by e4, so Kxf5 was unavailable. This cost a third pawn. Checks and attacks on f2/g2 did not recover material. The g/h-pawn exchange left White four pawns against one. Lateral checks nearly repeated, but White chose Kd4. Final Black Ke6/Rh3/g6 versus White Kd4/Rd5/b5/e4/f4/g5. Practical resignation, not a proved theoretical win. Positive local exchange/defender checks did not prevent further pawn errors.

## Trial 22 assessment — fixed evaluation 157–162 complete
1W/0D/5L, 249 own moves / 500 plies, one illegal submission. MAX 0/2, skill 0 1/2, nominal 1800 0/2. Elo 1500 [1370,1620] -> 1450 [1330,1570]; overlapping conditional intervals, no causal effect estimate. First 15 clean in 157–159 only (3/6). Direct pawn captures repeatedly cost pieces in 160, the e-pawn fork cost a bishop in 161, and pawn defence was misread in 162. The sole win involved major opponent errors and an earlier queen concession.

The six remembered/controlled branches passed mechanical legality; both fresh practices stopped unfinished at their declared caps, and the bishops disappeared early. That limited mixed-piece coverage. Neither the remembered passes nor correct individual benchmark decisions establish reliable transfer. This trial failed its practical aim. Revise the focus rather than repeat or extend this block.

# Trial 23 — Pawn capture directions and immediate advances
Declared 2026-10-03 07:36 UTC, after all 162 benchmarks were complete and before this study. Baseline 56W/3D/103L; Elo 1450 [1330,1570]. Fixed next evaluation: games 163–168, all six in the unchanged rotation, no replacement or extension.

Problem: long tactical calculation repeatedly omits ordinary pawn captures, pawn support on the other diagonal, or a one-square pawn fork. Previous longer lists and remembered legality passes did not establish transfer.

Plan: at most 30 minutes total, ending by 08:06:06 UTC. Review four own remembered errors: 160 ...Nxc3/bxc3; 160 ...Rd6/exd6; 161 c4/...e4; 162 ...f5/Rxf5. Read only these own PGNs. Write the pawn origin and both forward capture squares, and distinguish a pawn's attack from its possible forward advance. No automated analysis or new tactical search. These are remembered examples, not fresh test successes.

Then exactly two fresh opponent practices from the normal starting position against maximum strength, White then Black, capped at 16 own legal moves each or the combined deadline. End unfinished drills explicitly; no repeats or extra practices. Normal opening positions address the early pawn forks that the previous sparse mixed endings did not cover. Every move remains my own.

Behaviour to try: before committing a move, briefly account for the opponent pawn nearest the candidate piece, including both capture diagonals and any immediate advance that attacks two pieces; when judging a king capture, include friendly pawn support of the target. This replaces the prior emphasis; no expanded mandatory checklist, speed requirement, or claim of parameter training.

Observable transfer: record unexpected pawn captures/forks, queen/rook losses to pawns, and whether the first 15 own moves avoid unanticipated material loss in games 163–168. A useful result would be fewer such errors than 157–162, especially no queen/rook lost to an omitted pawn capture. Six games are descriptive, not a causal trial. Wins alone, the Elo point estimate, or practice completion cannot establish learning.

## Remembered study completed — 2026-10-03 07:38 UTC
Read own full PGNs 160, 161, and 162; manually reviewed exactly the four declared examples. No chess-analysis code, external source, or independent fresh test was used.
- 160: the white b2-pawn captures a3 or c3. Moving Nb1 to d2 did not remove b2; ...Nxc3 therefore still allowed bxc3.
- 160: the white e5-pawn captures d6 or f6. A bishop defending the rook on d6 permits a later recapture, but does not make giving a rook for that pawn sound. White delayed exd6 for a move and then played it.
- 161: a black pawn on e5 captures d4/f4; after its ordinary advance to e4 it captures d3/f3. Those were exactly the bishop and knight squares. My c4 move did not address that fork.
- 162: the white pawn on e4 supports BOTH d5 and f5. ...f5 offered a pawn to Rd5xf5, and the rook remained pawn-protected on f5. My imagined ...Kxf5 was not available. Looking only at the first occupied support square was the error.

These facts are recalled corrections, not four new puzzle solves. I have not proved alternative saving moves or an improvement in play. Proceed to the two predeclared fresh practices.

## Practice 41 — White versus MAX, fresh normal start
Stopped at the declared 16 own moves / 32 plies, zero illegal submissions, 2026-10-03 07:41:15 UTC. Seq 1283; hash d79b09bf1ce37bfe25f4aa779f25897aad1f84affb4c963fc04a6985dd4459a8. Unfinished, no score. Full PGN read.

Castled 8, all minors developed by 10, Re1 on 11. Anticipated ...dxc4/...cxd4 and recaptured. However 12.d5 concentrated on ...exd5 and omitted the actual ...Nxd5. Bxe7/Ncxe7 did not recover the pawn. First 15 NOT clean. The queen was then chased by ...Nf4/...Neg6. I rejected Qf5 because e6 could capture it, a correct immediate pawn observation, but Qe3 allowed actual ...Nxg2, forking Qe3/Re1. I had considered that fork but did not establish a safe king-capture continuation; none was played before the cap. At stop White QR2BN2/4 pawns against Black QR2BN2/6 pawns, with the black knight on g2. Do not call it a solved loss or draw, or claim a successful defence.

This exposed a scope problem: attention to pawn errors did not replace the need to see ordinary knight captures and forks. No extra moves or repeat of the practice.

## Practice 42 — Black versus MAX, fresh normal start
Stopped at the declared 16 own moves / 33 total plies (White moved first and replied with 17.c4), zero illegal submissions, 2026-10-03 07:44:26 UTC. Seq 1319; hash a515ad9a1eaee6c59c5165f46c154d5b8fbf6a46c1b7526fb84bff45e9a769c5. Unfinished, no score. Full PGN read.

Castled 8, all minors developed by 9, rook e8 on 10. First 15 clean by the stated material-loss criterion, not a position evaluation. Retained the e5/d6 centre and noticed d5 would attack Nc6. My initial Re8 comment falsely described e5 support through Be7; corrected before Bf8 cleared the line. After a4/Qb3, Na7 added a second b5 defender. Following axb5 I caught that ...axb5 would open Ra1 against the undefended Na7, and instead played ...Nxb5. Material was balanced at stop (all pieces and seven pawns each); White's last c4 attacks Nb5. No continuation or claim that the knight is permanently secure was tested.

## Trial 23 learning phase completed
Finished 07:44 UTC, before the 08:06:06 deadline. Exactly four declared remembered examples reviewed and exactly two fresh MAX practices, 32 own moves / 65 plies, zero illegal submissions; both drills unfinished. One practice had unanticipated material loss in its first 15, one did not. A few correct pawn/line observations coexist with a missed knight capture, a queen/rook fork, and an initially false rook-support description. No demonstrated strength gain or successful full-game conversion. No extra study, repeat, or replacement. Return to the unchanged predeclared benchmark evaluation 163–168. Pawn focus is an aid to complete move checking, not a reason to ignore other pieces.

## Benchmark 163 — White versus MAX, loss
Resigned after 24...Nh4+, 24 own moves / 48 plies, zero illegal submissions, 2026-10-03 07:50:50 UTC. Seq 13439; hash 63f7b9ec55bb5a59fe44fb6a8935720d2da5832b3be1b43073ab217692edb04d; snapshot 877693058d43ff64a19e7c222f67fbebf182f3fc8c8c503f898dbb3aecd6bfec. Full PGN read. Cumulative 56W/3D/104L in 163, MAX 0W/2D/53L. Elo unchanged 1450 [1330,1570], MAX excluded. Storage 53,013,635 bytes.

Opening repeated practice 41 through 11...Bb7; chose Rc1 instead of the failed d5. Castled 8, all minors developed 10, Re1 11/Rc1 12. First 15 had no completed unanticipated material loss, but the queen/defender arrangement already contained the next failure. This is a narrow remembered-opening correction, not fresh independent transfer. Bh4 escaped the h6 pawn. Qd3 met ...Nb4; Qe2 retained nominal Bc4 defence but removed d4 defence. ...Bxf3 eliminated the other d4 defender. I chose gxf3 to keep Qe2 defending Bc4 rather than allow ...Rxc4 after Qxf3, but ...Qxd4 then won the pawn. Bg3 saved the other bishop from the queen.

I incorrectly treated Qe2 as sufficient Bc4 defence. Actual ...Qxc4/Qxc4/...Rxc4 exchanged queens while losing the bishop: the c8 rook was the second attacker. This was a whole-exchange/defender-count failure. Ne4, supported by f3, escaped the attacked c3 square and ...Rxc1/Rxc1 exchanged one rook pair. ...Nfd5/...Nd3/...Ne1 attacked the remaining rook and pawns. Rc2 defended b2/f2, but after ...Ne1 I could not preserve f3 with the rook retreat I chose; Re2/...Nxf3+ lost it. Kg2 attacked the knight, which checked again from h4.

Final White Kg2/Re2/Ne4/Bg3/a3/b2/f2/h2 versus Black Kg8/Rf8/Nd5/Nh4/Be7/a7/b6/e6/f7/g7/h6. Practical resignation with an extra enemy minor and two-pawn deficit, not a forced-mate proof. No illegal moves and no piece lost to an omitted pawn capture, but overall defence still failed. Continue the unchanged declared evaluation with 164–168.

## Benchmark 164 — Black versus MAX, loss
Resigned after 23.bxc5, 22 own moves / 45 plies, zero illegal submissions, 2026-10-03 07:57:44 UTC. Seq 13486; hash 76f601eed90cd239465c640fe3dc68071a08a6d0b2bfca641d3d3f497fe551b9; snapshot b0e959f7a2f1c0eca8d3a232a9af0eb77b9ceb044b7660d46cd662cfdc2f72e6. Full PGN read. Cumulative 56W/3D/105L in 164; MAX 0W/2D/54L. Elo unchanged 1450 [1330,1570], 108 rated / latest 50, 56 MAX excluded. Storage 53,460,525 bytes.

Castled 8, minors developed 9, Re8 10. First 15 clean by immediate material-loss criterion. Opening repeated practice 42 through 11...Bf8, with the rook-line description corrected this time. Chose ...b4, supported initially by Nc6, rather than the earlier ...h6. White a5 fixed the queenside. After Ba4, ...Re7 moved the rook off the bishop diagonal; I also rejected ...Re6 because d5 would fork that rook and Nc6. Actual d5 attacked the knight. I rejected ...Nxa5 because cxb4 would attack it while d5 controlled its c6 return (other retreats were also problematic in my calculation); this was a local manually assessed danger, not an independently proved forced trap. Played ...Nb8/...Nbd7.

Moving Nc6 removed b4's defender, so cxb4 won the pawn. The new white b4 pawn also made ...Nc5 unsafe. I prepared ...c5 with ...Qc8, considering the possible en-passant capture dxc6 and the bishop/queen recaptures on c6. That preparation missed a different consequence: moving c7 also removed d6's pawn defender, after the queen had already moved away from d8. Actual Nxd6 won a second pawn and forked Qc8/Bb7. ...Qc7 defended the bishop and attacked the knight; Nxb7/Qxb7 exchanged them. But Bc6 then forked Qb7/Ra8. ...Qb8/Bxa8/...Qxa8 conceded the exchange, and bxc5 captured another pawn. I did not play ...Nxc5 into the queen on c2.

Final Black Kg8/Qa8/Re7/Bf8/Nd7/Nf6/a6/e5/f7/g7/h6 versus White Kg1/Qc2/Ra1/Re1/Bc1/Nf3/a5/b2/c5/d5/e4/f2/g2/h3. Practical resignation with an exchange and three-pawn deficit and strong connected enemy pawns, not a forced-mate proof. Several pawn-capture/advance checks were correct, but vacated pawn defences and the bishop fork still produced a decisive deterioration. No reliable overall transfer. Continue 165–168 without changing the declared block.

## Benchmark 165 — White versus skill 0, win
Referee checkmate 28.Qh7#, 28 own moves / 55 plies, zero illegal submissions, 2026-10-03 08:11:35 UTC. Seq 13543; hash a9d1ac20d51618dfaa53f48d237462d8e9e18b57866e2faf690b85b751bb2525; snapshot 1643f9ba5d1395631f22ed5f2ee8f1379ff1c849dbb2648653cbb16654acbc44. Full PGN read. Cumulative 57W/3D/105L in 165; skill 0 44W/1D/10L. Elo 1460 [1340,1580], 109 rated / latest 50; 56 MAX excluded. Storage 53,906,156 bytes.

Castled 6, minors developed 7, Rad1 10. First 15 clean. a3 controlled the b4 advance against Nc3. e5/dxe5/dxe5 was anticipated; ...Nd5 attacked both Nc3 and Be3, so Nxd5/exd5 removed that knight. Qxd5 won the pawn because Nd7 blocked Qd8. e6 was queen-supported, and fxe6/Qxe6+ opened the king attack. Bd3+/...Kh8/Qg6 threatened the supported Qh7, but ...Nf6 defended h7; I explicitly did not play Qh7 into that knight. Ne5/Qc7/Nf7+/...Rxf7/Qxf7 won the exchange. The other rook's line was blocked by Qc7, and the queen's line by Be7.

After ...Qc6 I made h3 for a king escape square and g4 control. ...Be6 attacked the queen; Qg6 escaped, and Qg3 later regrouped on a square supported by f2. Black then gave major material away: ...Bg4 allowed h3xg4, and ...Nh5 allowed g4xh5. I considered the possible recaptures on g4 without assuming that Qxg4 would be safe against Qc8. These actual pawn captures are positive local evidence for the trial focus, but arose from severe skill-0 errors.

...Bd6 attacked Qg3, so Qg6 escaped and renewed Qh7 with the defending knight gone. Black ...Qg4 failed to stop it. Qh7# was supported by Bd3; g7 blocked Ra7 from h7. Both rooks survived; no queen concession or further material loss. My last pre-move commentary incorrectly called Qh7 a capture; h7 was empty, and the move was a non-capturing checkmate (corrected in commentary afterward). No claim that all hypothetical attack branches were proved or that this one win establishes sustained learning. Continue fixed evaluation 166–168.

## Benchmark 166 — Black versus skill 0, loss
Resigned after 31.Bc2, 30 own moves / 61 plies, zero illegal submissions, 2026-10-03 08:32:42 UTC. Seq 13606; hash 3e26653a18088971ec4d2366bf25b9523579c6e45a9e43c2da8f4516f660ad87; snapshot e2f3396e97f3874d4004b745d39675f9a402cb23b91ea8cb202dd1c4d6a77e5f. Full PGN read. Cumulative 57W/3D/106L in 166; skill 0 44W/1D/11L. Elo 1430 [1310,1550], 110 rated / latest 50, 56 MAX excluded. Storage 54,326,732 bytes.

Castled 7, minors developed 8, Rad8 10. First 15 clean. ...d5/cxd5/...Nxd5 was supported by the queen, ...Be6 added knight support, and ...a6 addressed b5 against Nc6. After ...f5, Nc5 forked Qd7/Be6; ...Bxc5/Qxc5 was an equal minor exchange. ...b6 attacked the queen while Qd7 retained Nc6 defence. ...e4 attacked Nf3/d3 with f5 support; ...h6/Nxe6/...Qxe6 exchanged the other bishop for the remaining white knight. dxe4/fxe4 left a queen-supported e4 pawn.

...b5 attacked Qc4, and White counterattacked my queen with Bg4. I correctly treated ...bxc4/Bxe6+ as a queen exchange, not a free queen win. ...Kh7 escaped. Rd1 added a second attack on Nd5, met by ...Nce7. Rd4 then attacked both c4 and e4. I deliberately advanced ...c3, supported by Nd5, and allowed Rxe4; ...Nf6 attacked the rook, and after Rc4, ...Rd3 defended c3. I then reinforced with ...Ned5, considering the possible Bxd5 recaptures.

The decisive omitted reply was instead Bf5+, forking Kh7 and Rd3. ...Kh8/Bxd3 lost the entire rook, not an exchange. The subsequent ...Nb6/...Nfd5 kept the passer defended and ...Rd8 sought activity, but White moved Bc2 and no material was recovered. Final Black Kh8/Rd8/Nb6/Nd5/a6/c7/c3/g7/h6 versus White Kg1/Ra1/Rc6/Bc1/Bc2/a3/b4/e3/f2/g2/h3. Practical resignation a rook and pawn down, not an independently proved forced loss.

No piece was lost to an omitted pawn capture, and several pawn/queen exchanges were accounted for correctly. However the bishop check/fork defeated a long local defence calculation. This does not demonstrate reliable overall improvement. Trial 23 through four benchmarks: 1W/0D/3L, 104 own moves / 209 plies, zero illegal submissions. Complete 167–168 before assessment or another learning period.


## Benchmark 167 — White, nominal 1800, loss
Finished 2026-10-03 08:54:37 UTC by resignation after 40...Ra2: 40 own moves, 80 plies, zero illegal submissions. Castle 6, minors developed 7, rook centralization 9; no material concession in first 15. Cumulative 57W/3D/107L; provisional Elo 1420 [1290,1540]. Result seq 13688, hash e57b1c4178e082a93141a4a2bbad653980b0221617b1d9d145cdf8f638985bfd, snapshot 6aec2666c55ce6deb4482de56ba8fb5ffcc81bbbf5245ceca08bb78eb84679fe.

The opening kept material balanced. Bf3 answered extra pressure on e4, e5 advanced the f4-supported pawn, and Nxe4/Bxe4 exchanged the central knights. Qf2 defended both c2 and g2 against Be4. The queen exchange was supported by the bishop. However 24.Rf3 allowed ...Be2 to fork both rooks. I considered Nxe2 but calculated back-rank danger after vacating d4; those alternative lines were not mechanically verified or established as best play. Rd2 kept the file blocked, but ...Bxd4 Bxd4 Bxf3 gxf3 left an exchange deficit. This is another missed bishop fork, not a pawn-capture failure.

I continued the ending: exchanged one rook pair, activated the king, and correctly recaptured h4 after the pawn exchange. My note for 37.b3 incorrectly claimed support for c2; it supports c4, and I corrected this explicitly on move 38. ...Rc5 attacked the bishop and ...Rxc2 won a pawn; ...Ra2 attacked a3. Final White Kg3/Bd4/a3,b4,f4 versus Black Kg6/Ra2/a6,b5,e6,h5. I resigned with an exchange and pawn deficit and no concrete recovery found; no forced-mate or independently proved loss claim. The pawn focus did not prevent a decisive error of another kind. Saved PGN read in full.


## Benchmark 168 — Black, nominal 1800, loss
Finished 2026-10-03 09:06:43 UTC, resignation after 41.Bxe2. 40 own moves / 81 plies, zero illegal submissions. Castled 5, remaining bishop developed 9, Rad8 11. First 15 materially clean. Full PGN read. Result seq 13771, hash e983ae164b9a0d1eaea25481e91a6747544e52b64c62510a4eb7c57ee14d1c23, snapshot c9afab28635e05d9ce6d6ae1bc6267bdf75a9ef6e3a848c85fb8a52af46ab223.

Development and several exchanges remained balanced through 29 moves. On 22.axb6 I chose Qxb6 instead of the previously anticipated cxb6 because the queen also defended a6 against Ra1. ...g4/hxg4/...Nxg4 opened the kingside. Rh4 added a second attack on Ng4. I chose ...Ne3+, calling attention to d4 support, but omitted the white f2 pawn: fxe3 simply captured the knight. ...dxe3 recovered a pawn, not the piece. This is a direct failure of the trial's pawn-direction focus.

...Rd2 was supported by e3 and attacked Qh2. White instead played Rxh6+, allowing ...Qxh6/Qxh6+/...Kxh6. The sixth rank had become clear, and this actual sequence recovered material to an exchange advantage. After Rxa6+ I activated the king with ...Kg5/...Kf4, exchanged rooks on g6, and captured the undefended e4 pawn. But after 39.Bb5 I chose ...Rg2 to get behind the passed g6 pawn, completely omitting Kf1xg2. The rook was taken immediately. ...e2/Bxe2 then eliminated my remaining advanced passer. Final Black Ke4/c5,e5 versus White Kg2/Be2/b3,c2,g6. Resigned with a bishop and pawn deficit and White's near-promotion passer; no forced-mate claim. Rg2 was a whole-rook oversight, not a justified simplification.

## Trial 23 fixed evaluation — complete after 168
Benchmarks 163–168: 1W/0D/5L, 184 own moves / 370 plies, zero illegal submissions. MAX 0/0/2, skill 0 1/0/1, nominal 1800 0/0/2. First 15 materially clean in 6/6 by the immediate-loss criterion (latent defender failure in 163 still mattered later), compared with 3/6 in trial 22. This narrow opening observation did not become improved full-game outcomes. Baseline Elo 1450 [1330,1570] after 162; endpoint 1410 [1280,1530]. Cumulative 57W/3D/108L in 168. Each opponent has 56 scored games: MAX 0W/2D/54L; skill 0 44W/1D/11L; nominal 1800 13W/0D/43L. Storage 55,280,308 bytes. Model uses latest 50 of 112 rated games and excludes 56 MAX games.

Four remembered manual pawn cases and two unfinished MAX opening drills produced some correct local pawn checks and a clean skill-0 attacking win. They did not establish independent transfer: 168 again lost a knight to an omitted pawn capture, while bishop forks and whole-rook losses recurred elsewhere. No queen or rook was lost directly to an omitted pawn capture in this block, but the knight loss and king capture prevent calling the method reliable. Decision: end this focus as the main trial, replace it with a short destination-and-check verification exercise that explicitly includes enemy kings; do not infer improvement from longer notes or remembered repairs.


# Trial 24 — verify the destination and opposing checks

Declared 2026-10-03 09:08:20 UTC after 168 scored games and before study. Baseline 57W/3D/108L, Elo 1410 [1280,1530]. Fixed next evaluation: all six benchmarks 169–174. Do not extend, replace, repeat, or add drills based on outcomes.

Weakness: favorable plans and long candidate calculations have omitted immediate captures by pawns and kings, and checking bishop forks. Try briefly reconstructing the candidate's destination and the opponent's immediate captures/checks before choosing it, including the opposing king. This replaces the pawn-only focus; no added mandatory long checklist or time-per-move rule. Similar ideas have failed in prior trials; this is another test, not a novel or proven method.

Bound: at most 20 minutes combined study/practice, ending 09:28:20 UTC. Exactly four remembered cases: game 166 before 26...Ned5, game 167 before 24.Rf3, game 168 before 30...Ne3+, and game 168 before 39...Rg2. Read/reconstruct only these own records, identify the actual omitted reply, and consider at most one repair per case. Mechanical board reconstruction or checking explicitly chosen lines is allowed; no search, evaluation, attack maps, or generated candidate moves.

Then exactly two MAX opponent drills, at most 12 own moves each or earlier natural completion/deadline. First: Black from game 168 after ply 77, a remembered position with fresh opponent continuation. Second: White from the self-constructed position 6k1/4R2p/1p3P2/3Kp3/2P3b1/1P6/8/8 w - - 0 1. The latter is new but deliberately favorable in material and has no independently established evaluation. If the deadline prevents a drill, record that; no extension. Do not claim remembered replay success or a favorable practice win as benchmark transfer.

Observable benchmark outcomes: queen/rook losses to immediate captures, minor losses to omitted pawn captures, missed checking forks, full-game W/D/L and Elo uncertainty. Compare descriptively with trial 23's 1W/5L and recurrent material losses. Preserve all records. No external chess sources or assistance.

## Remembered review
Reconstructed only the four declared own positions. System Python initially lacked python-chess; reran with the existing vendored chess library and bytecode disabled. No files under .arena were changed. The saved verification script checks only the twelve explicitly supplied moves in four three-ply lines; all were legal. It does not search, evaluate, generate candidate moves, or establish best play.

166: ...Ned5 missed Bf5+, which attacked Kh7 and Rd3. Proposed ...Rd6 Bf5+ Kg8 moves the rook off that diagonal, but also relinquishes its defence of c3; this is a local repair with a cost, not a winning claim.
167: Rf3 let ...Be2 attack both rooks. Proposed Rf2 Be2 Rd2 keeps the f-rook off the e2–f3 diagonal and preserves a blocker on the d-file. Only this line was checked.
168, move 30: support by d4 did not prevent f2xe3 from taking the knight. Proposed ...Nf6 Rxh6+ ...Kg7 avoids that capture but concedes h6 and leaves an attack; no claim it resolves all threats.
168, move 39: Kf1 can capture g2 directly. Proposed ...Rd8 g7 ...Rg8 instead places the rook far from that king and blocks promotion. This narrow repair is remembered; the next opponent drill tests subsequent choices.

Updated playing reminder: reconstruct the candidate destination, include opposing kings and pawns among immediate capturers, and notice checking forks. This is a brief verification focus, not a longer checklist or an evidence claim.

## Practice 43 — Black MAX, loss
Started from own game 168 after ply 77, a remembered setup. Resigned 09:14:43 UTC after seven own moves / 14 plies, zero illegal submissions. Seq 1335, hash 8ee020d70b1b415d5cb95493dadfc7e473af7f59350dc74751dc561231aed3cb. PGN read in full: 39...Rd8 40.Ke1 Rg8 41.Bc4 Rg7 42.Bf7 Kf3 43.c3 e2 44.b4 Rh7 45.gxh7 Ke3 46.h8=Q. The remembered Rg2 error was avoided; I also avoided an unverified ...Rxg6/Bd3+ fork line. Then ...Rh7 simply placed the rook on g6's capture square. I noticed a possible forward g7 advance but omitted gxh7. White promoted; resignation recorded as a practice loss, not an unfinished drill. This is strong negative evidence for reliability even within the local exercise. No repeat.

## Practice 44 — White MAX, unfinished at cap
Ended 2026-10-03 09:18:29 UTC after exactly 12 own moves / 24 plies, zero illegal submissions. Seq 1362, hash 3b3880d2ac365233c43c78e484dd9fb3e4b629e54b57bebb5cc136e23e53d570. PGN read in full: 1.Rg7+ Kf8 2.Rxg4 h5 3.Rh4 Kf7 4.Kxe5 b5 5.cxb5 Kg6 6.b6 Kh7 7.b7 Kg6 8.b8=Q Kg5 9.Qb4 Kg6 10.Qf4 Kf7 11.Rxh5 Kg6 12.Qf5+ Kf7 *.

The deliberately favorable constructed setup allowed a supported rook check and then winning the bishop. I moved away from h5's capture on g4, defended f6 with Kxe5, promoted the distant b-pawn, and twice defended the rook against the nearby king (Qb4, later Qf5+). I waited to take h5 until the king was farther away. Final White Ke5/Qf5/Rh5/b3,f6 versus Black Kf7. Rook and queen retained, but the declared cap ended play before checkmate: no win recorded and no full conversion claim.

## Learning period closed
Finished 09:18:29 UTC, within the declared 09:28:20 deadline. Exactly four remembered cases with twelve explicitly supplied mechanically legal plies, then exactly two MAX drills: one resignation loss, one unfinished; 19 own moves / 38 plies, zero illegal submissions. The first drill repeated a direct pawn-capture oversight and lost the rook; the second favorable exercise showed some correct local captures/king-range checks. These mixed observations do not establish reliable transfer. No extras or repeats. Return to the fixed evaluation 169–174 with the declared brief focus.

## Benchmark 169 — White MAX, loss
Resigned after 28...Raf8 at 2026-10-03 09:28:43 UTC. 28 own moves / 56 plies, zero illegal submissions. Seq 13829, hash 3881ca587491a497bd3054c887613f05208fd630cddbfcfca8552edb0d31896c, snapshot 5b0a0f4fd3fc5af423032b9f2e262c1fdad6a08966a2a179826bbbc07c6eac9e. Full PGN read. Cumulative 57W/3D/109L in 169; MAX 0W/2D/55L. Elo unchanged 1410 [1280,1530], MAX excluded. Storage 56,634,289 bytes.

Castled 5, minors developed 7 before the exchanges, Rad1 13. First 15 materially clean. Two minor exchanges doubled the b/e pawns and opened files. Qd3 supported e4 before ...Bb7, and d5 closed the diagonal. But Nh4 allowed ...Ba6, skewering Qd3 and Rf1. Nb5 interposed; ...Nxe4 Qxe4 Bxb5 exchanged knights and cost the central pawn. My initial mental idea that Qxe4 simply won the knight had omitted the consequence of moving the queen away from Nb5; the actual move comment acknowledged the bishop recapture. Nf5 gained a queen tempo, then Rfe1 escaped the bishop line. ...g6 chased the knight, ...f5 chased the queen, and ...f4 chased the knight again.

I moved Qf3 to d3 to avoid a potential ...Bg4 skewer, but ...f3 attacked Ne2 and g2. Correctly recognized that immediate gxf3 would expose Kg1 to Qg5. Ng3 blocked the file and escaped the pawn's capture square, but overlooked the forcing forward ...f2+, checking Kg1 and attacking Re1. Kh1 fxe1=Q+ Rxe1 cost a whole rook for a pawn. My first commentary called this an exchange loss, which was wrong and explicitly corrected. Final White Kh1/Qd3/Re1/Ng3/b2,b3,c4,d5,e4,g2,h2 versus Black Kg8/Qg5/Rf7/Rf8/Bd7/a5,b6,c7,d6,e5,g6,h7. Practical resignation a rook down under king pressure, not a forced-mate proof.

This block has already repeated a pawn-advance fork/promotion failure and lost a rook. No reliable transfer claim from the practice. Continue fixed 170–174 without extra study or changed opponents.

## Benchmark 170 — Black MAX, loss by checkmate
Referee confirmed 23.Qxf6# at 2026-10-03 09:38:40 UTC. 22 own moves / 45 plies, zero illegal submissions. Seq 13876, hash 87a9de2fe33f24d47b75b9b37c5a22cf05fb3ffe19fff86fb813af9bb2a1c67f, snapshot c1a0ec73bffbbf5ed05bb7abd450f1fa2dafd55a6b33931e90de4ef476c92eb2. Full PGN read. Cumulative 57W/3D/110L in 170; MAX 0W/2D/56L in 58. Elo unchanged 1410 [1280,1530], 112 rated / latest 50, 58 MAX excluded. Storage 57,081,220 bytes.

Castled 8, minors developed 9, first rook centralization 17. First 15 materially clean. Deviated from the earlier ...Re8/...Bf8 opening with ...exd4/...d5, meeting e5 by ...Ne4 supported by d5. ...Nxc3/bxc3 exchanged knights; ...Na5 attacked Bb3 and opened Bb7 support of d5. ...c5 challenged the centre. White Qd3 built a queen/bishop battery toward h7; ...g6 blocked it, Bh6 attacked Rf8, and ...Re8 escaped. But e6/fxe6/Rxe6 opened the king attack. ...Bf8 sought to defend and challenge the rook, yet Rxg6+ broke through. I recognized danger in ...hxg6 and chose ...Bg7, conceding the bishop to Rxg7+.

...Kf8 escaped the immediate rook check, but Qf5+ left the king trapped: the rook on g7 also controlled e7, an escape square I had incorrectly treated as available in earlier mental branches. ...Qf6 blocked the file and Qxf6# ended the game. This actual mate is confirmed; my alternative attack/defence lines were only mental calculations and are not proved forced or best play. No pawn-capture loss of my rook here; the failure was king safety, an incomplete forcing-line calculation, and overlooked rook rank control. No reliable positive transfer. Trial 24 through two benchmarks: 0W/0D/2L, 50 own moves / 101 plies, zero illegal submissions. Complete 171–174.

## Benchmark 171 — White skill 0, win
Referee confirmed 27.Qd8# at 2026-10-03 09:48:32 UTC. 27 own moves / 53 plies, zero illegal submissions. Seq 13931, hash b341db917b93d9bfc0352a438d6f7dab090a9d68804ab1183933eae4e7fef7cc, snapshot 41200afeebadf384b7a8a60bc1b6790098bd3c9b72cf06eb2d09183ca5dff0d6. Full PGN read. Cumulative 58W/3D/110L in 171; skill 0 45W/1D/11L. Elo 1420 [1290,1540], 113 rated / latest 50, 58 MAX excluded. Storage 57,556,447 bytes.

Castled 5, minors developed 7, Rad1 9. First 15 materially clean. ...Bxf3/gxf3 exchanged a bishop for my knight and weakened the king shelter. Kg2 defended h3 against Qd7 and supported f3. d4/dxe5 opened the centre; Black ...g4 left Nf6 attacked, allowing exf6. I anticipated ...gxf3+ and chose Kh2; rejected Kxf3 because of a possible ...Ne5+ fork of king and Bc4 (unverified alternative). Black castled and then moved the h-rook, allowing the same pawn to take Be7 and Rd8 with promotion/check. ...Kxd8 recaptured the promoted queen, but the knight, bishop and rook had already been won.

Rg1 challenged the remaining rook; ...Rg2+ Rxg2 followed. Black did not play the anticipated ...fxg2, instead moving its king. I then moved Rg3 out of that pawn's capture square. ...Na5 and ...c6 chased Bc4 through d5 to b3; the bishop stayed supported. ...Nc4 forked Qd2/Be3 but now allowed Bxc4, removing the last knight. Black ...Qxh3+ gave away the queen to Rxh3. Qxd6 was supported by Rd1, and Qd8# was also rook-supported with Bc4 controlling f7. Both original rooks survived.

This is an actual successful conversion with correct local pawn/king checks, but it depended on several severe opponent errors and does not establish sustained improvement. Trial 24 through 169–171: 1W/0D/2L, 77 own moves / 154 plies, zero illegal submissions. Continue fixed 172–174.

## Benchmark 172 — Black skill 0, draw by repetition
Referee recorded threefold repetition after 44...Kd6 at 2026-10-03 10:12:10 UTC. 44 own accepted moves / 88 plies, one illegal submission. Seq 14022, hash b8f77bd29b1bcc5fa0cdf8d80c505caf41bc94d462f4e9ca991a8a14d5a6cf52, snapshot 0b31275e8ea8361fce953f270052f1c2022f78a6bc5fe61f3172825e7619f705. Full PGN read. Cumulative 58W/4D/110L in 172; skill 0 45W/2D/11L in 58. Elo 1410 [1290,1540], 114 rated / latest 50, 58 MAX excluded. Storage 58,020,728 bytes.

Castled 6, minors developed 8, Rad8 10; first 15 materially clean. The centre was supported through ...Nxd5, ...Bxd5, ...Bf7 in response to e4, and ...Nd4/Nxd4/...exd4. On 18.exf5 I tried the impossible bishop move f7-f5, mentally treating f7-e6-f5 as a straight diagonal. The referee rejected it; I corrected to ...Qxf5 without another illegal attempt. That queen recapture left c7 undefended, and Qxc7 won the pawn. ...Qd7 offered an exchange, accepted through ...Qxc7/Rxc7.

In the ending I defended b5 with a6, challenged Ra7 with ...Ra8 supported by Rf8, and met Re7 with ...Rae8 to protect Be6 through recapture. One rook pair exchanged. ...Kf7/...Ke6 activated the king, and ...Bf6 escaped f4 while maintaining d4 support. The rook blocked Rc7+ on e7 with king support. After ...g5/Bg4+ I moved ...Kd6; fxg5/Bxg5 followed. I wrongly described the capture as attacking Bd2 without recognizing its reciprocal diagonal: Bd2xg5 immediately captured my undefended bishop. The f4 square had just been cleared. This was a bishop-line/capture oversight, not a sound sacrifice.

...Re5 escaped Bg5 and attacked it. ...h5 was rook-supported, ...h4/hxg3/Bxg3 exchanged the h/g pawns, and ...a5/...a4 locked the queenside. Bf4 and later Bg3 pinned Re5 to Kd6, while the other bishop and rook restricted the king. I could not establish a material-preserving solution; the rook had no legal move off that pin. ...Ke7 left e5 undefended, but White chose Bh4+ rather than taking the rook. ...Kd6/Bg3/...Ke7/Bh4+/...Kd6 repeated, and the referee claimed the draw. Final Black Kd6/Re5/Bd5/a4,b5,d4 versus White Kg1/Rc5/Bh3/Bh4/a3,b4,d3,h2. Draw while a bishop and pawn down, with substantial opponent cooperation; no forced-draw proof or claim the earlier errors were justified.

Trial 24 through 169–172: 1W/1D/2L, 121 own moves / 242 plies, one illegal submission. Both saved result and successful win are actual scores, but the target errors persist. Finish fixed 173–174 before assessment or further study.


## Benchmark 173 — White, nominal 1800, loss (2026-10-03 10:42:27 UTC)
- Referee: resignation after 56...Rxh7+, 56 own moves / 112 plies, 2 illegal submissions on separate turns. Result seq 14138, hash `6a39978addcb16c0b91aa179cbd5cf5053abb50bbd29f73169beca967fa49940`, snapshot `abc1eab2ece4228fd9ae5922289e31046bd317b8555f52900a8050e647ab18ad`. Own full PGN read; no engine analysis.
- Castled on 5, minors developed by 7, Rfe1 16 and Rad1 17; first 15 moves had no immediate own material loss. Bishop-for-knight exchanges left two knights against bishops. Qe2, e5, Rfe1, Rad1 supported the center. Ne4 and c4 chased the queen; Ng3 cleared the e-file while attacking it. Qe3 added d4 protection before Nc4-d6. Nxg7 exchanged a bishop. Qg5 was correctly supported by h4 and led to a queen trade.
- A specific successful precaution: 34.Rd2 left the d1-h5 bishop-fork diagonal before 35.Rxh5. Nxb7+ then won another pawn. Black later declined exposed b4 twice (39...Kd7, 40...Ke7), so those continuations were cooperative, not proof of sound pawn defense.
- Decisive failure: 39.Re5/40.Re3/41.Rxg3 relied on a proposed h4xg3 recapture. That is a BACKWARD white pawn capture. 41...Rxg3 won a whole rook for a pawn; attempted 42.h4g3 was rejected. Earlier in this same game I had correctly used h4's forward capture to g5, then reversed its direction in a later calculation. This directly fails the destination/pawn-capture trial.
- Continued with king activity and the passed h-pawn. 53.g5 fxg5+ also uncovered the f8 rook, so my earlier proposed Nxg5 would not answer the double check; I recognized this before submission and played Kxg5. Black repeatedly allowed h7 to survive; no claim of a forced recovery.
- Second decisive calculation failure: 56.Kh6 was intended to add h7 support but put my own king between Rh2 and h7. After ...Rxh7+, attempted Rh2xh7 was rejected because h6 was occupied by my king. Resigned with Kh6/Rh2/Nd6 and b2,c5,d4 versus Ke7/Rf8/Rh7/Bb1 and a4,c6; substantial material deficit, not a claimed forced-mate proof.
- Cumulative 173 scored: 58W/4D/111L. Nominal1800 13W/0D/44L (57); MAX 0W/2D/56L (58); skill0 45W/2D/11L (58). Referee Elo 1400 [1280,1530] conditional 95% credible interval; 115 rated total/latest 50, MAX excluded. Storage 58,529,843 bytes. Trial24 through five games: 1W/1D/3L, 177 own moves / 354 plies, 3 illegal submissions. Finish predetermined game174 before assessment/new study.


## Benchmark 174 — Black, nominal 1800, loss (2026-10-03 11:07:14 UTC)
- Referee resignation after 49.Kh6: 48 own moves / 97 plies, 0 illegal attempts. Result seq14237, hash `bd2c9012cb0085dc4a372d480e990551c0a00b4f7f923b510bf42b00c054dc97`, snapshot `223e4682d8ae5cd1061d2e648bf651b0c9bd86d77498647803336b065c2666fd`. Own full PGN read.
- Castled5, remaining minor developed9, Rad8 11, first15 no immediate material loss. Be7 provided a second recapture on f6; Bxf6/Nxf6+/Qxf6 exchanged minor pairs without damaging the king pawns. Bxh3 traded the remaining bishops; d4 used pawn and knight support. I considered but rejected an immediate ...Nd4 because c3 could capture it. Qh6 pressured the unguarded Nh3, f5 opened the file, Rxf5-h5 used queen support, and Qg6/Qxg6/hxg6 traded queens legally.
- Rh4/Rdh8 kept the forward rook protected from Kg3. Nxe5-d3xb2xc4 won three pawns with successive attacks on White's rook. Ne3 was supported by d4. However, Rf7+ and Rxd4+ opened the position and White's active rooks recovered d4, g7 and c7 while my rooks remained passive on the h-file. Kc5 attacked Rd4 and avoided a checking Nf7 fork; R8h6 then defended g6.
- 36...Nh7 avoided the prospective Re6+ fork of king/knight. The actual sequence Rxh7 Rxh7 Nxh7 Rxh7 correctly exchanged both knights and one rook each; no lost piece hidden in that sequence. Rd6+ then exposed g6, and Rxg6 left me a pawn down. Active king play Kb4-a3xa2 restored equal pawn counts.
- The rook ending still failed: White's g/h passers were much farther advanced than my a/b pawns. ...a5 did not establish a winning or drawing race. ...Re7-e3+-e4+, ...Re1 and ...Rg1+ failed to keep the white king away from shelter. Final White Kh6/Rd8/g6,h5 versus Black Ka2/Rg1/a5,b7; g7-g8 promotion was supported by the eighth-rank rook. Practical resignation, not engine-verified forced-mate analysis. No claim that the three-pawn lead was objectively winning, but it was plainly not converted.
- Cumulative174: 58W/4D/112L. MAX0W/2D/56L, skill0 45W/2D/11L, nominal1800 13W/0D/45L, each58 games. Elo1390 [1270,1520], 116 rated total/latest50, 58MAX excluded. Storage59,039,331bytes.

## Trial24 fixed evaluation complete — games169–174
- All six predetermined games retained: 1W/1D/4L, 225 own moves / 451 plies, 3 illegal submissions. All six passed the narrow first15-move immediate-material-loss observation, but this did not predict later safety or conversion.
- Baseline after168:1410 [1280,1530]; after174:1390 [1270,1520]. Cumulative58W/4D/112L. Descriptive small-block change only, not a causal estimate.
- Failed transfer:169 lost a whole rook to a checking pawn promotion fork;170 was mated;172 lost a bishop to reciprocal bishop capture and drew with opponent cooperation;173 lost a whole rook after inventing a backward pawn recapture, then rejected a rook move through its own king;174 failed to retain/convert a three-pawn lead. 171's win involved severe opponent errors. The earlier practice43 rook drop to a pawn was already negative evidence.
- Positive local observations are limited:173 avoided a d1/h5 bishop fork before capturing h5;174 correctly executed the Nh7 exchange sequence and several king/rook defenses. These do not establish sustained improvement. The destination-check focus failed as a general method; replace it before the next fixed block.


# Trial25 — literal recaptures (declared 2026-10-03 11:09:25 UTC)

Baseline:174 scored,58W/4D/112L; provisional Elo1390 [1270,1520]. Fixed next evaluation:games175–180, all six retained in the existing MAX W/B, skill0 W/B, nominal1800 W/B rotation. No result-dependent extras or extension. Endpoint remains200 scored benchmarks.

Weakness: I repeatedly treat an imagined recapture as real even when the pawn moves backward, a bishop changes diagonal, or my own king blocks a rook. Longer speculative calculations have not prevented these errors.

Chosen intervention: replace the broad destination checklist with a literal recapture check. For a material transaction I rely on, identify the piece's actual origin and destination and the intervening occupied squares after the preceding capture. A remembered defender is not sufficient. Prioritize the immediate forcing reply in the current referee board before broad speculative branches. No per-move speed limit and no new mandatory long checklist. Similar geometric ideas have failed before; this is a narrower procedural revision, not a novel or proven method.

Bounded study/practice:20minutes combined, ending no later than11:29:25UTC. Exactly four remembered cases, no searches for extra examples:173 before41.Rxg3 (ply80),173 after56...Rxh7+ (ply112),172 before18...Qxf5 (ply35),174 before36...Nh7 (ply71). First three get one explicitly chosen legal alternative line each; the fourth is the successful actual five-ply exchange. Mechanical own-PGN reconstruction and legality checks only, including the known failed submissions; no evaluation/search/attack-map/candidate generation. Corrections to my factual recollection may be recorded, not concealed.

Then exactly two MAX drills, each capped at10 own moves or natural completion, with the shared deadline overriding both caps. First:White from game173 ply80, trying to preserve material without a backward recapture. Second:new self-constructed White position `r7/1k6/1p4PP/p4K2/8/8/7R/8 w - - 0 1`, concentrating on clear rook support behind passed pawns. This second setup is chosen by me and is not an independently assessed test; no claimed starting evaluation. Stop at the cap/deadline even if favorable. No repeats or extra practice.

Observable transfer: incorrect claimed recaptures, illegal submissions, major-piece losses caused by direction/obstruction errors, and the whole six-game W/D/L plus Elo/interval. Record any successful local decisions without treating them as evidence of a general improvement. Independently chosen benchmark replies, not remembered-case success, are the transfer test.


## Four remembered cases reviewed (between games, 2026-10-03)
Mechanical results are in `literal-recaptures-25-legality.json`; explicit script retained. No engine, move menu, search, attack map, or evaluation. Sixteen supplied plies were legal and the three known failed submissions were illegal. This includes two actual pre-error captures, not sixteen independent test items.

1.173/ply80:Rxg3 Rxg3 h4g3 fails because White must increase its pawn rank when capturing: h4 can capture g5, not g3. I had correctly used that same h4 pawn to support Qg5 earlier, then reversed its direction. One chosen alternative Rf3 Rg6 Ne4 was legal; it merely avoids that specific invented recapture, with no claim of best play or complete safety.
2.173/ply112:Rh2xh7 fails because the path includes occupied h6, my own king. Legal escape Kg5 Rg7+ Kh4 does not repair the earlier rook loss or establish a viable endgame.
3.172/ply35:Bf7f5 is vertical, not diagonal. The imagined intermediate e6 would make it two bishop moves with a change of diagonal, not one move. Actual Qd7xf5 Qc2xc7 Qf5d7 is legal and still concedes c7; legal is not synonymous with good.
4.174/ply71:Nh7 Rxh7 Rh6xh7 Ng5xh7 Rh4xh7 is legal. The last rook path becomes clear specifically because h6 has been vacated. Both knights and one rook on each side disappear; each side retains one rook. This successful local transaction did not prevent losing the subsequent rook ending.

These are remembered examples. Correct reconstruction after seeing the failures is not transfer evidence. Continue with the two declared drills only.


## Declared practice complete — 2026-10-03 11:20:57 UTC
Both own practice PGNs read. Exactly two MAX drills,20 own moves/40 plies total,0 illegal submissions. Both stopped at10-own-move caps, both unfinished, no wins or draws claimed. Learning ended before11:29:25 deadline; no extra practice or result-dependent extension.

- Practice45, White from remembered173/ply80: `41.Rf3 Rxb4 42.Ke2 Rxh4 43.Rxg3 Rbxd4 44.Rxd4 Rxd4 45.Rd3 Rb4 46.Rd2 Rb3 47.Kf2 a5 48.g3 Kf6 49.Ne4+ Ke5 50.Nc3 Bf5 *`. Stopped11:15:27.416172UTC, resultseq1385 hash`77ccc2830105eca599cbb2005fd834f14fe3f2232a4962b82d53976a5b7f68bb`. Avoided the backward h4xg3 fiction; captured g3 only after ...Rxh4 moved the opposing rook off the g-file. The actual rook exchange on d4 was legal and equal. Nc3 had the real forward b2xc3 pawn recapture available. However, the initial two-pawn surplus disappeared: lost b4,h4,d4 and captured g3. Final White Kf2/Rd2/Nc3/b2,c5,g3 versus Black Ke5/Rb3/Bf5/a5,c6,f7. Equal material and an active opposing king/rook, not an established draw or good evaluation.
- Practice46, White from the self-constructed setup: `1.h7 Rf8+ 2.Kg5 Rc8 3.h8=Q Rc5+ 4.Kf6 Rc6+ 5.Kg7 Rc8 6.Qh4 Rc7+ 7.Kh6 Ka7 8.Qg4 Ka6 9.g7 Rc6+ 10.Kh7 Rc7 *`. Stopped11:20:57.162415UTC, seq1408 hash`c6f4ae3d216052aa3020bf4fac69f2341e7a1e49c907d5c6afa1264f285f06ac`. Promoted with a clear rook support path; opponent chose rook checks instead of capturing the new queen. Kept queen and rook. Later Kh6 knowingly blocked the h-rook file, so I explicitly stopped relying on a recapture through it; Qg4 and g7 used the separate clear g-file, and Kh7 answered a check without blocking that queen support. Final White Kh7/Qg4/Rh2/g7 versus Black Ka6/Rc7/a5,b6. Material advantage in an intentionally chosen favorable setup, no full conversion within cap and no independent starting evaluation.

Decision: test the narrower recapture procedure in the predetermined175–180 block. Remembered repair success and favorable promotion practice do not establish benchmark transfer. Baseline remains174 scored,58W/4D/112L,1390 [1270,1520].


## Benchmark175 — White MAX, loss by mate (2026-10-03 11:46:09 UTC)
- Referee 39...fxg1=Q#:39 own moves/78plies,0illegal submissions. seq14317,hash`141dc3c69f7f84b1a3349058772d056ffe88bfd554caedfb90d8319d134e1f86`,snapshot`c6b009634dfa1b1a077889183e2b7883abb48f882372176df219a82f710f3274`. Own full PGN read.
- Castled5, all minors developed7, Re1 10/Rad1 15; first15 no immediate material loss. Bg5/Bxf6/Qxf6/Nd5 chased the queen. b4 met ...Na5 and ...Nxc4 with the real forward d3xc4 recapture, preserving material but creating doubled c-pawns.
- 16.Ne3 escaped c6's attack but blocked the queen's e4 defense; ...fxe4 won a pawn and attacked Nf3. Nd2/f3/exf3/Nxf3 used the intended legal knight recapture. Kh1 left the a7-g1 pin before further knight movement. Qd3 defended c4, but Qe4 and Qc2 moved away; after ...Bxe3 Rxe3 the remaining c4 defender had been exchanged, allowing ...Bxc4. Two pawns down.
- Qf2 added f3 protection; Qe2 kept the diagonal defense while removing the queen from behind Nf3 on the f-file. Actual ...Bxf3 Rxf3 Rxf3 gxf3 traded minor pieces and one rook pair with legal recaptures. No backward pawn move or blocked rook capture was submitted. This is a narrow observation, not proof the method improved play.
- The heavy-piece ending deteriorated. Qg2/Rg1 created a g7 entry threat, met by Qf7. Rf1 defended f3 but ...e4 created new tension. Re1 left the battery; Qf1 defended f3/h3, but ...exf3 and ...f2 created a dangerous passer. Re3/Re2 did not stop the attack. Referee-confirmed finish ...Qf3+ Kh2 Qg3+ Kh1 Qg1+ Qxg1 fxg1=Q#. I recognized the final promotion recapture and rook support before submitting the forced queen capture; recognition at that late point did not prevent mate.
- Cumulative175:58W/4D/113L; MAX0W/2D/57L(59),skill0 45W/2D/11L(58),nominal1800 13W/0D/45L(58). Elo remains1390 [1270,1520],116rated total/latest50,59MAX excluded. Storage60,025,276bytes. Trial25 fixed block continues through180; no additional study now.


## Benchmark 176 — Black, maximum strength, loss (2026-10-03)
Read the complete referee PGN after resigning following 34.dxc6. 33 own moves, 67 plies, zero illegal submissions. Castled on move 8, completed minor development by move 9, and connected a rook with Re8 on move 10; the first 15 moves contained no immediate own material drop. Later 20...Nc5 obstructed the queen's c-file defense after the b5 pawn was removed, and 21.Nxc4 lost another pawn. The decisive failure was 32...Nxc6 33.bxc6 Qxc6?? 34.dxc6: I deliberately sacrificed the knight while considering the different d-pawn recapture, then noted the actual d5 pawn remained but nevertheless placed the queen on its capture square. The queen loss was unintended. This directly contradicts the trial's proposed post-capture reconstruction habit; zero illegal moves did not establish safe play. Final material: down a queen and knight with six pawns each; practical resignation, not a proved forced mate.
Verified cumulative score: 58 wins, 4 draws, 114 losses in 176 scored games. Maximum strength 0/2/58 in 60 games; skill 0 45/2/11 in 58; nominal 1800 13/0/45 in 58. Provisional engine-relative Elo remains 1390, 95% credible interval [1270, 1520], latest 50 of 116 rated games; 60 maximum-strength games excluded. Storage 60,499,458 bytes. Trial 25 so far: 0/0/2, 72 own moves, 145 plies, zero illegal submissions. Continue the declared evaluation through game 180.


## Benchmark 177 — White, skill 0, win
Complete own PGN read. Checkmate with 30.Qf7#, 30 own moves / 59 plies, zero illegal submissions. Castled on move 4, minors developed by 7, Rad1 on 9. The central d-pawn was lost with 14...Nxd4, and c2 fell later, so this was not a clean first-15 material record. Opponent 11...Nf4 omitted recapturing Be7; 16...Qc6 omitted exf4; 18...Ne3 put the knight on the actual f2 pawn's forward capture square, and 19.fxe3 took it. 20...Qxc3 gave up its queen for a knight; 21.Qxc3 was a clear one-step recapture. Converted the resulting huge advantage through checks and Bxf6+ gxf6, then Qc7+ Kf8 Qf7# supported by Bd5. This is successful conversion of severe opponent errors, not evidence of general strength improvement.
Verified cumulative: 59/4/114 in 177 games. Skill 0 now 46/2/11 in 59. Provisional Elo 1400 [1280,1530], 117 rated total / latest 50; 60 maximum-strength games excluded. Trial 25 so far 1/0/2, 102 own moves, 204 plies, zero illegal submissions. Continue through game 180.


## Benchmark 178 — Black, skill 0, win
Full own PGN read. 28...Rxf1#; 28 own moves, 56 plies, zero illegal submissions. Castled on move 5, minor development by 9, Rad8 on 12; no immediate material drop in the first 15. 8...a6 provided the actual a7 retreat when a5 later chased Bb6. Gained pawns with axb5, fxe4 and Rxf2, then completed Rxf1+ Nxf1. Explicitly noticed that an e4-pawn advance would uncover Qc2's diagonal to Qg6, so first used Bd5: the later 22...e3+ was a discovered check, forcing White to respond, and 23.Bf3 allowed 23...Qxc2. White also left Ra1 and Nf1 to be captured; converted with Qf2+ Kh1 Rxf1#. Useful correct local line reconstruction and conversion, aided by major opponent errors; not proof of transfer across strengths.
Verified cumulative 60/4/114 in 178 games; skill 0 47/2/11 in 60. Elo 1410 [1290,1540], latest 50 of 118 rated games; 60 maximum games excluded. Trial 25 so far 2/0/2, 130 own moves, 260 plies, zero illegal submissions. Continue the declared trial to 180.


## Benchmark 179 — White, nominal 1800, loss
Full own PGN read after practical resignation following 35...Nd7. 35 own moves, 70 plies, zero illegal submissions. Castled 6, minors 7, Rae1 9. First-15 material record failed: 14.Nf5 Bxf5 15.exf5 removed the e4 pawn's defense of d5, allowing 15...Nxd5. 20.Nh4 left the knight on the queen's e7-f6-g5-h4 diagonal; 20...d5 attacked Bc4 simultaneously. I chose 21.Bxd5 cxd5 22.Nf3, conceding a bishop for a pawn to save the knight. Later 29.f4 met the Qe5/Bd6 mating battery; after ...exf3 en passant, I recognized the opened e-file queen contact and exchanged queens before Nxf3. Rxd5 recovered a pawn. But 33.Rd4? Be3+ repeated the checking bishop fork pattern, losing an exchange after Kh1 Bxd4 Nxd4. Final: White Kh1 Rf1 Nd4 and a2,b2,f5,g5,h3 versus Black Kg8 Ra8 Re8 Nd7 and a6,f7,g7,h5: a whole rook down for one pawn, no forced-mate proof. Correct local recaptures coexist with loss of defenders, an exposed knight, and a checking fork; the trial has not prevented the targeted failures.
Verified cumulative: 60/4/115 in 179 games; nominal 1800 13/0/46 in 59. Elo 1400 [1280,1530], latest 50 of 119 rated games. Trial 25 so far 2/0/3, 165 own moves, 330 plies, zero illegal submissions. Finish declared evaluation with game 180.


## Benchmark 180 — Black, nominal 1800, draw by stalemate
Complete referee PGN read. 56 own moves / 112 plies, zero illegal submissions. Castled on 5, completed minor development with Bd7 on 14, Rfe8 on 16; first 15 contained no immediate own material loss. Won a pawn, but 20...Rxa5 and 21...dxe5 allowed 22.Qxc7, forking Ra5 and Bd7. 22...Raa8 preserved the rook and 23.Qxd7 lost the bishop. This was a direct failure to inspect the opponent's immediate double attack. White later chose Qxf7+ Qxf7 Bxf7+ Kxf7, allowing the king to take the bishop and restoring material; I do not claim that recovery was forced against other choices. Rxb7+ then Rxd5 led to two rooks and four pawns each. The central pawns reached d2/e3, but both were captured after fxe3 and R4xd2; no promotion, and no verified claim that the earlier position was winning. A rook exchange led to a pawn ending with Black two pawns against three. White's Ke1 allowed Kxe3, and gxh4 created an outside passer. In the final position I explicitly chose 55...h2 56.g6 hxg6, correctly anticipating stalemate: White Kh1 is not checked; g1 is attacked by h2, and g2/h2 by Kg3. Referee confirmed stalemate. This is a correct local ending calculation, not proof that drawing was optimal throughout the game.
Verified cumulative 60 wins / 5 draws / 115 losses in 180 scored games. All three opponent classes now have 60 games: maximum 0/2/58; skill 0 47/2/11; nominal 1800 13/1/46. Provisional Elo 1400 [1270,1520], latest 50 of 120 rated games; 60 maximum-strength games excluded. Storage 62,450,224 bytes.

## Trial 25 fixed evaluation concluded at 180
Games 175–180: 2 wins, 1 draw, 3 losses; 221 own moves / 442 plies; zero illegal submissions. Four of six had no immediate own material loss in the first 15. Baseline after 174 was 1390 [1270,1520]; endpoint 1400 [1270,1520]. A ten-point change within these intervals is not sustained improvement evidence. Both wins were against skill 0 and included severe opponent errors. Remembered legality checks and two unfinished drills did not prevent 176's direct queen loss to a pawn, 179's undefended-knight/defender-removal errors and checking fork, or 180's queen fork. Legal recaptures and one correct stalemate calculation are local positives, not evidence that the general problem is solved. Decision: abandon literal-recapture emphasis as sufficient, and try a small candidate-comparison exercise focused on the first opposing check or double attack. No rating-method, opponent, move-rule, or past-record changes.


# Trial 26 — first opposing reply

Declared 2026-10-03 12:46:45 UTC after 180 scored benchmarks and no active game. Hard learning deadline 13:06:45 UTC. Baseline 60/5/115; provisional Elo 1400 [1270,1520]. Fixed evaluation games 181–186, exactly one full existing rotation; no extra benchmarks or altered endpoint based on results. The whole experiment still stops at 200 scored games.

Weakness: long own-plan calculation has repeatedly missed the opponent's first check, direct capture or double attack. This overlaps earlier unsuccessful trials and is not a novel or validated method. Compare the actual failed move against one deliberately quieter alternative in exactly three remembered positions: game 176 after ply 65, game 179 after ply 64, game 180 after ply 41. Supply the lines myself before mechanical reconstruction; verify only their legality, SAN and board state, never search, evaluate, enumerate alternatives or ask for advice. Remembered examples are not an independent test.

Then exactly two maximum-strength drills, each stopped at 10 own moves or an earlier terminal result, no repeats or replacement drills. First: White from game 179 ply 64, avoiding the remembered Rd4/Be3+ checking fork. Second: White in this self-constructed, materially balanced position: r3r1k1/pp3ppp/8/2b5/2B5/8/PP3PPP/R3R1K1 w - - 0 1. It has two rooks and one bishop per side, with five pawns each. This is new to this run, self-selected and uncalibrated; not an independent evaluation. If the time cap arrives, end an unfinished drill and return to benchmarks without adding drills.

Playing change: before committing a material capture or rook/queen move, compare the intended move with one safe-looking alternative and identify the opponent's first forcing reply from the actual post-move arrangement. Prefer a candidate for which that reply has been accounted for; do not treat a planned recapture as the only threat. No timer or longer mandatory checklist during play, no claim that extra thought itself is learning. Track accepted check/capture forks, whole-piece drops, illegal attempts, W/D/L and Elo interval over the fixed block. Resume normal legal moves using only my own reasoning and the referee during games.


## Remembered-case comparison — trial 26
Mechanically reconstructed only the three declared own-game positions and the explicitly supplied lines. All 20 supplied plies were legal: 11 plies from actual failures and 9 from chosen alternative lines. These are remembered cases, not 20 independent tests, and legality does not certify safety or best play. In 176, Qd8 c7 Qd7 avoids the immediate d5xc6 queen capture but leaves the earlier knight deficit and dangerous pawns. In 179, h4 Be3+ Kh1 leaves the rook on d5, outside that bishop's d4 capture square, but does not repair the earlier bishop deficit. In 180, Qe7 exd6 Qxd6 puts the queen where a later Qxc7 can be answered by Qxc7 and retains defense of Bd7; White is not required to select that supplied line. No automated scoring, search, attack-map analysis or recommendations were used.


## Practice 47 — remembered position, maximum strength, loss
Started from benchmark 179 ply 64, already a bishop down for a pawn. Terminal result before the 10-own-move cap: 8 own moves / 16 plies, zero illegal submissions; 40...R8e3# at 12:51:16 UTC. Complete practice PGN read: 33.h4 Nc6 34.Rd3 Re4 35.Kg2 Rae8 36.Rd7 Ne5 37.Nxe5 Bxe5 38.Rh1 Re2+ 39.Kf3 Bb8 40.Rhd1 R8e3#. Avoided the exact Rd4/Be3+ fork and exchanged the knights legally, but the final move failed against the first forcing reply. I had considered a rook check on e3 but wrongly assumed the king could escape; the other rook remained on e2, covering f2/g2, while Bb8 and h5 restricted the remaining squares. This is negative evidence for the proposed habit in practice. No replacement drill or extra remembered-case study; continue with the one declared new position.


## Practice 48 and learning cutoff — trial 26
New self-constructed equal-material position, White versus maximum strength. Stopped at exactly 10 own moves / 20 plies, zero illegal submissions, 12:54:47 UTC, before the 13:06:45 deadline. Full practice PGN read: 1.h3 Rxe1+ 2.Rxe1 Rd8 3.Kf1 g6 4.Ke2 Rd7 5.Kf3 Kf8 6.Re4 Bb6 7.b3 Rd2 8.Re2 Rd6 9.Ke4 h5 10.g3 Bc5 *. One rook pair disappeared immediately, limiting the intended two-rook test. I mobilized the king, supported Bc4 with b3, and answered ...Rd2's pawn threats with Re2; material remained equal. Final White Ke4 Re2 Bc4 with a2,b3,f2,g3,h3; Black Kf8 Rd6 Bc5 with a7,b7,f7,g6,h5. Unfinished is neither a draw nor a win.
Learning period now closed: exactly three remembered cases, one failed remembered-position drill, one short unfinished self-selected drill, no additional drills or replacements. The failure in practice 47 is strong evidence that merely identifying a nominal first check is insufficient when its escape squares are misread. The legal supplied lines and balanced short drill do not establish general improvement. Proceed with the already fixed benchmark block 181–186 and record all outcomes.


## Benchmark 181 — White, maximum strength, loss
Full own PGN read after resignation following 25...Rxe1+. 25 own moves / 50 plies, zero illegal submissions. Castled 5, Re1 on 7, minor development by 10. First-15 material record failed: the 11.d4 exd4 12.cxd4 Nxd4 13.Nxd4 Bxd4 sequence lost a pawn, and 14.Nb3 allowed the immediate checking fork 14...Bxf2+ of Kg1/Re1. After Kh1 Bxe1 Qxe1 Qxb2, I was an exchange and three pawns down. The Bxb7/Bxb7/Rxb7 transaction recovered a pawn and exchanged bishops, but I only partly accounted for the back-rank reply: 23...Qa1+ 24.Ne1 Rc1 overloaded the knight's queen defender, and 25.Kg1 Rxe1+ lost the knight. Practical resignation: White Kg1 Qe3 Rb7 and a2,e4,g2,h2 versus Black Kg8 Qa1 Re1 Rf8 and a4,c7,d6,f7,g5,h6, a whole rook and two pawns down. No forced-mate proof. Considering an initial forcing reply did not amount to calculating its consequences correctly; direct negative transfer evidence in the first fresh trial-26 game.
Verified cumulative 60/5/116 in 181 scored games. Maximum strength 0/2/59 in 61; other opponents unchanged. Elo remains 1400 [1270,1520], latest 50 of 120 rated games, 61 maximum games excluded. Storage 63,891,980 bytes. Trial 26 so far 0/0/1, 25 own moves / 50 plies, zero illegal submissions. Continue fixed evaluation through 186, preserving all results.


## Benchmark 182 — Black, maximum strength, loss
Full own PGN read after practical resignation following 30.Qxd7. 29 own moves / 59 plies, zero illegal submissions. Castled 8, minor development by 12, Rfe8 on 13; first 15 without an immediate material drop. The closed center and white b4/d5 pawns restricted both knights. The a-file pawn and bishop exchanges were legal and level in material. White's two knights then overloaded c4's sole queen defense: 25.Naxc4 could not be met by Qxc4 because Nd2xc4 would take the queen. 28.Nxd6 took a second pawn and attacked Re8; I preserved the rook with Rf8. But 29...Qd7?? walked directly onto White Qa4's clear a4-b5-c6-d7 diagonal. 30.Qxd7 took the queen, with no recapture. I overlooked a simple first capture while considering longer knight/bishop continuations, exactly contradicting the trial. Final material: a queen and two pawns down (White seven pawns, Black five), with both sides still having two rooks, two knights and one bishop. No forced-mate claim.
Verified cumulative 60/5/117 in 182 scored games. Maximum strength 0/2/60 in 62; skill 0 47/2/11 in 60; nominal 1800 13/1/46 in 60. Elo unchanged 1400 [1270,1520], latest 50 of 120 rated games, 62 maximum games excluded. Storage 64,341,269 bytes. Trial 26 so far 0/0/2, 54 own moves / 109 plies, zero illegal submissions. Continue the unchanged evaluation through 186; 18 scored games remain until the overall stop at 200.


## Benchmark 183 — White, skill 0, win
Full own PGN read after 95.Qb2#; 95 own moves / 189 plies, two illegal submissions. Castled 5, Re1 on 8, minor development by 11; first 15 without a material drop, but exchanges left tripled c-pawns. Bxc5/Bxc5/Rxc5 and Rb5/Rxb5/axb5/axb5 lost two pawns; Qxb5 recovered one. First illegal attempt was 32.Rb1-b4 through my own Qb3. More seriously, 35.Rb5 uncovered Qa3 to Qd6 along d6-c5-b4-a3; Black chose ...h6 instead of taking the queen. Qxd6 Nxd6 then attacked both my rook and knight, but Ne6+ gained time to escape and Rxe5 recovered the second pawn. The f4/Rxe5/fxe5 rook exchange used an actual legal pawn recapture. In the knight ending, ...c5 displaced the defender of e6 and Kxe6 won that pawn. Checks recovered b6 and h6 after Black took c2, while 59.h5 provided a real defender for Ng6. Black eventually took c3. Second illegal attempt was 80.Kg4xg5, overlooking Nf7's protection of g5. I corrected the route via Kh5/Kg6/Kg7, captured Nh8 and promoted h7 on move 85; Black took Nf5. Then Qxc4/Qxg4 removed the pawns, Qe2 restricted the bare king, and king approach supported Qb2 mate. Positive local endgame conversion, but two illegal attempts, an exposed queen the opponent declined, and opponent king moves delaying the pawn race prevent treating this win as evidence of a reliable new tactical habit.
Verified cumulative 61/5/117 in 183 scored games. Maximum 0/2/60 in 62; skill 0 48/2/11 in 61; nominal 1800 13/1/46 in 60. Referee Elo 1390 [1260,1510], latest 50 of 121 rated games, 62 maximum games excluded; a rolling estimate, not a per-win guaranteed increase. Storage 64,925,037 bytes. Trial 26 so far 1/0/2, 149 own moves / 298 plies, two illegal submissions. Continue fixed evaluation through 186. Seventeen scored games remain to the overall stop.


## Benchmark 184 — Black, skill 0, win
Full own PGN read after 28...Qd1#; 28 own moves / 56 plies, zero illegal submissions. Minor development by 8, castled 10, Rfe8 on 15; first 15 without a material drop. Answered Qb3's b7 threat with Qc8 and used actual cxd6/hxg6 recaptures. The legal 16...exf3 en-passant capture and 17...Rxe3 won two pawns after White castled away. But 19...dxe4 boxed Re3 behind its own e4/f3 pawns; 20.Kd2 attacked the rook, and Rd3+ Bxd3 exd3 Kxd3 conceded the exchange and a pawn. This is another own-pawn blocker/mobility failure, not a fully calculated sacrifice. The remaining rook and queen developed threats against the exposed king: Qe4+ Rd3 Qe1 Rdd2 Re2 attacked both rooks, supported by f3 and Qe1. Rdxe2 fxe2 retained a protected advanced pawn. I chose Qd1+ to clear e1 for promotion; the referee established it was already checkmate. I had not accurately enumerated every escape before submission, so do not claim a fully foreseen mating combination. Positive concrete double-attack/recapture sequence and a recorded win, alongside an earlier rook trap and opponent king exposure.
Verified cumulative 62/5/117 in 184 scored games. Maximum 0/2/60 in 62; skill 0 49/2/11 in 62; nominal 1800 13/1/46 in 60. Elo 1400 [1280,1520], latest 50 of 122 rated games; 62 maximum games excluded. Storage 65,387,936 bytes. Trial 26 so far 2/0/2, 177 own moves / 354 plies, two illegal submissions. Two nominal-1800 games remain in this fixed block; sixteen scored games remain in the overall experiment.


## Benchmark 185 — White, nominal 1800, win
Full own PGN read after 42.Qf7#; 42 own moves / 83 plies, zero illegal submissions. Castled 7, minors by 8, Rad1 on 10; first 15 without material loss. After fxe6, I answered ...Nc4's queen/bishop fork with Qe2 but missed ...Nxb2's combined rook attack and opening of Qc7's line to Nc3. Rd3 protected c3 while conceding the exchange after Nf5 Nxd3 Qxd3. Nd5 Nxd5 exd5 produced connected central pawns. After fxe6/dxe6, Black's Rxf5 allowed the real Qd3-e4-f5 recapture, restoring material equality; Bxf3/Rxf3 then exchanged bishops. Local positives: h3 supplied a real escape against Qb1+; Be3 interrupted Bb6's support of a possible ...Qg1 mate after the tempting Rg3; I correctly rejected g7 captures while Qa1 defended g7. Black then allowed Bxb6 and Bxc7, yielding a large advantage, and the supported e-pawn promoted on 35.
Strong negative evidence despite the win: 36.Qe4+?? dropped the newly promoted queen directly to ...d5xe4. I falsely assessed a mating net while overlooking the immediate pawn capture, repeating the precise trial target. The original queen, rook and bishop still gave a large advantage. I subsequently captured e4, coordinated Qe8/Rf8, legally took the undefended checking queen with Kxg2, and gave Qf7 mate after ...g6. The opponent's piece losses, delayed resistance to promotion and final queen sacrifice were material contributors. This is a measured nominal-1800 win, not evidence that the first-reply habit became reliable.
Verified cumulative 63/5/117 in 185 scored games. Maximum 0/2/60 in 62; skill 0 49/2/11 in 62; nominal 1800 14/1/46 in 61. Elo 1410 [1290,1540], latest 50 of 123 rated games; 62 maximum games excluded. Storage 65,904,178 bytes. Trial 26 so far 3/0/2, 219 own moves / 437 plies, two illegal submissions. One game remains in the fixed block; fifteen scored games remain to the overall stop at 200.


## Benchmark 186 — Black, nominal 1800, loss; trial 26 evaluation
Full own PGN read after practical resignation following 25.Rxe8+. 24 own moves / 49 plies, zero illegal submissions. Castled 7, minors by 9, Re8 on 10; first 15 without material loss. dxe5 and the queen exchange won a pawn. Rd3 was actually supported by e4; Nxb6/axb6 legally traded a bishop for a knight but doubled b-pawns. White's g-pawn advances drove Bf5 to e6 and Nf6 to h5. Be6 blocked Re8's defense of e4; I recognized that Nh5 left e4 undefended. g6/Bxh5/gxh5 was a legal minor-piece trade; Rxe4 restored equal pawn counts. Then 24...Bd5?? removed the e6 blocker, exposing undefended Re8 to 25.Rxe8+. I considered my rook's attack down the file while missing the opponent's immediate capture up that same file. There was no recapture: Rd7 did not defend e8 and Kg8 was two files away. Resigned a whole rook down, with six pawns each: White Re8,Ra1,Bc1; Black Rd7,Bd5. This is a practical material judgment, not a forced-mate proof.
Verified cumulative 63/5/118 in 186 scored games; each opponent has 62 games. Maximum 0/2/60; skill 0 49/2/11; nominal 1800 14/1/47. Elo 1420 [1300,1550], latest 50 of 124 rated games; 62 maximum games excluded. Storage 66,393,913 bytes.
Trial 26 final: 3 wins, 0 draws, 3 losses; 243 own moves / 486 plies, two illegal submissions. Five of six games passed the narrow first-15 material check, but later failures included a checking bishop fork, two direct queen drops (182 and the promoted queen in 185), a rook lost on the opened e-file, a blocked illegal rook move, and an illegal king capture ignoring a knight defender. Wins included concrete local conversions and significant opponent errors. Elo moved 1400 [1270,1520] to 1420 [1300,1550]; overlapping intervals, changing rolling-window composition and repeated targeted mistakes do not support a reliable improvement claim. Comparing a quieter candidate and naming the first reply did not reliably produce an accurate final board. Change the next trial to actual defender/blocker reconstruction; no extra trial-26 games. Fourteen scored games remain to the stop at 200.


# Trial 27 — actual defenders after a move

Declared 2026-10-03 14:33:10 UTC after 186 scored benchmarks and no active game. Hard learning deadline 14:53:10 UTC. Baseline 63/5/118; Elo 1420 [1300,1550]. Fixed next evaluation: games 187–192, one unchanged rotation, with no additions based on results. Overall stop remains 200 scored games.

Target the recurring mismatch between an intended attack and the actual post-move board: moving a blocker exposes my own rook; a promoted queen is still capturable by a pawn; a pawn recapture can trap its own rook. Exactly three remembered comparisons, supplied before mechanical checking: game 185 after ply 70, game 186 after ply 47, game 184 after ply 37. Verify only legality/SAN/FEN of the supplied lines; no search, evaluation, attack-map generation or advice. These are remembered cases, not independent tactical tests.

Chosen lines: 185 actual Qe4+ dxe4 versus Qe7 Qe5+ Qxe5 (the alternative keeps clear of the d5 pawn's e4 capture and answers only that supplied queen check). 186 actual Bd5 Rxe8+ versus Rd8 Re8+ Rxe8 (the alternative puts the rook on d8, where the d7 rook supports it, and supplies an actual recapture against the remembered e8 check). 184 actual dxe4 Kd2 Rd3+ Bxd3 exd3 Kxd3 versus Rxe4 Bd3 Re8 (rook recapture leaves the e-file free for retreat instead of blocking it with my pawn). Opponents are not obliged to select the supplied alternatives; legality does not certify safety or best play.

Then exactly two maximum-strength drills, each capped at 12 own moves or an earlier terminal result, no repeats or replacements. First: Black from game 186 ply 47, using my chosen Rd8 instead of the remembered Bd5. Second: White from a new self-constructed equal-material position, r3r1k1/pp3pp1/2b5/7p/7P/2B5/PP3PP1/R3R1K1 w - - 0 1. Two rooks, one bishop and five pawns per side; each bishop initially guards its e-file rook. Self-selected and uncalibrated, not independent evaluation. If the deadline arrives, end any unfinished drill and return to the fixed benchmark block without replacement practice.

Playing change: for a critical move, reconstruct the resulting placement briefly and name the actual defender, if any, of an exposed rook/queen and the opponent's direct pawn capture. Do not infer protection from a nearby king, an adjacent rank, a rook behind my own blocker, or the fact that I am giving check. Prefer a supported piece or a clear retreat when available. This substantially overlaps earlier failed trials; no novelty or improvement claim. Do not expand this into a longer compulsory checklist or speculative search. Track direct piece losses, blocker/defender errors, illegal attempts and W/D/L/Elo on the fresh fixed block.


## Remembered reconstruction — trial 27
Checked the three declared own-game positions and supplied lines only. Final report contains 20 legal supplied plies and one rejected ply; these include repeated starts and are not independent tests. The original 186 repair line was wrong: after Red8, the bishop still on e6 blocks White's proposed Re4-e8, so that reply was illegal and the following recapture was never tested. Preserved the failed line. Corrected same-case continuation Red8 Bb2 Rd3 was legal; the d8 rook now really supports d3 through the vacated d7/d6/d5/d4 squares. This shows a legal alternative arrangement, not best play or an opponent obligation. In 185, Qee7 Qe5+ Qxe5 was legal and avoids the immediate d5xe4 capture, but begins from an already overwhelming remembered advantage. In 184, Rxe4 Bd3 Ree8 legally retains an open retreat file; the actual pawn recapture blocked that retreat. The failed reconstruction is negative evidence for my board accuracy even in remembered cases. No search, scoring, attack maps or move recommendations used. End remembered work and perform the two declared drills without additions.


## Practice 49 — remembered position, maximum strength, unfinished
Full practice PGN read. Black from 186 ply 47, stopped at exactly 12 own moves / 24 plies at 14:42:03 UTC, zero illegal submissions. 24...Red8 25.Bb2 Rd3 26.h4 Bf5 27.Re7 R3d7 28.Rxd7 Rxd7 29.c5 bxc5 30.bxc5 Rd2 31.Bf6 Kf8 32.c6 bxc6 33.a4 Rc2 34.a5 c5 35.a6 Be4 36.Rd1 *. The known Bd5/Rxe8+ loss was avoided. Rd8 supplied the actual d7 recapture, and Bf5/Be4 supported Rc2 via e4/d3. The b-pawn captures were legal and yielded a one-pawn lead. Final Black Kf8 Rc2 Be4 with c7,c5,f7,h7,h5; White Kg1 Rd1 Bf6 with a6,f2,g5,h4. White's advanced a-pawn and Rd1's back-rank threat remain unresolved at the cap; the bishop's route toward a8 depended on moving c6 out of its way. Positive short retention of material after a remembered repair, not a win/draw, independent transfer test, or established favorable evaluation. No extension or replacement.


## Practice 50 — new self-constructed position, maximum strength, loss; learning cutoff
Full practice PGN read. Terminal mate before the 12-own-move cap: 8 own moves / 16 plies, one illegal submission, 14:46:25 UTC. 1.Rac1 f6 2.Kf1 Rxe1+ 3.Kxe1 Bxg2 4.Kd2 Rd8+ 5.Ke3 Re8+ 6.Kf4 Re4+ 7.Kf5 Kf7 8.f4 g6#. The king recapture itself was legal, but removed the king's defense of g2 and lost that pawn. My attempted 4.Ke1-f1 was rejected because Bg2 already attacked f1; I then played Kd2. The repeated checks drove the king into a constrained position. I recognized ...g6 as a mating threat but falsely assumed f4 created an escape on g4 by blocking Re4's fourth-rank line. Black's h5-pawn still attacked g4, so the anticipated escape was illegal and ...g6 was mate. This is direct negative practice evidence for defender/pawn-square reconstruction, not a successful generalization. No replacement or additional practice.

Learning period closed at 14:46:51 UTC, before the 14:53:10 hard deadline. Exactly three remembered cases (including the preserved failed alternative), one remembered-position drill stopped at 12 moves with unresolved threats, and one new self-selected drill lost in 8 moves. Twenty legal supplied verification plies and one rejected ply do not establish tactical competence; neither drill counts toward benchmark score. Retain the stated concise move habit and test its actual fresh-game behavior in the already fixed games 187–192. Do not claim learning success from notes or remembered repairs. Overall stop remains 200 scored games.


## Benchmark 187 — White, maximum strength, loss
Full own PGN read after resignation following 24...Rdf8; 24 own moves / 48 plies, zero illegal submissions. Castled 5, Re1 on 7, minor development by 11. Re2 supplied an actual extra defender of f2 against ...Ng4, and the knight retreated. First-15 material check failed: dxc4 removed the e4 pawn's defender while Be3 blocked Re2, allowing ...Nxe4. Bxc5/Nxc5 exchanged bishops without repairing the pawn deficit. The doubled rooks on e1/e2 really supported one another, b3 supported c4, and c4 supported Nd5. But 22.Nf1 removed Nh2's control of f3. I considered other central threats while overlooking 22...Nf3+, which forked Kg1, Qd2 and Re1. Kg2 Nxd2 Rxd2 exchanged my queen for a knight. Final White Kg2,Re1,Rd2,Nd5,Nf1 and six pawns versus Black Kg8,Qd7,Rf7,Rf8,Ne6 and seven pawns. Practical resignation with queen-for-knight deficit plus a pawn, not a forced-mate proof. Two direct fresh recurrences of the trial's defender-removal error; the remembered repair did not transfer reliably.
Verified cumulative 63/5/119 in 187 scored games. Maximum 0/2/61 in 63; skill 0 49/2/11 in 62; nominal 1800 14/1/47 in 62. Elo unchanged 1420 [1300,1550], latest 50 of 124 rated games; 63 maximum games excluded. Storage 67,869,191 bytes. Trial 27 so far 0/0/1, 24 own moves / 48 plies, zero illegal submissions. Continue the fixed block through 192; thirteen scored games remain to the stop at 200.


## Benchmark 188 — Black, maximum strength, loss
2026-10-03T15:08:13.073724Z; 27 own moves / 55 plies; zero illegal submissions; resigned after 28.d7. Result seq 15298, hash d48e16097a5d3f586d149e4caa1b0fc34520c5bb6817fbecfca80faa92cab0de. Castled 8, all minors developed 9, first rook activation 10; first 15 moves material-clean. The c4 pawn from ...bxc4 became isolated and fell to Nxc4. 21...Rb8 22.Ba4 Rf8 allowed 23.Nd7, forking both rooks; ...Rc8 Nxf8 Qxf8 cost the exchange. 25...Rc7 really defended Bb7 along the seventh rank, but 26.d6 attacked that rook and its retreat would abandon the bishop; ...Rc6 Bxc6 Bxc6 cost a second exchange. Final Black Q+2B+N+6P versus White Q+2R+B+7P, with White pawn on d7. Practical resignation, not a verified forced-mate claim. Actual recaptures were legal, but placement/next-reply errors persisted; no positive transfer claim. Trial 27 now 0W/0D/2L, 51 own moves/103 plies/0 illegal. Cumulative 63W/5D/120L over 188; max 0/2/62, skill0 49/2/11, nominal1800 14/1/47. Elo 1420 [1300,1550], latest 50 of 124 rated games; 64 max excluded. Storage 68,356,901 bytes. Fixed evaluation continues through 192; bounded endpoint remains 200.


## Benchmark 189 — White, skill 0, loss
2026-10-03T15:16:52.432562Z; 37 own moves / 74 plies, zero illegal submissions; resigned after 37...Qxe7. Result seq15374 hash b4154454ca9dbdc2a3af96a068408bc4a2bb312470e7af5954431b90b5f98c58. Castle5, minors7, rook9, first15 material-clean. 17.Qd3 allowed ...Nxb2 forking queen and rook; ...c5 declined the rook, allowing Re1. ...Nc4 also uncovered Bg7 toward Ra1; the opponent again declined that exchange. Later Bc3/R1e2/Bd4 created two attackers on Re3 and Qe1 Bxe3+ Rxe3 actually lost the exchange. 35.Ne7 attacked Rg8 and was initially queen-defended; after ...Rg6 Qxf7+ Rg7, 37.Qf6 overlooked the new Rg7-e7 backing for ...Qxe7 (Qxe7 would be answered Rxe7). Final Q+6P versus Q+R+6P, practical resignation, not forced-mate proof. Recovered f7 pawn and some legal recapture checks were local positives, outweighed by repeated forks and overloaded/changed defenders; no transfer improvement. Trial27 0/0/3, 88 own moves/177 plies/0 illegal. Cumulative63/5/121 over189, max0/2/62, skill0 49/2/12, nominal1800 14/1/47. Elo1410 [1290,1540], latest50 of125 rated,64max excluded; storage68,866,758. Continue fixed evaluation through192, bounded200 endpoint.


## Benchmark190 — Black, skill0, win
2026-10-03T15:23:52.579882Z;28 own moves/56 plies/0 illegal;28...Qb2#;resultseq15432 hashe33124c9a7e1136269e0196fd0ff2bee9baf547bee3556a0d4eb4aa25332e2a9. Castle10,minors11,rook12;first15 material-clean after recovering gambit pawn with9...Bxc5. Strong dependence on opponent errors:13.Ne5 Nxe5 14.f3 declined recapture;15...Nxd2 16.Qd1 declined again;16...Nxf1 17.Bc7 left bishop toQxc7. Saved Nf1 withNe3 supportedBc5;Nc4 really pawn-defended, laterNf4 queen-defended andBe3 knight-defended. White22.h4 ignored Be3 attack on queen;...Bxd2 Kxd2 won queen for bishop. Qxe2+ supportedNf4, thenNd3+Kb1Qe3Rd2Qxd2h6Qb2#: final queen supportedNd3 and king escapes enumerated before submission; referee confirmed mate. No illegal moves or direct losses beyond chosen bishop-for-queen exchange, but finish planning was slow; easy blunders do not establish improvement. Trial27 now1/0/3,116 own moves/233plies/0illegal. Cumulative64/5/121 in190;max0/2/62,skill0 50/2/12,nominal1800 14/1/47. Elo1420[1300,1550],126rated/latest50,64maxexcluded;storage69,356,138. Evaluation remains187–192;10 scored games remain to200.


## Benchmark191 — White, nominal1800, loss
2026-10-03T15:30:48.675353Z;27own/54plies/0illegal;resigned after27...Rxc3;seq15488 hash3b1a63bf45b87b545409a6244904c9201d50e8fc258fdde60f8a04f5ca798ded. Castle7,minors8,rook10,first15material-clean. 15.Rxf2 put rook on bishop diagonal;16.exd5 Bf5 17.dxc6 Bc5 gained two pawns but pinnedRf2 and allowed ...Bxf2 after queen/rook exchanges. Rxc2/Rxb2 recovered both extra pawns, bishop trade left N versus R and five pawns each. 26.Kc4 defendedNc3; after ...Rc2,27.Kd5 protectedc6 but abandonedNc3 to ...Rxc3. Exact defender-removal recurrence, despite recognizing rook's file attack. Final WhiteKing+5P vsR+5P; practical resignation, no forcedmate proof. Local real recaptures and material-clean opening did not transfer into reliable middlegame/endgame defense. Trial27 1/0/4,143own/287plies/0illegal. Cumulative64/5/122 in191;max0/2/62,skill0 50/2/12,nom1800 14/1/48. Elo1410[1290,1540],127rated/latest50,64maxexcluded;storage69,847,633. Finish192 before next declared learning period; endpoint200 unchanged.


## Benchmark192 — Black, nominal1800, loss
2026-10-03T15:41:58.983563Z;32own/65plies/0illegal;resigned after33.h8=R+;seq15555 hash418524b13e1877d3ee0c2645985514f5f2d7babd8b12a236ce773d4bbd40d72a. Castle5,minors10,rook11;first15material-clean. Bxh5 won the pawn after h5/Ng5. Qc7 correctly vacated d8 before moving its d6 blocker, but Rce8 allowed Nb5 fork of Qc7/Bd6. ...Qb8 h5 Ne5 Nxd6 Nxg4 traded bishops, thenRh4 Nf6 Nxe8 Qxe8 lost exchange. ...Re6 really supportedNf6 before ...g6 removed the pawn defender. But ...Bd5 Rxd5 Nxd5 vacated f6 blocker on Ba1–h8, enabling h7+Kf8 h8=R+; underpromotion actually to rook, not queen as forecast. FinalBlackQ+R+N+5P vsWhiteQ+2R+B+5P; practical resignation down rook, not forcedmate proof. Strong repeated fork/blocker failures despite some locally correct protection.
Trial27 final1W/0D/5L,175own/352plies/0illegal,5/6 first15material-clean. Elo1420[1300,1550] before and after: no measured increase, and errors targeted recur. Remembered checks and practice did not show generalization. Cumulative64W/5D/123L in192;max0/2/62,skill0 50/2/12,nom1800 14/1/49. 128rated/latest50,64maxexcluded;storage70,356,966. No activegame.


## Trial28 — retain the defender
Declared 2026-10-03T15:43:45.536224+00:00 after192 with no active game. Hard learning deadline 2026-10-03T15:55:45.536224+00:00. Fixed evaluation193–198 (maxWhite/Black,skill0White/Black,nominal1800White/Black); no additions, replacements or extensions based on results. Baseline64/5/123,Elo1420[1300,1550].
Weakness: active king or rook moves abandon an attacked piece; knight forks remain frequent. Two remembered comparisons only:191 after26...Rc2 (actualKd5 Rxc3; chosenKd4 Rc1 Ne4),188 before22...Rf8 (actualRf8 Nd7 Rc8 Nxf8 Qxf8; chosenRe7 Nd7 Rc8). Mechanical reconstruction and legality of these supplied lines only, no search/evaluation/candidate generation. Then exactly one maxWhite drill, capped at8 own moves or earlier terminal, from own constructed equal R+N+5P FEN 8/p3kppp/1p3n2/8/3K1PP1/1PN4P/P1r5/7R w - - 0 1. It is a selected, related setup, not an independently sampled test. No repeat if loss or early terminal. Close learning when completed or deadline, then fixed evaluation.
Playing change: prefer a move that preserves an attacked piece's actual defender or moves that piece to support; briefly check the moved king/rook's former duty and the opponent's immediate knight/pawn capture. This refocuses earlier unsuccessful methods, not a novel proven checklist. Track abandoned defenders, knight forks, direct major-piece losses, illegals, WDL/Elo. Practical evidence would be fewer such errors in new benchmark positions, not correct recalled lines alone.


Learning28 remembered checks:13/13 supplied plies legal (7 actual,6 alternative), two known cases and repeated starts, not independent examples or evaluations.191 alternativeKd4 retains adjacent protection ofNc3 againstRc2; suppliedRc1/Ne4 leaves knight supported byKd4.188Re7 avoids placing both rooks onNd7's attack squares; after suppliedNd7,Rc8 saves the only attacked rook whileQd8 supportsRe7. Opponent continuations were chosen by me, not forced or best-play proofs. No attack maps, search, scoring, engine analysis, or move generation used.


Practice51 — White vsMAX, own related setup, unfinished at8 own/16plies,0illegal. Stopped2026-10-03T15:47:09.350117Z,seq1514 hash754538abc6019deb428ccbafaa0ff88b8d8a0b50263a1c3a374ed5a90bbde030. Actual:1.Nd5+ Nxd5 2.Kxd5 Rxa2 3.Re1+ Kd7 4.Kc4 Rf2 5.f5 a5 6.Rb1 Kc6 7.Kd4 Rf3 8.h4 Rf4+*. Knight stayed king-defended through exchange but abandoning its a2-pawn duty lost a pawn; early trade reduced mixed-piece test. Rb1 deliberately replaced king protection ofb3 beforeKd4, and f5 pawn advanced to g4 support. FinalWhiteKd4Rb1Pb3f5g4h4 vsBlackKc6Rf4Pa5b6f7g7h7;Whiteincheck and1Pawn down, no favorable evaluation or win/draw claim. No repeat/replacement. Related self-selection, not independent test.
Learning28 closed early after all declared activities, before12minute deadline.13remembered legal plies do not establish transfer; practice mixed/negative. Preserve concise defender focus for fixed193–198 evaluation; no extra study within block. Endpoint remains200.

Closed at 2026-10-03T15:47:39.642048+00:00


## Benchmark193 — White, MAX, loss
2026-10-03T15:58:20.929388Z;32own/64plies/0illegal;resigned after32...Nxe1+;seq15621 hash1a8dfd672f0cafc81c6f8e04f668028a7aeb14d288fbb50e02980e6c6e4de119. Castle5,minors7,rook12;first15FAIL:14.Nh4 b4 15.Ne2 Nxe4 lost pawn after sole defender forced away. Some limited local checks: avoided ...g5 queen/rook pawn fork byQe1, chosehxg4 rather thanRxg4 to keepRf4 blockingRf8's attack onNf3, and movedQe1-e2 before ...Nf3+ instead of allowing immediate queen fork. Then afterKf1 Qg3,32.Qe1 put queen back on the same knight attack square; ...Nxe1+ captured queen while uncoveringRf8's check onKf1, preventing an immediate rook recapture. Long speculative escape analysis missed the direct capture, undoing earlier local success. FinalWhiteR+N+5P vsBlackQ+R+N+6P; practical resignation, not forcedmateproof. Strong negative transfer evidence. Trial28 now0/0/1,32own/64plies/0illegal. Cumulative64/5/124 in193;MAX0/2/63,skill0 50/2/12,nom1800 14/1/49. Elo1420[1300,1550],128rated/latest50,65MAXexcluded;storage71,364,292. Fixedblock193–198 continues;7scored remain to200.


## Benchmark194 — Black,MAX,loss
2026-10-03T16:07:40.889800Z;25own/51plies/0illegal;resigned after26.Qxa8+;seq15674 hash8989770c969e3a71b53685d0df28c379e68b5281ee9a71c6727281a3712c7f40. Castle8,minors9,rook10,first15material-clean. Central dxc5/cxd6 won two pawns forWhite whileknights forced back; ...fxe5 eventually recovered one. Some actual protection maintained:16...Bc6 defendedNd5 againstopenedQd1file; ...Nb6 vacated bishop line whileNa5 still defendedBc6; ...Re6 supportedNb6 andsavedrook fromd7 pawn; ...Rd6 wasactuallyBf8-supported, soRxd6 Bxd6 exchangedrooks. But25...Qxb6 recapturedbishop and abandonedRa8 toQf3–e4–d5–c6–b7–a8:26.Qxa8+ lostwhole rook. Repeated defended-piece abandonment despite long local recapture analysis. FinalWhiteQ+R+N+6P vsBlackQ+B+5P, practical resignation, no forcedmateproof. Trial28 0/0/2,57own/115plies/0illegal;oneof2first15clean. Cumulative64/5/125 in194;MAX0/2/64,skill0 50/2/12,nom1800 14/1/49. Elo1420[1300,1550],128rated/latest50,66MAXexcluded;storage71,867,857. Fixedblockthrough198;6remaining to200.


## Benchmark195 — White,skill0,loss
2026-10-03T16:22:48.583660Z;31own/62plies/0illegal;resigned after31...Bxd6;seq15738 hash6dd26a0362cc7d1e0115572b0e7ec521736bf815d14cbc28ce7fbea1c6a04ccf. Castle6,rook7,minors9,first15material-clean. Ba4 had no safe retreat after ...c4 and ...b5:17.Bxb5 axb5 18.Nxb5 conceded bishop for2pawns.19.Qf3 maintainedBf4 recapture againstNh5 fork andQxf4 waslegal.23.Ng4 openedQf4–d6 defense, but ...Ng6 attackedqueen and24.Qf3 abandonedNd6;opponentKh8 declinedQxd6,allowingNf5. AfterNxg6+fxg6,29.Ne7 attackedQc8 but vacated f5 blocker,overlookingRf8xf3 queen capture.30.Nxc8 capturedBlackqueen, so this was ultimately a queen-for-queen transaction, not a netqueen loss; however ...Rf7 leftNc8 with attacked retreat squares,31.Nd6 Bxd6 lost it. FinalWhite2R+7P vsBlack2R+2B+5P; practical resignation2bishopsfor2pawnsdown, no forcedmateproof. Attack failed, repeated omitted duties/blockers and trappedpieces; long calculation not progress. Trial28 0/0/3,88own/177plies/0illegal;2/3first15clean. Cumulative64/5/126 in195;MAX0/2/64,skill0 50/2/13,nom1800 14/1/49. Elo1410[1290,1540],129rated/latest50,66MAXexcluded;storage72,376,642. Continuefixedblockthrough198,thenbounded200;5scoredremain.


## Benchmark 196 — Black versus skill 0 — win, 49...Rh1#
Completed 2026-10-03T16:42:46.090879+00:00; 49 own moves / 98 plies; 0 illegal attempts. Result seq 15838, sha256 19b0bcdebacf1a707ff7645600db4a59aa2ea36dbb9036a5761ce53caba5811d; snapshot 61ef64fbeb4090ae7f8b4f821394108711a7be107c3ffe6408c042d23049a42b. Full saved PGN read. Castled move 10, both minors developed by 9, rook developed 11; no material loss in first 15 moves.
Local positives: the e4 pawn supported ...Nd3; ...Qe8 supported e4 before ...f4. 27.Qxd3 exd3 28.Rxe8 Rfxe8 exchanged both queens and gained an exchange, NOT an unopposed queen win. My initial commentary about the offered queen was corrected after the complete exchange. 32...Re1 allowed Rxd2, losing the advanced pawn. 34...Bxf4 attacked Rd2, which 35.Kg4 left available; ...Bxd2 won it. After ...Rxf2, Bxd2 Rxd2 exchanged bishops; 40.h5 left Bc2 for ...Rxc2. Opponent errors were decisive.
The two-rook conversion was slow. I spent excessive time considering rook arrangements and noticed several hypothetical king captures before submission; these were not illegal attempts or played sacrifices. The final ...Rg5 (supported by Kg6), ...Rc1, ...Rh1# was deliberately selected despite d8=Q: the promoted queen could not answer the h-file check. This is a local successful finish after multiple opponent concessions, not strong-opponent transfer evidence.
After 196: 65W/5D/126L; MAX 0/2/64, skill 0 51/2/13, nominal 1800 14/1/49. Provisional Elo 1400 [1280,1520], latest 50 of 130 rated games; 66 MAX excluded. The rolling estimate fell despite this win. Storage 72,921,540 bytes. Trial 28 evaluation continues through 198; no extra study or practice added.


## Benchmark 197 — White versus nominal 1800 — draw by unintended stalemate
Completed 2026-10-03T16:52:33.367410+00:00; 46 own moves / 91 plies; 0 illegal attempts. Result seq 15931, sha256 066c07424d0372cc1c765e17cb5ffb4b255da293166a21d11d3cef912d28bdae; snapshot 930a2af7dbb3f1d1cbe63bfe3861e53184ceecae26285b63454e2904ff3c6197. Full PGN read. Castled 9, all minors developed by 8, rook developed 11; first 15 without material loss.
12.Nd5 removed the knight's e4 defense while Be3 still blocked Qe2; opponent played ...h6 instead of capturing e4. I recognized this after the reply and restored pawn support with 13.f3. Later Bf2 cleared Qe2's e4 defense before f4. The central knight and rook exchanges were materially even; 43...Qxc6 was met by the actual d5 pawn recapture 44.dxc6. These are local correct recaptures, with an earlier reprieve explicitly retained.
The opponent declined to recapture 40.Bxb6 (40...Kf8); Bxa5 and Bxd6 then left me a bishop and two pawns ahead. After ...a5, c7 Kh7, I promoted 46.c8=Q and STALEMATED Black. I had falsely assumed a spare black pawn move remained. In fact a5 was blocked by a4, e5 by e4, f7 by f6, and g6 by g5; none had a capture. The queen controlled g8/h8, f6 controlled g7, g5 controlled h6, and g6 was occupied. Black was not checked and had no move. This is failed conversion, not a successful draw-saving decision or a win. No unplayed continuation is counted.
After 197: 65W/6D/126L; MAX 0/2/64, skill 0 51/2/13, nominal 1800 14/2/49. Elo 1410 [1290,1540], latest 50 of 131 rated games; 66 MAX excluded. Storage 73,456,294 bytes. Trial 28 remains fixed through 198; no additional study yet.


## Benchmark 198 — Black versus nominal 1800 — loss by resignation
Completed 2026-10-03T17:02:53.992795+00:00; 33 own moves / 67 plies; 0 illegal attempts. Seq 16000, sha256 9ac7bcba2db359fa2f37746c1f631e0fa36cda6aba4a9ca8560321a16beb6a58; snapshot b0c8330e3007c153a9e0501c225294d766633f6dd8551149849c8faef8377f16. Full PGN read. Castled 7, minors developed by 8, rook 12; first 15 without material loss.
17...Bf5 put the bishop on the queen's open diagonal, c2-d3-e4-f5. 18.Qxf5 captured it: the rook on f8 could not recapture through my own Bf6. I missed the actual blocker. 18...Bxd4 recovered a pawn and opened the rook's attack on the queen, but did not recover the lost bishop. The later bishop/knight exchanges were not a material recovery. At 32.Rxd5 cxd5, moving c6 abandoned the c-file blocker and 33.Rxc8+ captured the rook. Resigned after 34.Qd3 with Q+R+5P against Q+R+2N+4P; a practical resignation, not a proven forced mate.
After 198: 65W/6D/127L; MAX 0/2/64, skill 0 51/2/13, nominal 1800 14/2/50. Elo 1400 [1270,1520]; latest 50 of 132 rated games; 66 MAX excluded. Storage 73,980,754 bytes.

## Trial 28 closed — fixed benchmarks 193–198
1W/1D/4L, 216 own moves / 433 plies, zero illegal attempts; 5/6 first-15 material-loss screens passed. Elo 1420 [1300,1550] to 1400 [1270,1520], overlapping wide intervals. The remembered comparisons and single capped practice did not yield reliable transfer. Major-piece losses, abandoned defenders and a blocked rook line recurred. Game 196's rook mate was a local success following opponent concessions. Game 197 preserved material well for much of the game but failed conversion by stalemate; its early e4 reprieve is retained. No sustained improvement demonstrated. The declared evaluation is complete; no replacements or extensions.


# Trial 29 — final bounded review: complete the immediate position

Evaluation: benchmarks 199 and 200 ONLY, the remaining fixed White/Black maximum-strength pair. Stop the entire experiment at 200 scored games. Baseline after198:65W/6D/127L; provisional Elo1400 [1270,1520]. MAX games are excluded by the unchanged rating method, so this pair cannot by itself update that Elo.

Weakness: remembered recapture rules have not reliably survived actual blockers, and a successful promotion in197 immediately stalemated. Keep the decision focused on the resulting concrete position, rather than extending speculative branches.

Bounded activity: at most eight minutes from the declaration timestamp below. Review exactly two remembered cases from my own games:198 before17...Bf5 and197 before46.c8=Q. Compare each played move/sequence with one manually selected alternative, using only reconstruction and legality of explicitly supplied moves. No move generation, search, attack-map code or evaluation. No external study and no opponent-practice game in this final trial. No extra examples, repeats or extensions. Close early when these two comparisons are complete, then play199–200.

These are known positions. Selecting this plan already included mentally considering alternate sequences; this is remembered correction work, not a blind or independent test. Mechanical legal acceptance will establish only legality of the supplied line. A chosen opponent reply does not establish best defense.

Implementation cue: name the immediate reply against the candidate and verify its real line to the target in the resulting position; at a near-terminal move include whether the opponent has any move. Keep this brief. This revises focus within already tried methods, not a newly proven improvement.

Observe in199–200: direct material losses from imaginary defense/abandoned blockers, legality rejections, first-15 material-loss screen, W/D/L and any terminal-position error. Two maximum-strength games are a small descriptive check, not causal evidence or a demand for a win.

Declared: 2026-10-03T17:05:20.547411+00:00; hard study deadline: 2026-10-03T17:13:20.547411+00:00


## Remembered review and closure
Both saved starting positions were reconstructed from my own PGNs. All 15 explicitly supplied plies were legal: 3 played plies and 12 alternative plies, over exactly two remembered cases. No move menu, engine evaluation, search or attack-map code was used. Legality data and the fixed verifier are saved alongside this note.

198, after17.d4: played ...Bf5 Qxf5 loses the bishop because Bf6 blocks Rf8. Chosen ...Bf7 b5 axb5 instead keeps the bishop on f7, actually supported by Rf8 and Qe7, and uses the existing a6 pawn to meet b5. This is one legal selected continuation, not evidence that ...Bf7 is optimal or that White must play b5.

197, before46.c8=Q: the recorded promotion stalemated because all four black pawns were blocked and the king's remaining squares were covered. Chosen line:46.Be7 Kh8 47.c8=Q+ Kh7 48.Qh3+ Kg8 49.Bd8 Kf8 50.Qh8#. The supplied moves are mechanically legal; the final mate annotation is my manual rule assessment, not engine analysis or a separately played practice result. At the end Qh8 checks Kf8, the queen covers e8/g8, Bd8 covers e7, Pf6 covers g7, f7 is occupied, and the black pawns have no moves. The initial black reply was chosen, so this line alone is not a best-defense proof. Crucially, Bd8 deliberately leaves f8 available before the final check instead of making another stalemate.

The reviews repaired known examples only. They do not erase the two benchmark errors, demonstrate generalization, or establish a stronger playing method. No fresh case or opponent practice was added. The next and final evaluation is199–200.

Learning closed: 2026-10-03T17:06:22.099464+00:00; stopped early after the two planned comparisons.


## Benchmark 199 — White versus maximum strength — loss by resignation
Completed 2026-10-03T17:19:23.454171+00:00; 37 own moves / 74 plies; zero illegal attempts. Seq16076, sha25614e3def92b311c963e59a21eddfc9ea2489940e91a8e3fdd3eeb7192b31086e9; snapshotc75587b002479f336c1ff64d1ad8945b7ecffbec37cd70698c311f99d2e1de05. Full PGN read. Castled5, developed minors by7, rook15; first15 without material loss.
The familiar opening was changed with11.Nd5 Nxd5 12.exd5 and13.e4. Material remained level initially, but18.Nd2 abandoned the knight's actual defense of d4;20...exd4 won that pawn. This is recurrence of defender removal after the final review, not evidence that the cue worked. The rook trades and26.Nxg4 Qxe4+27.Qxe4 Bxe4+ were actually even exchanges except for the pawn already lost. I distinguished ...Qxe4+ from the different ...Bxe4+ line rather than blindly recapturing a bishop with the queen.
No direct major-piece loss or terminal-position error occurred. The resulting knight was tied to g4, Black's bishop restricted king routes, and the king penetrated f7-f6-g5-f4-e3-d2-c2. After37...Kxb2 the ending was N+4P versus B+6P with an advanced black d-pawn; I resigned practically. No forced-win proof or engine evaluation was obtained. The clean major-piece record is a local positive, but the pawn-defense failure and poor endgame activity remain.
After199:65W/6D/128L; MAX0/2/65, skill0 51/2/13, nominal1800 14/2/50. Elo unchanged1400 [1270,1520];132 rated, latest50;67 MAX excluded. Storage74,506,059 bytes. Exactly one benchmark remains. No additional study before200; final trial remains fixed199–200.
