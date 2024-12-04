from pathlib import Path

HOME = Path(__file__).parent

TARGET = "MAS"
valid = ((TARGET[0], TARGET[2]), (TARGET[2], TARGET[0]))

total = 0
with open(HOME / "input.txt") as f:
    data = f.read().splitlines()

    X, Y = len(data[0]), len(data)

    for y, row in enumerate(data[: -len(TARGET) + 1]):
        for x, col in enumerate(row[: -len(TARGET) + 1]):
            if (
                data[y + 1][x + 1] == TARGET[1]
                and (col, data[y + 2][x + 2]) in valid
                and (data[y][x + 2], data[y + 2][x]) in valid
            ):
                total += 1
    print(total)
