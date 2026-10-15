# Geometry cards from my games

My own reconstructions from recorded play. These are reminders, not engine-verified evaluations or evidence of improvement.

## Opened defender: game 8, after 20.Qe1

Relevant pieces: Black Qa5, Nb4; White Bd2, Qe1. The line is e1–d2–c3–b4–a5.

Bxb4 removes the knight and vacates d2. Qa5 now attacks the bishop on b4, but Qxb4 Qxb4 loses the black queen. A queen behind a pinned knight is not sufficient defense when the capturing bishop is backed by another queen. Count the final recapture and its value.

## Rook rank: game 8, after 31.Rg7+

White Rg7 and Qh6; Black Kf7, Bb7, Qd5, Re5, Ra8. The rook's leftward ray is g7–f7–e7–d7–c7–b7, ending at the black bishop. Every empty square on that ray is controlled, not just f7.

Ke8 Qh8+ leaves no king escape. Qg8 Qxg8# finishes the game. The black king on e8 prevents Ra8 from traveling through e8 to interpose on f8 or g8.

## Discovered check: game 7, final net

Before 29...Rc8+, Black Rc3 shielded Bb4 from White Kd2. Moving the rook to c8 uncovered Bb4–c3–d2 and controlled c1/c2/c3 along the c-file. Bb3 controlled d1 via c2. White's own Be2 and e3 pawn occupied two other escape squares. Kd3 was forced, then Bc2+ forced Kd4 and Bc3# followed.

The alternative 29.Ke1 in the preceding position allowed Rc1#, checking with both rook and bishop. Capturing the rook with Ra1 would leave the bishop check unresolved.

## Use before a forcing line

1. Identify occupied squares along each relevant ray, including my own blockers.
2. After each move, update the vacated and occupied squares before assigning checks or defenders.
3. At a check, count every checking piece and every legal king escape before calculating a longer continuation.
4. At an exchange, finish the recaptures and count material; one expensive defender may not protect a target from a cheaper supported attacker.

## Queen changes line: game 9, after 55...Be1+

White Kg3, Rg7, Ne5, pawns a2/c2/f4; Black Kc8, Qd5, Be1, pawns a4/b6/f5. I chose 56.Kh3 to avoid Qxf4 with check, but missed 56...Qh1# along d5–e4–f3–g2–h1.

On h1, the queen checks along the h-file. Be1 controls g3 and h4, while f5 controls g4. The queen controls g2 and h2. White cannot capture the queen or interpose on h2, so every response fails. The alternative Kh2 avoids this particular immediate mate; it is not a claim that the losing position could be saved.

The missed check came from a change of line: the queen traveled diagonally, then attacked along a file. Checking only the most prominent capture, Qxf4, was insufficient.

## Optional recapture: game 11, 21.Qe4?

Black Qf4 and Bb7 both attacked e4 through clear paths. I placed my queen there while imagining a queen exchange followed by minor-piece exchanges. Black instead played Bxe4. After a white bishop or knight recapture, Black was not obliged to put its queen on e4; after Rxe4, it could move the attacked queen away. A defended queen was still available to the cheaper attacker. The played 22...g5 23.Rxf4 gxf4 subsequently reduced my loss to an exchange, but did not justify 21.Qe4.

## Illegal king recapture: game 11, 45.Ne5?

Relevant pieces: White Kf4 and Nf3; Black Rd5, Ng4, and h5 pawn. I played Ne5 and counted Kf4 as a defender. After ...Nxe5, the knight on e5 was protected by Rd5 along d5–e5. Kxe5 would move into rook check and was therefore illegal. The king's adjacency did not make the knight safe.

## Pawn pinned to king: game 12, after 48.Ra5

White Ra5, Black b5 pawn and Kc5 lie on a5–b5–c5. I submitted ...b4, forgetting that vacating b5 would expose the king to the rook. The referee rejected it. The played ...Kb6 kept the pawn defended and removed the pin; ...b4 followed after 49.Ra8. This was one illegal submission, not an infrastructure fault.

## Rook check inventory: game 12, after 56...Rf5?

White: Kg2, Re7, Rb3, pawns f2/g3/h4. Black: Kc5, Rf5, Rc2, pawns f7/g7/h6. My move had defended f7 while leaving king and rook aligned on the c-file.

The two white rooks have four checking moves: Re7–c7, Re7–e5, Rb3–c3, and Rb3–b5. The local answers to the latter three are ...Rxe5, ...Rxc3, and ...Kxb5 respectively. These are square-by-square reconstructions, not engine evaluations.

