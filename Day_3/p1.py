from pathlib import Path
import re


HOME = Path(__file__).parent

with open(HOME / "input.txt") as f:
    print(
        sum(
            int(a) * int(b)
            for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", f.read())
        )
    )
