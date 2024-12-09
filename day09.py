from collections import deque
import heapq

with open("input.txt", "r") as f:
    inp = f.read().strip()

drive = []
space_idxs = deque()
for i, c in enumerate(inp):
    c = int(c)
    if i % 2 == 0:
        drive.extend([i//2] * c)
    else:
        space_idxs.extend(range(len(drive), len(drive) + c))
        drive.extend(["."] * c)

while len(space_idxs) > 0:
    while True:
        file = drive.pop()
        if file != ".":
            break
    idx = space_idxs.popleft()
    if idx >= len(drive):
        drive.append(file)
        break
    drive[idx] = file
print(sum(i*drive[i] for i in range(len(drive))))

files = []
spaces = {i: [] for i in range(1, 10)}
idx_at = 0
for i, c in enumerate(inp):
    c = int(c)
    if i % 2 == 0:
        files.append({"id": i//2, "size": c, "idx": idx_at})
    else:
        if c != 0:
            heapq.heappush(spaces[c], idx_at)
    idx_at += c

for file in reversed(files):
    space_size = None
    for i in range(file["size"], 10):
        if len(spaces[i]) > 0 and (space_size is None or spaces[i][0] < spaces[space_size][0]) and spaces[i][0] < file["idx"]:
            space_size = i
    if space_size is None:
        continue
    
    idx = heapq.heappop(spaces[space_size])
    new_space_idx = idx + file["size"]
    new_space_size = space_size - file["size"]
    file["idx"] = idx
    if new_space_size != 0:
        heapq.heappush(spaces[new_space_size], new_space_idx)

checksum = 0
for file in files:
    for i in range(file["size"]):
        checksum += file["id"] * (file["idx"] + i)
print(checksum)
