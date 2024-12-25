from pathlib import Path
import numpy as np

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
        heights.append(row)  # type: ignore

    if c == "#":
        locks.append(heights)
    else:
        keys.append(heights)

locks_arr = np.array(locks)[np.newaxis, :, :]
keys_arr = np.array(keys)[:, np.newaxis, :]

print(np.all(locks_arr <= keys_arr, axis=-1).sum())
