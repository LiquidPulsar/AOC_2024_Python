from collections import defaultdict
from pathlib import Path

HOME = Path(__file__).parent

def in_bounds(p: complex) -> bool:
    return 0 <= p.real < X and 0 <= p.imag < Y

with open(HOME/"input.txt") as f:
    types:dict[str,set[complex]] = defaultdict(set)
    antinodes = set()
    for y,row in enumerate(f.readlines()):
        for x,col in enumerate(row.strip()):
            if col != '.':
                types[col].add(x+y*1j)
    Y,X = y+1,x+1 # type: ignore

for t in types.values():
    l = list(t)
    for i,a in enumerate(t):
        for b in l[i+1:]:
            delta = a - b
            p = a
            while in_bounds(p):
                antinodes.add(p)
                p += delta
            p = b
            while in_bounds(p):
                antinodes.add(p)
                p -= delta
print(len(antinodes))

