with open("input.txt", "r") as f:
    inp = f.read().strip()

wires = {}
for line in inp.split("\n\n")[0].splitlines():
    wire, val = line.split(": ")
    wires[wire] = int(val)

mapping = {}
ops = []
for line in inp.split("\n\n")[1].splitlines():
    ops.append(line.replace("->", "").split())
    mapping[ops[-1][3]] = ops[-1][:3]

def run(name):
    if "x" in name or "y" in name:
        return wires[name]
    left, op, right = mapping[name][0], mapping[name][1], mapping[name][2]
    left = run(left)
    right = run(right)
    if op == "AND":
        return left & right
    elif op == "OR":
        return left | right
    elif op == "XOR":
        return left ^ right
    else:
        assert False

num = 0
for i in range(0, 46):
    num |= run("z" + str(i).rjust(2, "0")) << i
print(num)

"""
for op in ops:
    if op[3][0] == "z" and op[1] != "XOR" and op[3] != "z45":
        print("NEED XOR", op[:3], op[3])
"""

"""
for j in range(45):
    wires["x" + str(j).rjust(2, "0")] = 1
    wires["y" + str(j).rjust(2, "0")] = 1

    num = 0
    for i in range(0, 46):
        zname = "z" + str(i).rjust(2, "0")
        bit = run(zname)
        num |= bit << i
    if num != (2**j)*2:
        print(j, num, (2**j)*2)

    wires["x" + str(j).rjust(2, "0")] = 0
    wires["y" + str(j).rjust(2, "0")] = 0
"""

"""
i figured these out manually from the information that is produced if you uncomment the two blocks
above. in the NEED XOR case, the gate that produces that particular z output bit must be swapped,
because a binary adder *must* always xor in the final step for each bit (except the last since there
is only a carry bit and no inputs). so, it is simple to just ctrl+f in the input file to figure
things out. this gives 6 wires. for the last two, i just looked at which 2 bits produce an incorrect
result, and then i manually reverse-engineered where the mistake for that particular output bit must
be. binary adders are simple enough for this to feasible.

the final swaps:
    qdg <-> z12 vvf <-> z19 nvh <-> z37 dck <-> fgn
"""

print(",".join(sorted(["qdg", "z12", "vvf", "z19", "nvh", "z37", "dck", "fgn"])))
