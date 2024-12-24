from collections import defaultdict
from pathlib import Path

HOME = Path(__file__).parent

vals, conns = (HOME / "input.txt").read_text().split("\n\n")

names = {}
for line in conns.splitlines():
    l, op, r, _, out = line.split()
    if l > r:
        l, r = r, l
    names[l, op, r] = out

"""
Binary full adder:

A XOR B -> X
A AND B -> Y

C_in XOR X -> S
C_in AND X -> Z
Y OR Z -> C_out


-----

Lines in file:
numbers = 2*45 = 90
blank line = 1
gates for 1 half adder = 2
gates for 44 full adders = 45*5 = 225

Total = 313
Lines in file = 313

So the file contains no superfluous gates,
no obfuscation.
"""

# x y input gates are always correct

def which_gate(l, r, op) -> str | None:
    if l > r:
        l, r = r, l
    return names.get((l, op, r))


# The swaps are all very localised!
to_swap = set()
carry = None
for out in range(45):
    inp_and = which_gate(f"x{out:02d}", f"y{out:02d}", "AND")
    inp_xor = which_gate(f"x{out:02d}", f"y{out:02d}", "XOR")
    assert inp_and is not None
    assert inp_xor is not None

    if carry is not None:
        internal_and = which_gate(inp_xor, carry, "AND")
        if internal_and is None:
            to_swap |= {inp_xor, inp_and}
            inp_xor, inp_and = inp_and, inp_xor
            internal_and = which_gate(inp_xor, carry, "AND")
            assert internal_and is not None

        out_z = which_gate(inp_xor, carry, "XOR")

        if internal_and[0] == "z":
            to_swap |= {internal_and, out_z}
            internal_and, out_z = out_z, internal_and
        if inp_and[0] == "z":
            to_swap |= {inp_and, out_z}
            inp_and, out_z = out_z, inp_and
        if inp_xor[0] == "z":
            to_swap |= {inp_xor, out_z}
            inp_xor, out_z = out_z, inp_xor

        carry = which_gate(internal_and, inp_and, "OR")
        assert carry is not None
        if carry[0] == "z" and carry != "z45":
            to_swap |= {carry, out_z}
            carry, out_z = out_z, carry
    else:
        carry = inp_and

print(",".join(sorted(to_swap)))