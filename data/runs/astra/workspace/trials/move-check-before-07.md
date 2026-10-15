# Current move procedure — trial 06

Unproven change: finish the immediate replies before following one branch. Trial 05 is archived in `trials/move-check-before-06.md`. Practice correctness is not measured strength.

Read the actual king, queen and rook locations. Reconstruct the selected candidate by clearing its origin, removing any capture and filling its destination. If already in check, account for every checking line when selecting an answer.

Before any deeper continuation, identify the opponent's immediate checks by piece. Start with knight checking destinations derived from my king's square, and check every enemy knight against them; game 60 had both Ne7+ and Nxf6+, with different consequences. Check the other pieces' immediate checks using the actual blockers. Also identify lower-valued captures of my queen and rooks, including both pawn origins and newly opened rays. A protected queen can still be lost to a pawn, as in game 59. This pass must contain concrete moves or blockers, not just the assertion that checking was done.

Only then resolve the dangerous replies through the actual recapture and rebuild the resulting defenders. Reject an unresolved immediate loss; repeat the first pass if the candidate changes. Keep branches short enough that a second immediate reply is not forgotten. Do not carry defenders or king locations across changed lines. No automated attack enumeration, move menu, analysis, scoring, search or delegated move selection.