57.Rc7+ instead creates c7–c6–Kc5–c4–c3–Rc2. The king blocks Rc2 from reaching the checking rook or interposing above the king. The f5 rook cannot interpose on c6. The legal king escapes d4/d5/d6 all leave c2 unprotected; the played ...Kd6 58.Rxc2 lost the rook.

Inspecting only nearby checks missed the remote rook move to c7. Check the rank/file intersections for **each** enemy rook after the final candidate. This repeats the king-and-major-piece alignment error from game 6, with a rook instead of a queen behind the king.

## Bishop protects the queen's mating square: game 13

After 20...Bf3+, White Kg2 was checked by Bf3, supported by the black e4 pawn and Rf8. Kxf3 was illegal. I played 21.Kh2?, allowing 21...Qh4+ 22.Kg1 Qh1#.

After Qh4+, g1 was the only legal king escape: Qh4 controlled h3/g3 and the h-file, while Bf3 controlled g2/h1. On h1 the queen was protected by that same bishop along f3–g2–h1. At the final position, my Rf1 and f2 pawn occupied two escape squares, and Kg1 blocked Rf1 from capturing Qh1. Qe1 was also blocked by my rook and king. No capture, interposition, or king move resolved the mate.

Before choosing Kh2, I could instead consider 21.Nxf3, capturing the bishop with Nd2. After ...exf3+, 22.Kg3 is a legal escape in my reconstruction. Removing Bf3 removes its protection of h1. This is an untested alternative to the played mating line, not proof of a draw or a saved game. Other king choices at move 21 have not been exhaustively assessed.

The earlier weakening 16.g4 Nxg4 17.hxg4 Bxg4 removed both kingside pawns. I had considered the sacrifice but underestimated the resulting attack. Counting a nominal extra minor piece did not establish king safety. Retaining the pawn cover with a move such as 16.Qe2 is an untested earlier alternative.

## Queen exchange changes the back rank: game 14, move 18

After 17...Qd8 18.Nf6+, I initially wanted ...Nxf6, expecting exf6 and a queen exchange on d4. White could instead use 18...Nxf6 19.Qxd8 Rxd8 20.Rxd8+ Ne8 21.Rxe8#. The knight's departure from d7 opens the whole d-file. Re8's capture on d8 then opens the eighth rank to White's rook. Bc8 blocks Ra8, h7 is still occupied by Black's pawn, and White's h6 pawn controls g7. I rejected ...Nxf6 at move 18 and played ...Kf8.

This mating reconstruction applies before White captures h7. After 19.Nxh7+ the escape-square inventory changes; the old mate label must not simply be copied into the later position.

## Promotion threat prevents recapture: game 14, final position

The played sequence was 21.Qb4+ Re7 22.h7 Kg7 23.Qxe7. I resigned with a rook and two pawns less. The tempting 23...Qxe7 allows 24.h8=Q#. Rh3 protects h8 through the newly vacated h7 square and controls h6. Nf6 and the new queen cover g8/h7; e5 protects the knight on f6; Black's own f7/g6 pawns occupy the remaining nearby squares. Bc8 blocks Ra8 from reaching h8, and Qe7 cannot capture the new queen. This verifies that recapture fails, not that every defense immediately mates. The legal ...Qh8 retains the queen but does not recover the lost rook.

Earlier, ...g6 kept the h-file closed but left White's h6 pawn beside the king. The knight checks removed h7 and turned that pawn into a promotion threat. A blocked rook file did not establish king safety. The alternative 15...gxh6 16.Rxh6 removes the advanced pawn but opens lines; it is untested, not a proved saving line.

## Preserve the recapture ray: game 15, move 10

After 9.e4 Bxc3, I chose 10.bxc3 instead of Qxc3. Keeping Qc2 behind Bd3 allowed 10...dxe4 11.Bxe4 Nxe4 12.Qxe4: the bishop's departure cleared c2–d3–e4. With Qc3 instead, that last queen recapture would not exist. This was a correctly checked local exchange, not proof that 9.e4 was best.

## Cheaper attacker backed by the queen: game 15, move 24

After 23...Qb7, White had Qc6/Rb6 and Black had Qb7/Bc8. I used 24.Rxb7. The possible ...Bxb7 25.Qxb7 would exchange my rook for Black's queen and bishop. The played ...a4 instead left the queen unrecovered. This is the favorable side of the supported cheaper-attacker pattern that cost me material in earlier games. Count the actual capture order rather than assuming the offered queen trade.

## Knight protects the mating queen: game 15, finish

After 30...f5, f6 was empty. The played 31.Ng5+ was protected by Be7 along e7–f6–g5. After ...Kh6, 32.Qh8+ forced ...Kg6, and 33.Qh7# followed. Ng5 protected h7 and controlled f7; Be7 controlled f6 and defended Ng5; Qh7 controlled h6; Black's own f5/g7/h5 pawns occupied the remaining adjacent squares. There was no capture or interposition against the adjacent diagonal queen check.

