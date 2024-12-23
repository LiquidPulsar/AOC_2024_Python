from collections import defaultdict
from pathlib import Path

from more_itertools import ilen

HOME = Path(__file__).parent

conn = defaultdict(set)
with open(HOME / "input.txt") as f:
    for line in f:
        a, b = line.rstrip().split("-")
        conn[a].add(b)
        conn[b].add(a)

total = 0
for a, bs in conn.items():
    for b in bs:
        if a < b and (x := (conn[b] & bs)):
            lt = (c for c in x if b < c)
            if a[0] == "t" or b[0] == "t":
                total += ilen(lt)
            else:
                total += ilen(filter(lambda x: x[0] == "t", lt))

print(total)
