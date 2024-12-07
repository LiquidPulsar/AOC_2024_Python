from pathlib import Path

HOME = Path(__file__).parent

TARGET = "XMAS"
total = 0
with open(HOME / "input.txt") as f:
    data = f.read().splitlines()

    X, Y = len(data[0]), len(data)

    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == TARGET[0]:
                target = TARGET
            elif col == TARGET[-1]:
                target = TARGET[::-1]
            else:
                continue

            if row[x : x + len(target)] == target:
                # print("row",y,x)
                total += 1
            if y + len(target) <= Y:
                if all(data[y + i][x] == target[i] for i in range(len(target))):
                    # print("col",y,x)
                    total += 1
                if x + len(target) <= X and all(
                    data[y + i][x + i] == target[i] for i in range(len(target))
                ):
                    total += 1
                if x - len(target) >= -1 and all(
                    data[y + i][x - i] == target[i] for i in range(len(target))
                ):
                    total += 1

    print(total)
