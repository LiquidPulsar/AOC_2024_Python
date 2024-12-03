from pathlib import Path
import re


HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    active = True
    total = 0
    for do,dont,a,b in re.findall(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", f.read()):
        if do:
            active = True
        elif dont:
            active = False
        elif active:
            total += int(a) * int(b)
    print(total)