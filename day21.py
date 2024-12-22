from collections import deque
import re
from functools import cache

with open("input.txt", "r") as f:
    inp = f.read().strip()

codes = inp.splitlines()

num_keypad = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    (1, 3): "0",
    (2, 3): "A",
}

dir_keypad = {
    (1, 0): "^",
    (2, 0): "A",
    (0, 1): "<",
    (1, 1): "v",
    (2, 1): ">",
}

def get_paths(pad, pos, dest):
    queue = deque([(pos, "")])
    visited = set()
    results = []
    while queue:
        curr_pos, curr_path = queue.popleft()
        if curr_pos == dest:
            curr_path += "A"
            results.append(curr_path)
            continue
        visited.add(curr_pos)
        ns = (
            ((curr_pos[0] + 1, curr_pos[1]), ">"),
            ((curr_pos[0] - 1, curr_pos[1]), "<"),
            ((curr_pos[0], curr_pos[1] + 1), "v"),
            ((curr_pos[0], curr_pos[1] - 1), "^"),
        )
        for n, d in ns:
            if n in pad and n not in visited:
                queue.append((n, curr_path + d))

    min_len = min(map(len, results))
    return [r for r in results if len(r) == min_len]

def generate_mapping(pad):
    mapping = {}
    for pos0, name0 in pad.items():
        for pos1, name1 in pad.items():
            paths = get_paths(pad, pos0, pos1)
            mapping[(name0, name1)] = paths
    return mapping

num_keypad_mapping = generate_mapping(num_keypad)
dir_keypad_mapping = generate_mapping(dir_keypad)

@cache
def rec(mapping, inp, depth, max_depth):
    mapping = {
        "num": num_keypad_mapping,
        "dir": dir_keypad_mapping,
    }[mapping]
    
    if depth == max_depth:
        return len(inp)
    
    at = "A"
    result = 0
    for digit in inp:
        lens = []
        for p in mapping[(at, digit)]:
            lens.append((p, rec("dir", p, depth + 1, max_depth)))
        result += min(lens, key=lambda x: x[1])[1]
        at = digit
    
    return result

for depth in (3, 26):
    result = 0
    for code in codes:
        count = rec("num", code, 0, depth)
        result += int("".join(re.findall(r"\d", code))) * count
    print(result)
