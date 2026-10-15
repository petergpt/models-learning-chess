# Trial 14 — keep the king's defenders usable

Declared after benchmark 108, reference clock 2026-10-02 07:34:42 UTC. Baseline 1660 [1540, 1780], 45W/2D/61L; 72 rated total/latest 50 used, 36 maximum exclusions. Next fixed benchmark endpoint: games 109–114. Opponent rotation, estimator, model and fair-play rules remain unchanged.

Target: a legal king move can pin or obstruct the very piece needed against the next check. In 108, ...Ke8 put Be7 between Re1 and the king; Nxf6+ then made the intended bishop capture illegal. In 104, the checking bishop departure from d2 changed the king/rook defense. Trials 04 and 05 already studied changed lines and defenders and failed. This trial is a focused rehearsal of an old weakness, not a claim of novelty or a longer checklist proving learning.

Practice change: defend from my own side against maximum strength for a longer short continuation, instead of the six-move role-reversed captures in trial 13. Exactly two recorded sessions, in order:

1. Black from game 108 after ply 45, before the failed ...Ke8. Remembered. Manually consider ...Qc6 as an unverified alternative: it would defend f6 with the queen while keeping the king off the e-file. The actual opponent may choose a different attack; this is not a supplied engine answer.
2. Black from game 104 after ply 49, in check after Bxh6+. Remembered. Reconstruct the checking line and choose the defense on the actual starting board. Do not presume that an earlier imagined king square is legal or safe.

Each session ends naturally or explicitly unfinished after twelve own moves and the final opponent reply. Combined practice-and-review ceiling: 2026-10-02 08:04:42 UTC. No extra repeats, no replacements for an unfavorable starting position, and no later historical move lookup during either session. End any active drill at the ceiling and record omissions. Both are remembered own failures, so even a clean continuation is rehearsal, not independent proof of transfer or a completed defense unless the game actually ends.

The immediate practice objective is to reduce the attack while preserving legal recaptures and king exits. Before a selected king move, reconstruct the new rook/bishop/queen line through the king, including any own blocker now pinned; then inspect the next forcing check using that resulting board. A piece geometrically reaching a capture square is not a usable defender if moving it exposes its king. When an opponent exchanges a defender, discard that defender from the next branch. Keep direct destination captures and ordinary checks in view, but use only brief factual notes when useful, without mandatory per-move audit claims.

Record the actual lines, material changes, illegal attempts, newly imposed pins or obstructions, and whether the attack was resolved at the cap. For benchmarks 109–114, retain every analogous recurrence and the full W/D/L/Elo outcome. A recurrence rejects reliable execution; a clean block or small rating rise still requires later repeated evaluations before sustained improvement can be claimed. Revise at 114 rather than continuing this method indefinitely.

Only own chess reasoning, own existing notes and the referee during play. No external move advice, engine analysis, automated move search/scoring/attack enumeration, tablebases or delegated chess work. No valid new cumulative usage counter is available.


## Practice 23 — remembered 108 defense, immediate mate

Finished naturally at 2026-10-02 07:36:14 UTC, one own move / two plies, zero illegal submissions. Result seq 687, hash `09189acc28a4f90e59ca78a1439a7e38594543c9817e0e9ff074bff8b5fa6c60`. PGN read back. Actual line: 23...Qc6 24.Qh8#.

The proposed ...Qc6 did add queen support to f6 while leaving Kf8 off the e-file, but it failed to answer the immediate mating threat. In the manual assessment I incorrectly treated e8 as an escape after Qh8+, focusing on Be7 blocking Re1; the queen on h8 itself controls e8 along h8-g8-f8-e8 once the king leaves f8. Be7 occupied e7, f7 was occupied, and the queen covered g7/g8. The referee confirmed mate on the next move. This is an omitted immediate check and a wrong king-exit assessment, not a successful alternative to ...Ke8.

