from pathlib import Path
from collections import Counter

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    data = [
        list(map(int, line.split()))
        for line in f
    ]
    l,r = [*zip(*data)]
    counts = Counter(r)
    print(sum(a * counts[a] for a in l))