from itertools import count
from statistics import stdev, mean
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
    positions.append(tuple(map(int, robot)))

ratios = []
for t in count():
    new_positions = []
    for x,y,vx,vy in positions:
        new_positions.append(((x + vx) % W, (y + vy) % H, vx, vy))

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