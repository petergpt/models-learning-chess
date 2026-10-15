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
