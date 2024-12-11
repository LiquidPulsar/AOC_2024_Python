from pathlib import Path

HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    data = [list(map(int, l.rstrip())) for l in f]
    X, Y = len(data[0]), len(data)


def dfs(
    data: list[list[int]], x: int, y: int, v: int, seen: dict[tuple[int, int], int]
) -> int:
    if x < 0 or y < 0 or x >= X or y >= Y or data[y][x] != v:
        return 0
    if (x, y) in seen:
        return seen[x, y]
    if v == 9:
        seen[x, y] = 1
        return 1
    seen[x, y] = s = sum(
        dfs(data, x + dx, y + dy, v + 1, seen)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0))
    )
    return s


dct = {}
print(
    sum(
        dfs(data, x, y, 0, dct) for y in range(Y) for x in range(X) if data[y][x] == 0
    )
)
