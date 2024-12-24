from pathlib import Path

HOME = Path(__file__).parent

# hyperfine "pypy --jit max_unroll_recursion=0 p2.py" --warmup 5

def unconc(a: int, b: int):
    x = 1
    while x <= b:
        x *= 10
    q,r = divmod(a, x)
    return q if r == b else -1

def try_fix(curr: int, parts: tuple[int, ...], i: int):
    # Do this first, as triggered 19654 times
    if i < 0:
        return curr == 0
    # Do this second, as triggered 18960 times (0.964)
    if curr < 0:
        return False

    a = parts[i]
    q,r = divmod(curr, a)
    return (
        not r and try_fix(q, parts, i - 1)
        or try_fix(unconc(curr, a), parts, i - 1)
        or try_fix(curr - a, parts, i - 1)
    )


with open(HOME/ "input.txt") as f:
    total = 0
    for line in f:
        _res, _parts = line.split(":")
        parts = tuple(map(int, _parts.split()))
        res = int(_res)
        if try_fix(res, parts, len(parts) - 1):
            total += res
    print(total)
