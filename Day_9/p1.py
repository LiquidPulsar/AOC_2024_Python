from collections import deque
from pathlib import Path

HOME = Path(__file__).parent


File = tuple[int, int] # id, size
# stack of free spaces, stack of files
# list of done (optimise out by calc on the fly)

filesys = deque()
done = []

# hack to make length even
m = map(int,Path(HOME/"input.txt").read_text()+"0")
for idx,(file,free) in enumerate(zip(m,m)):
    filesys.append((idx,file))
    filesys.append(free)

print(filesys)
filesys.pop() # remove dummy 0

while filesys:
    curr = filesys.pop()
    if isinstance(curr, int): continue

    idx,length = curr
    while filesys:
        l = filesys.popleft()
        if isinstance(l, int):
            if l >= length:
                if l > length: filesys.appendleft(l-length)
                done.append((idx,length))
                length = 0
                break
            else:
                done.append((idx,l))
                length -= l
        else:
            done.append(l)
    if length > 0: # unfinished
        done.append((idx,length))

print(done)

total = ofs = 0
for idx,length in done:
    total += idx * sum(range(ofs,ofs+length))
    ofs += length
print(total)