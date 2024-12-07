from pathlib import Path
from tqdm import tqdm

HOME = Path(__file__).parent


def unconc(a: float, b: int):
    ia = int(a)
    if a != ia:
        return -1
    bs = str(b)
    return a // (10 ** len(bs)) if str(ia).endswith(bs) else -1


def try_fix(curr: float, parts: list[int]):
    if not parts:
        return curr == 0
    if curr < 0:
        return False

    a, *rest = parts
    return (
        try_fix(curr - a, rest)
        or try_fix(curr / a, rest)
        or try_fix(unconc(curr, a), rest)
    )


with open(HOME / "input.txt") as f:
    total = 0
    for line in tqdm(f):
        res, parts = line.split(":")
        res = int(res)
        if try_fix(res, [*map(int, parts.split()[::-1])]):
            total += res
    print(total)  # 12498581459