The starting position may already require an earlier defensive improvement, but no claim that every legal defense loses has been proved. The late remembered selection cannot test recovery from a sound position merely by being called practice. Retain it, with no replacement or extra repeat. The first session already refutes reliable execution of this trial's immediate objective. Complete only the second predeclared session and preserve the benchmark endpoint 109–114; practice has no Elo effect.


## Practice 24 — remembered 104 defense, rook saved and then lost to promotion

Finished naturally at 2026-10-02 07:47:26 UTC by 37.h8=R#, twelve own moves / 24 plies, zero illegal submissions. Result seq 713, hash `65012f1d5663213d1ca35b1259a20cbf74be11c74a2d3bfd66369bdf03ad07a3`. PGN read back. Line: 25...Kc8 26.Bxg7 Rf7 27.h6 Bf8 28.Bxf8 Rxf8 29.g5 Rh8 30.Rh1 Nb6 31.g6 Nd5 32.g7 Ne7 33.gxh8=Q+ Kd7 34.Rd1+ Nd5 35.h7 Ke7 36.Qg7+ Ke8 37.h8=R#.

The starting board showed c6/c7 occupied by my own pawns and d6 attacked by e5; I chose ...Kc8 without an illegal attempt. ...Rf7 escaped Bg7 while attacking it. After h6 defended the bishop, I avoided ...Rxg7/hxg7 and instead used ...Bf8, genuinely supported by Rf7. Bxf8/Rxf8 traded bishops while retaining the rook, unlike the measured game's exchange concession.

That limited improvement did not hold the defense. ...Rh8 and the knight route a4-b6-d5-e7 focused on blockading g8/h8. I explicitly rejected ...Nf6 because e5 could capture there, but then omitted the most immediate consequence of 32.g7: the pawn now directly attacked Rh8. 32...Ne7 covered g8 but did nothing against 33.gxh8=Q+, an actual unanticipated rook loss with promotion. This repeats the direct pawn-capture failure despite the narrower king/defender focus. The later checks drove the king back; the actual final promotion was to a rook, not the queen I had anticipated, and the referee confirmed mate.

Initial material was R+B+N+6P each. After Bxg7 and the bishop exchange, Black had R+N+5P against R+N+6P. Final Black material was N+5P against Q+2R+N+4P. The saved rook in the early continuation is limited rehearsal evidence; the whole drill failed. Neither the starting position's objective evaluation nor an earlier best defense has been established.

## Trial-14 practice endpoint

Both predeclared sessions completed by 07:47:26 UTC, before the 08:04:42 ceiling, with no repeats or replacements: thirteen own moves / 26 plies, two checkmate losses, zero illegal submissions. Practice 23 missed an immediate queen mate and misread the eighth-rank king escape. Practice 24 initially kept the rook, then missed a direct pawn capture and promotion. The first objective has already failed reliable execution; the second demonstrates that concentrating on king lines can still displace an elementary capture threat elsewhere.

No improvement is claimed from these drills, and practice does not enter Elo. Return to fixed games 109–114 as declared, preserving these failures. Keep the modest cue about newly pinned defenders without treating it as a complete safety certificate or adding successful-audit counts. The benchmark baseline remains 1660 [1540, 1780], 45W/2D/61L through 108. No valid new cumulative usage counter is available.


## Benchmark 109 — White versus maximum strength, defender exchange and e-file loss

Finished 2026-10-02 08:04:50 UTC by practical resignation after 22...Qxe1+, 44 plies / 22 own moves, zero illegal submissions. Result seq 8829, hash `438a919b5e48bb48494437394e51d6828e8571f731ae45d85f2ff674726298a3`; snapshot `ebf48a6171d6dbc8fc02e1be6026c815096e938cdb14b9d580b93e0f3a5ac79f`. PGN read back.

