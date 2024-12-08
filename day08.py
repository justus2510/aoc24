from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.read()

lines = inp.splitlines()
w, h = len(lines[0]), len(lines)
map_ = defaultdict(lambda: [])
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            map_[c].append((x, y))

def in_map(p):
    return 0 <= p[0] < w and 0 <= p[1] < h

def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

part1 = set()
part2 = set()
for freq in map_.keys():
    for pos0 in map_[freq]:
        for pos1 in map_[freq]:
            if pos0 == pos1:
                continue
            dist = vsub(pos1, pos0)
            for a in [vsub(pos0, dist), vadd(pos1, dist)]:
                if in_map(a):
                    part1.add(a)
            p = pos0
            while in_map(p):
                part2.add(p)
                p = vsub(p, dist)
            p = pos1
            while in_map(p):
                part2.add(p)
                p = vadd(p, dist)

print(len(part1))
print(len(part2))

