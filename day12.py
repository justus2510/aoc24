with open("input.txt", "r") as f:
    inp = f.read()

lines = inp.splitlines()
w, h = len(lines[0]), len(lines)
map_ = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        map_[(x, y)] = c

regions = []
for p in map_.keys():
    if any(p in r for r in regions):
        continue
    r = set()
    def dfs(letter, p):
        if p not in map_ or p in r or map_[p] != letter:
            return
        r.add(p)
        dfs(letter, (p[0] + 1, p[1]))
        dfs(letter, (p[0] - 1, p[1]))
        dfs(letter, (p[0], p[1] + 1))
        dfs(letter, (p[0], p[1] - 1))
    dfs(map_[p], p)
    regions.append(r)

part1 = 0
part2 = 0
for r in regions:
    area = len(r)
    perimeter = 0
    shape = []
    sides = 0
    for p in r:
        ns = [
            (p[0] - 1, p[1]),
            (p[0] + 1, p[1]),
            (p[0], p[1] - 1),
            (p[0], p[1] + 1),
        ]
        for n in ns:
            if n not in r:
                perimeter += 1
                if n[0] == p[0]:
                    if n[1] > p[1]:
                        shape.append((n, (n[0] + 1, n[1]), +1))
                    else:
                        shape.append((p, (p[0] + 1, p[1]), -1))
                elif n[1] == p[1]:
                    if n[0] > p[0]:
                        shape.append((n, (n[0], n[1] + 1), +1))
                    else:
                        shape.append((p, (p[0], p[1] + 1), -1))
                else:
                    assert False
        
    i = 0
    while i < len(shape):
        l0 = shape[i]
        for j in range(i+1, len(shape)):
            if i == j:
                continue

            l1 = shape[j]
            if len({l0[0][0], l0[1][0], l1[0][0], l1[1][0]}) == 1 and len({l0[0][1], l0[1][1], l1[0][1], l1[1][1]}) <= 3 and l0[2] == l1[2]:
                x = l0[0][0]
                normal = l0[2]
                miny = min(l0[0][1], l0[1][1], l1[0][1], l1[1][1])
                maxy = max(l0[0][1], l0[1][1], l1[0][1], l1[1][1])
                shape[i] = ((x, miny), (x, maxy), normal)
                del shape[j]
                break
            elif len({l0[0][1], l0[1][1], l1[0][1], l1[1][1]}) == 1 and len({l0[0][0], l0[1][0], l1[0][0], l1[1][0]}) <= 3 and l0[2] == l1[2]:
                y = l0[0][1]
                normal = l0[2]
                minx = min(l0[0][0], l0[1][0], l1[0][0], l1[1][0])
                maxx = max(l0[0][0], l0[1][0], l1[0][0], l1[1][0])
                shape[i] = ((minx, y), (maxx, y), normal)
                del shape[j]
                break
        else:
            i += 1

    part1 += area * perimeter
    part2 += area * len(shape)

print(part1)
print(part2)