My unplayed reconstruction against 31...Kg6 was 32.Qf7+ Kh6 33.Rxe6+ g6 34.Qh7#. That line was calculated mentally, not submitted to a referee or verified by an engine. The actual shorter finish was confirmed as mate by the referee.

## A rook behind the queen does not make the trade equal: game 16

The sequence 16...e4 17.dxe4 Bxe4 cleared d3 and put Be4 on the diagonal to White's Qc2, while also attacking Nf3. White played 18.Rc1, defending the queen with a rook. I used 18...Bxc2: even ...Rxc2 would leave a queen exchanged for a bishop. White instead played h3 and left the bishop unrecovered. This repeats the optional-recapture lesson from game 11 with the colors reversed.

After 20...Bxf3 21.exf3, White's e-pawn no longer occupied e2. The knight could consequently use ...Ne5–d3 without an e2 pawn capture. White's 23.Rf1 left Rc1 attacked, and ...Nxc1 took it. The played ...Nb3 later preserved the knight when White again declined a recapture.

## Adjacent ranks and the last escape square: game 16, finish

The finish was 29...d3 30.Rc3 Bxc3 31.bxc3 Qe1+ 32.Ka2 Re2#. The pawn advance opened Bf6–e5–d4–c3–b2 and threatened a supported queen mate on b2. Capturing the interposing rook removed White's last piece.

In the final position, Qe1 controls a1/b1 along the first rank, Re2 controls b2 along the second rank, and Na5 controls b3. White's own a3 pawn occupies the remaining king escape. Re2 is protected by both Qe1 and d3. White's remaining pawns cannot capture the rook or interpose on b2/c2/d2. The referee confirmed checkmate.

## Decline the automatic rook recapture: game 17, move 31

After 30.Ne5 Rxb4, White had Rc4/Ne5 and Black had Rb4/Nd5/Qe8 with a pawn on c6. The immediate Rxb4 Nxb4 would exchange rooks and leave the b-pawn lost. I instead played 31.Rxc6. Ne5 protected c6, making ...Qxc6 Nxc6 favorable to White. The observed ...Nb6 left the rook on c6 and restored the material count to a one-pawn lead. Choosing whether to recapture is part of the position, not an automatic step in the exchange.

## Interpose and defend the attacked rook: game 17, move 39

After 37.Rc8 Rxc8 38.Nxc8 Qe5+, Black's queen checked Kh2 along e5–f4–g3–h2 and also attacked Rd4. White Qf3 moved to f4. The queen now blocked the check and protected d4 along f4–e4–d4; Rd4 simultaneously protected it along the same rank. The played ...Qxf4+ 40.Rxf4 therefore traded queens without losing the rook. The board geometry was verified before moving the rook off d1, then rebuilt at the actual checking position.

## Vacate the promoted queen's ray with useful knight coverage: game 17, finish

After 52.a8=Q Kh8, Nc8 still blocked Qa8's line across the eighth rank. The played 53.Ne7+ cleared it while controlling g8 and g6. After ...Kg7, 54.Qg8+ was protected by the knight and forced ...Kh6: the queen covered f8/f7/g7/h7/h8, Rf4 covered f6, and Ne7 covered g6. Then 55.Qg6# used the same knight to prevent Kxg6. The queen covered g5/g7/h7, and Black's own h5 pawn occupied h5. The referee confirmed mate.

## Recapturing with the king can restore a pawn pin: game 18

After 38...Rd6 39.Rxd6 Kxd6, White Ra6, Black c6 pawn, and Black Kd6 again lay on the sixth rank. White's 40.cxb5 could not be answered by ...cxb5: vacating c6 would expose the king. I recognized the illegality before submission, but the preceding exchange had already made the b5 pawn unavailable to that defender.

After ...Rc8, ...Kc5, and 42.bxc6 Rxc6, b5 was empty. White's 43.Ra5+ then opened a different ray: a5–b5–Kc5–d5–e5–f5. The played ...Kd4 removed the king from that ray, and Rxf5 took the pawn. Rebuild the rook's entire rank after the pawn capture and the king escape; the old blocker on b5 no longer exists.

## An unpinned bishop and the actual defender count: game 18, move 60

After 60.Kg4, the relevant position was White Kg4, Re6, Bf3, pawn d5; Black Kd2, Rd3, Bb3. The bishop on f3 was no longer pinned to a king on g3. Black nevertheless had two attackers on d5, Bb3 and Rd3, against the bishop's one defense. Re6 supported a possible advance to d6, not the pawn on d5 itself. The played ...Bxd5 Bxd5 Rxd5 therefore recovered the pawn and exchanged bishops without losing the rook.

