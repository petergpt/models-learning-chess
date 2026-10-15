# Trial 10: endgame races and legal recaptures

Declared 2026-10-01 21:44 UTC after benchmark 84. Baseline 1700 [1580, 1820], overall 35W/2D/47L. No sustained improvement established. Trial 09 and its timing data are preserved; discontinue its 20-second target. Use ordinary ./play interfaces. Opponent, estimator, model and fair-play rules remain fixed.

Weakness: in game 84 I treated an advanced connected pawn pair as adequate compensation without completing the defender's rook-sacrifice line. A king's geometrical contact with a square was wrongly treated as a usable recapture despite the opposing king. Training will focus on a specific endgame skill, rather than another longer general checklist.

Before each race decision, mentally carry both sides' promotion or capture line through the next actual capture and check whether each king recapture is legal. Count moves for both sides, including checks and rook sacrifices; a promotion is not the end of the line. Record concrete errors after each session. These are my own calculations, not certified evaluations.

Bounded practice: three sessions, at nominal 1800 as Black, at most 25 learner moves each including the opponent reply. First and second start from benchmark 84 after ply 116 (58...Kxg2; White moves first), allowing one explicitly remembered repetition. Third uses the new constructed rook-ending FEN `r7/8/4k3/P4p1p/1P4p1/3K4/6PP/2R5 b - - 0 1`. The new position is an unvalidated exercise, not a known theoretical result. Combined ceiling 22:29 UTC on 2026-10-01, including setup/reviews; stop unfinished practice at the ceiling, preserve all sessions, and do not add repetitions to seek a win. Own board reasoning and referee only; no engine evaluation, move suggestions or automated chess analysis.

Next fixed evaluation: benchmark games 85–90 after this practice, regardless of practice outcome. Assess all six results and Elo uncertainty, actual endgame opportunities/errors, and recurrence of earlier tactical losses. A block with no relevant ending cannot establish endgame transfer; do not force favorable benchmark positions. Any rating rise remains provisional and requires repeated evaluation. Practice is excluded from Elo. Revise again if the approach fails.


## Practice 10 — first remembered-position session, loss

Completed 2026-10-01 21:46:31 UTC by practical resignation after 66.h6; 15 session plies, seven learner moves, zero illegal submissions. Result seq 401, hash `5d6a509b01545a5c37f0fed219e5fec51b89893f92a67cce0e232060a07c929a`. PGN read back. The supplied ply 116 is after 58...Kxg2, not after 58.Rxc8 as initially described. The referee therefore played White's 59.Rc1 before my first move. Corrected the description, retained the session unchanged; the second session will use that same specified ply.

Actual line: 59.Rc1 f3 60.Ke3 f2 61.Ke2 Kh2 62.h5 f1=Q+ 63.Rxf1 g2 64.Rb1 g1=Q 65.Rxg1 Kxg1 66.h6. I avoided the original illegal conceptual Kxf2 recapture by choosing ...Kh2, but did not escape the rook-sacrifice mechanism. Both black pawns promoted and both queens were captured. White gave its rook for the second pawn, drawing my king to g1 while its h-pawn remained unstoppable. This demonstrates why promotion alone is not a successful race endpoint. Some analogous rook-sacrifice lines were anticipated in my own reasoning, but I still chose a continuation that allowed the mechanism. No winning alternative or theoretical value of the starting position is established. Resignation is a practical conclusion, not a solver result. Practice remains excluded from Elo.

Seven own moves used, session finished below the 25-move cap. Two declared sessions remain; do not add extra repetitions or change the practice outcome into benchmark evidence. Next try a king route that addresses the h-pawn before pushing both pawns, while recognizing that the starting position may already be lost; this is an unverified candidate plan, not a supplied solution.


## Practice 11 — sole remembered repetition, loss by checkmate

Completed 2026-10-01 21:49:24 UTC, 13 session plies, six learner moves, zero illegal submissions. Result seq 416, hash `00d2eaf8c36ed49557a6254dd43fdd841e6502051b588fb44e9feac3ae3c20a2`. PGN read back. Same benchmark-84 ply-116 starting position; opponent chose Rd8 instead of Rc1.

