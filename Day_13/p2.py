from pathlib import Path
import numpy as np
import re

HOME = Path(__file__).parent

games = re.findall(
    r"X\+(\d+), Y\+(\d+)\n.*X\+(\d+), Y\+(\d+)\n.*X=(\d+), Y=(\d+)",
    (HOME / "input.txt").read_text(),
)

total = 0
for game in games:
    x1, y1, x2, y2, tx, ty = map(int, game)
    t = np.array([10000000000000 + tx, 10000000000000 + ty])

    m = np.array([[x1, x2], [y1, y2]])
    cost = np.round(np.linalg.inv(m) @ t)
    if np.all(m @ cost == t) and np.all(cost >= 0):
        total += cost @ np.array([3, 1])
print(total)
