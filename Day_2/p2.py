from pathlib import Path

HOME = Path(__file__).parent


def old_safe(line):
    p, *parts = line
    up = None
    for c in parts:
        if not (1 <= abs(c - p) <= 3) or up == (c < p):
            return False
        up = c > p
        p = c
    return True

def safe(line):
    parts = [*map(int, line.split())]
    return any(
        old_safe([*parts[:i], *parts[i+1:]])
        for i in range(len(parts))
    )

with open(HOME / "input.txt") as f:
    print(sum(map(safe, f)))
