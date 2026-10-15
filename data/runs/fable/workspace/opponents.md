# Opponent model (my prior understanding of Stockfish's skill mechanism, from public source knowledge; unverified for the pinned build)

- Skill Level < 20: engine searches with MultiPV 4 and, at depth 1+level, picks among the top 4 root moves with a weighted random rule. The deficit of worse moves is almost cancelled (weakness=120-2*level over 128), so the choice is close to random among the top 4 moves of that shallow search, with a random term proportional to the gap between best and 4th move (capped at one pawn).
  - **skill-0**: pick at depth 1 (+ quiescence). Expect: sees direct captures/recaptures, but chooses nearly at random among 4 depth-1 moves; may even fail to recapture or to take a hanging piece when the random term is large. Blind to 2+ move tactics (forks after a check, pins followed by capture, quiet mate threats).
  - **elo-1800 setting**: UCI_Elo 1800 maps to fractional level ~3.3 -> pick at depth ~4, weakness ~113. Expect: sees most 2-move tactics, still often plays the 2nd-4th move; positional errors; weak in long plans and deep combinations; may miss 3-move tactics.
  - **full-strength**: skill 20, 1M nodes ~ very strong (well above 3000). Any inaccuracy is punished.
- All three use NNUE evaluation, so their quiet moves look positionally sensible.

## Exploitation plan
- skill-0: develop safely, create multiple threats, attack the king; take everything that is free; convert cleanly; never gamble on it responding sensibly. Avoid stalemate/repetition.
- elo-1800: solid structure, keep pieces defended, build pressure, prefer threats requiring 3+ ply to parry, win endgames with technique.
- full-strength: solid London/Caro/Slav, trade when possible, no pawn grabs, resign when hopeless.

## Observed behaviour (fill in from games)
- full-strength (games 1-2): punished every inaccuracy; found knight-harassment (…Na2) and a mating net with Q+2N. No chances unless I play flawlessly.
- skill-0 (game 3, loss): exploited my hanging knight and rook immediately; its attack with Q+R on my king was coherent. It is NOT safe to leave anything loose against it.
- skill-0 (game 4, win): left a knight on d2 unrecaptured for two moves, then left Nd2/Ng1 en prise; walked its king into a mating net. Pattern: when it has no immediate capture it drifts; it misses my 2-move threats (forks after a check).
