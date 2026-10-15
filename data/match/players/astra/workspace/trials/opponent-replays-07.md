# Trial 07: short replays against an opponent

Planned on 2026-10-01 after benchmark game 66. Planning reference: 12:45:02 UTC. Practice ceiling: 50 minutes, ending no later than 13:35:02 UTC. Baseline: 1710 [1580, 1840], 44 rated games. Next measured evaluation: fixed benchmark games 67–72, beginning after these drills. The goal, usage counter, opponent rotation and rating method remain unchanged.

Weakness: correct supplied practice branches have not transferred to actual replies. Long speculative calculations still omitted checking moves, changed defenders and piece traps. Trial 06 failed. The new intervention is recorded opponent play from remembered failure positions, followed by an immediate short review and one revised replay. The opponent supplies only its played moves; it is not an analysis service.

Preselected initial drills, all at the nominal 1800 setting:

1. White, benchmark 65 after 62 plies: before Bxb6 and the subsequent Qb5+/Qd3/Bf1+ failure. Preserve the queen and account for the checking queen's second target.
2. Black, benchmark 66 after 59 plies: before ...Rb5 and the later b4/Bc5+/c4 rook trap. Keep the rook mobile and use real, unobstructed defenders for d3.
3. Black, benchmark 60 after 39 plies: before ...Bxb2 omitted Ne7+. Choose and play an alternative against whatever replies the opponent actually makes.
4. White, benchmark 61 after 42 plies: before Nd2 blocked the bishop's retreat and ...f4 trapped it. Preserve an actual retreat or concrete exchange response.

Each drill ends at a terminal result or after at most six learner moves, with the final opponent reply included. Use `practice end` to retain an unfinished drill explicitly. After all four, choose the most instructive failure or unresolved example for one additional replay at the same setting, again at most six learner moves. Record that adaptive selection and its reason before starting it. Stop sooner if the time ceiling is reached; record omitted drills rather than extend study indefinitely. No drill is a blind puzzle, and the repeated fifth drill is expressly a remembered correction.

Execution change: compare at most two sensible candidates at a time. On the reconstructed board, finish a short answer to the concrete forcing reply before pursuing a remote plan. Recheck immediate checks and cheaper captures before submission. Use an actual legal retreat when moving a piece into a confined area. Rebuild the board after the opponent's reply rather than continuing an imagined branch. Aim for about a minute on routine moves; longer calculation is not evidence of better play, and unresolved dangerous lines should remain labeled unresolved. This is an unproven practice change, not a claim of exhaustive checking.

After each drill record the actual continuation, starting and ending material changes, targeted errors avoided or repeated, and any unexpected reply that invalidated my plan. A remembered tactic not selected by the opponent is not a successful test of that tactic. Mechanical legality is not a strength assessment. Do not seek evaluations, hints, best moves, search output, automated tactical analysis, or delegated advice.

Evaluation: practice should produce usable corrections that survive actual replies, without hiding concessions or treating easier wins as progress. During games 67–72, record missed checks or captures that lose material and failures of defender lines or piece escape. Any recurrence prevents claiming reliable transfer. At game 72 compare all benchmark outcomes and the unchanged Elo interval with baseline. Revise on failure. A single cleaner block or rating rise still needs later confirmation before claiming sustained improvement.

Practice records live in the referee's separate `data/practice/` ledger and do not enter benchmark Elo, W/D/L or rotation. This file will contain the concise review of each drill.

## Drill 1 — practice record 1, White from game 65 / ply 62

Completed the six-move drill and explicitly ended it unfinished. Actual continuation: b3 Qd7, Ke1 Bd5, Qd4 Qb5, b4 h5, f4 Bf3, Qd2 Bg4. No captures occurred: both sides began and ended with queen, bishop and five pawns. The final position is not evaluated or proved safe beyond the supplied play.

