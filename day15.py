with open("input.txt", "r") as f:
    inp = f.read().strip()

mapstr, moves = inp.split("\n\n")
moves = moves.replace("\n", "")
lines = mapstr.splitlines()

w, h = len(lines[0]), len(lines)
map_ = {}
pos = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ".":
            continue
        elif c == "@":
            pos = (x, y)
            map_[(x, y)] = c
        elif c in "O#":
            map_[(x, y)] = c
        else:
            assert False

def add_dir(p, d):
    if d == "^":
        return (p[0], p[1] - 1)
    if d == "v":
        return (p[0], p[1] + 1)
    if d == "<":
        return (p[0] - 1, p[1])
    if d == ">":
        return (p[0] + 1, p[1])
    assert False

def move(p, d):
    next_p = add_dir(p, d)
    if next_p in map_:
        if map_[next_p] == "#":
            return False
        elif map_[next_p] == "O":
            if not move(next_p, d):
                return False
        else:
            assert False

    tmp = map_.pop(p)
    map_[next_p] = tmp
    return True
    
for d in moves:
    if move(pos, d):
        pos = add_dir(pos, d)

print(sum(100*p[1] + p[0] for p, c in map_.items() if c == "O"))

wide_lines = []
for l in lines:
    wide_lines.append(l.replace(".", "..").replace("#", "##").replace("@", "@.").replace("O", "[]"))

w, h = len(wide_lines[0]), len(wide_lines)
map_ = {}
pos = None
box_id_counter = 0
for y, line in enumerate(wide_lines):
    for x, c in enumerate(line):
        if c == ".":
            continue
        elif c == "@":
            pos = (x, y)
            map_[(x, y)] = c
        elif c in "O#":
            map_[(x, y)] = c
        elif c == "[":
            continue
        elif c == "]":
            ident = "O" + str(box_id_counter)
            map_[(x-1, y)] = ident
            map_[(x, y)] = ident
            box_id_counter += 1
        else:
            assert False

def move_wide_box(p, d):
    if map_.get(l := add_dir(p, "<"), "") == map_[p]:
        ps = [l, p]
    else:
        ps = [add_dir(p, ">"), p]
        assert map_.get(ps[0], "") == map_[p]
    
    can_move = []
    for p in ps:
        next_p = add_dir(p, d)
        next_thing = map_.get(next_p, None)
        if next_thing is None:
            res = True
        elif next_thing == "#":
            res = False
        elif next_thing.startswith("O"):
            if next_p in ps:
                res = True
            else:
                res = move_wide_box(next_p, d)
        else:
            assert False
        can_move.append(res)

    if all(can_move):
        for p in ps:
            tmp = map_.pop(p)
            map_[add_dir(p, d)] = tmp
        return True
    else:
        return False

for d in moves:
    next_p = add_dir(pos, d)
    thing = map_.get(next_p, "")
    if thing == "":
        del map_[pos]
        map_[next_p] = "@"
        pos = next_p
    elif thing == "#":
        pass
    elif thing.startswith("O"):
        copy = map_.copy()
        moved = move_wide_box(next_p, d)
        if moved:
            del map_[pos]
            map_[next_p] = "@"
            pos = next_p
        else:
            map_ = copy
    else:
        assert False

print(sum(100*p[1] + p[0] for p, c in map_.items() if c.startswith("O") and map_.get(add_dir(p, "<"), "") != c))
