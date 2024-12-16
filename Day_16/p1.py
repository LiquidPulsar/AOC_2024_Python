from collections import defaultdict
from pathlib import Path
from heapq import heappop, heappush

HOME = Path(__file__).parent

grid = (HOME / "input.txt").read_text().splitlines()
start = (1, len(grid) - 2)


def display(grid, path, ex, ey):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if x == ex and y == ey:
                print("X", end="")
            elif (x, y) in path:
                print("*", end="")
            else:
                print(c, end="")
        print()
    print()


heap: list[tuple[int, int, list[tuple[int, int]]]] = [(0, 0, [start])]
dct = defaultdict(lambda: 1000000000000)
while heap:
    t, d, [*path, (x, y)] = heappop(heap)
    # print(t)
    if t >= dct[(x, y, d)]:
        continue
    dct[(x, y, d)] = t

    # display(grid, path, x, y)
    if grid[y][x] == "E":
        print("Done:", t)
        break
    for nd, (dx, dy) in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]):
        nx, ny = x + dx, y + dy
        if grid[ny][nx] != "#":
            # 0 -> 3
            abs_rot = abs(d - nd)
            rot = min(abs_rot, 4 - abs_rot)
            heappush(heap, (t + 1 + 1000 * rot, nd, [*path, (x, y), (nx, ny)]))
