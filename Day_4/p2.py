from pathlib import Path
from more_itertools import sliding_window

HOME = Path(__file__).parent

TARGET = "MAS"
valid = ((TARGET[0], TARGET[2]), (TARGET[2], TARGET[0]))

total = 0
with open(HOME / "input.txt") as f:
    for rs in sliding_window(f, len(TARGET)):
        for c1,c2,c3 in sliding_window(zip(*rs), len(TARGET)):
            if (
                c2[1] == TARGET[1]
                and (c1[0], c3[2]) in valid
                and (c1[2], c3[0]) in valid
            ):
                total += 1
    print(total)
