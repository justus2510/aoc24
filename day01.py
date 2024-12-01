from collections import Counter
from operator import sub

with open("input.txt", "r") as f:
    inp = f.read()

left, right = [], []
for line in inp.splitlines():
    split = line.split()
    left.append(int(split[0]))
    right.append(int(split[1]))
left.sort()
right.sort()
dist = sum(abs(sub(*x)) for x in zip(left, right))
print(dist)

count = Counter(right)
score = sum(x * count[x] for x in left)
print(score)
