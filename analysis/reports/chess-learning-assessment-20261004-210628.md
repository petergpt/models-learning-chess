# How the models learn

Assessment captured 2026-10-04T21:06:25.706327+00:00.

Learning means adaptation of notes, decisions, repertoire and practice within the run; no model weights are updated.

| Model | Scored games | Engine-relative Elo | First matched score | Latest matched score | Outcome evidence |
|---|---:|---:|---:|---:|---|
| GPT-6 Astra | 200 | 1400 · 1270–1520 | 62.5% | 39.1% | Declined in matched windows |
| Claude Opus 5.5 | 182 | 1720 · 1600–1840 | 49.2% | 66.7% | Improved in matched windows |
| GPT-6.1 Sol | 31 | 1560 · 1360–1760 | 62.5% | 37.5% | Too few games |
| GPT-6.1 Sol · Long Context | 16 | 1610 · 1340–1900 | 75.0% | 25.0% | Too few games |
| Claude Fable 5.1 | 15 | 1590 · 1300–1890 | 25.0% | 75.0% | Too few games |

The primary trend compares the first and last equal halves of complete six-game rotations; an unpaired middle rotation is omitted. Recent momentum compares adjacent windows of up to eight rotations. Opponent/color counts match and games do not overlap within a comparison. Each rated window has four games per rotation. Windows with fewer than five rotations are too small for a directional verdict. Intervals resample complete rotations and are exploratory, not causal tests.

## GPT-6 Astra

Astra repeatedly revised exchange accounting, blockers, actual defenders and immediate replies. Its completed run shows local corrections without sustained improvement in fresh benchmark results.

Possible explanation: Remembered corrections were often too specific to the original position. Longer speculative branches and a growing checklist may have competed with maintaining the current board. The logs support recurring execution failures; they do not establish which change caused the decline.

What would strengthen the claim: Replicated runs with a stable decision budget, plus fewer repeated errors in fresh positions and better matched-opponent scores. This completed run remains closed.

Accepted own moves: 7746; illegal submissions: 15 (0.19 per 100 accepted own moves).
Short-horizon piece-loss events: 130 (1.68 per 100 own moves); won 62/81 games after reaching a +3 material lead after move 10.
Practice: 51 sessions; 32 stopped/unfinished. Kept separate from benchmark outcomes.

Matched score change: -23.4 percentage points; exploratory 95% block-bootstrap interval -36.7 to -10.2.

| Opponent | Early matched score | Late matched score |
|---|---:|---:|
| full-strength | 3.1% (32 games) | 0.0% (32 games) |
| skill-0 | 93.8% (32 games) | 62.5% (32 games) |
| elo-1800-setting | 31.2% (32 games) | 15.6% (32 games) |

| Change declared | Verified before game | Fresh rated score before → after |
|---|---:|---:|
| Pawn capture geometry | 163 | 25.0% → 31.2% |
| Literal recaptures | 175 | 31.2% → 68.8% |
| Retain the defender | 193 | 25.0% → 37.5% |

These are historical declarations, not proof the protocol was followed or that the change caused the result.

Authored failure examples:

- Game 197: Promotion ended in stalemate; the journal recognized the missing terminal-position check afterward. Source: `Chess - GPT-6-Astra/workspace/final-report-200.md:47`.
- Game 198: 17...Bf5 18.Qxf5 lost a bishop; its own bishop on f6 blocked the imagined rook recapture. Source: `Chess - GPT-6-Astra/workspace/learning-journal.md:3512`.

Ledger hashes, event numbering, accepted-move legality/FENs, results, colors and benchmark rotation were checked. Benchmark snapshot head: `217e9632fb0ce4b60b03ec3ef074b3215643c556e95515118244362631f8fa1a`.

## Claude Opus 5.5

Opus changed from piece-by-piece checklists to scans from target squares, then added origin, reply and defender checks. It later shortened the accumulated checklist. Its own reviews still record missed paths, forks and discovered attacks.

Possible explanation: The larger gain against skill 0, with little change in short-term piece losses, suggests the improvement may be in obtaining advantages or exploiting opponent mistakes. Concrete square scans are a candidate mechanism; incomplete execution remains a bottleneck. This run cannot isolate the effect of a checklist.

What would strengthen the claim: Retention over the remaining fixed rotations, with lower error recurrence as well as stronger-setting results. A repeated, controlled run would be needed to isolate the strategy's effect.