## A pawn-protected rook check forces an adverse exchange: game 18, move 70

After 69...Ke5, White had Kh4, Rf6, and Pg4; Black had Ke5 and Rd5. White played Rf5+. The pawn on g4 protected f5, making Kxf5 illegal. Ke5 stood between Rd5 and the checking rook, so ...Rxf5 was also unavailable. There was no interposition against the adjacent rook check.

I played ...Ke6, keeping Rd5 defended, but White used Rxd5 Kxd5 to reach the pawn ending. The resulting position was White Kh4/Pg4, Black Kd5, White to move. A supported rook was still subject to an unfavorable exchange. Checking the legality of the last recapture is necessary but insufficient; rebuild and assess the ending before allowing the checking sequence. No claim is made that a particular earlier alternative was a proved draw.

## King support before promotion: game 18, final position

White Kh7/Pg6 faced Black Kf8 after 84.Kh7. Pg6 controlled f7; Kh7 controlled g7 and g8. Only ...Ke7 or ...Ke8 remained legal. White could then advance g7 and promote on g8 with the king's protection. I resigned. The illustrative ...Ke8 g7 ...Kf7 g8=Q+ is my unplayed reconstruction, not a referee-tested line or a claim that mate had already occurred.

## A defender can be exchanged before the pawn is taken: game 19

After 20.c4, White Rc1 and Nd2 defended c4 against Black Rc7 and Na5. Black played ...Bb4, attacking Nd2. The actual 21.a3 Bxd2 22.Bxd2 Nxc4+ removed the knight defender and won the pawn with check. Counting two defenders in the initial position did not establish that both would remain available. I have not proved that every alternative to 21.a3 lost the pawn.

Nd2 also blocked Rd1's file. After the earlier 17...Bxd5, Rxd5 was impossible because d2 was occupied by my knight; I used exd5. Recheck friendly blockers after moving a defender into position.

## Exchange the rooks before the knight recapture: game 19, move 24

After 23.Ka2 Nxd2, White had Rc1/Rd1 and Black Rc7/Nd2. Moving the d1 rook immediately to d2 would leave Rc1 unprotected against ...Rxc1. Instead, 24.Rxc7+ Kxc7 25.Rxd2 traded the c-file rooks first and then recovered the knight.

Ka2 mattered to this sequence: ...Nxd2 did not check that king, so White could use the rook exchange with check. In the unplayed alternative with the king on b3, ...Nxd2+ would require an immediate response to the knight check. These are local capture-order checks, not an evaluation of every king move.

## The king capture adds a defender: game 19, move 28

After 27.Rd3 e4 28.Re3, Black played ...Kxd5. The king's arrival on d5 defended e4 diagonally as well as capturing White's passed pawn. Rxe4 would therefore allow ...Kxe4; neither White Kb3 nor the white f2 pawn protected e4. The f2 pawn attacked e3/g3. Rebuild the king's eight adjacent squares after its move before calling the rook's pawn target available.

## A protected interposition ends the rear checks: game 19, finish

The played sequence 35.Rd8+ Ke3 36.Re8+ Kd2 37.Rd8+ Kc1 38.Re8 Rc2 39.Re3 Kd1 40.Rd3+ Rd2 put Black Kd1 behind Rd2, with the passed pawn on e2. Kd1 protected both the blocking rook on d2 and the promotion square e1. Rd2 also defended e2 horizontally.

I resigned. The unplayed illustrative 41.Rxd2+ Kxd2 leaves the pawn free to promote before Kb3 can stop it. The alternative 41.Re3 e1=Q 42.Rxe1+ Kxe1 removes White's rook while Black retains Rd2. Earlier forcing checks delayed promotion but did not establish a perpetual check; the rook's supported block changed the defense.

## A supported rook can still be driven into an exchange sacrifice: game 20

After 32.Nc4, I moved Ra3 to a6. Qc8 defended it through the now-vacant b7 square. White's 33.b5 attacked a6 with the pawn from b4 and also supported Bc6. I had checked queen support but omitted the pawn advance and the rook's subsequent escape squares. The actual ...Rxc6 34.dxc6 gave the exchange. This does not prove that all earlier alternatives lost, but establishes the failure of the intended safety argument. Before placing a major piece, check pawn pushes that attack its destination and a usable retreat after that push.

## A different knight landing square makes the fork: game 20

After 35.Nb6 Qc7, Black had Kg8, Qc7, and Be7. White played 36.Nd5. From d5 the knight attacked both c7 and e7. I had concentrated on Nd7 and failed to audit the other available destinations from b6. The played ...Qa5 37.Nxe7+ lost the bishop.

