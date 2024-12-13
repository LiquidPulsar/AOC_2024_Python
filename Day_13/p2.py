from pathlib import Path
import numpy as np
import re

HOME = Path(__file__).parent

games = re.findall(
    r"X\+(\d+), Y\+(\d+)\n"
    r".*X\+(\d+), Y\+(\d+)\n"
    r".*X=(\d+), Y=(\d+)", 
    (HOME / "input.txt").read_text()
)

total = 0
for game in games:
    x1,y1,x2,y2,tx,ty = map(int,game)
    t = np.array([10000000000000+tx,10000000000000+ty])

    m = np.array([
        [x1, x2],
        [y1, y2]
    ])


    cost = c1,c2 = np.linalg.inv(m) @ t
    # print(cost)
    # print(f"{c1:.20f} {c2:.20f}")
    if np.all(np.dot(m,list(map(round,cost))) == t) and c1 >= 0 and c2 >= 0:
        # print(3*c1 + c2)
        total += 3*c1 + c2
print(total)