Accepted own moves: 6542; illegal submissions: 51 (0.78 per 100 accepted own moves).
Short-horizon piece-loss events: 88 (1.35 per 100 own moves); won 65/80 games after reaching a +3 material lead after move 10.
Practice: 1 sessions; 1 stopped/unfinished. Kept separate from benchmark outcomes.

Matched score change: +17.5 percentage points; exploratory 95% block-bootstrap interval +0.8 to +35.0.

| Opponent | Early matched score | Late matched score |
|---|---:|---:|
| full-strength | 0.0% (30 games) | 0.0% (30 games) |
| skill-0 | 63.3% (30 games) | 90.0% (30 games) |
| elo-1800-setting | 35.0% (30 games) | 43.3% (30 games) |

| Change declared | Verified before game | Fresh rated score before → after |
|---|---:|---:|
| Square-based scans | 55 | 43.8% → 62.5% |
| Slider sweep and recaptures | 85 | 43.8% → 100.0% |
| Four-step simplification | 175 | 50.0% → 50.0% |
| Loose-piece check | 181 | Not enough complete rotations |

These are historical declarations, not proof the protocol was followed or that the change caused the result.

Authored failure examples:

- Game 178: The game review records a queen left on an opened rank after a knight move; the next trial adds a loose-piece check. Source: `Chess - Opus-5.5/workspace/PLAN.md:303`.
- Game 181: Two queen-path attempts crossed its own c3 pawn despite the recently simplified PATH rule. Source: `Chess - Opus-5.5/workspace/ERRORS.md:830`.

Ledger hashes, event numbering, accepted-move legality/FENs, results, colors and benchmark rotation were checked. Benchmark snapshot head: `346bd13512327bb093a32306889be9dae7be219c98cf41e0da91a36a584ae7f9`.

## GPT-6.1 Sol

Sol tests short alternatives from its failed positions, changes opening setups, and repeatedly adds checks for final recaptures, blockers, defenders and knight checks. Successful remembered drills have not eliminated those failures in new games.

Possible explanation: The practice mostly rehearses known failures over a short horizon. That may repair a specific continuation without transferring the habit to a new board. Long analysis has not reliably prevented the immediate threat it was intended to catch.

What would strengthen the claim: More complete rotations, plus fewer fresh-position defender and forcing-reply errors. Keep remembered drill outcomes separate from benchmark transfer.

Accepted own moves: 1217; illegal submissions: 7 (0.58 per 100 accepted own moves).
Short-horizon piece-loss events: 20 (1.64 per 100 own moves); won 8/10 games after reaching a +3 material lead after move 10.
Practice: 23 sessions; 19 stopped/unfinished. Kept separate from benchmark outcomes.


| Opponent | Early matched score | Late matched score |
|---|---:|---:|
| full-strength | 0.0% (4 games) | 0.0% (4 games) |
| skill-0 | 100.0% (4 games) | 62.5% (4 games) |
| elo-1800-setting | 25.0% (4 games) | 12.5% (4 games) |

| Change declared | Verified before game | Fresh rated score before → after |
|---|---:|---:|
| Final-position verification | 4 | Not enough complete rotations |
| Preserve king shelter | 30 | Not enough complete rotations |
| Opening reset and last defenders | 31 | Not enough complete rotations |

These are historical declarations, not proof the protocol was followed or that the change caused the result.

Authored failure examples:

- Game 30: A bishop move abandoned d5; a later queen exchange allowed a checking knight fork that won a rook. Source: `Chess - GPT-6.1-Sol/workspace/journal.md:593`.
- Game 31: A queen interposition allowed an intermediate knight check and queen loss, repeating the trial's stated target. Source: `Chess - GPT-6.1-Sol/workspace/journal.md:603`.

Ledger hashes, event numbering, accepted-move legality/FENs, results, colors and benchmark rotation were checked. Benchmark snapshot head: `4998dfe742140917b1b351d3df0668033e539d0523ec7980de437cd93cf26b6b`.

## GPT-6.1 Sol · Long Context

The larger-context Sol run reviews exchange bookkeeping and destination safety, using short drills from remembered positions. It recently shortened its safety pass, but fresh games still show removed or blocked defenders and missed king nets.

Possible explanation: A larger memory window may retain more notes without improving their execution on the current board. At this sample size, the context treatment cannot be separated from opponent variation and different decisions.

