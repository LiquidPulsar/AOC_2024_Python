from pathlib import Path

HOME = Path(__file__).parent

grid, instrs = (HOME / "input.txt").read_text().split("\n\n")
instrs = instrs.replace("\n", "")
grid = [*map(list, grid.split("\n"))]
W, H = len(grid[0]), len(grid)

y, x = next((i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == "@")
grid[y][x] = "."

dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for instr in instrs:
    dy, dx = dirs[instr]

    cy, cx = y + dy, x + dx
    while grid[cy][cx] == "O":
        cy, cx = cy + dy, cx + dx
    if grid[cy][cx] == ".":
        grid[cy][cx] = "O"
        y, x = y + dy, x + dx
        grid[y][x] = "."

    # grid[y][x] = instr
    # for row in grid:
    #     print("".join(row))
    # grid[y][x] = "."
    # print()

total = 0
for y,row in enumerate(grid):
    for x,c in enumerate(row):
        if c == "O":
            total += 100 * y + x
print(total)