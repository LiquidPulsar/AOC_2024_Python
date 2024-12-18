from pathlib import Path

HOME = Path(__file__).parent

from time import perf_counter

tick = perf_counter()

data = []
coords = set()
with open(HOME / "input.txt") as f:
    for line in f:
        x, y = map(int, line.split(","))
        coords.add((x, y))
        data.append((x, y))


def floodfill(x, y, seen, parents, i):
    if x < 0 or y < 0 or x > X or y > Y:
        return
    if (x, y) in seen:
        return
    if (x,y) in coords:
        return
    seen.add((x, y))
    parents[x][y] = i
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        floodfill(x + dx, y + dy, seen, parents, i)

X = Y = 70

seen = set()
parents = [[None] * (Y + 1) for _ in range(X + 1)]
for x in range(X + 1):
    for y in range(Y + 1):
        if (x,y) in coords:
            continue
        floodfill(x, y, seen, parents, (x,y))

def find(x, y):
    while parents[x][y] != (x, y):
        x, y = parents[x][y]
    return x, y

def unite(xy1, xy2):
    # TODO: path compression, union by rank?
    x1, y1 = find(*xy1)
    x2, y2 = find(*xy2)
    parents[x1][y1] = (x2, y2)

for x,y in data[::-1]:
    # Add pos back in, see what sets it connects
    parents[x][y] = (x,y)
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= X and 0 <= ny <= Y and parents[nx][ny] is not None:
            unite((x, y), (nx, ny))
    
    if find(0, 0) == find(X, Y):
        print(x, y)
        break

tock = perf_counter()
print(tock - tick)