The unplayed ...Qc8 would not repair this fork: Nxe7+ would attack Kg8 and Qc8 simultaneously. This is a mental geometric illustration, not an engine-tested saving-line analysis. Scan every reachable landing square of the enemy knight before relying on a queen retreat.

## A promotion capture is an opponent choice: game 20, finish

After 37...Kf8 38.c7, Black had Kf8, Rb8, Nd8, and Ne4; White had Ne7 and the pawn on c7, with the original queen still on e2. The king's played ...Kxe7 legally took the undefended knight. It did not resolve the pawn's two capture promotions.

I concentrated on the unplayed cxd8=Q+ Rxd8. White instead played 39.cxb8=Q, taking the rook that the other line needed for a recapture. White now had two queens, and I resigned. Check the straight promotion and both capture promotions independently; a convenient checking promotion is not the opponent's only option. The actual final move was not checkmate.

## A protected checking rook can still be captured by a pawn: game 21

After 30...Kh6, White had Qf7/Re6/Rf1/Bd3; Black had Kh6/Qg3 and pawns g6/h7. I played 31.Rxg6+ after examining ...Qxg6 and ...Kh5, but omitted the actual ...hxg6. Qf7 and Bd3 protected g6 against a king capture. They did not prevent h7 from capturing the rook.

For a white piece landing on g6, the two possible black pawn origins are f7 and h7. For a black piece landing on g3, the analogous white pawn origins are f2 and h2. Inspect those squares explicitly before treating a capture inventory as complete. This is ordinary capture geometry, not a move recommendation from an external source.

After ...hxg6, the unplayed Qxg6+ Qxg6 Bxg6 must also include ...Kxg6. Kh6 is adjacent to g6, and the bishop on g6 would have no remaining defender. This was corrected before choosing the actual next move.

## A checking queen fork after the missed recapture: game 21

After 31...hxg6, the played 32.Qf4+ checked Kh6 along f4–g5–h6 and attacked Qg3 diagonally. Rf1 protected Qf4 through the empty f2/f3 squares. Black's ...g5 blocked the check but left the queen on g3, so 33.Qxg3 captured it. In the unplayed alternatives, ...Qxf4 Rxf4 or ...Qg5 Qxg5+ Kxg5 would exchange queens. The observed queen win depended on the chosen pawn block.

## Bishop support and rook coverage complete the mate: game 21

The finish 35.Qh3+ Kg7 36.Qh7# placed the queen on h7 with Bd3's protection along d3–e4–f5–g6–h7. Rf1 controlled f6/f7/f8. Qh7 controlled g6/g8/h6/h8 and the seventh rank, while the bishop prevented Kxh7. No capture or interposition answered the adjacent queen check.

During Qh3+, Black's g5 pawn occupied g5 and blocked Be7–f6–g5–h4, so that bishop could not interpose on h4. Bd3 controlled g6 and h7; the queen controlled the h-file. Kg7 was the played escape, and the referee confirmed the subsequent mate.

## Remove the piece attacking the queen: game 22, move 18

White's Ne4 attacked Black Qf6. Black Bd5 could capture that knight immediately. The played ...Bxe4 Nxd4 Bd5 exchanged one bishop for one knight and preserved the extra pawn. Searching only for queen retreats had obscured this direct answer to the threat. This is the observed local exchange, not a claim that it was uniquely best.

## The queen behind the rook changes the e-file exchange: game 22

After 21.Qe1, White had Qe1/Re3/Ra1/Nd4; Black had Re8/Ra8/Qf6 and Kg8. Taking the now-loose knight with ...Qxd4 would allow Rxe8+ Raxe8 Qxe8+. Kg8 was not adjacent to e8 and could not capture the queen there. I instead played ...Rxe3, and fxe3 made the pawn the new defender of Nd4.

The hypothetical sequence is a mental capture-order illustration, not an engine-tested evaluation of every alternative. Count the final capture by the queen behind the rook before taking material elsewhere.

## Rook support and the later knight fork: game 22

After ...axb4 axb4, the a-file was clear. The played ...Ra2 was protected by Bd5 along d5–c4–b3–a2. White chose Qxa2 and ...Bxa2 captured the queen for a rook.

The subsequent Nxc6 removed the pawn but threatened Ne7+, forking Kg8 and Qg6. I moved Qg6 to e4. After the actual Ne7+, Qxe7 captured the checking knight: Rc1 had protected c6 along the c-file, not e7. Updating both the knight's fork destinations and its new defenders mattered.

## A rook return outside the checking segment cannot interpose: game 22, finish