Actual line: 59.Rd8 Kh3 60.Ke4 Kxh4 61.Rh8+ Kg4 62.Rb8 f3 63.Rg8+ Kh3 64.Kxf3 e5 65.Rh8#. The alternative king route removed the h-pawn, but ...f3 and the checking rook drove the king away from that pawn, letting Kxf3 capture it. I then considered an e-pawn advance to draw the white king away from the g-pawn, and missed the immediate mating threat. Rh8# confines Kh3 because White Kf3 controls g2/g3/g4 and my own g3 pawn blocks that square. This is an actual missed mate, referee-confirmed, and another example of a longer race idea displacing the immediate opponent reply. No claim that the earlier position was defensible or that ...e5 was the first losing move.

Both remembered drills lost. No extra repetition will be added; finish the declared third new-position session, then benchmark 85–90 regardless of its outcome. These six own moves finished below the cap. Practice remains excluded from Elo.


## Practice 12 — new constructed rook ending, draw; practice phase complete

Completed 2026-10-01 21:53:04 UTC by referee automatic threefold-repetition claim after 21...Ra6+, 41 session plies, 21 learner moves, zero illegal submissions. Result seq 459, hash `b8812c8df1920c209bdad33e6599634e1f6ced724c37e4d9f2908ab82a1da042`. PGN read back. The position was the declared constructed FEN, not an independently evaluated theoretical exercise.

After ...Ke5, Rc5+ drove the king away and Rxf5 took the f-pawn. ...h4/...g3 and ...Rh8 preserved the remaining pawns temporarily. White advanced b5/a6/a7; I used ...Kc5/...Kxb5 and ...Ra8/...Rxa7 to remove both passers without giving up the rook. Leaving h8 conceded h4 to Rxh4. ...Ra3+ defended g3 while checking; I brought the king through c5/d5/d4. White eventually used Rxg3 with Kf4 protecting that rook. I declined the rook exchange because the resulting pawn ending looked unfavorable, preserving my rook with ...Ra1. This is my own assessment, not a proved endgame value.

With rook against rook and g/h pawns, ...Ra5+/...Ra6+ kept checking the exposed white king from the side. White alternated among g6, f5 and e6 and the referee claimed repetition. The recorded draw does not prove a forced draw against every defense, and the earlier pawn losses are not erased. No direct unreciprocated major-piece loss, illegal move, or actual missed immediate mate was identified in this session.

Trial-10 practice total: 0W/1D/2L, 34 learner moves, 69 session plies, zero illegal submissions. All three finished below their 25-own-move caps and by 21:53:04, before the 22:29 combined ceiling. The two remembered drills retained the same starting position and every loss; the new exercise was not repeated. Practice 11's missed rook mate is a clear failure, while practice 12's side-check draw is one useful defensive result, not established transfer. No further practice is added before the declared fixed benchmark 85–90. Continue that block with the trial-10 endgame focus and ordinary referee commands; the trial-09 20-second target remains discontinued.

Elo remains the benchmark-84 value 1700 [1580, 1820], with 56 rated games total / latest 50 used. No sustained improvement is established. All moves and reviews were my own, without external chess advice, automated chess analysis, engine evaluation, or delegation. Actual observed cumulative whole-goal usage after these sessions: 16,173,564 tokens / 172,631 elapsed seconds.


## Benchmark 85 — White versus maximum strength, loss

Completed 2026-10-01 22:00:50 UTC by practical resignation after 26...Bxb7; 52 plies, 26 own moves, zero illegal submissions. Result seq 7087, hash `3440787a1b3e65dd2a8f4367691b251e9265fc6d1abf6e048900d9775261bded`, snapshot `a23ef28ba03d5e1a54afb2429f03f3c4152d5250de0477e0aaa37193e4d8ed35`. Saved PGN read back. No best-defense or first-losing-move certificate is claimed.

