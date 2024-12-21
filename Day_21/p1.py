from pathlib import Path

HOME = Path(__file__).parent

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""

keypad = [[7,8,9],[4,5,6],[1,2,3],[None,0,"A"]]
pos_dct = {str(v):(j,i) for i,row in enumerate(keypad) for j,v in enumerate(row) if v is not None}

codes = (HOME/"input.txt").read_text().splitlines()

# D -> D -> D -> N

"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

Always starts on A, will be at A before each instr

"""

num_keypad = [[None, "^", "A"],[ "<", "v", ">"]]
num_pos_dct = {v:(j,i) for i,row in enumerate(num_keypad) for j,v in enumerate(row) if v is not None}

strs = dict.fromkeys(range(4), "")

def cost(code: str, pos_dct, level=0) -> int:
    total = 0
    x,y = pos_dct["A"]
    dead_row = 3 * (level == 3)
    for c in code:
        nx,ny = pos_dct[c]
        dx,dy = nx-x,ny-y
        if level == 0:
            total += 1
        else:
            c = ""
            # Solve horizontal then vertical
            # But we could hit a dead spot if
            # y on row with dead spot and nx = 0
            c += "<>"[nx > x]*abs(nx-x)
            c += "^v"[ny > y]*abs(ny-y)

            cs = []
            if y != dead_row or nx != 0:
                cs.append(c)
            if dx and dy and (x != 0 or ny != dead_row):
                cs.append(c[::-1])
            costs = [cost(f"{c}A", num_pos_dct, level-1) for c in cs]
            # if any(cost != costs[0] for cost in costs):
            #     print(cs, costs, level)
            total += min(costs)
        x,y = nx,ny
    return total

total = 0
for code in codes:
    cst = cost(code, pos_dct, 3)
    total += cst * int(code[:-1])
    # print(code, cost(code, pos_dct, 3))
    # strs[3] = code
    # print(strs)
print(total)