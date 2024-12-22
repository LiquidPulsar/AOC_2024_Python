from pathlib import Path

PRUNE = 16777216
HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    nums = [*map(int, f)]

total = 0
for num in nums:
    for _ in range(2000):
        num ^= num << 6
        num %= PRUNE
        num ^= num >> 5
        num %= PRUNE
        num ^= num << 11
        num %= PRUNE
    total += num
print(total)