The queen-pawn opening exchanged the central pawns and then queens. ...Qd5 attacked Rh1; Nf3 blocked that diagonal and allowed Qxd1+/Kxd1. Black's subsequent bishop checks and rook development kept my king moving. ...Bb4 pinned c3, so Bd2 supplied a blocker before the knight exchange; ...Nxd4/cxd4/Rxd4/Bxb4/Rxb4 left me a pawn down. The recapture on b4 was understood, not a surprise piece loss. Black's active rook then took a2 and e2 while my rooks and king moved into exposed positions.

After ...Re5, 24.Rhb1 enabled ...Bc6+, skewering Kf3 and Bg2. I recognized the bishop loss once the check occurred, but had not accounted for it before Rhb1. Kg4/Bxg2 lost that bishop. The final 26.Rxb7+ was a separate direct rook blunder: I considered king replies and follow-up checking sequences but omitted the checking rook's capture by Bg2 along f3/e4/d5/c6/b7. Black played ...Bxb7. Rb1's protection did not rescue the tactic because Kb8 defended b7, so Rxb7+ would allow Kxb7. Resignation followed with R+3P against 2R+B+5P. A check being answerable by capture remains an actual recurring failure.

No pawn-promotion race occurred, so this game does not directly test the trial-10 race exercise. It does show another failed transfer of the broader immediate-capture discipline, with an actual major-piece loss. The result is preserved; no extra practice or altered benchmark opponent is introduced mid-block.

Through 85: overall 35W/2D/48L. Maximum strength 0W/2D/27L in 29 games; skill 0 26W/0D/2L and nominal 1800 9W/0D/19L, each in 28. Elo remains 1700 [1580, 1820], 56 rated total / latest 50 used, 29 maximum exclusions. Trial-10 benchmark currently one loss; finish 86–90 before its endpoint. No short-decision timing target applies. Observed cumulative whole-goal usage 16,298,116 tokens / 173,091 elapsed seconds. All decisions and review were my own; no external chess advice, automated chess analysis, engine evaluation or delegation was used.


## Benchmark 86 — Black versus maximum strength, loss

Completed 2026-10-01 22:09:44 UTC by practical resignation after 27.Qxa8+, 53 plies, 26 own moves, zero illegal submissions. Result seq 7143, hash `61e7175ba05b0409b11e5c062b254b2a231cbfc4c90b4210823a0d52081928e4`, snapshot `d1b0ff3a430dadbed97736ff21299a2347eee0b6e8818a6312be4f0d7ad44d14`. Saved PGN read back. No independent first-losing-move or optimal-defense claim.

The closed king-pawn opening reached ...c4/b4 and sent Na5 to b7. The ...a5/axb5/axb4 sequence opened the a-file, but White's b6 pawn attacked Qc7 and constrained my queen and knight. I moved Qc8 and recaptured Rxa8 with Qxa8; cxb4 left White an extra pawn. ...Qa2 attacked Bc2 but Qc1 defended it; Nc3 then attacked the queen. I chose ...Qa6 without foreseeing how Ra1 would confine it. After Qb2/f5/Ra1 I recognized that the direct queen retreat squares were occupied or attacked and chose ...Qxa1+/Qxa1 as a queen-for-rook concession. I considered interpositions but did not establish a sound saving line; this is not a claim that the concession was objectively forced.

The last move was an additional direct rook blunder, separate from the queen problem. After ...f4/Bc1 I played 26...Ra8 to attack Qa1, imagining queen retreats. I failed to apply the reciprocal attack along that same open file: the rook had no defender and White simply played 27.Qxa8+. This was not an intended exchange or a surprise remote tactic. I resigned with no major pieces against White's queen, in addition to the pawn deficit. Both the confined queen and the undefended rook are concrete failures preserved in the record.

White's advanced pawn mattered to the queen's confinement, but no promotion race or rook-only ending occurred. Thus the bounded endgame practice has not supplied positive transfer evidence in either maximum-strength game. The direct-capture failure recurred despite prior explicit notes; do not call the new trial effective.

Through 86: overall 35W/2D/49L. Maximum strength 0W/2D/28L in 30 games; skill 0 26W/0D/2L and nominal 1800 9W/0D/19L, each in 28. Elo unchanged at 1700 [1580, 1820], 56 rated total / latest 50 used and 30 maximum exclusions. Trial-10 benchmark currently 0W/0D/2L; finish 87–90 before the declared endpoint. Observed cumulative whole-goal usage: 16,475,357 tokens / 173,625 elapsed seconds. All chess decisions and review were my own; no external advice, automated chess analysis, engine evaluation or delegation.


