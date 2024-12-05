from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.read()

rules, updates = inp.split("\n\n")
rules = [[int(n) for n in r.split("|")] for r in rules.splitlines()]
updates = [[int(n) for n in u.split(",")] for u in updates.splitlines()]

before = defaultdict(set)
for r in rules:
    before[r[1]].add(r[0])

incorrect = []
correct = []
for u in updates:
    good = True
    for i in range(len(u)):
        for j in range(i+1, len(u)):
            if u[j] in before[u[i]]:
                good = False
    if good:
        correct.append(u)
    else:
        incorrect.append(u)
print(sum(u[len(u)//2] for u in correct))

for u in incorrect:
    i = 0
    while i < len(u):
        for j in range(i+1, len(u)):
            if u[j] in before[u[i]]:
                u.insert(i, u.pop(j))
                break
        else:
            i += 1
print(sum(u[len(u)//2] for u in incorrect))
