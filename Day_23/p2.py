from collections import defaultdict
from pathlib import Path

HOME = Path(__file__).parent

conn = defaultdict(set)
with open(HOME / "input.txt") as f:
    for line in f:
        a, b = line.rstrip().split("-")
        conn[a].add(b)
        conn[b].add(a)

best_len = 0
best = set()
for a, bs in conn.items():
    for b in bs:
        if a < b and (x := (conn[b] & bs)):
            if len(x) > best_len and all((conn[c] | {c}) >= x for c in x):
                best_len = len(x)
                best = x

print(",".join(sorted(best)))
