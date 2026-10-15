# Trial 15: Recapture lines

Own remembered failure, benchmark 18: 42.Qd3 Kg8 43.Rc6 Qe8 44.Qxg6 Qxg6 45.Rxg6. White Rc6 guarded g6 through d6/e6/f6 after Qe6 left. A queen defender on e8 was insufficient because White could recapture that queen with the rook. No best defense for the original position has been proved.

Constructed FEN, composed mentally without analysis code:

`6k1/8/2R1q1r1/8/8/3Q2P1/8/6K1 b - - 0 1`

Black: Kg8, Qe6, Rg6. White: Kg1, Qd3, Rc6, Pg3. Pg3 blocks Rg6's file toward Kg1, so the starting side-to-move is intended to be legal. This deliberately simplified example removes the real game's e5/d4 pawns and other pieces. In the real game e5 blocks Qe6-e1; Qe1+ is not a proposed legal repair there.

My own candidate: Qe1+. It gives check along e1-f1-g1, moves the attacked queen, and opens g6-f6-e6-d6-c6 for a possible rook capture. If White blocks with Qf1, I would consider Qxf1+ and then inspect the actual king recapture before selecting another move. This is mental preparation, not an engine recommendation, automated test, or proved best move.

Run recorded practice at skill 3, explicit Black, at most four own moves. Objective: keep the queen and rook safe, or trade queens without losing the remaining rook; identify whether an opponent rook still defends a recapture square after a piece vacates it. Stop explicitly and retain the record regardless of outcome. Next benchmark checkpoint: 24 scored games, after benchmarks 19–24. A remembered motif in this easier construction does not establish transfer.

Observed practice 17: Qe1+ Kg2 Rxc6 Qd8+ Kf7 Qd7+ Qe7 Qxc6. Stopped after four own moves/eight plies, zero illegal submissions. The first checking move enabled Rxc6; the subsequent king move allowed a checking queen double attack and lost the rook. Queen each and one extra White pawn at the stop. The preservation criterion failed. The construction is not solved, and no alternative is asserted best. Next measured test remains benchmarks 19–24.