After 31.Ra3, Black played Qe1#. The checking segment to White Kh1 was e1–f1–g1–h1. White's own g2/h2 pawns occupied the other adjacent squares. Ra3 could move to a1, but a1 was outside that segment; the move would leave the king in check. The rook could not reach f1 or g1 in one move or capture Qe1. The referee confirmed mate.

## Clear the actual defender's path: game 23, move 12

After Re1, White Be2 still stood between the rook and Pe4. The rook did not yet defend e4. The played Bf1 cleared e2, making Re1's e4 defense real. A desired rook alignment must be checked against friendly pieces as well as enemy ones.

## An intermediate knight capture makes a fork: game 23, move 19

After 18.Nxe5 h4, White Ne5 could take Black Nd7. On d7 it attacked both Qf6 and Rb8. Black could capture it with Bc8; the actual ...Qe7 instead allowed Nxb8. The later ...Rf8 left time for Bh2, preserving the bishop that h4 had attacked. The material gain depended on those replies, not on a forced queen retreat alone.

## A pawn defeats the proposed knight exit: game 23

After Nxb8, I initially proposed Nc6 because Pd5 defended c6. Black Pb7 also attacked c6 and could answer ...bxc6. A subsequent dxc6 would trade a knight for a pawn, not preserve the knight. For a white piece landing on c6, explicitly inspect black pawns on b7 and d7. I corrected the error before playing Nc6; the eventual escape was Nxd7, after Black put its bishop there.

## Recheck the final king capture when the queen's defender disappears: game 23

After 29...b5, White had Qd8/Qe7/Nf6 against Black Kg7/Rh8. The unplayed Qf8+ Rxf8 Qxf8+ would leave the last queen on f8 without a defender. Kg7 could then take it. Nf6 controls g8 and h7, not f8. The first queen's protection by Qd8 does not survive exchanging both that queen and the supporting queen's original position.

Instead, the played 30.Qxh8+ Kxh8 31.Qf8# moved the king to h8 before the remaining queen arrived on f8. From h8 the king could not capture f8 in one move; Qf8 covered g8/g7 and Nf6 covered h7. The rook had been removed, and no pawn could capture the queen or block on g8. The referee confirmed mate.

## A bishop capture would attack both rooks: game 24, move 30

After 30.Bb2, Black had Re7/Rg7 and Pf6. Bxf6 would land on a square from which the bishop attacked both e7 and g7. I answered with ...Be8, attacking White Bh5, and the actual Bxe8 Rxe8 exchanged that bishop pair. This is the played resolution, not a claim that White had no other reply. Audit the attacks from a capture's landing square, not only the captured pawn.

## Retain the blocker through the king recapture: game 24

After ...Reg8 and 34.g5, I used ...Rxg5 and kept Pf6 on the Bb2–c3–d4–e5–f6–g7 diagonal. The later 38.Rxh7+ R8g7 39.Rxg7+ Kxg7 was legal because f6 still blocked that bishop ray. Removing f6 in a hypothetical pawn capture would require rebuilding both the rook's safety and the king's eventual recapture; the geometry cannot be borrowed from the played line.

## Use the pawn before the rook in the file-opening exchange: game 24

After ...a6/...b5 and ...fxe4, White played axb5. The actual ...axb5 cxb5 Rxb5 removed both white queenside attackers before the rook occupied b5. An immediate ...Rxb5 would instead leave White Pc4 able to capture the rook. Support from another piece would not make that rook-for-pawn exchange favorable. The rook later took b3, White's final pawn.

## Moving the king can obstruct a necessary recapture: game 24, move 58

After 58.Kf3, Black had Kd4/Rb3/Pc4/Pe3 against White Kf3/Bc1. The unplayed ...Kd3 would obstruct Rb3–c3–d3–e3. After Bxe3, Rxe3 would be blocked by Black's own king, and Kxe3 would be illegal because White Kf3 protected e3.

The played ...Rd3 kept the rook's horizontal access to e3 and Kd4's protection of e3. White moved to g4, allowing ...e2. After Bb2+ Kd5 Bc3, the bishop covered e1 via d2, but ...Rxc3 removed it before promotion. Both examples require updating actual blockers and defenders after the most recent king move.

## Leave a move before delivering the file mate: game 24, finish

After ...Rf3 Kh7, Black played ...Qg5. The queen covered g6/g7/g8 and h6, while h8 remained legal. White therefore played Kh8. The subsequent ...Rh3# checked along h3–h4–h5–h6–h7–h8; Qg5 covered g7/g8 and the rook covered h7. There were no remaining white pieces to capture or interpose. The referee confirmed mate. Confinement without check must retain a legal move until the final mating check.

## Removing one attacker also removes a pawn's defender: game 25

