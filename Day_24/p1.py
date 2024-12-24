from pathlib import Path

HOME = Path(__file__).parent

vals, conns = (HOME / "input.txt").read_text().split("\n\n")
state = {}
for line in vals.splitlines():
    key, val = line.split(": ")
    state[key] = int(val)

sources = {}
for line in conns.splitlines():
    l, op, r, _, out = line.split()
    sources[out] = (l, op, r)


def get_val(x):
    if x in state:
        return state[x]
    if x in sources:
        l, op, r = sources[x]
        l = state[l] = get_val(l)
        r = state[r] = get_val(r)
        if op == "AND":
            return l & r
        if op == "OR":
            return l | r
        if op == "XOR":
            return l ^ r
    raise ValueError(f"Unknown key: {x}")


digits = []
dig = 0
out = 0
while (key := f"z{dig:02d}") in state or key in sources:
    v = get_val(key)
    out += v << dig
    digits.append(v)
    dig += 1

print(digits, out)
