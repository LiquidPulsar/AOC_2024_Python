from collections import defaultdict
from pathlib import Path
from heapq import heappop, heappush

HOME = Path(__file__).parent

grid = (HOME / "input.txt").read_text().splitlines()
start = (1, len(grid) - 2)
end = (len(grid[0]) - 2, 1)

heap: list[tuple[int, int, tuple[int, int]]] = [(0, 0, start)]
dct = defaultdict(lambda: 1000000000000)
target_time = None
while heap:
    t, d, (x, y) = heappop(heap)
    # print(t)
    if t >= dct[(x, y, d)]:
        continue
    dct[(x, y, d)] = t

    if target_time is not None and t > target_time:
        break

    # display(grid, path, x, y)
    if grid[y][x] == "E":
        if target_time is None:
            target_time = t
        print("Done:", t)

    for nd, (dx, dy) in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]):
        nx, ny = x + dx, y + dy
        if grid[ny][nx] != "#":
            # 0 -> 3
            abs_rot = abs(d - nd)
            rot = min(abs_rot, 4 - abs_rot)
            heappush(heap, (t + 1 + 1000 * rot, nd, (nx, ny)))

assert target_time is not None

# Backsolve
stack: list[tuple[int, int, tuple[int, int]]] = [
    (target_time, d, end) for d in range(4) if (*end, d) in dct
]
seen = set()

while stack:
    t, d, (x, y) = stack.pop()
    # print(t, d, path)
    seen.add((x, y))

    dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][d]
    nx, ny = x - dx, y - dy
    for nd, _ in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]):
        if grid[ny][nx] != "#":
            # 0 -> 3
            abs_rot = abs(d - nd)
            rot = min(abs_rot, 4 - abs_rot)
            # print([dct.get((nx, ny, i)) for i in range(4)])
            # print((nx, ny, nd),dct[(nx, ny, nd)],t - 1 - 1000 * rot)
            if dct[(nx, ny, nd)] == t - 1 - 1000 * rot:
                stack.append((t - 1 - 1000 * rot, nd, (nx, ny)))

print(len(seen))