The early d4 advance removed d3's support of e4, which Re1 restored. Qd3 unpinned Nf3, but the ensuing ...Bxf3/Qxf3/...exd4/cxd4/...Bxd4 sequence lost the central pawn. Bb5 avoided the additional Ne5 fork of Qf3 and Bc4. After Nc3 and Be3, however, I failed to carry ...Bxc3/bxc3 into the new e4 defense: Nc3 had departed and Be3 blocked Re1, leaving only the queen against ...Nxe4 supported by Re8. Black took a second pawn. Bd4 subsequently restored the rook and queen lines, but the earlier pawn loss remained.

The bishop-for-knight exchange on e5 was accounted. Qf3 defended c3, then 20.Rad1 was followed by the omitted ...Ng5: the knight attacked the queen while clearing the e-file between Re5 and Re1. With Qe7 behind the rook and White's king boxed by its pawns, the actual Qf4/Rxe1+/Rxe1/Qxe1+ sequence lost both white rooks for one black rook. I recognized this danger after ...Ng5 and deliberately chose that continuation; it was not an unexpected final queen capture, nor a proof that all earlier alternatives lost. The failure to prevent the forcing sequence belongs to the earlier position assessment.

At resignation White had Q+B+5P against Q+R+N+7P, nominally a rook and two pawns down. Bf1 remained a legal block of the current queen check; this was not checkmate and I did not claim a forced-loss certificate. The practical resignation retained the material loss and every played move.

After 109: 45W/2D/62L overall; maximum strength 0W/2D/35L in 37 games. Elo remains 1660 [1540, 1780], 72 rated total/latest 50 used, 37 maximum exclusions. Trial 14 has one benchmark loss following its two practice checkmates; no sustained improvement is established. Continue the declared block through 114 without adding practice mid-block.

The goal tracker was queried again at this checkpoint. It still returned the obsolete two-100-game maximum-strength objective with status blocked and the same stale 17,035,946-token / 178,558-second values, last updated before this continuation. This does not provide a valid new cumulative usage counter. No usage entry, goal reset, completion claim or status change was made. The latest user Continue and current local GOAL.md authorize continuing the revised measured-Elo experiment.


## Benchmark 110 — Black versus maximum strength, blocked king exit and exchanged rook defender

Finished 2026-10-02 08:23:00 UTC by practical resignation after 17.Qxh7, 33 plies / 16 own moves, zero illegal submissions. Result seq 8864, hash `3643b832b5c7a6cd1f50c252454f83aada36808619ee48b8d411360a742b45d3`; snapshot `2c162ef9d565d6ec363ef226a13ba22e448dc8984ac3b17b4f538aeb5238b375`. PGN read back.

The Caro-Kann pawn advance sequence led to ...fxe6 and an extra pawn, followed by Bxh7/Rxh7. I recognized the Qd3-g6-h7 danger and used ...Ne4 to block the diagonal, with d5 supporting that knight. After Nc3 I played 11...Nd7, intending ...Nf6 to defend Rh7 following an exchange on e4. This omitted White's 12.f3, and Nd7 also occupied the king's d7 escape square. In my subsequent manual calculation, immediately moving Ne4 to f6 or c3 would allow Qg6 with no identified legal answer. That is an unverified limited branch assessment, not a proof that every defense lost.

I chose 12...Ndf6 knowing the e4-knight remained exposed. The actual fxe4/dxe4/Nxe4 sequence left Black a knight down for one extra pawn. ...Qa5+ cleared d8, but Bd2 attacked the queen and required ...Qb6. White then played Nxf6+: the knight I had counted as Rh7's defender was exchanged. I had considered ...gxf6 opening the seventh rank for a possible ...Rf7 against Qg6+, but overlooked the simpler direct Qxh7 until the checking knight had already arrived. After ...gxf6, White captured the rook immediately along d3-e4-f5-g6-h7. No such extra defensive tempo was available.

