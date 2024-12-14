from math import prod
from pathlib import Path
import re

HOME = Path(__file__).parent

robots = re.findall(
    r"(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", (HOME / "input.txt").read_text()
)

W = 101
H = 103
T = 100

positions = []
for robot in robots:
    x, y, vx, vy = map(int, robot)
    positions.append(((x + vx * T) % W, (y + vy * T) % H))


# grid = [[0]*W for _ in range(H)]
# for x,y in positions:
#     grid[y][x] += 1

# for row in grid:
#     print(*row,sep="")


counts = [0]*4
for x,y in positions:
    if x == W//2 or y == H//2:
        continue
    counts[2*(x < W//2) + (y < H//2)] += 1

# print(counts)
print(prod(counts))