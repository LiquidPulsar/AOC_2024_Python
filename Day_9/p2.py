from pathlib import Path
from heapq import heappop, heappush

HOME = Path(__file__).parent

# from time import perf_counter_ns

# tic = perf_counter_ns()

# ofs, size, id
filesys: list[tuple[int, int, int]] = []


def range_sum(start: int, end: int) -> int:
    return start * end + (end * (end - 1)) // 2

# hack to make length even
m = map(int, Path(HOME / "input.txt").read_text() + "0")
freemap: tuple[list[int], ...] = tuple(([] for _ in range(10)))
ofs = 0
for idx, (file, free) in enumerate(zip(m, m)):
    filesys.append((ofs, file, idx))
    ofs += file
    if free:
        heappush(freemap[free], ofs)
        ofs += free

total = 0
for ofs, length, id_ in reversed(filesys):
    f, space = min(
        ((f, i) for i in range(length, 10) if (f := freemap[i]) and f[0] < ofs),
        default=(None, 0),
    )
    if f:
        loc = heappop(f)
        # print("Found space for", id_, length, space, loc)
        total += id_ * range_sum(loc, length)
        if space > length:
            heappush(freemap[space - length], loc + length)
    else:
        # print("No space for", id_, length, ofs)
        total += id_ * range_sum(ofs, length)

print(total)
# print((perf_counter_ns() - tic) / 1e6, "ms")