At resignation Black had Q+R+B+7P against Q+2R+B+N+6P, a rook and knight down for one pawn. Black was not in check; this was practical resignation, not checkmate or an established forced-loss proof. The same departed-defender mistake recurred, while the narrower king-move cue did not prevent an own knight from obstructing a needed king exit.

After 110: 45W/2D/63L overall; maximum strength 0W/2D/36L in 38 games. Elo remains 1660 [1540, 1780], 72 rated total/latest 50 used, 38 maximum exclusions. Trial 14 is 0W/0D/2L in benchmarks so far, with its practice failures retained. No sustained improvement is established. Continue the predeclared block through 114; do not add practice or reset results mid-block. No valid new cumulative usage counter is available.


## Benchmark 111 — White versus skill 0, retained material and a completed pin-based mate

Finished 2026-10-02 08:36:00 UTC by 31.Qg7#, 61 plies / 31 own moves, zero illegal submissions. Result seq 8927, hash `963d596c6bc7114f3e71ad18aba6f155ca196993c87aa8480cae4d7315015ce8`; snapshot `a607c9d0bf73a3853ab7008ead1fd5d9abaa4015d5bfd7195eeff4419162d8bf`. PGN read back.

Development and castling preceded e5. Qd2 supported Bf4 against ...Nh5, and exd6 attacked Qc7, making an immediate ...Nxf4 inappropriate. After exd6/Bxd6/Bxd6, Black played ...Qc8 instead of recapturing. Later ...Rf8 allowed Bxf8, and ...b5 again declined a recapture; Bd6 saved the bishop. Bxh5 won the other knight. I moved the bishop away from ...g6 and ...f5, and moved Nc3 to e2 after ...b4 rather than onto the pawn-controlled e4 or d5 squares.

Bxd5 offered a bishop-for-knight exchange, but Black instead played ...Qd7, permitting Nxd7. ...Kf7 declined that recapture too. Bb3 then saved the bishop from c6/e6 pawn attacks. The enormous advantage therefore arose largely from the opponent's repeated missed recaptures and queen loss, not from forcing those concessions. White retained every non-pawn piece through the game.

I did not play Qxe6 once ...Re8 defended the pawn. Nc5/Nxb7 removed Black's last bishop. After ...f4 attacked Qe3, the actual finish was Qe5+ Kf7, Qf5+ Kg7, Be5+ Kg8, Qg6+ Kf8, Qg7#. Qf5+ correctly relied on Bb3 absolutely pinning e6 to Kf7, so ...exf5 was unavailable. Be5 then supplied the final queen's protection and covered h8. The last four checking moves and this actual king route were calculated before Qf5+ and confirmed by the referee's mate result. This is a successful local tactical calculation in an already overwhelmingly won position, not sustained benchmark improvement.

Final material: White Q+2R+2B+2N+7P against R+7P. No actual unanticipated material loss or king-exit error was identified in this game. One earlier note called a hypothetical ...Nc4 fork a fork of the queen and bishops; the actual contemplated targets were Qd2, Bd6 and Ne5, with Ne5 able to capture Nc4. That branch did not occur.

After 111: 46W/2D/63L overall; skill 0 is 35W/0D/2L in 37 games. Elo 1670 [1550, 1790], 73 rated total/latest 50 used, 38 maximum exclusions. Trial 14 benchmarks are 1W/0D/2L so far. The small rating rise and this skill-0 conversion do not undo the two maximum-strength losses or practice failures. Continue the fixed endpoint through 114; no valid new cumulative usage counter is available.


## Benchmark 112 — Black versus skill 0, a large material lead lost to a forced king chase

Finished 2026-10-02 08:53:33 UTC by 27.Rh5#, 53 plies / 26 own moves, zero illegal submissions. Result seq 8982, hash `94722255bfe7c3bfff5cf3256a2bc3ef7288f8b282fe671f21f615341b018628`; snapshot `f08966b795508f8deedab3c774f20213366a71c58509662d05063e19718c4a43`. PGN read back.