The opponent diverged immediately with ...Qd7. Ke1 removed the original bishop-check geometry, so the later ...Qb5 was not check. I rejected Qc4 after ...Bd5 because the changed bishop could capture that queen, despite Qc4 having been usable in an earlier branch. After ...Bf3 I considered e6, then identified ...Qe2 as a mating reply against Ke1 and rejected the push. Qd2 supplied a queen capture against ...Qe2; the opponent instead chose ...Bg4. That unplayed mating assessment is my own calculation, not an independently verified solution.

The useful result is preserving all material through twelve actual plies and adapting to a newly played threat. This remembered position did not reproduce the original Bf1+ tactic, was stopped deliberately, and is neither a win nor evidence of an Elo increase.

## Drill 2 — practice record 2, Black from game 66 / ply 59

Ended unfinished after six learner moves and twelve plies. Actual continuation: ...Ke7/Raa1, ...Ke6/b4, ...Rdd5/f3, ...Rxh5/Bf4, ...Rxh1/Rxh1, ...Rd7/Rh4. Initially each side had two rooks, bishop and six pawns. At the endpoint each had one rook and bishop; Black retained six pawns and White had five. No major piece or bishop was lost outside the equal rook exchange.

Keeping Re5 instead of playing ...Rb5 preserved several exits. With the rook on e5 and b2 still unmoved, a contemplated Bc5+ could be met by ...Rxc5 without the b4-pawn recapture from the benchmark. After the actual b4, ...Rdd5 coordinated the rooks while both that rook and Bc4 still defended d3. ...Rxh5 was supported along the fifth rank by Rd5. The opponent chose Bf4 rather than Rxh5, so I traded on h1 and then used ...Rd7 to defend c7 against that newly placed bishop. The king stayed off the rook's d-file. The final Rh4 does not directly attack Bc4 because White's own bishop on f4 blocks the fourth rank.

This is a better local outcome than the remembered rook concession, and the opponent supplied a different continuation. It is not a proved winning position or a completed conversion; six moves are limited evidence. The original Bc5+/c4 trap was avoided rather than reproduced as a blind test.

## Drill 3 — practice record 3, Black from game 60 / ply 39

Ended unfinished after six legal learner moves and twelve plies, with one rejected illegal submission. Actual continuation: ...Nxd5/Bxd4, ...Re8/Bxg7, ...Qf5/Bd4, ...Rcc8/Rg3+, ...Kf8/Bc5+, ...Re7/Qd4. Initially both sides had queen, two rooks and two minor pieces; Black had six pawns to White's five. The minor-piece trade left Black with a knight and White with a bishop, and Bxg7 equalized the pawns at five each. No exchange was actually lost before the endpoint.

Removing Nd5 avoided the remembered Ne7+ fork, but the exposed g-file produced a new forcing sequence. I anticipated Rg3+ and Bc5+ without resolving a satisfactory king defense. Worse, I submitted ...Kh8 while Bd4 already controlled h8; the referee rejected it. Naming that bishop diagonal in my own reasoning did not prevent ignoring it in the submitted move. I corrected to ...Kf8. Against the actual Bc5+, I rejected ...Ne7 after calculating Qh6 mate, then used ...Re7; the opponent chose Qd4 rather than immediately exchanging bishop for rook. That unplayed mate assessment is my own calculation, not a verified result.

The endpoint has Re7 pinned to Kf8 by Bc5, with further queen threats unresolved. Equal material after twelve plies does not establish adequate defense. This drill failed the intended reliable application of immediate checks and defenders, despite avoiding the original fork, and is a candidate for the final adaptive replay.

## Drill 4 — practice record 4, White from game 61 / ply 42

Ended unfinished after six learner moves and twelve plies, with no captures or illegal submissions. Actual continuation: Ng5 Nc4+, Kb3 Bf6, Nf3 h6, Bd2 Rc5, Be1 Na5+, Kc2 Rhc8. Both sides retained two rooks, bishop, knight and six pawns.

