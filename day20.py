with open("input.txt", "r") as f:
    inp = f.read().strip()

lines = inp.splitlines()
grid = {}
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        p = (x, y)
        if c == "S":
            start_pos = p
            c = "."
        elif c == "E":
            end_pos = p
            c = "."
        grid[p] = c

path = [start_pos]
while path[-1] != end_pos:
    at = path[-1]
    ns = (
        (at[0] + 1, at[1]),
        (at[0] - 1, at[1]),
        (at[0], at[1] + 1),
        (at[0], at[1] - 1),
    )
    for n in ns:
        if grid.get(n, "") == "." and (len(path) == 1 or n != path[-2]):
            path.append(n)
            break
path = {p: i for i, p in enumerate(path)}

def cheat(maxlen):
    count = 0
    for pos0, i in path.items():
        for x in range(-maxlen, maxlen+1):
            for y in range(-maxlen, maxlen+1):
                pos1 = (pos0[0] + x, pos0[1] + y)
                j = path.get(pos1, None)
                if j is None:
                    continue
                if i >= j:
                    continue
                dist = abs(pos0[0] - pos1[0]) + abs(pos0[1] - pos1[1])
                if dist > maxlen:
                    continue

                saved = j - i - dist
                if saved >= 100:
                    count += 1
    
    return count

print(cheat(2))
print(cheat(20))
