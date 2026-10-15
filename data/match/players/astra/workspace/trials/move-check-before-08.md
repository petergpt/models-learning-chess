# Current move procedure — trial 07

Unproven change: short, recorded opponent replays replace supplied-line rehearsal. Trial 06 failed and is archived in `trials/move-check-before-07.md`. Practice outcomes are separate from benchmark Elo.

Read the actual board and immediate threat. Reconstruct each candidate by clearing its origin, removing a capture and filling its destination. Compare at most two sensible candidates at a time. If in check, resolve every checking line.

Before submitting the selected candidate, identify immediate opponent checks and cheaper captures of major pieces using the actual pieces and blockers. Finish a short concrete answer through the real recapture; do not treat naming a check as resolving it. If a piece is being confined, name a usable retreat or exchange. A king, knight or bishop placed on a rook's file can remove its supposed defense.

After the actual opponent reply, rebuild the position instead of continuing the imagined branch. Keep routine decisions near a minute where feasible. Unresolved dangerous replies remain unresolved; depth and a longer checklist are not evidence of learning. No automated chess analysis, move menus, engine advice or delegation.
