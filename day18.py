with open("input.txt", "r") as f:
    inp = f.read().strip()

w, h = 71, 71
lines = inp.splitlines()
start_pos = (0, 0)
end_pos = (w-1, h-1)

def dikstra(corrupted):
    cost = {start_pos: 0}
    open_ = set([start_pos])
    closed = set()
    while open_:
        curr = None
        for p in open_:
            if curr is None or cost[p] < cost[curr]:
                curr = p
        if curr == end_pos:
            break
        open_.remove(curr)
        closed.add(curr)

        ns = (
            ((curr[0] + 1, curr[1]), cost[curr] + 1),
            ((curr[0] - 1, curr[1]), cost[curr] + 1),
            ((curr[0], curr[1] + 1), cost[curr] + 1),
            ((curr[0], curr[1] - 1), cost[curr] + 1),
        )
        
        for next_pos, next_cost in ns:
            if next_pos in closed: continue
            if next_pos in corrupted: continue
            if next_pos[0] < 0 or next_pos[0] >= w: continue
            if next_pos[1] < 0 or next_pos[1] >= h: continue

            if next_cost < cost.get(next_pos, float("inf")):
                cost[next_pos] = next_cost
                open_.add(next_pos)

    return cost.get(end_pos, None)

corrupted = set()
for i in range(1024):
    corrupted.add(tuple(map(int, lines[i].split(","))))
print(dikstra(corrupted))

for i in range(1024, len(lines)):
    corrupted.add(tuple(map(int, lines[i].split(","))))
    if dikstra(corrupted) is None:
        print(lines[i])
        break
