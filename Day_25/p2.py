from pathlib import Path
import numpy as np

from time import perf_counter

t0 = perf_counter()

HOME = Path(__file__).parent

locks = []
keys = []
for image in map(str.splitlines, (HOME / "input.txt").read_text().split("\n\n")):
    heights = []
    c = image[0][0]
    for col in range(len(image[0])):
        for row in range(len(image)):
            if image[row][col] != c:
                break
        heights.append(row) # type: ignore

    if c == "#":
        locks.append(heights)
    else:
        keys.append(heights)

print(perf_counter() - t0)

locks_arr = np.array(locks)[np.newaxis, :, :]
keys_arr = np.array(keys)[:, np.newaxis, :]

print(np.all(locks_arr <= keys_arr, axis=-1).sum())
# print(sum(all(map(int.__le__, lock, key)) for lock, key in product(locks, keys)))

print(perf_counter() - t0)

# locks.sort()
# keys.sort()

# print(locks, keys)


# for key in keys:
#     lock_ptr = 0
#     while lock_ptr < len(locks) and all(map(int.__le__, locks[lock_ptr], key)):
#         lock_ptr += 1
#     print(key, [6 - i for i in key], lock_ptr, locks[lock_ptr] if lock_ptr < len(locks) else None)