Ng5 kept d2 open but allowed the unanticipated ...Nc4+ fork of king and bishop. I considered ...Nxe3 followed by fxe3 and the newly exposed knight on g5; the opponent instead chose ...Bf6 and then ...h6, allowing Nf3. Thus preserving material in actual play does not resolve that omitted forcing branch. Bd2 supplied a bishop retreat, but also temporarily blocked Rd1's defense of d6. I noticed that after ...Rc5 and moved Be1, restoring the rook line before the pawn was captured. I answered the later ...Na5+ with Kc2.

The original ...f4 trap was not played. This local continuation preserved all material, but includes an omitted check and a temporary defender obstruction; it does not establish reliable transfer or a sound initial alternative.

## Adaptive replay selection — declared after all four drills

Repeat Black from game 60 / ply 39 at nominal 1800, again at most six learner moves. Drill 3 is the clearest unresolved failure: it included an illegal king move despite an identified bishop diagonal, and exposed the king to the actual Rg3+/Bc5+ sequence. This fifth drill is explicitly remembered practice, not a blind test. Try an earlier queen relocation (...Qd7 is the current candidate) to avoid the original Ne7+ queen fork while retaining the g-pawn and checking actual defenders after subsequent exchanges. The opponent may choose a different continuation. Preserve every outcome and do not label an avoided original tactic as proof of safety.

## Drill 5 — practice record 5, adaptive repeat of game 60 / ply 39

Ended unfinished after six learner moves and twelve plies, with no illegal submissions. Actual continuation: ...Qd7/Nf4, ...Bxb2/Rxb2, ...Qxd2/Rxd2, ...Rc7/h4, ...Re8/Rdd1, ...h6/Nd5. Equal bishop and queen exchanges left both sides with two rooks and a knight; Black kept six pawns against five and retained g7. Unlike drill 3, no checking sequence drove the king from g8.

Moving the queen first changed the original fork geometry. After the actual Nf4, I checked that the knight's available jumps did not repeat the Ne7+ king-and-queen fork before exchanging on b2. ...Rc7 covered the seventh rank and ...Re8 supplied another real defender for e4. The endpoint Nd5 attacks Rc7 and Nf6. My unplayed response candidate is ...Nxd5, with ...Re8 still defending e4 after a possible Rxd5; that continuation was not executed or independently verified. The drill is not a completed conversion or a proof that ...Qd7 is best.

## Practice assessment before benchmark 67

All five declared drills finished by 13:14:34 UTC, within the 13:35:02 ceiling: 30 legal learner moves, 60 played plies, one illegal attempt, and five explicitly retained unfinished records. There were no wins or draws. The actual opponent continuations were more informative than supplied-line rehearsal, particularly the g-file checks in drill 3. Drill 5 produced a better local material and king-cover outcome than drill 3, but uses the same remembered starting position and a different opponent continuation.

The practice exposed continuing failures: an identified bishop diagonal was not applied to a king move; an immediate knight check was omitted; and a bishop retreat temporarily obstructed a rook defender. None is repaired merely by recording it. The concrete lesson to carry into the unchanged short move procedure is to apply the actual lines to the selected destination and finish the immediate response, rather than count a named threat as handled. No reliable transfer is established.

Proceed to the predeclared fixed benchmark games 67–72. The baseline remains 1710 [1580, 1840], 44 rated games. Retain and report all new outcomes and targeted recurrences, then review at 72. Observed cumulative active-goal usage after the drills was 13,620,442 tokens, covering the entire goal rather than this practice period alone. No external chess advice, automated analysis, engine output beyond opponent play, or delegated move selection was used.

## Benchmark 67 — White versus maximum, loss

Resigned after 32...Rxg2+, 64 plies and no illegal submissions. Elo remains 1710 [1580, 1840], because this uncalibrated maximum-strength game is excluded from that estimator. The overall record is now 28 wins, one draw and 38 losses. Trial 07's benchmark block begins with one loss.

