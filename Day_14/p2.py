from itertools import count
from pathlib import Path
import re

HOME = Path(__file__).parent

robots = re.findall(
    r"(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", (HOME / "input.txt").read_text()
)

W = 101
H = 103
T = 100

positions = [tuple(map(int, robot)) for robot in robots]
ratios = []
for t in count():
    new_positions = [
        ((x + vx) % W, (y + vy) % H, vx, vy) for x, y, vx, vy in positions
    ]
    grid = [[0]*W for _ in range(H)]
    for x,y,_,_ in positions:
        grid[y][x] += 1
        if grid[y][x] == 2:
            break
    else:
        for row in grid:
            print(*row,sep="")
        print(t)
        break

    positions = new_positions