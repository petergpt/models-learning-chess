# Practice 1 — Black vs elo-1800 — lost by checkmate (32.Rc8#), 63 plies

Good: the written scan caught several traps (the Qa2 x-ray on d5 twice, Bxf7+ geometry after a knight move, hanging-rook recaptures) and the knight fork 24...Nc3 won the queen; I was +3 in material at move 31.
Fatal: 31...Rxf7?? allowed 32.Rc8#: the recapturing rook became PINNED on the a2-g8 diagonal, so my planned block ...Rf8 was illegal. My scan line C listed the check and the block but never asked "is the blocking piece pinned?".
Also noted: at move 13 I counted my queen as a defender of d5 although my own bishop on d6 blocked the d-file — defenders must be traced like attackers.
Scan patch (v2.1): for every enemy check listed in line C, verify each intended reply is LEGAL (pinned pieces cannot leave the pin line; a king cannot stay on a line the checker's departure opens). Add a back-rank item: if an enemy rook/queen can reach my king's rank, name the blocker and check it is not pinned.
