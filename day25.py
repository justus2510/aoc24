with open("input.txt", "r") as f:
    inp = f.read().strip()

keys = []
locks = []
for s in inp.split("\n\n"):
    lines = s.splitlines()
    if "w" not in globals():
        w, h = len(lines[0]), len(lines)
    
    grid = set()
    kind = "lock" if all(c == "#" for c in lines[0]) else "key"
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                grid.add((x, y))
    
    if all(c == "#" for c in lines[0]):
        locks.append(grid)
    else:
        keys.append(grid)

result = 0
for key in keys:
    for lock in locks:
        if len(key | lock) == len(key) + len(lock):
            result += 1
print(result)