After 22...Nc4, Black's knight attacked Pe3. The played Bxc4 removed it, but ...Rxc4 attacked Pe4 along c4–d4–e4. Bd3, the bishop just exchanged, had been e4's defender. Ne2 defended c3, not e4. The actual Rd3 held c3/e3 and allowed ...Rxe4. Count the defenders lost by an exchange as well as the attacking piece it removes; no claim is made that the pawn loss was forced from the earlier position.

## A pawn move would remove the knight's only defender: game 25

After 26...h5, White had Ng3, Ph2/Pe3, and Rd3; Black had Rg4. The unplayed h3 would attack the rook but remove h2's protection of g3. Black could answer ...Rxg3: h3 would no longer capture g3, and Pe3 would still block Rd3–e3–f3–g3. I rejected h3 before playing it.

The played Rd2 instead defended g2 along e2/f2. After ...h4, Nf1 kept that line clear. The alternative Ne2 would obstruct the rook's defense of g2 just as Ng3 vacated the g-file. A retreat must preserve the actual defensive line, not merely land on an unattacked square.

## Choose which rook moves by checking the mating net: game 25, move 31

After 30...Rxc3, White had Kb2/Ra1/Rd2/Nf1/Pa3 and Black had Rc3/Rc8/Be6. The unplayed Rd6 Rb3+ Ka2 Rc2# illustrates the danger of moving Rd2 away while Ra1 still occupies a1. Rb3 is protected by Be6, Rc8 covers c1/c2 before moving, Pa3 blocks a3, and Ra1 blocks a1. The remote rook on d6 cannot interpose on b2 or capture Rc2.

The actual Rad1 preserved Rd2's capture on c2 and also vacated a1 for the king. The game continued with ...Rb3+ Ka2. This was a mentally checked alternative, not an engine-tested variation or a claim that Rad1 was uniquely best.

## A discovered check invalidates the planned recapture: game 25, move 32

After ...Rb3+ Ka2, Black played ...Rxe3+. The rook's departure from b3 uncovered Be6–d5–c4–b3–a2. White Nf1 attacked e3, but Nxe3 would not answer the bishop check. I moved to b2 instead, losing the pawn while Black saved its rook with another check.

The earlier statement that Nf1 defended e3 was insufficient after moving the king onto a2. Rebuild the legality of the recapture after both the capturing piece's departure and the king's most recent move. The subsequent repeated checks produced the referee-recorded draw; they do not erase this failed defense or prove that the earlier position was drawable.

## Audit the proposed queen recapture as a new move: game 26, move 15

I played ...Bg5 intending Bxg5 Qxg5. White's Nf3 could then capture the queen on g5. I noticed this only after the bishop had already been taken and played ...f6 instead, losing the bishop. The queen's ability to recapture did not make the exchange sound. The landing square g5 was attacked by a cheaper knight; a complete exchange audit must include that last capture.

## The unmoved rook both protects the mating queen and blocks its capture: game 26, finish

After ...Qxe6, White played Rb8+ with the upper rook. The lower rook on b2 still blocked Qa1's diagonal, so ...Kg7 was legal. R2b7+ then gave double check and forced ...Kh6. Rxh7+ Kxh7 Qh8# completed the played mate.

Rb8 protected Qh8 along the eighth rank and simultaneously blocked Ra8's path to h8. Black could not capture the queen with the king or rook; Qh8 covered g8/g7/h6 and Black's own Rg6 occupied g6. My earlier analysis of Rh8+ Raxh8 did not apply: in that different line the rook would leave b8 and unblock Ra8. The queen move retained the blocker and the defender. The referee confirmed the actual Qh8 mate.

At the earlier Rb8+ position, ...Raxb8 would instead allow the lower rook's Rxb8#, which both opened Qa1–h8 and checked along rank eight. Identifying that trap did not excuse omitting the separate queen mate after the chosen king move.

## A new queen defender changes the full exchange: game 27

Nxc5 was initially supported by Be3, later Bd4. After Black's ...Qb6, the sequence ...Bxc5 Bxc5 Qxc5 became available. I moved Bb5–c4 without accounting for that final queen recapture. The bishop's ability to recapture did not preserve both white pieces. I caught the omission at the next position, but Black actually played ...Rd8 instead of ...Qxc5, allowing Bxb6. The opponent's concession does not validate the incomplete exchange calculation.

## Keep the bishop's protection through both queen checks: game 27, finish

