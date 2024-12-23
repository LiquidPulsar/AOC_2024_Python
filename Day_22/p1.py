from pathlib import Path

HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    nums = [*map(int, f)]


# Note: inlining the 0x is faster on PyPy, but slower on CPython
total = 0
for num in nums:
    for _ in range(2000):
        num ^= num << 6
        num &= 0xffffff
        num ^= num >> 5
        num &= 0xffffff
        num ^= num << 11
        num &= 0xffffff
    total += num
print(total)
