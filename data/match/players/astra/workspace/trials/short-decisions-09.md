# Trial 09: shorter decisions with an observed clock

Declared 2026-10-01 at 19:44:59 UTC after game 78 and the trial-08 endpoint. Baseline: provisional engine-relative Elo 1680 [1560, 1800], 52 rated games total / most recent 50 used; overall 32W/2D/44L. Next fixed evaluation: benchmark games 79–84. Preserve the same referee, opponent rotation, estimator, model and reasoning setting.

Target: lengthy speculative branching repeatedly displaces simple current-board facts. Game 78 calculated king replies to a checking queen but omitted b4xc5; it later tried a rook route through its own pawn. Earlier destination, changed-line, defender, breadth-first, remembered-opponent and longer-game trials already failed. This trial tests actual decision duration and shallow scope. Rephrasing the existing safety instruction is not the new intervention.

Practice: two fresh standard-start opponent sessions at nominal 1800, White then Black. Cap each at 40 learner moves, including the final opponent reply, or finish naturally sooner. Combined ceiling: 20:29:59 UTC on 2026-10-01 (45 minutes from declaration, including setup and reviews). At the ceiling finish any pending reply and record an unfinished end; do not extend to seek a favorable outcome. Every session and result remains in the separate practice ledger and never enters Elo.

Use a 20-second decision target, observed from completion of the previous referee command to submission of the next chosen move. This includes tool, polling, commentary and other elapsed delays; it is not pure thinking time or a token budget. The timing helper only forwards caller-supplied commands to ./play and appends clock metadata. It contains no chess module, board parsing, move generation, scoring, search, fallback choice, or automatic move. It does not change the official untimed game or impose a forfeit. Record every overtime and rejected move; do not hide a miss by restarting the clock or omitting a result. A rejected move retains the earlier turn clock.

Decision format: use one working candidate and one short concrete reply/answer at a time, then submit within the target. Prefer an ordinary supported move if the continuation is unresolved. Do not turn a doubtful candidate into many remote branches. Immediate captures and the actual king/pawn defenders still matter; on a major-piece move, identify the two opposing pawn origins and the actual path blockers before looking beyond the first reply. These chess requirements are familiar and unproved in transfer. The experimentally changed feature is shorter, timed work, not checklist length. All moves remain my own decisions. No game advice, automatic analysis, engine output, move menus, or delegation.

Assessment: at least 90% of submitted legal moves within 20 seconds would show implementation of this decision format, not stronger chess. Report exact logged counts and any missing timing. Separately record actual direct queen/rook losses, illegal blocked moves, overlooked immediate mates, and concessions after short branches. Even clean practice at this strength is not an independent accuracy test or Elo evidence. If the format is not implemented, report that rather than attributing results to it.

Carry the same timing target into the declared fixed block 79–84, then compare all six results, the unchanged rating interval, and error recurrence with trial 08 (three of six games with targeted major-piece failures). A cleaner block and higher estimate would be provisional only and require repeated evaluation. Do not call this sustained improvement from one win, a lower elapsed time, a remembered example, or a temporary rating rise. Revise the method again if errors persist. Return to evaluation after the bounded practice even if the practice result is unfavorable.

## Practice and benchmark record

Pending.


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
