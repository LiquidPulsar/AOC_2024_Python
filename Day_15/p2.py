from pathlib import Path

HOME = Path(__file__).parent

grid, instrs = (
    (HOME / "input.txt")
    .read_text()
    .replace("#", "##")
    .replace("O", "[]")
    .replace(".", "..")
    .replace("@", "@.")
    .split("\n\n")
)

instrs = instrs.replace("\n", "")
grid = [*map(list, grid.split("\n"))]
W, H = len(grid[0]), len(grid)

y, x = next((i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == "@")
grid[y][x] = "."

dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for instr in instrs:
    dy, dx = dirs[instr]

    if instr in "<>":
        cy, cx = y + dy, x + dx
        while grid[cy][cx] in "[]":
            cy, cx = cy + dy, cx + dx
        if grid[cy][cx] == ".":
            if instr == "<":
                grid[y][cx:x] = grid[y][cx + 1 : x + 1]
            elif instr == ">":
                grid[y][x + 1 : cx + 1] = grid[y][x:cx]
            y, x = y + dy, x + dx
    else:
        cy = y + dy
        row = {x}
        rows = []
        can_move = True
        while row and can_move:
            rows.append(row)
            next_row = set()
            for cx in row:
                if grid[cy][cx] == "#":
                    can_move = False
                elif grid[cy][cx] == "[":
                    next_row.add(cx)
                    next_row.add(cx + 1)
                elif grid[cy][cx] == "]":
                    next_row.add(cx)
                    next_row.add(cx - 1)
            row = next_row
            cy += dy
        if not can_move:
            continue
        for row in rows[::-1]:
            cy -= dy
            for cx in row:
                grid[cy][cx] = grid[cy - dy][cx]
                grid[cy - dy][cx] = "."

        y, x = y + dy, x + dx

    # grid[y][x] = instr
    # for row in grid:
    #     print("".join(row))
    # grid[y][x] = "."
    # print()

grid[y][x] = "@"
for row in grid:
    print("".join(row))

total = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "[":
            total += 100 * y + x
print(total)