Early development and castling were followed by ...Nd4 and ...h6. After Nxd4/exd4, White moved Bg5-d2 instead of resolving both pawn attacks, allowing ...dxc3. Bxh6/gxh6 then lost White another bishop. ...cxb2/Qxb2 removed a further pawn with a queen/rook fork, and ...Rb8 defended b7. The ...a6/...b5 preparation avoided relying on an unsupported rook recapture on b5 in front of White's queen. ...Kh7 defended h6 before ...bxc4 took the central pawn.

Against d5 I used ...Nxe4 to attack Qd2, then met Qd4 with ...Bf5, both saving the bishop and defending Ne4. Bg4/Bxg4/hxg4 removed that defender, and I explicitly moved the knight rather than continuing to count the departed bishop. ...Ng5 was genuinely defended by Be7; I also correctly identified that h6 was pinned to Kh7 by the now-open h-file and could not capture off that file. These local recognitions did not make the subsequent king defense sound.

The actual losing finish was 22...Ng5 23.Rxh6+ Kxh6 24.Rh1+ Kg6 25.f4 Nh7 26.f5+ Kg5 27.Rh5#. The rook on h6 was not defended by Qd4 or White's pawns, but the remaining rook could immediately transfer from g1 to h1 and continue checking. I treated safe immediate capture squares as sufficient while failing to resolve the continuation. After f4, I rejected ...Ne6 because d5 could capture the knight and chose ...Nh7, relying on Kg6 to defend it against Rxh7. This omitted the forcing f5+: the knight itself then occupied the king's h7 exit, while Qd4 covered f6/g7, Rh1 covered the h-file, and f7 was occupied by my pawn. I identified only ...Kg5 manually and saw Rh5 mate before submitting it; the actual next move confirmed mate. No all-defenses proof for earlier positions is claimed.

At mate Black still had Q+2R+B+N+5P against Q+R+5P, a rook, bishop and knight ahead with equal pawn counts. Rh5 was protected by g4, and the queen, pawn and rook coverage left no king escape. This is a clear recurrence of an own piece obstructing the needed king route, and of stopping a defensive calculation before the opponent's next forcing check. It defeats any claim that the narrowly correct pin/defender observations constituted reliable execution. Zero illegal submissions did not prevent the tactical failure.

After 112: 46W/2D/64L overall; skill 0 is 35W/0D/3L in 38 games. Elo 1660 [1540, 1780], 74 rated total/latest 50 used, 38 maximum exclusions. Trial 14 benchmarks are 1W/0D/3L so far. The target has failed again, now against skill 0 despite a large lead. Preserve the result and finish the declared nominal-1800 pair 113–114 before the trial assessment and revision. No valid new cumulative usage counter is available.


## Benchmark 113 — White versus nominal 1800, queen concession and an undefended last rook

Finished 2026-10-02 09:35:35 UTC by practical resignation after 39...Qxe1+, 78 plies / 39 own moves, zero illegal submissions. Result seq 9062, hash `1fdb541991c793aea943923915d01d865b7a092e8365bf0c00bebb3da6714794`; snapshot `5bba03f7f26e132ca9eb51a8d6161aa944836a73a9ddfe33c4a3763f74b33cd4`. PGN read back.

Black's kingside pawn advance induced hxg4/Bxg4, pinning Nf3 to Qe2. I withheld the central d4 advance after recognizing that pin changed the available recaptures. Bxc5 was followed by ...Nh5 instead of ...dxc5, so Ba3 preserved an extra bishop and pinned d6 along a3-f8. Qe3/Bxf3/Qxf3 removed the original bishop pin without damaging f2/g2. Black's two knights nevertheless drove the queen back, and ...Qg5 threatened mate on g2.

