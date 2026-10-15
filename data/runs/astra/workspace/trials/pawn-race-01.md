# Practice trial 01: pawn races before liquidation

Plan recorded on 2026-09-30 after completed game 30, before any measured game 31. This is practice, not benchmark evidence.

Target: stop entering or assessing pawn endings on a pawn-push count that omits king interception, capture of a newly promoted piece, or a promotion check. Game 30 provides a recent failure; earlier reviews also contain mistaken pawn-ending judgments.

Method and duration: one session of eight manual exercises, expected 20–30 minutes and limited to 45 minutes. First state a conclusion and concrete line from the board; then check only the legality of that supplied line and manually reconsider the opposing king's route. No engine, tablebase, automated search, scoring, best-move generation, or delegated advice. Mechanical board rendering and legality checks are allowed. Two positions are remembered game-30 positions; the other six are self-composed variations, not independently selected unseen tests. Self-assessments remain unverified.

Transfer change: before a voluntary exchange that produces a pawn ending, reconstruct the resulting kings and pawns, count moves through promotion, and check whether either king can intercept or capture the promoted piece. A claim of a favorable or safe race must have a concrete line accounting for checks and king intervention. This is a narrow execution change, not a longer general move checklist.

Evaluation: resume the fixed measured rotation for games 31–36, then review the recorded Elo/95% interval and recurrence of this error. Baseline after game 30: 1780 [1590, 1990], 20 rated games; maximum-strength games excluded by the unchanged estimator. The six-game block includes both colors at each of the three settings. Record every relevant pawn-ending decision, including errors; if no relevant ending occurs, transfer is untested. No repeated false race claim and correct anticipation of actual king intervention would be process evidence, not proof of an Elo increase. Sustained rating improvement needs later evaluation as well. At game 36 decide whether to repeat, revise, or replace this method.

## Exercise prompts, fixed before solving

1. Remembered: game 30 after 69...Kxc2. White Ke3/Pf4; Black Kc2/Ph5; White to move. Reconstruct the played race and locate the mistaken assumption. Do not infer a forced result from one played line.
2. Remembered: game 30 after 73.f6. White Kg2/Pf6; Black Ke4/Ph4; Black to move. Test the checking push ...h3+ and the king chase ...Kf5.
3. Self-composed change to exercise 2: White Kg2/Pf5; Black Ke4/Ph4; Black to move. Does the same promotion argument still apply?
4. Self-composed: White Ka1/Pa6; Black Kh8/Ph3; White to move. Follow the direct pawn race and determine whether the first promotion changes the reply available to Black.
5. Self-composed change to exercise 4: Black king on g7 instead of h8. Follow the same direct pushes. Identify any promotion check without asserting the full queen-ending result.
6. Self-composed: White Ka1/Pc5; Black Kf6; White to move. Can Black catch the directly advancing pawn? Follow the line through a promotion capture if applicable.
7. Self-composed change to exercise 6: Black king on g6. Can Black still intercept the direct pawn advance?
8. Self-composed: White Ka1/Pa2; Black Kg4; White to move. Compare a3 with the initial double push a4, including the king's route and the final capture square.

## Work and observations

Manual conclusions recorded before the mechanical line check:

1. The played line was Kf2 Kd3 f5 h4 Kg2 Ke4 f6. White's king approaches the h-pawn while the f-pawn keeps moving beyond Black's king. The mistaken assumption was that Black's king could still stop promotion after White diverted its king toward h4. From f5, ...Kg6 does not control f8. This reproduces a remembered failure and is not a new test or a proof of best play at move 70.
2. ...h3+ Kxh3 Kf5 f7 Kg6 f8=Q leaves White with the queen; the checking push removes Black's remaining pawn rather than winning the race. After the immediate ...Kf5, f7 followed by f8=Q also outruns the king. The closest king approach cannot reach f8 in time. This is a remembered position.
3. ...Kxf5 is an immediate legal capture: White Kg2 does not defend f5. Moving the white pawn back one rank invalidates the promotion argument. No claim about the complete subsequent rook-pawn ending is needed.
4. a7 h2 a8=Q gives check along the eighth rank to Kh8. Black cannot respond with h1=Q while leaving that check unanswered. After ...Kh7, Qh1 can block the pawn. Here the first promotion changes the available reply.
5. a7 h2 a8=Q does not check Kg7; ...h1=Q checks White Ka1 along the first rank. Continuing the exchange matters: Qa8 can capture Qh1 along the clear diagonal. I initially considered stopping at two queens, then noticed this last capture during manual calculation. This is not evidence of an independently solved queen ending.
6. c6 Ke6 c7 Kd7 c8=Q+ Kxc8 catches the pawn even though the promotion gives check. The white king on a1 does not defend c8. A promotion count ending at the check symbol would give the wrong conclusion.
7. With Kg6 instead, c6 Kf6 c7 Ke6 c8=Q gives check and the king cannot capture c8. Its initial distance to c8 is four king moves, while White's direct advance allows only three black turns through the promotion-capture turn. The earlier pawn squares are also too far away for interception.
8. a3 Kf4 a4 Ke5 a5 Kd6 a6 Kc6 a7 Kb7 a8=Q+ Kxa8 permits capture. The double push changes the count: a4 Kf4 a5 Ke5 a6 Kd6 a7 Kc7 a8=Q promotes before the king can arrive. This final promotion is not check against Kc7. From g4 the king requires at least six moves to a8, while the double-push advance allows only five turns through the potential capture.

