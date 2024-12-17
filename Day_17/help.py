from itertools import count
from pathlib import Path

from tqdm import tqdm

HOME = Path(__file__).parent

regs_, instrs_ = (HOME / "input.txt").read_text().split("\n\n", 1)

regs = [int(line[12:]) for line in regs_.splitlines()]
instrs = list(map(int, instrs_[9:].split(",")))


def combo_op(i: int):
    return i if i < 4 else "ABC"[i - 4]


rsp = 0
while rsp < len(instrs) - 1:
    nxt = instrs[rsp + 1]
    match instrs[rsp]:
        case 0:  # adv
            print(f"A //= 1 << {combo_op(nxt)}")
        case 1:  # bxl
            print(f"B ^= {nxt}")
        case 2:  # bsi
            print(f"B = {combo_op(nxt)} % 8")
        case 3:  # jnz
            print(f"if A != 0: rsp = {nxt}")
        case 4:  # bxc
            # reads an arg but doesn't use it
            print("B ^= C")
        case 5:  # out
            print(f"out.append({combo_op(nxt)} % 8)")
        case 6:  # bdv
            print(f"B = A // (1 << {combo_op(nxt)})")
        case 7:  # cdv
            print(f"C = A // (1 << {combo_op(nxt)})")
    rsp += 2
