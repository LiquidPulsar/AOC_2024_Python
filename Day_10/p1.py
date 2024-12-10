from pathlib import Path

HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    data = [list(map(int, l.rstrip())) for l in f]
    X, Y = len(data[0]), len(data)


def bfs(
    data: list[list[int]], x: int, y: int, v: int, seen: set[tuple[int, int]]
) -> int:
    if x < 0 or y < 0 or x >= X or y >= Y or data[y][x] != v or (x, y) in seen:
        return 0
    seen.add((x, y))
    if v == 9:
        return 1
    return sum(
        bfs(data, x + dx, y + dy, v + 1, seen)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0))
    )


print(
    sum(
        bfs(data, x, y, 0, set()) for y in range(Y) for x in range(X) if data[y][x] == 0
    )
)