17.g3 blocked that immediate line. Before attempting gxf4 I recognized that g3 was now absolutely pinned to Kg1, so the pawn could not actually capture Nf4 off the g-file. I chose 18.Nd5 to challenge the knight instead. I had considered ...Nde2+ but stopped the king-retreat analysis too soon. After that check arrived, I manually found ...Qh5 mate after either Kh1 or Kh2: the knights covered the exits, g3 blocked Qe3-h3, and the available pieces could not answer the h-file check. I chose 19.Qxe2, knowingly allowing ...Nxe2+, rather than submit that mating line. This was a deliberate queen concession following an earlier tactical failure, not an unexpected knight capture and not a proof that every earlier defense lost.

The king then escaped through g2-f3-e3-d2-c1-b1. Rfe1 had cleared f1, but ...Nxg3 subsequently attacked f1, which I recognized before selecting Kf3. Bxb5 recovered a pawn. Against ...Nf5+ I used exf5/Qxf5 to remove the last black knight, while recognizing that e4 would no longer defend Nd5. Ne3 forked Qf5/Rg2, but ...Qxf2+ escaped with tempo. ...Qf4 then absolutely pinned Ne3 to Kc1; I did not submit Nxg2 and used Kb1 to remove the pin. These were locally correct changed-board observations amid an already compromised game.

After moving the knight away from repeated attacks, I exchanged rooks with Rxf4/exf4 and placed the remaining rook on f1. I rejected an immediate second Rxf4 because ...Qg1+ could exploit the boxed king, then played c3 with tempo against Qd4 and opened c2. Black answered ...Qe3, defending f4. The decisive new blunder was 39.Re1: I treated attacking the queen and supporting Ne4 as sufficient, but the rook on e1 was now undefended. The second white rook, which had supported it earlier in the game, had been exchanged. Black simply played ...Qxe1+. This was an actual unanticipated rook loss, repeating the missing-defender failure despite recognizing several other pins and king routes correctly.

At resignation White had 2B+N+4P against Q+R+6P, nominally a rook and two pawns down. Kc2 remained legal; this was not checkmate. The remaining rook loss and the failed king-retreat calculation outweigh the successful local observations and the opponent's earlier missed bishop recapture. No reliable transfer is established.

After 113: 46W/2D/65L overall; nominal 1800 is 11W/0D/26L in 37 games. Elo 1650 [1530, 1770], 75 rated total/latest 50 used, 38 maximum exclusions. Trial 14 benchmarks are 1W/0D/4L, with the final paired Black game 114 still required before the declared assessment. Continue that game without adding a new practice period mid-block. No valid new cumulative usage counter is available.


## Benchmark 114 — Black versus nominal 1800, incomplete exchanges and a failed pawn defense

Finished 2026-10-02 10:50:16 UTC by practical resignation after 80.g8=Q; 159 plies / 79 own moves, zero illegal submissions. Result seq 9223, hash `99930f83f49f7f7098cb34651939341e2a9842f25ca7170de04862b329a13cec`; snapshot `ffee30592cbe953df1c69dfa1654ccb9576cae1f130136f1d9230d4642ae4f67`. PGN and status read back.

The first material error was 11...Re8 12.Bxg4 Nxg4 13.Qxg4. I counted Nf6 as the bishop's defender but omitted Qa4's clear fourth-rank line to g4 after the recapture. Black lost a knight. The subsequent ...e4/...Ne5 and pawn advances drove the queen back, and ...e3/...exf2+ created counterplay. Later ...Ne3/Nxe3/Bxe3 and ...Bxc1/Rxc1 removed the remaining minor pieces. ...Qxe2 allowed Qxd5+, and White's Kg2 made Rxf2 possible despite queen support of f2: ...Qxf2 would allow Kxf2. I recognized that limitation before 32.Rxf2. Black then had equal pawns but one fewer knight.

