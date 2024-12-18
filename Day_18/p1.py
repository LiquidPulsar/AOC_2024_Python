from pathlib import Path
from collections import deque

HOME = Path(__file__).parent

coords = {}
with open(HOME / "input.txt") as f:
    for i, line in enumerate(f):
        x, y = map(int, line.split(","))
        coords[(x, y)] = i

LIMIT = 1024
X = Y = 70

queue = deque([(0, 0, 0)])
seen = set()
while queue:
    x, y, d = queue.popleft()
    if x < 0 or y < 0 or x > X or y > Y:
        continue
    if (x, y) in seen:
        continue
    if (x, y) == (X, Y):
        print(d)
        break
    seen.add((x, y))
    if coords.get((x, y), 10000000000) >= LIMIT:
        queue.extend(
            (x + dx, y + dy, d + 1) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
        )