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
            return False
        if grid[ni][nj] == "#":
            d = (d + 1) % 4
        else:
            curr = new
    return True

# Very slow, takes about a minute

total = 0
grid = [*map(list, grid)]
for row in tqdm(grid):
    for j, col in enumerate(row):
        if col == "#":
            continue
        row[j] = "#"
        if loops(start, grid):
            total += 1
        row[j] = "."

print(total)