Against Kg8 with Pg7/Ph6 and no remaining black pieces, White played Qe8+ Kh7 Be4+ g6 Qxg6+ Kh8 Qh7#. Qe8 covered the eighth rank and f7; after Be4+, the h6 pawn occupied a king escape and ...g6 interposed on the bishop ray. Be4 protected the queen first on g6 and then on h7 after g6 was vacated. At the final position Qh7 covered g7/g8, Kxh7 was illegal because of the bishop, and no interposition was possible against the adjacent queen. The referee confirmed mate.

## A knight departure combines a rook attack with two knight targets: game 28

After ...Qf6, White played Nf3–d4. This uncovered Rf2's attack on the queen while Nd4 attacked Be6 and Pc6. I had considered other knight departures but omitted this one before playing ...Qf6. The actual ...Qg6 defended Be6 and escaped the rook, but Nxc6 won a pawn and attacked Rd8. A partial list of knight routes did not satisfy the existing fork audit.

## Preserve the rook that can capture the checking knight: game 28, move 22

After Rxf8+, the unplayed ...Rxf8 would remove Re8's control of e7. White's Nc6–e7+ would then fork Kg8 and Qg6. I caught this before choosing the actual ...Nxf8, which left Re8 able to answer Ne7+ with Rxe7. The rook and knight were both legal recapturers, but their resulting defensive coverage differed.

## Breaking a pin does not itself save the pinned piece: game 28

After the queen exchange, ...Bd5 pinned Ne4 to Kh1 through f3/g2. White played Kh2. That king move removed the absolute pin but neither moved nor defended Ne4, so ...Bxe4 won the knight. The opened diagonal resulted from White's earlier g-pawn advance.

## Recheck pawn attacks and the king's latest square: game 28

After White h4, ...Ng5 would land on a square that pawn could capture; I rejected it. The played ...h5 gxh5+ Kxh5 used different geometry: Ph4 attacked g5, not h5, and Kh2 did not defend h5. The king capture was legal. Later Kh3 did defend Ph4, so I did not take that pawn until the white king returned to h2. A pawn's forward square and its capture square are different, and a king's defense changes immediately with its move.

## Remove the blocker before relying on the mating rook's defender: game 28, finish

After ...Rf2+ Kg1 ...Kg3, White played Nc4. That knight blocked Bb5–c4–d3–e2–f1. An immediate ...Rf1+ would leave the rook capturable by Kg1 because Kg3 did not protect f1. I instead played ...Bxc4, retaining the bishop's route to f1. The actual Kh1 Rf1# followed; the rook covered g1, Kg3 covered g2/h2, and White had no piece able to capture or interpose. The referee confirmed mate.

## Defend both targets through the final recapture: game 29

After ...Qb6, Black's Rd5/Qb6 pressured White Bb5/Nd4. Qc4 supported Bb5 along c4–b5 and Nd4 along c4–d4. In the illustrative ...Rxd4 Rxd4 Qxd4, Qc4 could take the black queen; in ...Rxb5 Nxb5 Qxb5, it could also take on b5. Stopping the calculation before that last queen capture gave the wrong material count. Earlier Qe2 had also defended Bb5 through d3/c4, a line I temporarily omitted.

## Check the cheap capture before extending a candidate: game 29

I considered Bc6 from b5 for a long time before noticing ...bxc6 from b7. Supporting c6 with a knight did not make a bishop-for-pawn exchange favorable. This repeats game 23's b7-pawn omission. The existing pawn-origin check belongs before remote branches, not only at the final audit.

## A new bishop defender changes a queen capture: game 29

Qxf7 removed the pawn that had protected Ng6. After Nf3 Rxd1+ Rxd1, Black played ...Bf5, now defending Ng6 along f5–g6. I therefore did not play Qxg6. The later Nh4 fork attacked Bf5/Ng6; ...Ne7 moved the knight to a square where Qxe7 was safe. Capturing with dxe7 would instead open the d-file to ...Rxd1+, so those captures were not interchangeable.

## A supported queen can still be captured by a knight: game 29

After ...Nh5, White Be5 supported g7 through f6. That made Kxg7 illegal against a queen on g7, but did not prevent Nh5xg7. I rejected the queen capture rather than treating bishop protection as sufficient for mate. Be2 then attacked the knight. The actual ...Rd7 allowed Qxd7, and ...Nf6 Bxf6 gxf6 removed the remaining knight.

## The second queen protects the adjacent mating check: game 29, finish

After Qxf6 and d8=Q, Black played ...Bd5. Qdh8# used Qf6–g7–h8 to protect the checker. Qh8 covered g8 and h6; Qf6 covered g7/g6. There was no square between Qh8 and Kh7 for an interposition, and Bd5 could not capture Qh8 or Qf6. The possible ...Be8 instead of ...Bd5 would have blocked the promoted queen's route through e8, so it required a separate continuation. The referee confirmed the played mate.
