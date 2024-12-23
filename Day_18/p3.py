from pathlib import Path

HOME = Path(__file__).parent
X = Y = 70

from time import perf_counter

tick = perf_counter()

"""
This takes a slightly different approach compared to `p2.py`
This time, we use UFDS to connect the top-right and bottom-left corners.
This version doesn't need to store the file data, and is an online algorithm.

However, this version is slower than `p2.py`, perhaps because the answer is near the end of the input.
"""


parents: list[list[tuple[int, int] | None]] = [[None] * (Y + 1) for _ in range(X + 1)]

def find(x, y):
    res = parents[x][y]
    if res != (x, y):
        res = parents[x][y] = find(*res)
    return res

def unite(xy1, xy2):
    x1, y1 = find(*xy1)
    x2, y2 = find(*xy2)
    parents[x1][y1] = (x2, y2)

# kinda wrong since this adds a block on each corner
parents[0][Y] = (0, Y)
parents[X][0] = (X, 0)

with open(HOME / "input.txt") as f:
    for line in f:
        x, y = map(int, line.split(","))
        parents[x][y] = (x, y)

        if x == 0 or y == Y:
            # In the bottom-left side
            unite((x, y), (0, Y))
            
        if x == X or y == 0:
            # In the top-right side
            unite((x, y), (X, 0))

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= X and 0 <= ny <= Y and parents[nx][ny] is not None:
                unite((x, y), (nx, ny))
        
        if find(0, Y) == find(X, 0):
            print(x, y)
            break

tock = perf_counter()
print(tock - tick)
