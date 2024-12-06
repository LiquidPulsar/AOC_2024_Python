from collections import defaultdict
from pathlib import Path

HOME = Path(__file__).parent


def fix(line):
    rest = set(line)
    for i, n in enumerate(line):
        rest.remove(n)
        if isec := before[n] & rest:
            loc = max(map(line.index, isec))
            line[i:loc] = line[i + 1 : loc + 1]
            line[loc] = n
            return False
    return True


with open(HOME / "input.txt") as f:
    before = defaultdict(set)
    a, b = map(str.splitlines, f.read().split("\n\n"))
    for line in a:
        l, r = map(int, line.split("|"))
        before[r].add(l)

    total = 0
    for line in b:
        line = [*map(int, line.split(","))]
        if not fix(line):
            while not fix(line):
                pass

            total += line[len(line) // 2]
    print(total)