The queenless opening stayed materially equal. I anticipated ...Na5+ and later ...Nc4+, and used Re1 to defend Be3 before Nb3. However, after the actual ...Nc4+/Kc2 I omitted ...Na3+, which forked the king and Rb1. I had resolved only the imagined ...Nxe3/Rxe3 branch. ...Nxb1+/Rxb1 conceded the exchange. This is a played recurrence of the targeted checking-sequence failure, so reliable transfer is already not established.

I anticipated the subsequent discovered rook check ...Bc5+ and used Ke2 to keep Be3 defended. After ...Bxe3/Kxe3, ...Rxc3+ took a pawn. Further checks collected a2; f4 attempted counterplay, but ...Rd3+/Kg4/...Rxg2+ left White rook, knight and three pawns against two rooks and six pawns. I resigned with legal king escapes still available, on my practical assessment rather than a forced-loss certificate.

Continue the five remaining predeclared games and review at 72. This loss is preserved; anticipating one check and defending its first target did not complete the actual forcing sequence.

## Benchmark 68 — Black versus maximum, loss

Resigned after 21.Qa8, 41 plies and no illegal submissions. Elo remains 1710 [1580, 1840], with 44 rated games and now 24 excluded maximum games. Overall record: 28 wins, one draw and 39 losses. Trial 07 is zero wins and two losses.

In the Advance Caro–Kann, I anticipated Qb5+ after ...Ncxe5 and answered ...Nd7. After dxe6/...fxe6/Rd1, ...Qe7 supplied a defender for the bishop and pawn, but Bg5 displaced it to f7. Against Ne4 I chose ...Be7 to avoid a loose bishop and a contemplated Nd6+ fork. That move blocked Qf7's line to Nd7. The actual Qxd7+ won the knight: Kxd7 was unavailable because Rd1 defended d7, and the bishop on e7 prevented ...Qxd7. This is an exact defender-obstruction failure, not a successful application of the earlier checks.

...Kf8 was followed by Qxb7. ...Rd8/Rxd8+/...Bxd8/Qa8 left the bishop pinned along the eighth rank and attacked by Bg5 as well. I resigned a knight and pawn down, with further material loss threatened, on my own practical assessment. No forced-loss or best-defense certificate was obtained. The block already has two targeted failures; finish games 69–72 before the declared review and revise the method at that endpoint regardless of easy-opponent results.

## Benchmark 69 — White versus skill 0, win

Won by 32.Ra8#, 63 plies, zero illegal submissions. The rounded estimate and interval remain 1710 [1580, 1840], now with 45 rated games. Overall record: 29 wins, one draw and 39 losses. Trial 07 is one win and two losses.

Useful actual handling included keeping Nf3 on the c6–g2 diagonal while Black's queen and bishop were aligned, retreating Bd4 to c3 while preserving its defense of Nf6, and using a real pawn recapture after Nxh5/...Rxh5/gxh5. Black's ...Qxc3 allowed bxc3 to win the queen for bishop, and ...Ng3 allowed fxg3. These large opponent errors enabled the conversion.

The passed pawns forced the remaining bishop to move; the unanticipated ...Bd4+ was answered by cxd4. After promotion and ...Bxf3, Qxf3 both recovered the bishop and cleared the e-file for Re1 to defend the promoted queen. ...Rxe8/Rxe8 removed Black's last rook. Against the actual ...c5, Ra8# was protected by Qf3 through e4/d5/c6/b7, with b7 also covered. No played targeted omission causing material loss was identified. This skill-0 result does not repair the failures in 67–68 or establish sustained improvement. Continue 70–72.


## Benchmark 70 — Black versus skill 0, win

Won by 36...Rd1#, 72 plies, zero illegal submissions. Elo remains 1710 [1590, 1840], with 46 rated games. Overall record: 30 wins, one draw and 39 losses. Trial 07 is two wins and two losses.

