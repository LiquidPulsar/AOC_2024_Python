from collections import defaultdict, deque
from pathlib import Path

from time import perf_counter
t0 = perf_counter()

PRUNE = 0xffffff
HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    nums = [*map(int, f)]

total_dct = defaultdict(int)
for num in nums:
    window = deque(maxlen=4)
    prev_price = num
    seen = set()
    for _ in range(2000):
        num ^= num << 6
        num &= PRUNE
        num ^= num >> 5
        num &= PRUNE
        num ^= num << 11
        num &= PRUNE
        price = num % 10
        window.append(price - prev_price)
        key = tuple(window)
        if key not in seen:
            total_dct[key] += price
            seen.add(key)
        prev_price = price

t1 = perf_counter()
print(t1 - t0)

print(*max(total_dct.items(), key=lambda x: x[1]))

t2 = perf_counter()
print(t2 - t1)