## Benchmark 87 — White versus skill 0, win

Completed 2026-10-01 22:19:35 UTC by 25.Qa8#, 49 plies, 25 own moves, zero illegal submissions. Result seq 7195, hash `6b0cf96f954febb186a77e4fc51b63e88e1bcbc6524d563e2b75a87188cb113d`, snapshot `8464d4e26ce1ef5b896ebbf26a2beba06a99dae99e3433a2223304ee5dd06f1e`. Saved PGN read back; terminal mate is referee-confirmed.

Black's ...Nxe4 and ...Nd6 allowed Qe2/Nc6+, a discovered check with a queen fork. After ...Qe7, Nxe7 captured the queen. Black chose ...a6 rather than recapturing; Nd5+ preserved the knight. I moved that knight when ...c6 attacked it, took the undefended Nc4 with Qxc4, and answered ...d5 by moving the attacked queen to d3. ...g5 attacked Bf4, so Be5 preserved it while attacking Rh8. ...Bf5 attacked Qd3 but was itself capturable; Qxf5 removed that bishop, followed by Bxh8.

Nd2 cleared the queenside castling path, and O-O-O completed castling legally. Qxf7 collected a pawn; Bd3 and Rhe1 completed development. Be5 offered a supported exchange, but ...Kc8 allowed Bxd6 without an immediate recapture. Qxa7 took the remaining rook. Re7 covered the king's escape along the seventh rank, and Qa8# completed the mate with Bd6 also controlling c7/b8. No actual direct unreciprocated queen/rook loss, illegal move, or missed immediate opponent mate was identified in the played line. Unplayed branches were not independently evaluated, and this is not a claim of optimal play.

Opponent concessions supplied the decisive advantage. This was not a promotion-race test, and an easy material conversion after winning a queen does not establish endgame transfer or stronger general play. Preserve the favorable result alongside the two previous maximum-strength losses.

Through 87: overall 36W/2D/49L. Skill 0 27W/0D/2L in 29; maximum strength 0W/2D/28L in 30; nominal 1800 9W/0D/19L in 28. Elo 1710 [1590, 1830], 57 rated total / latest 50 used, 30 maximum exclusions. Trial-10 benchmark so far 1W/0D/2L; games 88–90 remain. The 10-point increase from baseline has broadly overlapping uncertainty and is not sustained improvement. Observed cumulative whole-goal usage: 16,517,983 tokens / 174,216 elapsed seconds. All decisions and review were my own; no external chess advice, engine evaluation, automated chess analysis or delegation.


## Benchmark 88 — Black versus skill 0, win

Completed 2026-10-01 22:35:06 UTC by 41...Rd1#, 82 plies, 41 own moves, zero illegal submissions. Result seq 7280, hash `d826034ec6f9b700b4f5a35de34218d6889e920fbf4361e8acae63316539f02d`, snapshot `b5b3a6af516f9b1671d9a9c00dbe1a5a6217281d64df500fc5fd9245f5bacb48`. Saved PGN read back. The mate is referee-confirmed; no optimal-play claim.

White declined to recapture after ...exd4. ...Bc5 both supported that pawn and removed the potential e5 pawn fork of Bd6/Nf6. I answered the later queen, knight and bishop attacks with ...Qg6, ...Nf6 and ...Bb6. White's Ne5 removed Nf3's defense of Bg5, so ...Qxg5 captured it. ...Qxf4 answered the f-pawn attack by taking that pawn; ...fxg6 captured the knight that subsequently attacked the queen. Opponent concessions supplied a large advantage.

After ...Qxh3+/Nh2, the pinned knight could not take ...Bxg4. I chose ...Bf3+ after explicitly considering both Kg1 and Qxf3. White took the bishop; ...Qxf3+/Nxf3 traded queens, intentionally leaving the bishop unrecovered. This was a material concession for simplification from a large lead, not an unexpected loss or a proved necessity. The subsequent ...Nxe4/Ne5/...Rxe5/Rxe4/...Rxe4 exchanged the knights and won a rook. ...Rf8 was defended by Kg8; Rxf8+/Kxf8 removed White's final rook as intended. This differs from game 86's undefended reciprocal-file error.

