from collections import defaultdict
from pathlib import Path

from tqdm import trange

PRUNE = 16777216
HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    nums = [*map(int, f)]

"""
Store map of all sets of changes length 1-4 -> prices when seen
Use this to avoid searching too much:
- Suppose best is +1 +2 +3 +4
- If we check ? ? ? +5 and the best of the occurences doesn't beat it, skip!
"""


total_heuristic = defaultdict(int)
total_dct = defaultdict(int)
all_seen = set()
for num in nums:
    hist = [num % 10]
    diffs = []
    for _ in range(2000):
        num ^= num << 6
        num %= PRUNE
        num ^= num >> 5
        num %= PRUNE
        num ^= num << 11
        num %= PRUNE
        diffs.append(num % 10 - hist[-1])
        hist.append(num % 10)

    seen = set()
    heuristic = defaultdict(int)

    prev = diffs[:4]
    for d, p in zip(diffs[4:], hist[4:]):
        key = tuple(prev)
        for i in range(1, 4):
            heuristic[key[:i]] = max(heuristic[key[:i]], p)

        if key not in seen:
            total_dct[key] += p
            seen.add(key)

        prev.pop(0)
        prev.append(d)

    for key, value in heuristic.items():
        total_heuristic[key] += value
    
    all_seen.update(seen)

# target = (-2, 1, -1, 3)
# for monkey in monkeys:
#     dct, heuristic = monkey
#     print(dct[target] if target in dct else "Target not found")

best_target = (-1, -1, -1, -1)
best_score = 0
skipped_iters = 0
for d in trange(9, -10, -1):
    if total_heuristic[d,] <= best_score:
        # print("Skipping", d)
        skipped_iters += 19**3
        continue
    for c in range(9, -10, -1):
        if total_heuristic[c,d] <= best_score:
            # print("Skipping", c,d)
            skipped_iters += 19**2
            continue
        for b in range(9, -10, -1):
            if total_heuristic[b,c,d] <= best_score:
                # print("Skipping", b,c,d)
                skipped_iters += 19
                continue
            for a in range(9, -10, -1):
                target = (a,b,c,d)
                score = total_dct[target]
                if score > best_score:
                    # print("New best:", target, score)
                    best_score = score
                    best_target = target

print(skipped_iters, 19**4)
print(best_target)
print(best_score)