from pathlib import Path
from operator import add, mul

from tqdm import tqdm

HOME = Path(__file__).parent

def try_fix(res:int, curr:int, parts:list[int]):
    if not parts:
        return curr == res
    if curr > res:
        return False
    
    a,*rest = parts
    return any(
        try_fix(res, f(curr,a),rest)
        for f in (add,mul)
    )


with open(HOME/"input.txt") as f:
    total = 0
    for line in tqdm(f):
        res,parts = line.split(":")
        a,*rest = [*map(int,parts.split())]
        res = int(res)
        if try_fix(res,a,rest):
            total += res
    print(total)