The passed d-pawn then supplied a relevant, limited endgame instance. After ...d3+/Kf1 I placed the rook on d4 behind the pawn before advancing ...d2+. The king blockaded d1, so I brought my king forward and removed White's remaining pawns. When White moved Kc2, ...d1=Q+ was protected along the d-file by Rd4, preventing Kxd1. Qb3+ was protected by c4; ...Rd1# was protected by Qb3. I identified the own c4 pawn as a blocker before considering a rook capture along the fourth rank and made no illegal submission.

No unanticipated direct queen/rook loss or actual missed immediate mate was identified. The defended promotion is one correctly handled case, but White had already lost all pieces and posed no competing promotion threat by then. It does not validate performance in a contested race like game 84 or establish general improvement.

Through 88: overall 37W/2D/49L. Skill 0 28W/0D/2L in 30; maximum strength 0W/2D/28L in 30; nominal 1800 9W/0D/19L in 28. Elo 1720 [1600, 1850], 58 rated total / latest 50 used, 30 maximum exclusions. Trial-10 benchmark 2W/0D/2L; complete nominal-1800 games 89–90 before the endpoint. The small rating rise is provisional, with overlapping uncertainty. Observed whole-goal usage: 16,677,847 tokens / 175,147 elapsed seconds. All chess decisions and review were my own; no external advice, engine evaluation, automated chess analysis or delegation.


## Benchmark 89 — White versus nominal 1800, loss

Completed 2026-10-01 22:54:44 UTC by practical resignation after 33...Bh2+, 66 plies, 33 own moves, zero illegal submissions. Result seq 7349, hash `c1c106cc2d3263a13504d49790bcf1306a5e3724b2992b5f4b9d14a98460df14`, snapshot `4603afda667191547db7500d414371d195a0f680781f05020d6b4a5d58672ce0`. PGN read back. No independent optimal-defense or first-losing-move claim.

The Scandinavian opening reached d5/Nb4/Bc4/Bf5. Nd4 supplied a defender for c2 while attacking the bishop. I castled, but ...Bxd5/Nxd5/Nbxd5 removed the advanced pawn, leaving a pawn deficit. Further development and the ...Nxe3/Qxe3 exchange left B+N each with queens and rooks. I answered ...Bb4's attack on Re1 with c3 and moved the queen when ...h6 attacked it.

The f-pawn advance failed to produce a sufficient attack. After f4/...Nd7/f5/...Bd6, Ne5 was pinned to Qg3 and attacked twice. I explicitly rejected knight retreats that would expose the queen. The chosen f6 threatened the king but ...Nxf6 took that pawn; I then moved Qe3 to unpin, now two pawns down. This was a considered concession, not a claimed sound or forced sacrifice.

The queen was then driven through Qe4 and Qd4. After ...b4, Nc4, ...Bg3, Rf1, ...bxc3, bxc3 and ...c5, I found its direct retreats occupied or attacked. My own Nc4, Bd3 and c3 pawn restricted its movement, while Nd5, Bg3 and f5 covered key remaining squares. I had not anticipated that confinement when selecting Qd4 and Nc4. I chose 32.Qe3 knowing ...Nxe3 would capture it; 33.Nxe3 recovered the knight, and ...Bh2+ preceded resignation. Final material was 2R+B+N+4P against Q+2R+B+6P. A sound alternative at move 32 has not been independently ruled out, so do not call the concession objectively forced.

This is another actual queen-for-minor-piece loss after failing to anticipate confinement, alongside game 86. No promotion race occurred. The endgame practice does not establish improvement in these middlegame decisions, and the trial already contains major-piece failures in 85, 86 and 89.

