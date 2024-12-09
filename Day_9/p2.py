from pathlib import Path
from heapq import heappop, heappush

HOME = Path(__file__).parent


File = tuple[int, int, int]  # id, size, ofs

filesys: list[File] = []

# hack to make length even
m = map(int, Path(HOME / "input.txt").read_text() + "0")
freemap: dict[int, list[int]] = {k: [] for k in range(1, 10)}
ofs = 0
for idx, (file, free) in enumerate(zip(m, m)):
    filesys.append((idx, file, ofs))
    ofs += file
    if free:
        heappush(freemap[free], ofs)
        ofs += free

total = 0
for id_, length, ofs in reversed(filesys):
    # index 0 is heapmin
    loc, space = min(
        (
            (frees[0], space)
            for space, frees in freemap.items()
            if space >= length and frees
        ),
        default=(None, None),
    )
    if space is not None:
        assert loc is not None  # satisfy type checker
        # print("Found space for", id_, length, space, loc)
        total += id_ * sum(range(loc, loc + length))
        heappop(freemap[space])
        if space > length:
            heappush(freemap[space - length], loc + length)
    else:
        # print("No space for", id_, length, ofs)
        total += id_ * sum(range(ofs, ofs+length))
print(total)
