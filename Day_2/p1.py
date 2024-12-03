from pathlib import Path

HOME = Path(__file__).parent


def safe(line):
    p, *parts = [*map(int, line.split())]
    up = None
    for c in parts:
        if not (1 <= abs(c - p) <= 3) or up == (c < p):
            return False
        up = c > p
        p = c
    return True


with open(HOME / "input.txt") as f:
    print(sum(map(safe, f)))