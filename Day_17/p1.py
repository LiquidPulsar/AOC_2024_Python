from pathlib import Path

HOME = Path(__file__).parent

regs_, instrs_ = (HOME / "input.txt").read_text().split("\n\n", 1)

regs = [int(line[12:]) for line in regs_.splitlines()]
instrs = list(map(int, instrs_[9:].split(",")))


def combo_op(i: int):
    return i if i < 4 else regs[i - 4]

out = []
rsp = 0
while rsp < len(instrs) - 1:
    nxt = instrs[rsp + 1]
    match instrs[rsp]:
        case 0:  # adv
            regs[0] //= 1 << combo_op(nxt)
        case 1:  # bxl
            regs[1] ^= nxt
        case 2:  # bsi
            regs[1] = combo_op(nxt) % 8
        case 3:  # jnz
            if regs[0] != 0:
                rsp = nxt
                continue
        case 4:  # bxc
            # reads an arg but doesn't use it
            regs[1] ^= regs[2]
        case 5:  # out
            out.append(combo_op(nxt) % 8)
        case 6:  # bdv
            regs[1] = regs[0] // (1 << combo_op(nxt))
        case 7:  # cdv
            regs[2] = regs[0] // (1 << combo_op(nxt))
    rsp += 2
print(",".join(map(str, out)))
print(regs)