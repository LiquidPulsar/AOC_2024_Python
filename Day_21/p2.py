from functools import cache
from pathlib import Path

HOME = Path(__file__).parent

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    |0/^| A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

# replace ^ with 0 to combine both keypads
keypad = "789 456 123 _0A <v>".split()
pos_dct = {v:(j,i) for i,row in enumerate(keypad) for j,v in enumerate(row) if v != "_"}
dead_Y, dead_X = 3, 0
codes = (HOME/"input.txt").read_text().splitlines()

@cache
def paths(a,b):
    x,y = pos_dct[a]
    nx,ny = pos_dct[b]
    dx,dy = abs(nx-x),abs(ny-y)
    # Solve horizontal then vertical
    # But we could hit a dead spot if
    # y on row with dead spot and nx = 0
    c = "<>"[nx > x]*dx + "0v"[ny > y]*dy

    cs = []
    if y != dead_Y or nx != dead_X:
        cs.append(f"{c}A")
    if dx and dy and (x != dead_X or ny != dead_Y):
        cs.append(f"{c[::-1]}A")
    return cs

@cache
def cost(code: str, level=0) -> int:
    if level == 0:
        return len(code)
    total = 0
    curr = "A"
    for nxt in code:
        total += min(cost(path, level-1) for path in paths(curr,nxt))
        curr = nxt
    return total

total = sum(cost(code, 26) * int(code[:-1]) for code in codes)
print(total)