with open("input.txt", "r") as f:
    inp = f.read().strip()

lines = inp.splitlines()
w, h = len(lines[0]), len(lines)
map_ = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            start_pos = (x, y, 1, 0)
            c = "."
        elif c == "E":
            end_pos = (x, y)
            c = "."
        map_[(x, y)] = c

cost = {start_pos: 0}
prev = {}
open_ = set([start_pos])
closed = set()
while open_:
    curr = None
    for p in open_:
        if curr is None or cost[p] < cost[curr]:
            curr = p
    open_.remove(curr)
    closed.add(curr)

    ns = (
        ((curr[0] + curr[2], curr[1] + curr[3], curr[2], curr[3]), cost[curr] + 1),
        ((curr[0] - curr[3], curr[1] + curr[2], -curr[3], curr[2]), cost[curr] + 1001),
        ((curr[0] + curr[3], curr[1] - curr[2], curr[3], -curr[2]), cost[curr] + 1001),
    )
    
    for next_pos, next_cost in ns:
        if next_pos in closed or map_[(next_pos[0], next_pos[1])] != ".":
            continue

        if next_cost <= cost.get(next_pos, float("inf")):
            if next_cost == cost.get(next_pos, float("inf")) and next_pos in prev:
                prev[next_pos].append(curr)
            else:
                prev[next_pos] = [curr]
            cost[next_pos] = next_cost
            open_.add(next_pos)

best_c = float("inf")
for p, c in cost.items():
    if (p[0], p[1]) == end_pos:
        if c < best_c:
            best_c = c
print(best_c)

tiles = set()
for pos, cost in cost.items():
    if (pos[0], pos[1]) == end_pos and cost == best_c:
        def dfs(p):
            tiles.add((p[0], p[1]))
            if p not in prev:
                return
            for child in prev[p]:
                dfs(child)
        dfs(pos)
print(len(tiles))
