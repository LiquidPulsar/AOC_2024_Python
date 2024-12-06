from collections import defaultdict
from pathlib import Path

from tqdm import tqdm


Pos = tuple[int, int]
HOME = Path(__file__).parent

start = None
with open(HOME / "input.txt") as f:
    grid = f.read().splitlines()
    H, W = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "^":
                start = (i, j)
                break
        else:
            continue
        break

assert start is not None, "No start position found"

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0


def loops(curr, grid):
    d = 0
    cache: dict[Pos, list[int]] = defaultdict(list)

    while d not in cache[curr]:
        cache[curr].append(d)
        i, j = curr
        di, dj = deltas[d]
        new = ni, nj = i + di, j + dj
        if not 0 <= ni < H or not 0 <= nj < W:
            return False, cache
        if grid[ni][nj] == "#":
            d = (d + 1) % 4
        else:
            curr = new
    return True, cache

start_loops, cache = loops(start, grid)
assert not start_loops, "Start position loops"

total = 0
grid = [*map(list, grid)]
for i,row in tqdm(enumerate(grid), total=H):
    for j, col in enumerate(row):
        if (i,j) not in cache:
            continue
        row[j] = "#"
        if loops(start, grid)[0]:
            total += 1
        row[j] = "."

print(total)