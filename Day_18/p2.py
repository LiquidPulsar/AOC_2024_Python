from pathlib import Path
from collections import deque

HOME = Path(__file__).parent

"""
O(n) approach: connected component tree, run backwards
First time we see start component and end component in
the same connected component, we are done.
"""

data = []
coords = {}
with open(HOME / "input.txt") as f:
    for i, line in enumerate(f):
        x, y = map(int, line.split(","))
        coords[(x, y)] = i
        data.append((x, y))

X = Y = 70
def run(limit: int) -> bool:
    queue = deque([(0, 0, 0)])
    seen = set()
    while queue:
        x, y, d = queue.popleft()
        if x < 0 or y < 0 or x > X or y > Y:
            continue
        if (x, y) in seen:
            continue
        if (x, y) == (X, Y):
            return False
        seen.add((x, y))
        if coords.get((x, y), 10000000000) >= limit:
            queue.extend(
                (x + dx, y + dy, d + 1) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            )
    return True

lim = 1
while not run(lim):
    lim *= 2

low = lim // 2
high = lim
while low < high:
    mid = (low + high) // 2
    if run(mid):
        high = mid
    else:
        low = mid + 1
print(low, data[low-1])