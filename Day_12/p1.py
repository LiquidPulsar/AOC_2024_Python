from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    grid = [list(line.strip()) for line in f]

def fill(y:int, x:int, target:str, seen: set[tuple[int, int]]):
    seen.add((y,x))
    a,p = 1,0
    for dy,dx in ((0,1),(1,0),(0,-1),(-1,0)):
        y2,x2 = y+dy,x+dx
        if 0<=y2<len(grid) and 0<=x2<len(grid[0]):
            if grid[y2][x2] != target:
                p += 1
            elif (y2,x2) not in seen:
                da,dp = fill(y2,x2,target,seen)
                a += da
                p += dp
        else:
            p += 1
    return a,p

total = 0
seen = set()
for y,row in enumerate(grid):
    for x,col in enumerate(row):
        if (y,x) not in seen:
            a,p = fill(y,x,col,seen)
            total += a * p
print(total)