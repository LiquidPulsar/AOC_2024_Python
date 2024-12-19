from functools import cache
from pathlib import Path

from tqdm import tqdm

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    patterns = f.readline().rstrip().split(", ")
    f.readline()
    designs = f.read().splitlines()

@cache
def solve(design):
    if not design: return True
    return any(
        design.startswith(pattern) and solve(design[len(pattern) :])
        for pattern in patterns
    )

print(sum(solve(design) for design in tqdm(designs)))