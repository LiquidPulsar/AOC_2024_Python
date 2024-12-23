from collections import defaultdict
from pathlib import Path

HOME = Path(__file__).parent

conn = defaultdict(list)
with open(HOME / "input.txt") as f:
    for line in f:
        a, b = line.rstrip().split("-")
        conn[a].append(b)
        conn[b].append(a)

best_len = 0
best = []
for a, bs in sorted(conn.items()):
    s = set(bs)
    for b in bs:
        if a < b and (x := (set(conn[b]) & s)):
            x.add(b)
            x.add(a)

            if len(x) > best_len and all((set(conn[c]) | {c}) >= x for c in x):
                best_len = len(x)
                best = sorted(x)

print(",".join(best))