"""Verify only explicitly supplied moves in our own recorded positions."""
import gzip
import json
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True
root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / ".arena/vendor/chess-1.11.2"))
import chess

cases = json.loads((root / "workspace/trials/mixed-lines-22-inputs.json").read_text())

def recorded_board(game, ply):
    with gzip.open(root / ("data/games/%06d.pgn.gz" % game), "rt") as f:
        pgn = f.read()
    body = re.sub(r"^\[.*\]\s*$", "", pgn, flags=re.MULTILINE)
    tokens = [t for t in body.split() if not re.fullmatch(r"\d+\.(?:\.\.)?", t) and t not in ("1-0", "0-1", "1/2-1/2", "*")]
    board = chess.Board()
    for san in tokens[:ply]:
        board.push_san(san)
    assert len(board.move_stack) == ply
    return board

results = []
for case in cases:
    board = chess.Board(case["fen"]) if "fen" in case else recorded_board(case["game"], case["ply"])
    if case.get("edit") == "h7-to-h6":
        assert board.piece_at(chess.H7) == chess.Piece(chess.PAWN, chess.BLACK)
        assert board.piece_at(chess.H6) is None
        board.remove_piece_at(chess.H7)
        board.set_piece_at(chess.H6, chess.Piece(chess.PAWN, chess.BLACK))
    elif case.get("edit") == "remove-b3-bishop":
        assert board.piece_at(chess.B3) == chess.Piece(chess.BISHOP, chess.WHITE)
        board.remove_piece_at(chess.B3)
    item = {"id": case["id"], "valid": board.is_valid(), "initial_fen": board.fen(), "supplied_moves": []}
    for uci, expected in case["moves"]:
        move = chess.Move.from_uci(uci)
        legal = board.is_legal(move)
        item["supplied_moves"].append({"uci": uci, "expected_legal": expected, "actual_legal": legal, "matches": legal == expected})
        if not legal:
            break
        board.push(move)
        item["supplied_moves"][-1]["resulting_check"] = board.is_check()
    item["final_fen"] = board.fen()
    item["all_predictions_match"] = len(item["supplied_moves"]) == len(case["moves"]) and all(m["matches"] for m in item["supplied_moves"])
    results.append(item)
output = {"scope": "Mechanical legality of predeclared supplied moves only; no move menu, search, engine, attack map or evaluation.", "results": results}
(root / "workspace/trials/mixed-lines-22-legality.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps({"branches": len(results), "supplied_plies": sum(len(x["supplied_moves"]) for x in results), "all_valid": all(x["valid"] for x in results), "all_predictions_match": all(x["all_predictions_match"] for x in results), "results": results}, indent=2))
