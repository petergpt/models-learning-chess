# Trial 7 constructed geometry drills

These positions are my own constructions, using simple movement motifs from my own failures. No external solution or evaluation has been consulted. They are near-transfer exercises, not measured strength tests. Choose all moves mentally and use only the referee during each practice.

## A: Rook destination and a black pawn's actual captures

FEN: `6k1/8/8/1p6/2R5/8/8/6K1 w - - 0 1`

White: king g1, rook c4. Black: king g8, pawn b5. The black b5 pawn attacks a4 and c4, so the rook is already attacked. My own initial candidate is Re4. Recompute the pawn's captures from the actual returned board after every opponent move; do not retain b5's attack squares if the pawn advances.

Skill 0, White, four own moves maximum, explicitly stop if still active. Success criterion: no rook placed directly onto the current pawn's capture square and no illegal path submission. This is easy material and says nothing about benchmark transfer by itself.

## B: Queen recapture blocked by my own bishop

FEN: `6k1/8/8/8/2p5/3bBQ2/2P5/6K1 w - - 0 1`

White: king g1, queen f3, bishop e3, pawn c2. Black: king g8, bishop d3, pawn c4. The e3 bishop blocks f3-d3. My own initial candidate is cxd3, a pawn capture with no intervening square. If Black recaptures with cxd3, resolve the resulting position myself; the queen's horizontal route remains blocked until e3 is vacated. A later plan is not an already usable recapture.

Skill 0, White, four own moves maximum, explicitly stop if still active. Success criterion: use a real path and real defender on each submitted move, with no illegal queen-through-bishop attempt. This is a mirrored construction of an earlier motif and is not independent evidence of learning.