Active rooks and the queen pin on Nf3 recovered a5. Qc6 saved the attacked queen while still defending Re8 and Rd5. White's 41.Qxf6+ allowed ...Qxf6/Rxe8+, exchanging White's queen for a rook and pawn. Black now had Q+R against 2R+N, with equal pawns; ...Qxc3 briefly added a pawn. This opponent concession supplied the new opportunity. ...g4 maintained a pawn chain, and ...Qf3/...Rd2 threatened the pinned Ng2. White checked repeatedly and then played 53.Rxf3, which I had not included in the selected king-route continuation. After ...gxf3/Re6+/...Kf5/Re8/...Rxg2+, however, the actual sequence recovered the knight and reached equal rook-and-three-pawn material. The unanticipated queen capture is a calculation omission, but calling it a queen loss with no subsequent compensation would misstate the completed exchange.

I correctly avoided immediately pushing f3 while Rg2 depended on that pawn against Kh3, and used ...Rg1 first. The next failure was 57...Ke4 58.Kg4 Ke3 59.Rxf3+: I had counted my king's support of f3 without applying the opposing king's protection of the capturing rook. Kxf3 would put the kings adjacent. The passer was lost and Black entered R+2P against R+3P. No best earlier defense is established.

The queenside king route and ...a5/bxa5 created an a-passer. Supported advances to a3 induced 73.Rxa3/Kxa3, leaving Black's rook against the connected g/h pawns with the black king on a3. I did not establish that this position was winning; the later result must not be described as losing a proved win. While the king returned through b4/c5/d6, White advanced g5/g6/g7. ...Rg1 stopped an unsupported promotion, but Kh7 supported g8 and h6 retained the second passer. ...Rg5 and ...Ke7 were too late in the actual continuation: 80.g8=Q.

Final position: Black Ke7/Rg5 against White Kh7/Qg8/h6. Black was not in check and Kf6 remained legal. The considered rook-for-queen exchange left a further h-pawn promotion threat; the actual result was practical resignation, not checkmate or a complete proof of every defense. Zero illegal submissions did not prevent the errors in exchange completion, king-protected captures, or pawn timing.

After 114: 46W/2D/66L overall. Maximum strength 0W/2D/36L, skill 0 35W/0D/3L, nominal 1800 11W/0D/27L, each over 38 completed games. Provisional engine-relative Elo 1640 [1520, 1760], 76 rated total/latest 50 used, 38 maximum exclusions; storage 27,422,576 bytes. No valid new cumulative usage counter is available.

## Trial 14 endpoint — failed; revise the intervention

Fixed benchmarks 109–114 finished 1W/0D/5L, 213 own moves / 428 plies, zero illegal submissions. Both maximum-strength games and both nominal-1800 games were lost; skill 0 split 1–1. The only win relied heavily on declined opponent recaptures. The two predeclared remembered practices also ended in checkmate losses, thirteen own moves / 26 plies in total, without repeats or replacements.

Elo declined from 1660 [1540, 1780] through 108 to 1640 [1520, 1760] through 114. The intervals overlap broadly; the result supplies no sustained-improvement evidence. The king/defender focus failed its stated execution objective: 112 obstructed a needed king exit and was mated despite a large material lead; 113 lost its remaining undefended rook after forgetting the other rook had departed; 114 again stopped an exchange too early and later relied on a king recapture forbidden by the opposing king. The practice mates and 109–110 supply further failures. Isolated correct recognition of pins and departing defenders does not overturn those results.

Retire trial 14 as the main intervention. Long branching, short timed decisions (trial 09), static reconstruction, and remembered defensive continuations have all already failed to establish transfer. The next intervention must declare a bounded learning activity and fixed new evaluation endpoint; do not claim novelty from restating these same safety cues or improvement from completing another worksheet. Preserve every record.

The goal tracker was read again after 114. It still has the superseded two-100-game maximum-strength objective, status blocked, and unchanged stale 17,035,946-token / 178,558-second values. No new usage entry, reset, completion claim, or status change was made. Current GOAL.md and the user's Continue still authorize the measured-Elo experiment.
