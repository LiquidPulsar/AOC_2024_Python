from pathlib import Path

HOME = Path(__file__).parent
X = Y = 70

from time import perf_counter

tick = perf_counter()

data = []

parents: list[list[tuple[int, int] | None]] = [[None] * (Y + 1) for _ in range(X + 1)]
TAKEN = (-1, -1)

with open(HOME / "input.txt") as f:
    for line in f:
        x, y = map(int, line.split(","))
        parents[x][y] = TAKEN
        data.append((x, y))


def floodfill(x, y, parents, i):
    if x < 0 or y < 0 or x > X or y > Y:
        return
    if parents[x][y] is not None:
        return
    parents[x][y] = i
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        floodfill(x + dx, y + dy, parents, i)


for x in range(X + 1):  # sourcery skip
    for y in range(Y + 1):
        if parents[x][y] is None:
            floodfill(x, y, parents, (x, y))

# for row in zip(*parents):
#     print(row)


def find(x, y):
    while parents[x][y] != (x, y):
        x, y = parents[x][y]
    return x, y


def unite(xy1, xy2):
    # TODO: path compression, union by rank?
    x1, y1 = find(*xy1)
    x2, y2 = find(*xy2)
    parents[x1][y1] = (x2, y2)


for x, y in reversed(data):
    # Add pos back in, see what sets it connects
    parents[x][y] = (x, y)
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= X and 0 <= ny <= Y and parents[nx][ny] not in (None, TAKEN):
            unite((x, y), (nx, ny))

    if find(0, 0) == find(X, Y):
        print(x, y)
        break

tock = perf_counter()
print(tock - tick)