These conclusions are my own analysis. A mechanical check will establish only whether the explicitly supplied moves are legal; it will not certify wins, draws, optimal defense, or transfer to measured games.

## Session outcome and decision

Completed all eight exercises by 18:11 UTC on 2026-09-30, faster than the initial 20–30 minute estimate and within the 45-minute ceiling. The mechanical check accepted the ten supplied legal lines and rejected the deliberately supplied ...h1=Q that ignored check in exercise 4. Results are in `pawn-race-01-legality.json`; the inputs were recorded before that check in `pawn-race-01-lines.json`. Only the board/legality module was used, with bytecode writing disabled; no engine or analysis interface was imported.

The significant manual correction was extending exercise 5 through the final queen capture instead of stopping at two promotions. These small, self-composed examples are easier than choosing moves in a full game and provide no independent accuracy score or rating evidence. Decision: carry the narrow king-interception and final-capture check into games 31–36, then assess the predeclared transfer criterion. No additional practice is being substituted for that evaluation point.

## Measured transfer log

- Game 31, White, maximum strength: loss by resignation, 84 plies, no illegal submissions. No pure pawn ending played. Two candidate liquidations were explicitly reconstructed and judged unfavorable because Black could capture d6 immediately; these were own unverified calculations. The actual material loss began with 21.e4 Ne3+, a checking-fork omission outside this trial's narrow target. Rating unchanged at 1780 [1590, 1990], as maximum-strength games are excluded by the fixed estimator. No evidence of improved Elo or independently verified transfer from this game. Continue the planned block; evaluation remains after game 36.
- Game 32, Black, maximum strength: loss by checkmate, 59 plies, no illegal submissions. No pawn ending or candidate pawn liquidation arose, so the narrow practice target was untested. Missed the direct Qh5+–Qxh8# finish while considering more complicated continuations; this is a recurring forcing-move omission outside the trial target. Rating unchanged at 1780 [1590, 1990]. Continue the planned block through game 36.
- Game 33, White, skill 0: win by checkmate, 75 plies, no illegal submissions. No pawn ending or candidate pawn liquidation occurred; transfer remains untested. Immediate knight and queen checks were anticipated, but the win depended on substantial opponent material concessions. Elo 1790 [1600, 1990] from 21 rated games; the 10-point movement from baseline is not evidence that the pawn-race trial worked. Continue through game 36.
- Game 34, Black, skill 0: win by checkmate, 64 plies, no illegal submissions. No pure pawn ending or actual promotion. Related middlegame opportunity: with a pawn on a2, explicitly checked that promotion would not check because White's rook blocked the first rank; also checked the final queen recapture after a possible rook capture on a1. Answered the actual Qxg7 mate threat with ...Qxh6 before pursuing the pawn. These own counterfactual calculations overlap with the practice theme but do not establish transfer or causation. The opponent later lost its queen by taking the defended a2 pawn. Elo 1790 [1600, 2000]; next evaluation remains after game 36.

- Game 35, White, 1800 setting: loss by resignation, 138 plies, no illegal submissions. No pure pawn ending was played, though several candidate rook trades were manually examined. The actual rook ending reached two extra pawns. I caught the stalemate after hypothetical Kxf6 against Kh8, then missed the more basic final capture: 67.Rg8+ Kxh7 68.a6 Kxg8. The king's capture of h7 removed the pawn defending g8 and brought the king next to the rook. This is a recurrence of the final-capture/king-intervention error in a new position and negative evidence for reliable transfer. Elo 1770 [1580, 1960], 23 rated games. Preserve the declared game-36 evaluation point; the method needs revision or replacement, not a success claim based on the earlier local checks.

- Game 36, Black, 1800 setting: loss by resignation, 69 plies, no illegal submissions. No pure pawn ending. The actual 25...Qf6 26.Qxg6 Qxg6 27.Bxg6 lost a rook because I omitted the bishop's last recapture, despite noticing a related exchange on f5. Later ...Nb4 blocked Bd6's defense of a3 and allowed Rxa3. Elo 1740 [1570, 1930], 24 rated games. This is further negative evidence for reliable transfer of final-capture accounting.

## Evaluation after game 36 — 2026-09-30

The declared block is complete: 2 wins and 4 losses, with both skill-0 games won and both games at each of the maximum and 1800 settings lost. All six games had no illegal submissions. The estimator includes the four weaker-setting games and excludes the two maximum-setting games. Baseline: 1780 [1590, 1990], 20 rated games. Endpoint: 1740 [1570, 1930], 24 rated games. The 40-point decrease and overlapping uncertainty intervals do not establish a statistically reliable decline, and there is no evidence here of an Elo increase.

No pure pawn ending was reached, so the specific pawn-race transfer criterion was not directly tested in played pawn endings. Some candidate liquidations were counted and some local promotion/stalemate issues were caught. Those observations are outweighed for the broader final-capture concern by the actual ...Kxg8 omission in game 35 and Bxg6 omission in game 36. The exercise method has not produced reliable application in full play. Self-composed practice performance was not an independent accuracy score.

Decision: replace this trial with explicit reconstruction of short exchanges and defender/blocker changes. Use the fresh game-35/game-36 failures and controlled variants, account for the pieces remaining after every supplied ply, and then verify only supplied-move legality. The new trial has its own plan and evaluation point at games 37–42. Do not repeat the pawn-race drill unchanged or claim that additional checklist text constitutes learning.
