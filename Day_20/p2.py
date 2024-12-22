from pathlib import Path
from collections import defaultdict, deque

HOME = Path(__file__).parent

grid = (HOME / "input.txt").read_text().splitlines()
W, H = len(grid[0]), len(grid)

start = next(
    (x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "S"
)
end = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "E")

d = None
queue = deque([(*end, 0)])  # x, y, d
dists = [[1000000000] * W for _ in range(H)]
while queue:
    x, y, d = queue.popleft()
    if dists[y][x] <= d:
        continue
    dists[y][x] = d
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if grid[ny][nx] != "#":
            queue.append((nx, ny, d + 1))


def phases(y, x):
    # check 20 steps right, and generally down L/R
    for nx in range(min(W-1, x+1), min(W-1, x + 21)):
        if grid[y][nx] != "#":
            yield y, nx, abs(nx - x)
    
    for ny in range(min(H-1, y+1), min(H-1, y + 21)):
        rem = 20 - abs(ny - y)
        for nx in range(max(0, x - rem), min(W-1, x + rem + 1)):
            if grid[ny][nx] != "#":
                yield ny, nx, abs(ny - y) + abs(nx - x)


saves = defaultdict(int)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        dist = dists[y][x]
        if c != "#":
            for ny, nx, d in phases(y, x):
                new_dist = dists[ny][nx]
                dist_delta = abs(dist - new_dist)
                if dist_delta > d:
                    saves[dist_delta - d] += 1

# for k in sorted(saves):
#     if k >= 50:
#         print(saves[k], k)

print(sum(v for k, v in saves.items() if k >= 100))