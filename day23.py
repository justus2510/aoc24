from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.read().strip()

mapping = defaultdict(set)
names = set()
conns = set()
for line in inp.splitlines():
    a, b = line.split("-")
    conns.add(tuple(sorted((a, b))))
    names.add(a)
    names.add(b)
    mapping[a].add(b)
    mapping[b].add(a)

for name in names:
    added = set()
    for conn in conns:
        if all(name in mapping[c] for c in conn):
            added.add(tuple(sorted(conn + (name,))))
    conns |= added

print(sum(1 for c in conns if len(c) == 3 and any(n[0] == "t" for n in c)))
print(",".join(sorted(max(conns, key=len))))
