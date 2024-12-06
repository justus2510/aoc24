with open("input.txt", "r") as f:
    inp = f.read()

world = {}
guard_pos = None
for y, row in enumerate(inp.splitlines()):
    for x, c in enumerate(row):
        if c == "^":
            assert guard_pos is None
            guard_pos = (x, y)
            c = "."
        world[(x, y)] = c

def run(world, guard_dir, path, cache):
    path = path.copy()
    while True:
        next_pos = (path[-1][0] + guard_dir[0], path[-1][1] + guard_dir[1])
        if next_pos not in world:
            return path
        elif (next_pos, guard_dir) in cache:
            return None
        elif world[next_pos] == ".":
            path.append(next_pos)
            cache.add((next_pos, guard_dir))
        elif world[next_pos] == "#":
            guard_dir = (-guard_dir[1], guard_dir[0])
        else:
            assert False

path = run(world, (0, -1), [guard_pos], {(guard_pos, (0, -1))})
print(len(set(path)))

obstacles = set()
for i, p in enumerate(path[:-1]):
    # this is dumb, there is no need to always test the path from the beginning
    # but it's fast enough so who cares
    n = path[i+1]
    assert world[n] != "#"
    modified_world = world.copy()
    modified_world[n] = "#"
    res = run(modified_world, (0, -1), [guard_pos], {(guard_pos, (0, -1))})
    if res is None:
        obstacles.add(n)
print(len(obstacles))
