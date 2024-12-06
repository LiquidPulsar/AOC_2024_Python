from collections import defaultdict
from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    before = defaultdict(set)
    a,b = map(str.splitlines,f.read().split("\n\n"))
    for line in a:
        l,r = map(int,line.split("|"))
        before[r].add(l)

    total = 0
    for line in b:
        line = [*map(int,line.split(","))]
        rest = set(line)
        for n in line:
            rest.remove(n)
            if before[n] & rest:
                break
        else:
            total += line[len(line)//2]
    print(total)