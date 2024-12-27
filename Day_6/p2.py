from collections import defaultdict
from pathlib import Path

from multiprocessing import Pool

Pos = tuple[int, int]
HOME = Path(__file__).parent

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def loops_start(curr, grid, H, W):
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

def loops(args):
    curr, obstacle, grid, H, W = args
    d = 0
    cache: dict[Pos, list[int]] = defaultdict(list)

    while d not in cache[curr]:
        cache[curr].append(d)
        i, j = curr
        di, dj = deltas[d]
        new = ni, nj = i + di, j + dj
        if not 0 <= ni < H or not 0 <= nj < W:
            return False
        if grid[ni][nj] == "#" or new == obstacle:
            d = (d + 1) % 4
        else:
            curr = new
    return True

def main():
    start = None
    with open(HOME / "input.txt") as f:
        grid = f.read().splitlines()
        H, W = len(grid), len(grid[0])
        start = next((i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == "^")

    assert start is not None, "No start position found"

    start_loops, cache = loops_start(start, grid, H, W)
    assert not start_loops, "Start position loops"

    grid = [*map(list, grid)]
    start_opts = ((start, (i,j), grid, H, W) for (i,j) in cache)
    with Pool() as pool:
        print(sum(pool.imap_unordered(loops, start_opts, chunksize=25))) # Found by hyperfine param scan

if __name__ == "__main__":
    main()