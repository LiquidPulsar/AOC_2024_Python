from itertools import product
from pathlib import Path
from more_itertools import ilen
from itertools import takewhile

HOME = Path(__file__).parent

locks = []
keys = []
for image in map(str.splitlines, (HOME / "input.txt").read_text().split("\n\n")):
    t = [*zip(*image)]
    get_heights = lambda tgt: [ilen(takewhile(lambda x: x == tgt, col)) for col in t]
    if all(c == "#" for c in image[0]):
        heights = get_heights("#")
        locks.append(heights)
    else:
        heights = get_heights(".")
        keys.append(heights)

# locks.sort()
# keys.sort()

# print(locks, keys)

print(sum(all(map(int.__le__, lock, key)) for lock, key in product(locks, keys)))

# for key in keys:
#     lock_ptr = 0
#     while lock_ptr < len(locks) and all(map(int.__le__, locks[lock_ptr], key)):
#         lock_ptr += 1
#     print(key, [6 - i for i in key], lock_ptr, locks[lock_ptr] if lock_ptr < len(locks) else None)
