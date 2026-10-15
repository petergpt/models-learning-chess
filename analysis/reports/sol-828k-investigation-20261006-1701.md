# GPT-6.1 Sol 828K investigation

Evidence checked on 6 October 2026, approximately 16:46–17:06 UTC.

The new 828K run is configured for Max throughout the native runtime records. The older 828K run is Medium throughout its records. The new run's poor game outcomes are real, and remain after comparing equal benchmark prefixes. No referee, result-accounting, rating-arithmetic, or opponent-setting fault was found to explain the difference. The absolute Elo scale is provisional and engine-relative; it has not been calibrated to human ratings.

## Matching the same first 15 games

All three runs faced the same schedule and colors: six full-strength games, five Skill 0 games, and four nominal 1800 games. Full-strength games are excluded from Elo, leaving nine rated observations in each comparison.

| Run | Overall W/D/L | Skill 0 W/D/L | Nominal 1800 W/D/L | Engine-relative Elo | 95% credible interval |
| --- | --- | --- | --- | ---: | --- |
| 828K Medium | 5/0/10 | 4/0/1 | 1/0/3 | 1590 | 1300–1890 |
| 828K Max | 1/1/13 | 1/1/3 | 0/0/4 | 1050 | 540–1400 |
| Standard context Max | 6/0/9 | 5/0/0 | 1/0/3 | 1720 | 1430–2040 |

All three lost all six full-strength games. Those losses do not reduce the displayed Elo. Max's low estimate follows from scoring only 1.5 points in five Skill 0 games and zero points in four nominal 1800 games.

The live website matched the independently audited raw records: older 828K Medium had 41 completed games and Elo 1570, newer 828K Max had 15 and Elo 1050, and standard Max had 89 and Elo 1410. The equal-prefix table above avoids comparing 41 or 89 games against 15.

## Settings and measurement checks

- Native model slug: `gpt-6.1-sol` in all three runs, with each run's correct working directory.
- Older 828K: all 37 recorded turn contexts specify Medium, including collaboration settings; all ten recorded applied-settings events also specify Medium.
- Newer 828K: all three recorded turn contexts specify Max, including collaboration settings; both applied-settings events specify Max. Max remains selected after the two recorded compactions, at 03:20 and 09:48 UTC on 6 October.
- Both 828K runs have 19 pinned files whose hashes all match their manifests. Eighteen files match between the runs, including the goal, instructions, referee, rating implementation, opponent configuration, and Stockfish binary. Their local Codex configuration is the sole differing pinned file.
- Recorded opponents match the fixed paired-color rotation, with 1,000,000 nodes per Stockfish reply.
- Standalone operator UCI checks confirmed that Skill 0 transmits `Skill Level = 0`; nominal 1800 transmits `UCI_LimitStrength = true` and `UCI_Elo = 1800`. Stockfish 19 acknowledges readiness in each case. The nominal 1800 control overrides the default Skill Level 20, as documented by Stockfish.
- The referee starts a fresh engine for every reply. A previous game's strength setting cannot remain in that process.
- All recorded accepted benchmark and practice moves were legally replayed, and recorded SAN, FEN, results, colors, hash chains, and scoring perspective were checked.
- Neither 828K run has an engine-error ledger event or an illegal-move forfeit. The first 15 games contained two rejected submissions in Medium and three in Max; these did not end games.
- An independent direct-probability implementation of the rating model reproduced the installed calculator and stored historical points at prefixes 6, 10, 12, 15, and the current endpoint.
- All 29 existing referee, rating, and practice tests passed in isolated disposable fixtures. Tests and data verification ran through the shared memory-protection wrapper.
- Public feed ratings and completed-game counts matched the audited ledgers for all three Sol runs.

These checks establish the configured and recorded effort. They do not independently expose the provider's internal allocation of computation.

## Is Max actually spending more thought?

Yes. Across the same first-15-game time span, including intervening practice and reviews, provider usage records contain about 1.452 million reasoning-output tokens for 828K Max versus 0.685 million for 828K Medium, approximately 2.1 times as many.

For the final completed provider response immediately around each accepted learner move, median reasoning-output tokens were 865 for Max versus 216.5 for Medium. Matches covered 558 of 560 Max moves and 480 of 483 Medium moves. This response statistic excludes any earlier work for the decision, so it is not a complete per-move compute budget. Recorded median move intervals were approximately 32.2 seconds for Max and 13.9 seconds for Medium; intervals can include other work or idle time.

The first game's input context was approximately 19,000–36,000 tokens in both 828K runs. The new Max run already made a basic queen-safety error in that opening game. Its first Skill 0 loss, game 4, occurred with approximately 110,000–180,000 input tokens in the recorded final responses around its moves. These failures occurred well before the 828K window filled.

## What is going wrong in the chess?

