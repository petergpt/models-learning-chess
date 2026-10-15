# Trial 11 — opposing-king captures in sparse-board conversions

Declared 2026-10-01 23:13 UTC after benchmark 90 and the completed trial-10 review. Baseline 1720 [1600, 1840]; overall 38W/2D/50L. No sustained improvement established. Opponents, estimator and fair-play rules remain fixed.

Specific failure: in game 90 I calculated captures involving the active rook while forgetting that the other rook on f1 was capturable by Kg2. The eventual win concealed a direct rook loss. Training now isolates the opposing king as an attacker, including threats to pieces that did not move. Before choosing a conversion move, locate the opposing king and my remaining major pieces on the actual board, and resolve a legal king capture of a loose major piece before collecting unrelated pawns. A rook being elsewhere in a calculated line is not evidence that it is safe on the current board. This is a narrow practice cue, not another expanded general checklist.

Bounded practice: three recorded sessions against maximum strength, at most 15 own moves each, with a combined stopping ceiling of 23:43 UTC on 2026-10-01 including reviews. Session 1: Black, benchmark 90 after ply 51 (26.b4), an explicitly remembered position. Session 2: White, new constructed FEN `3R4/2k5/8/1p2p3/8/1R6/5PPP/6K1 w - - 0 1`. Session 3: Black, new constructed FEN `1k6/ppp5/6r1/8/3P2P1/8/5K2/4r3 b - - 0 1`. The constructed positions deliberately vary the king/rook geometry; they are not independent rated tests or certified theoretical exercises. Preserve unfinished sessions with practice end at either limit, and add no repetitions to seek a favorable outcome.

Practice observations: actual unexpected king captures or other direct major-piece losses, whether the exposed rook was moved or was left elsewhere, and whether a conversion was completed within the limit. A stopped drill is not a draw. Correcting the remembered position is not transfer. Use only own reasoning, referee board and legality checks; no external advice, delegated moves, engines as analysis tools or automated chess analysis.

Next fixed evaluation: benchmark games 91–96, all six in the existing rotation, regardless of practice results. Record Elo and uncertainty, all direct queen/rook losses and actual king-capture opportunities, including errors in games eventually won. A block with no relevant sparse ending cannot validate the specific skill. Seek repeated measured improvement rather than a practice win or a temporary rating rise; revise again if errors persist. No trial-09 clock target applies.



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