I recognized Nd2's new defense of Rf1 and rejected ...Qxf1+. The chosen ...Nxe3 was nevertheless an unproved sacrifice: the actual checking line and queen trade left three extra pawns for a knight. The later win does not establish that this was sound or preferable. I prepared ...f4 with ...h6/...g5 after recognizing the bishop-and-rook captures available against an unsupported push. Against Ng3, ...f4 forked bishop and knight; Bxf4/...gxf4 recovered a minor piece, and Rh2/...Bg4+/Kd2/...fxg3 won another.

White then allowed ...Rf2+/Ke1/...Rxg2 and left the last knight to ...Bxd4. ...Bxc3+ and the two-rook finish produced recorded mate. No played targeted omission causing material loss was identified, but the sacrifice assessment remains uncertain and major opponent errors drove the win. The failures in 67–68 remain. Complete 71–72 before the declared method revision.


## Benchmark 71 — White versus nominal 1800, loss

Resigned after 12...Rxh6, 24 plies, zero illegal submissions. Elo is 1700 [1580, 1830], 47 rated games. Overall record: 30 wins, one draw and 40 losses. Trial 07 is two wins and three losses.

After normal development and castling, I played Bxh6/Bxh6/Qxh6/Rxh6. I explicitly knew Rh8 had an open line to h6 but treated the queen's attack on that rook as forcing a retreat, ignoring that the rook could capture the undefended queen on the same line. This is a third clear process failure. It is not explained by calculation depth or an obscure tactic. The actual ...Bxh6 should have triggered a fresh recapture check and did not.

I resigned queen down for a pawn on my own practical assessment. The loss is retained. The declared endpoint remains game 72, after which the ineffective practice method must change; neither recording this error nor recalling the line counts as correction.


## Benchmark 72 — Black versus nominal 1800, loss

Lost to 66.Qg5#, 131 plies, no illegal submissions. Elo is 1700 [1570, 1820], 48 rated games. Overall record: 30 wins, one draw and 41 losses. Trial 07 finishes two wins and four losses.

Early development, a central exchange and ...Rxb2 produced an extra pawn. At 30.f3 I identified the discovered-check danger and chose ...Ng3/Bf2+/...Ne2+. I omitted the effect of Kf1: Ne2 remained pinned and the white king supported Rxe2. ...Kd6/Rxe2 lost the knight. The checked initial interposition did not resolve the actual continuation.

Connected queenside passers and ...a1=Q recovered counterplay. I caught the possible Bb4+ fork before taking a3 and later applied the changed white-king defense of e1. Both sides promoted; ...Qc1/...Rxe1+/Rxe1/...Qxe1+ recovered the bishop and exchanged rooks. This reached a queen ending with two pawns each, but it did not erase the earlier failure.

After Qd4+/...Kg5/Qg7+/...Kh5/f4, I pushed ...b2 and missed Qg5#. White's f4 pawn now defended g5, preventing the king capture. The final immediate mate is a second clear targeted failure in this game. No best-play or forced-win assessment was obtained.

## Endpoint and decision

The predeclared games 67–72 are complete: 2W/0D/4L. Maximum: 0/2; skill 0: 2/2; nominal 1800: 0/2. Baseline 1710 [1580, 1840], endpoint 1700 [1570, 1820]. The uncertainty overlaps; the result supplies no sustained increase. Targeted failures occurred in four of six benchmark games. Observed cumulative whole-goal usage at the endpoint was 14,265,653 tokens.

The five short remembered drills failed to produce reliable live application. Archive this move procedure and replace the practice format with longer play from fresh initial positions at a selectable intermediate strength. Specify the new duration, stopping rules and benchmark point before starting. Merely restating a safety check is not evidence that it will be applied. No external move advice, automated analysis or delegation was used.
