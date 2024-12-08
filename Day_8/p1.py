from collections import defaultdict
from pathlib import Path

HOME = Path(__file__).parent

def in_bounds(p: complex) -> bool:
    return 0 <= p.real < X and 0 <= p.imag < Y

with open(HOME/"input.txt") as f:
    grid = [*map(list,f.read().splitlines())]
    Y,X = len(grid),len(grid[0])
    types:dict[str,set[complex]] = defaultdict(set)
    antinodes = set()
    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            if col != '.':
                types[col].add(x+y*1j)
    
    for t in types.values():
        l = list(t)
        for i,a in enumerate(t):
            for b in l[i+1:]:
                delta = a - b
                for p in [a + delta,b - delta]:
                    if in_bounds(p):
                        antinodes.add(p)
    print(len(antinodes))