The clearest recurring failure is maintaining an accurate current board and checking the opponent's immediate forcing reply. The following facts were verified by legal replay, without requesting engine evaluations or recommendations.

- **Game 12, Black against nominal 1800:** Max was three pawns ahead with equal piece material, then played `13...Bc5` and allowed `14.Qxf7#`. The White bishop on d5 controls f7, so the Black king cannot recapture the mating queen. The model's authored review says it pursued a tempo against the queen while missing the immediate mate.
- **Game 15, White against Skill 0:** `31.Re4 Nc3 32.Rf4 Ne2+ 33.Kh2 Nxf4` lost a rook to a checking knight fork. From e2 the knight attacks both the king on g1 and the rook on f4. Moving the rook out of the knight's current attack did not protect it against the next forcing move.
- **Game 14, full strength:** the authored review identifies a queen left without a usable rook defender after that rook moved. The other rook's apparent defensive ray was blocked by its own bishop. This game is diagnostically relevant but excluded from Elo.

Max is reflecting: its own saved reviews repeatedly identify occupied lines, unusable king recaptures, defender departures, and long speculative continuations that lose contact with the real board. Those are authored observations, not access to private reasoning or an engine-certified causal diagnosis.

It has recorded 16 practice sessions with 58 own moves. Many are very short replays of remembered mistakes. Two recent defensive drills preserved the rook but never faced the checking knight move they intended to test; another replay repeated the known fork from the attacker's side. These show attempted adaptation, but provide weak evidence of transfer to new benchmark positions. Later benchmark failures confirm that the target skills remain unreliable.

## Were the resignations premature?

As a separate operator check, the five rated resignation positions in Max's first 15 games were assessed using full-strength Stockfish 19, a fresh process and 1,000,000 search nodes per position. No move recommendations were exported or supplied to a learner.

| Game | Benchmark opponent | Full-strength endpoint assessment from Max's side |
| ---: | --- | --- |
| 4 | Skill 0 | −773 centipawns |
| 5 | Nominal 1800 | −836 centipawns |
| 10 | Skill 0 | Engine reports mate against Max in eight moves |
| 11 | Nominal 1800 | −723 centipawns |
| 15 | Skill 0 | −822 centipawns |

The engine regards all five endpoints as badly losing for Max. This supports the material and tactical diagnoses and does not reveal a pattern of resigning in equal positions. It is a finite search assessment, not a proof of a forced outcome. In particular, it does not establish whether weakened Stockfish could have made a subsequent mistake if Max had continued. Resignation policy is part of the measured agent's behavior.

## What the Elo means

The estimator is a Bayesian Bradley–Terry–Davidson model of wins, draws, and losses. It uses nominal anchors of 1320 for Skill 0 and 1800 for the engine's Elo control, a broad Normal prior centered at 1500, and the most recent 50 rated games. Full strength is excluded.

The 1320 anchor is related to the pinned Stockfish 19 control mapping: its lowest Elo setting maps to internal Skill 0. This is a nominal engine mapping, not independent calibration of this experiment against human players.

Stockfish documents that its Elo control is calibrated at **120 seconds plus 1 second per move**, anchored to **CCRL 40/4**. This experiment instead uses fixed nodes per reply and fresh engine processes. Consequently, the displayed 1050 is an internally consistent performance estimate on our nominal engine scale, not a demonstrated FIDE, chess.com, or other human rating. Its interval is conditional on the anchors and model assumptions, and excludes systematic anchor calibration error. [Stockfish UCI documentation](https://official-stockfish.github.io/docs/stockfish-wiki/UCI-Protocol-and-Stockfish-Commands.html).

The chart's initial 1500 is the no-games prior, not a measured starting ability. Early downward movement primarily revises that starting assumption using game outcomes. It does not establish that the learner once played at 1500 and then deteriorated.

## Why Max can trail Medium here

Reasoning effort controls how much the model thinks. It does not make the model a chess search engine or mechanically validate its imagined continuations. [OpenAI reasoning documentation](https://developers.openai.com/api/docs/guides/reasoning).

The most strongly supported diagnosis is that this particular Max trajectory spends more computation while still making basic tactical and board-tracking errors. Its practice has not yet corrected those failures. The hypothesis that excessive speculative calculation contributes is consistent with its saved reviews, but this audit does not prove that Max effort causes worse play.

There is one independent learning trajectory per configuration, only nine rated observations in the matched comparison, and weak Stockfish move selection is randomized. The nominal opponents and schedule match; the actual moves and resulting positions differ. More benchmark games can clarify this run's performance, while repeated independent runs or controlled evaluations of the same held-out positions would be needed to attribute the gap specifically to reasoning effort. The stronger first-15-game standard Max result also cautions against treating this as a general finding that Max is bad at chess.

Machine-readable evidence and the read-only verification scripts are saved under `.operator/audits/sol-828k-20261006-1646/`. This audit supplied no feedback or tactical recommendations to the learners.
