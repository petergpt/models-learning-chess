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
