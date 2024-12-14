import re
from math import floor
import itertools

with open("input.txt", "r") as f:
    inp = f.read().strip()

w, h  = 101, 103
robots = []
for line in inp.splitlines():
    ns = [int(x) for x in re.findall(r"-?\d+", line)]
    robots.append(ns)

for i in itertools.count(start=1):
    if i == 101:
        quad = [0]*4
        for r in robots:
            x, y = r[0], r[1]
            if x < floor(w/2) and y < floor(h/2):
                quad[0] += 1
            elif x > floor(w/2) and y < floor(h/2):
                quad[1] += 1
            elif x < floor(w/2) and y > floor(h/2):
                quad[2] += 1
            elif x > floor(w/2) and y > floor(h/2):
                quad[3] += 1
        product = 1
        for c in quad:
            product *= c
        print(product)

    m = bytearray(b"." * (w*h))
    for r in robots:
        r[0] = (r[0] + r[2]) % w
        r[1] = (r[1] + r[3]) % h
        m[r[1]*w + r[0]] = ord("*")

    if b"*"*10 in m:
        assert i > 101
        print(i)
        break
