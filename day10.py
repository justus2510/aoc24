with open("input.txt", "r") as f:
    inp = f.read().strip()

lines = inp.splitlines()
w, h = len(lines[0]), len(lines)
map_ = {}
heads = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        map_[(x, y)] = int(c)
        if c == "0":
            heads.append((x, y))

def rec(pos, reached9s, part):
    if map_[pos] == 9:
        if part == 1 and pos in reached9s:
            return 0
        else:
            reached9s.add(pos)
            return 1
    ns = [
        (pos[0] + 1, pos[1]),
        (pos[0],     pos[1] + 1),
        (pos[0] - 1, pos[1]),
        (pos[0],     pos[1] - 1),
    ]
    return sum(rec(n, reached9s, part) for n in ns if n in map_ and map_[n] == map_[pos]+1)

[print(sum(rec(h, set(), p) for h in heads)) for p in (1, 2)]
