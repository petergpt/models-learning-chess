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
