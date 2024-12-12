from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    grid = [list(line.strip()) for line in f]

def fill(y:int, x:int, target:str, seen: set[tuple[int, int]], borders: set[tuple[int, int, int, int]]):
    seen.add((y,x))
    a = 1
    for dy,dx in ((0,1),(1,0),(0,-1),(-1,0)):
        y2,x2 = y+dy,x+dx
        if 0<=y2<len(grid) and 0<=x2<len(grid[0]):
            if grid[y2][x2] != target:
                borders.add((y,x,y2,x2))
            elif (y2,x2) not in seen:
                da = fill(y2,x2,target,seen,borders)
                a += da
        else:
            borders.add((y,x,y2,x2))
    return a

def num_sides(borders:set[tuple[int,int,int,int]]):
    s = 0
    while borders:
        y,x,y2,x2 = borders.pop()
        s += 1
        if y!=y2:
            l = 1
            while (y,x+l,y2,x2+l) in borders:
                borders.remove((y,x+l,y2,x2+l))
                l += 1
            l = -1
            while (y,x+l,y2,x2+l) in borders:
                borders.remove((y,x+l,y2,x2+l))
                l -= 1
        else:
            l = 1
            while (y+l,x,y2+l,x2) in borders:
                borders.remove((y+l,x,y2+l,x2))
                l += 1
            l = -1
            while (y+l,x,y2+l,x2) in borders:
                borders.remove((y+l,x,y2+l,x2))
                l -= 1
    return s

total = 0
seen = set()
for y,row in enumerate(grid):
    for x,col in enumerate(row):
        if (y,x) not in seen:
            borders = set()
            a = fill(y,x,col,seen,borders)
            # print(col, a, n:=num_sides(borders))
            total += a * num_sides(borders)
            # break
    # break
print(total)