#!/usr/bin/env python3
"""Mechanical FEN -> ASCII rendering (board with rank/file labels + piece lists).
Pure rendering of the position string: no move generation, search, attack maps or evaluation."""
import sys

ORDER = 'KQRBNP'

def grid(fen):
    rows = fen.split()[0].split('/')
    g = []
    for row in rows:
        cells = []
        for ch in row:
            if ch.isdigit():
                cells.extend(['.'] * int(ch))
            else:
                cells.append(ch)
        g.append(cells)
    return g

def render(fen):
    g = grid(fen)
    out = ['    a b c d e f g h']
    for i, cells in enumerate(g):
        out.append(f"{8 - i}   " + ' '.join(cells) + f"   {8 - i}")
    out.append('    a b c d e f g h')
    return '\n'.join(out)

def piece_lists(fen):
    g = grid(fen)
    found = {'w': {p: [] for p in ORDER}, 'b': {p: [] for p in ORDER}}
    for i, cells in enumerate(g):
        for j, ch in enumerate(cells):
            if ch == '.':
                continue
            side = 'w' if ch.isupper() else 'b'
            found[side][ch.upper()].append('abcdefgh'[j] + str(8 - i))
    lines = []
    for side, name in (('w', 'White'), ('b', 'Black')):
        parts = []
        for p in ORDER:
            sq = sorted(found[side][p])
            if sq:
                parts.append(p + ' ' + ','.join(sq))
        lines.append(f"{name}: " + ' | '.join(parts))
    return '\n'.join(lines)

if __name__ == '__main__':
    for fen in sys.argv[1:] or [sys.stdin.read().strip()]:
        print(render(fen))
        print(piece_lists(fen))
        fields = fen.split()
        if len(fields) > 1:
            print('to move:', 'White' if fields[1] == 'w' else 'Black')
