# Formal checkpoint — 138 scored benchmarks

Verified after benchmark 138, 2026-10-09. Overall: 39 wins, 7 draws, 92 losses; 138 scored, zero unfinished benchmarks, no active game. Fixed rotation retained.

| Opponent | Scored | W | D | L | Score fraction |
|---|---:|---:|---:|---:|---:|
| Maximum skill | 46 | 0 | 0 | 46 | 0 |
| Skill 0 | 46 | 32 | 4 | 10 | 0.7391304347826086 |
| Nominal 1800 | 46 | 7 | 3 | 36 | 0.18478260869565216 |

Referee estimate: 1560 provisional engine-relative Elo; conditional 95% Bayesian equal-tail credible interval [1440,1680]. Latest 50 of 92 rated games; 46 uncalibrated maximum-strength games excluded from this estimator. Nominal anchors are 1320 and 1800. Interval excludes systematic anchor calibration error; this is not human FIDE/platform Elo and not strength at a fixed inference budget.

Latest block 133–138: L, L, W, D, L, L; 1W/1D/4L. Full-strength pair both losses; skill-0 pair win/draw; nominal-1800 pair both losses. The skill-0 win relied on major gifts; the draw salvaged a queen blunder and was automatically claimed by the referee. Full strength remains 46 straight losses. Early material retention sometimes improved locally, but games 133 and 138 exposed king nets; 134 lost a queen to a second bishop ray, and 137 lost a rook after the king first blocked and then cleared its sole guard ray. No sustained full-strength transfer is established.

Comparisons: formal 126 was 1500 [1380,1630], formal 132 was 1530 [1400,1650], and formal 138 is 1560 [1440,1680]. Intervals overlap. Formal 120 was also 1530. The estimate rose from 1550 to 1560 after the loss in 138, illustrating the changing rolling window rather than success in that game. These movements do not establish causal or sustained improvement.

Own maximum-strength drills since formal 132: practice 109 resigned after two own moves and did not establish a saved king flight; practice 110 stopped at four own moves with equal material but unresolved blockade/king development; practice 111 stopped at four with a one-pawn deficit and an attacked queen, leaving the intended bishop escape untested; practice 112 lost by mate on its fourth own move despite retaining major material; practice 113 retained majors locally but failed its deficit target, stopping at minus 5; practice 114 retained a king guard and majors for four moves at minus 1, but ended with its rook under a cheap bishop attack and no escape played. These are remembered local tests with differing replies, not independently solved positions or whole-game repairs. Practice never entered benchmark Elo.

Current methods: cheap-guard inventories, complete recapture chains, departure/arrival first-body checks, royal flight checks and bounded replays of my own failures. They have helped catch some unsubmitted illegal ideas, but failures recur and the routine has become too slow. More notes and longer mental branches are not evidence of progress. Trial 229 will test the alternative king reply in game 138, then benchmark 139 will test new-position transfer; next formal checkpoint 144. Whole-game royal safety must accompany material retention.

Actual get_goal observation at this checkpoint: status active, tokensUsed 31488555, timeUsedSeconds 391820, remainingTokens null, no token budget. Both counters returned unchanged from the observation at checkpoint 132. Record the observed counter honestly; do not infer new token use, per-move use, or elapsed experiment time from the unchanged values. Fair-play and shared memory rules preserved; all started games retained; no other learner or operator comparison inspected.

## Trial 229 outcome and next trial — practice 115

Verified PGN/result: MAX Black from own 138 ply 111, LOSS by 60 Bxe5#, four own moves/eight plies/zero illegal submissions. Result seq 1153, 2026-10-09T00:17:45.179249+00:00. Actual line: 56...Kh8 57 Rg1 Bg6 58 Rxg6 Re5 59 Bd4 e3 60 Bxe5#.

All local targets FAILED: mate at the bound, the unguarded e5 rook lost to Bxe5, and final nominal deficit 9. Kh8 changed Rg1 from a checking move to a nonchecking move, but that extra tempo did not solve the net. My Bg6 block was captured by the rook, not by the h5 pawn as one imagined branch assumed. The capturing rook on g6 still covered g8, and Rd7 covered h7. Re5 blocked the d4-h8 diagonal but became an absolute royal shield and was undefended. Final Bxe5 was referee-established mate. No saved game or benchmark transfer. Timing remains poor; the imagined bishop block was an ineffective method and will not be repeated as a repair claim.

Trial 230, before benchmark 139: one earlier reconstruction, own 138 ply 109 after 55 Be3, MAX Black. Candidate 55...Kg8 instead of the actual Kg7, accepting the possibility of losing the h6 pawn instead of placing the king on the seventh rank to guard it. Four own moves maximum, unless the game ends earlier. Local targets remain no mate, no whole queen/rook loss, and deficit at most 3. Rebuild actual reply rays and legal king destinations, without treating a king's nominal guard as a legal recapture automatically. This is a remembered single-candidate test, not proof that the position is saveable. After this test return to fixed benchmark 139; formal review 144. Do not add another replay before 139.

## Trial 230 outcome and benchmark Trial 231

Practice 116, MAX Black from own 138 ply 109, stopped at four own moves/eight plies/zero illegal submissions. Result * remains unscored and excluded from Elo. Result seq 1164, 2026-10-09T00:25:33.962605+00:00. Verified PGN: 55...Kg8 56 Rd7 Re6 57 a7 Rxb7+ 58 Rxb7 Rf6 59 Rg1+ *.

Local no-mate-at-four target MET, but major-retention and deficit-at-most-3 targets FAILED. Final own rook, bishop and four pawns versus two rooks, bishop and four pawns: nominal deficit 5. Rxb7+ took one pawn and was captured by the d7 rook; that was a whole rook loss for a pawn, not a fair rook exchange. Rf6 guarded h6 and left e8 clear, but the final check response was unplayed. The king position and a7 passer remained unresolved. This is not proof of a game save or transfer. Moving the king earlier did not by itself solve the combined passed-pawn and checking-rook constraints. Only the recorded local outcomes are established; imagined follow-up recaptures and escapes are unverified.

Decision after Trials 229–230: stop these late-position replays and return to new-position evaluation. Both attempted fixes failed their overall targets. Prioritize legal king space earlier, rather than trying to keep every pawn once checking rooks have closed the flights; preserve actual piece-body and recapture accounting. The early no-major-loss target needs a whole-game king-safety assessment alongside it. Timing and excessive speculative branches remain unresolved, not repaired by these trials.

Trial 231, fixed benchmark 139, White against maximum strength: develop and secure the king using own reasoning, then before any king move or shield/pawn change inspect the opponent's immediate forcing check and the resulting occupied/attacked flight squares. Favor a concrete pawn concession over entering a net when the actual alternatives support that choice. This is a hypothesis for new-position transfer, not an asserted general best move. Observable first-20 target: no mate and no whole queen/rook loss. Whole-game assessment: record any king-net or royal-shield loss even if the early target passes; score/result and illegal attempts must remain honest. No additional practice before 139. Choose another learning trial after 139 completes; formal checkpoint 144. Current scored count remains 138, 39W/7D/92L, estimate 1560 [1440,1680].
