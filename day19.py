from functools import cache

with open("input.txt", "r") as f:
    inp = f.read().strip()

lines = inp.splitlines()
patterns = lines[0].split(", ")
designs = lines[2:]

@cache
def solve(d):
    if d == "":
        return 1
    possib = 0
    for p in patterns:
        if d.startswith(p):
            possib += solve(d[len(p):])
    return possib

print(sum(solve(d) > 0 for d in designs))
print(sum(solve(d) for d in designs))
