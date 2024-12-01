from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    data = [
        list(map(int, line.split()))
        for line in f
    ]
    l,r = [*zip(*data)]
    print(sum(abs(a-b) for a,b in zip(sorted(l),sorted(r))))
