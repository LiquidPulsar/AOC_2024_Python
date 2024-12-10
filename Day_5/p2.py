from collections import defaultdict
from pathlib import Path
from functools import cmp_to_key

from time import perf_counter_ns

tic = perf_counter_ns()

HOME = Path(__file__).parent


def ok(line):
    rest = set(line)
    for n in line:
        rest.remove(n)
        if before[n] & rest:
            return False
    return True

def cmp(a, b):
    if a in before[b]:
        return -1
    return 1 if b in before[a] else 0
key = cmp_to_key(cmp)

with open(HOME / "input.txt") as f:
    before = defaultdict(set)
    a, b = map(str.splitlines, f.read().split("\n\n"))
    for line in a:
        l, r = map(int, line.split("|"))
        before[r].add(l)

    total = 0
    for line in b:
        line = [*map(int, line.split(","))]
        if not ok(line):
            line.sort(key=key)

            total += line[len(line) // 2]
    print(total)

print((perf_counter_ns() - tic) / 1e6, "ms")
assert total == 6004
