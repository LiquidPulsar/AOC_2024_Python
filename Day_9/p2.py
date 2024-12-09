from collections import deque
from pathlib import Path

HOME = Path(__file__).parent


File = tuple[int, int] # id, size
# stack of free spaces, stack of files
# list of done (optimise out by calc on the fly)

filesys = []

# hack to make length even
m = map(int,Path(HOME/"input.txt").read_text()+"0")
for idx,(file,free) in enumerate(zip(m,m)):
    filesys.extend(((idx, file), free))
filesys.pop() # remove dummy 0

for i in range(len(filesys)-1,-1,-1):
    if isinstance(filesys[i], int):
        continue
    _,length = fi = filesys[i]
    for j,f in enumerate(filesys[:i]):
        if isinstance(f, tuple):
            continue
        if f == length:
            filesys[i] = length
            filesys[j] = fi
            break
        elif f > length:
            filesys[i] = length
            filesys[j] -= length
            filesys.insert(j,fi)
            break

# print(filesys)

total = ofs = 0
for d in filesys:
    if isinstance(d, int):
        ofs += d
    else:
        idx,length = d
        total += idx * sum(range(ofs,ofs+length))
        ofs += length
print(total)