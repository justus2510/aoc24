import re

with open("input.txt", "r") as f:
    inp = f.read().strip()

nums = [int(n) for n in re.findall(r"\d+", inp)]
prog = nums[3:]

def run(a_reg=None):
    ip = 0
    regs = dict(zip("ABC", nums[:3]))
    output = []
    if a_reg is not None:
        regs["A"] = a_reg
    
    while ip < len(prog):
        op = prog[ip]
        literal = prog[ip+1]
        if literal <= 3:
            combo = literal
        elif literal == 4:
            combo = regs["A"] 
        elif literal == 5:
            combo = regs["B"]
        elif literal == 6:
            combo = regs["C"]
        else:
            assert False

        if op == 0:
            regs["A"] = regs["A"] // 2**combo
        elif op == 1:
            regs["B"] = regs["B"] ^ literal
        elif op == 2:
            regs["B"] = combo % 8
        elif op == 3:
            if regs["A"] != 0:
                ip = literal - 2
        elif op == 4:
            regs["B"] = regs["B"] ^ regs["C"]
        elif op == 5:
            output.append(combo % 8)
        elif op == 6:
            regs["B"] = regs["A"] // 2**combo
        elif op == 7:
            regs["C"] = regs["A"] // 2**combo
        else:
            assert False

        ip += 2
    
    return output

print(",".join(map(str, run())))

possib = []
for a in range(1024):
    out = run(a)
    a = format(a, "010b")
    possib.append((a, out[0]))

res = []
def solve(ns, result_bits):
    if len(ns) == 0:
        n = 0
        for i, b in enumerate(reversed(result_bits)):
            if b == "1":
                n += 2**i
            pass
        res.append(n)
        return

    for bs, n in possib:
        if n == ns[0] and (result_bits == "" or bs[3:] == result_bits[:7]):
            solve(ns[1:], bs[:3] + result_bits if result_bits != "" else bs)

solve(prog, "")
print(min(res))