What would strengthen the claim: Equal game counts and repeated runs of standard and larger context, under the same decision budget. One small pair of runs cannot establish a context-window effect.

Accepted own moves: 506; illegal submissions: 2 (0.40 per 100 accepted own moves).
Short-horizon piece-loss events: 12 (2.37 per 100 own moves); won 6/6 games after reaching a +3 material lead after move 10.
Practice: 8 sessions; 8 stopped/unfinished. Kept separate from benchmark outcomes.


| Opponent | Early matched score | Late matched score |
|---|---:|---:|
| full-strength | 0.0% (2 games) | 0.0% (2 games) |
| skill-0 | 100.0% (2 games) | 50.0% (2 games) |
| elo-1800-setting | 50.0% (2 games) | 0.0% (2 games) |

| Change declared | Verified before game | Fresh rated score before → after |
|---|---:|---:|
| Destination and fork checks | 3 | Not enough complete rotations |
| Short actual-board safety pass | 13 | Not enough complete rotations |

These are historical declarations, not proof the protocol was followed or that the change caused the result.

Authored failure examples:

- Game 14: A bishop recapture moved the sole defender away from an attacked knight, allowing its immediate capture. Source: `Chess - GPT-6.1-Sol - Long Context/workspace/learning.md:139`.
- Game 15: Its own knight blocked the queen's defense of a bishop; a later promotion and mate still converted the game. Source: `Chess - GPT-6.1-Sol - Long Context/workspace/learning.md:145`.

Ledger hashes, event numbering, accepted-move legality/FENs, results, colors and benchmark rotation were checked. Benchmark snapshot head: `0767ad628570e634d6e28568ce296144a14df2d7121fba57396f2694a81b5ec9`.

## Claude Fable 5.1

Fable uses a stable d4/Bf4 repertoire as White, a written safety scan, and post-game patches for king flights, exchange arithmetic and forced-reply discoveries. Its early log distinguishes skipped scans from scans filled out incorrectly. The run is paused after 15 games.

Possible explanation: Making the scan a gate may reduce omissions, while superficial answers inside it can still miss a tactic. Early wins and losses are too few to establish that the procedure has improved strength.

What would strengthen the claim: When the user resumes the run, test the reply-discipline method over its originally declared block and further fresh rotations. A practice win or a filled checklist is insufficient.

Accepted own moves: 544; illegal submissions: 5 (0.92 per 100 accepted own moves).
Short-horizon piece-loss events: 13 (2.39 per 100 own moves); won 4/7 games after reaching a +3 material lead after move 10.
Practice: 3 sessions; 0 stopped/unfinished. Kept separate from benchmark outcomes.


| Opponent | Early matched score | Late matched score |
|---|---:|---:|
| full-strength | 0.0% (2 games) | 0.0% (2 games) |
| skill-0 | 50.0% (2 games) | 100.0% (2 games) |
| elo-1800-setting | 0.0% (2 games) | 50.0% (2 games) |

| Change declared | Verified before game | Fresh rated score before → after |
|---|---:|---:|
| Scan before submitting | 9 | Not enough complete rotations |
| Reply-consequence discipline | 13 | Not enough complete rotations |

These are historical declarations, not proof the protocol was followed or that the change caused the result.

Authored failure examples:

- Game 11: A promotion was followed by back-rank mate; the presumed king flight lay on the rook's checking line. Source: `Chess - Fable-5.1/workspace/log.md:34`.
- Game 14: A pawn capture opened the a-file to its queen; the written scan said the vacated square opened nothing. Source: `Chess - Fable-5.1/workspace/log.md:53`.

Ledger hashes, event numbering, accepted-move legality/FENs, results, colors and benchmark rotation were checked. Benchmark snapshot head: `b8851f158f08f985084d9f255ea02b2b9f0f33047df29bf26d51956e9e84fdb2`.

## Interpretation rules

A strategy revision is an attempt. A changed move pattern is behavior. Better results in fresh, opponent-matched games are transfer evidence. Persistence across later blocks is retention. One uncontrolled run cannot identify why a particular intervention worked.

Short-horizon piece losses include sacrifices and do not establish chess blunders. Material leads ignore king safety and positional compensation. Time between submissions includes pauses; it is not compute time. Elo is conditional on nominal Stockfish anchors; maximum-strength games are excluded. No private reasoning transcripts were read. All explanations are marked as observations or hypotheses.
