from collections import defaultdict
from pathlib import Path


Pos = tuple[int, int]
HOME = Path(__file__).parent

curr = None
with open(HOME / "input.txt") as f:
    grid = f.read().splitlines()
    H, W = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "^":
                curr = (i, j)
                break
        else:
            continue
        break

assert curr is not None, "No start position found"

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0


cache: dict[Pos, list[int]] = defaultdict(list)

while d not in cache[curr]:
    cache[curr].append(d)
    i, j = curr
    di, dj = deltas[d]
    new = ni, nj = i + di, j + dj
    if not 0 <= ni < H or not 0 <= nj < W:
        break
    if grid[ni][nj] == "#":
        d = (d + 1) % 4
    else:
        curr = new

print(len(cache))
# grid = [*map(list,grid)]
# for i, j in cache.keys():
#     grid[i][j] = '*'

# for row in grid:
#     print("".join(row))
