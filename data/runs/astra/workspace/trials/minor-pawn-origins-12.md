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
