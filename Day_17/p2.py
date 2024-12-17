from itertools import count
from pathlib import Path

from tqdm import tqdm

HOME = Path(__file__).parent

regs_, instrs_ = (HOME / "input.txt").read_text().split("\n\n", 1)

regs = [int(line[12:]) for line in regs_.splitlines()]
instrs = list(map(int, instrs_[9:].split(",")))


def combo_op(regs: list[int], i: int):
    return i if i < 4 else regs[i - 4]


def run(regs: list[int], instrs: list[int]) -> list[int]:
    out = []
    rsp = 0
    while rsp < len(instrs) - 1:
        nxt = instrs[rsp + 1]
        match instrs[rsp]:
            case 0:  # adv
                regs[0] //= 1 << combo_op(regs, nxt)
            case 1:  # bxl
                regs[1] ^= nxt
            case 2:  # bsi
                regs[1] = combo_op(regs, nxt) % 8
            case 3:  # jnz
                if regs[0] != 0:
                    rsp = nxt
                    continue
            case 4:  # bxc
                # reads an arg but doesn't use it
                regs[1] ^= regs[2]
            case 5:  # out
                out.append(combo_op(regs, nxt) % 8)
            case 6:  # bdv
                regs[1] = regs[0] // (1 << combo_op(regs, nxt))
            case 7:  # cdv
                regs[2] = regs[0] // (1 << combo_op(regs, nxt))
        rsp += 2
    return out


def run_a(regs: list[int], a: int, instrs: list[int]):
    return run([a, *regs[1:]], instrs)


possible = [0]
for i in range(len(instrs)):
    possible = [
        n * 8 + a
        for n in possible
        for a in range(8)
        if instrs[-i - 1 :] == run_a(regs, n * 8 + a, instrs)
    ]
print(possible[0])
