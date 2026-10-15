# Trial 16 — safe queen exchanges as a position choice

Declared after benchmark 120 at 2026-10-02 15:36:16 UTC. Baseline: 1590 [1470,1710], 48W/2D/70L; 80 rated games total, latest 50 used, 40 uncalibrated MAX exclusions. Fixed next evaluation: benchmarks 121–126 in the unchanged paired-color rotation. No estimator, opponent, model, or fair-play changes.

## Weakness and change

Trial 15 failed: 2W/0D/4L and a lower Elo endpoint. Early development did not prevent queen exposure, missed immediate recaptures, or later rook losses. The long speculative branches in 119 omitted the actual ...Rxb2 reply. Trial 09 already tested shorter timed decisions, failed its implementation criterion in most games, and did not prevent a queen loss even within the time target. Do not restart that discontinued clock method or relabel inventory/checklist work as new training.

This trial changes the positions selected. At materially comparable positions, prefer a concretely safe, materially equal queen exchange over an unverified queen attack or pawn raid. Consider a supported exchange offer when it improves development or activity. This is conditional, not a requirement to remove queens at any cost: respond to checks and captures, preserve sound forced gains, and avoid an exchange whose last recapture loses material. Keep the trial-15 opening preferences as a fallback so the new variable is the simplification preference. Do not manufacture a queen sortie merely to offer a trade.

The hypothesis is that earlier queen removal will reduce the recurring queen-exposure failures and allow more decisions in positions with fewer long-range attackers. This cannot excuse later rook or minor-piece blunders. Game 120 is one encouraging example of surviving an inferior queenless position and converting opponent mistakes, not proof of the hypothesis.

## Bounded learning and practice

First review the following own-game facts, then play exactly two fresh standard-start opponent-practice sessions at nominal 1800: White, then Black. Each has a maximum of 20 learner moves, including the reply after move 20, or ends naturally sooner. Combined deadline, including setup and reviews: 2026-10-02 16:21:16 UTC (45 minutes). At the deadline finish any already pending referee reply and end an active drill as unfinished. No favorable-result extensions or repeats. Practice records remain separate from Elo and benchmark W/D/L.

Own-game contrasts:
- In 120, ...Qc7/Qxc7/Bxc7 completed an equal queen exchange because Bd6 actually reached c7. Later ...Rc8 supplied a real defender to Bc7. The opponent declined the later bishop trade offered by ...Bc8; retain the actual continuation.
- In 119, Qxc4/Bxc4 removed queens but left White down the exchange and left Re2 attacked. The trade did not repair the earlier Qd3/Ba6 skewer or guarantee a safe ending.
- In 116, Qd5 did not leave the d-file. In 118, Qe3+ remained capturable by f2xe3. A queen's active-looking destination or checking move does not establish a safe transaction.
- In 120, Kxf7 did not win a net bishop because Rxc8 followed. Also, 79.Kg7 was an opponent error that let ...Kxf5 win the pawn; do not claim every earlier rook-versus-pawn line was proved winning.

During practice, record actual queen offers, whether they were accepted or declined, the final recapture and material result, and all unexpected piece losses. If no reasonable exchange opportunity occurs, record the lack of exposure instead of forcing one or extending practice. A stopped opening/middlegame drill has no full-game score.

## Evaluation and continuation

Return to benchmarks 121–126 after these two sessions, regardless of practice results. At 126 compare Elo with its uncertainty, full W/D/L, actual queen losses, other direct piece losses, and whether/how early queen exchanges occurred (including games that kept queens). Exchange frequency is implementation evidence, not strength. A clean practice, one win, or a single higher point estimate is insufficient; seek sustained measured improvement across repeated evaluations. If the policy merely produces inferior endings or the same blunders, revise again.

Only own reasoning, pre-existing notes and the referee during play; no external position advice, engine analysis, automated search/scoring/attack enumeration, legal-move menu, or delegation. No decision-clock target or invented token counter.

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