Through 89: overall 37W/2D/50L. Nominal 1800 9W/0D/20L in 29; skill 0 28W/0D/2L and maximum strength 0W/2D/28L, each in 30. Elo 1710 [1590, 1830], 59 rated total / latest 50 used, 30 maximum exclusions. Trial-10 benchmark 2W/0D/3L, with game 90 still due before its endpoint. Observed cumulative whole-goal usage 16,848,644 tokens / 176,325 elapsed seconds. Every move and review was my own; no external chess advice, engine evaluation, automated chess analysis or delegation.


## Benchmark 90 — Black versus nominal 1800, win

Completed 2026-10-01 23:09:28 UTC by 41...Rc1#, 82 plies, 41 own moves, zero illegal submissions. Result seq 7434, hash `308b2fdd9e2c6e99b0c594eec3d6324ec9c408398aaa70d904a8b9b3aa17339a`, snapshot `7da82978c232c844c59ae9e879d6b614905db72b2fcbab5695cea03d5302be66`. Saved PGN read back; mate is referee-confirmed. No optimal-play or first-losing-move certificate.

Against e3/Be2 I developed with ...d5, ...Nf6, ...e6, ...c5, ...Nc6 and castled. White's knight retreats allowed ...e5 and normal development. The c4/d4/exd4/exd4 sequence produced a passed d-pawn. I exchanged the blockading Nd3 with ...Bxd3 and the dark bishops with ...Bd6/Bxd6/Qxd6. ...Ne5 attacked the queen; ...Nxf3+/gxf3 weakened the white king's cover.

The central sequence was a useful calculation success: ...d3/Bxd3/Rxe1, followed by White's c5 instead of recapturing, permitted ...Rxf1+/Kg2/...Qxd3/Qxd3/...Rxd3. I carried the queen exchange through the rook recapture and emerged with two rooks and a knight against pawns. White's refusal to recapture the first rook and subsequent king move supplied a much larger gain than the initially considered line; this is not proof that all defenses lose the same amount.

The conversion then contained an actual unanticipated rook loss. Rf1 was within White Kg2's capture reach. While concentrating on pawn captures and avoiding other king attacks, I left that rook loose through ...Rc3 and ...Rxa3; 28.Kxf1 captured it. Neither Rd3/Ra3 nor Nf6 defended f1. This was not a deliberate sacrifice for simplification. The remaining rook, knight and pawns still supplied a large advantage, but the win does not erase the failure to inspect the unmoved rook.

I removed b4, f4, f3 and c5, then promoted the a-pawn with the white king far away. White's lone h-pawn could not produce a competing promotion. ...Qe5+/Kh1/...Qg3 left h5 as the pawn move before ...Rc1#. This was an easy promotion/conversion after overwhelming material gain, not evidence of solving a contested race. All moves and review were my own, without external chess advice, engine evaluation, automated chess analysis or delegation.

Through 90: overall 38W/2D/50L. Maximum strength 0W/2D/28L; skill 0 28W/0D/2L; nominal 1800 10W/0D/20L, each in 30 games. Elo 1720 [1600, 1840], 60 rated total / latest 50 used, 30 maximum exclusions. Observed cumulative whole-goal usage 16,938,003 tokens / 177,221 elapsed seconds.


## Trial 10 endpoint — revise; no sustained improvement established

The declared benchmark block 85–90 finished 3W/0D/3L: both maximum games lost, both skill-0 games won, nominal 1800 split 1–1. Elo moved from 1700 [1580, 1820] to 1720 [1600, 1840], with broadly overlapping intervals. The trial does not establish sustained improvement. Practice was 0W/1D/2L, with a missed mate in practice 11. Benchmark games 88 and 90 contained correctly completed promotions against opponents already without pieces; neither tested a contested rook-sacrifice race like game 84.

Substantial safety failures remained in four of the six benchmark games: 85's bishop skewer and captured checking rook, 86's queen confinement and undefended rook, 89's queen confinement, and 90's missed king capture of an unmoved rook. The central exchange calculation in 90 was better handled, but did not generalize even to preserving the resulting material. Retire the race-focused trial as the main intervention; preserve its notes and all results. The next bounded trial will target recognizing the opposing king as an active attacker during sparse-board conversions, with recorded practice followed by another fixed six-game evaluation. No success claim is made from this choice itself.
