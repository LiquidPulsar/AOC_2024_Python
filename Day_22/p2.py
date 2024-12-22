from collections import defaultdict, deque
from multiprocessing import Pool
from pathlib import Path

from time import perf_counter
t0 = perf_counter()

PRUNE = 0xffffff
HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    nums = [*map(int, f)]

def worker(num: int) -> dict[tuple[int, int, int, int], int]:
    window = deque(maxlen=4)
    prev_price = num
    dct = {}
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
        if key not in dct:
            dct[key] = price
        prev_price = price
    return dct

if __name__ == "__main__":
    total_dct = defaultdict(int)
    with Pool() as pool:
        for result in pool.imap_unordered(worker, nums):
            for k, v in result.items():
                total_dct[k] += v

    t1 = perf_counter()
    print(t1 - t0)

    print(*max(total_dct.items(), key=lambda x: x[1]))

    t2 = perf_counter()
    print(t2 - t1)