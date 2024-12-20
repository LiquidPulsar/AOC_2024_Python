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
    # cross at most 2 walls in a row and end on an empty space
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if grid[ny][nx] == "#":
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != "#":
                yield ny, nx


saves = defaultdict(int)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        dist = dists[y][x]
        if c != "#":
            for ny, nx in phases(y, x):
                new_dist = dists[ny][nx]
                if new_dist < dist:
                    saves[dist - new_dist - 2] += 1

# for k in sorted(saves):
    # print(k, saves[k])

print(sum(v for k, v in saves.items() if k >= 100))