from collections import Counter

with open("input.txt", "r") as f:
    inp = f.read().strip()

nums = [[int(n)] for n in inp.splitlines()]

def rng(seed):
    n0 = seed
    n1 = n0 * 64
    n2 = n1 ^ n0
    n3 = n2 % 16777216
    n4 = n3 // 32
    n5 = n4 ^ n3
    n6 = n5 % 16777216
    n7 = n6 * 2048
    n8 = n7 ^ n6
    n9 = n8 % 16777216
    return n9

for ns in nums:
    for _ in range(2000):
        ns.append(rng(ns[-1]))

print(sum(ns[-1] for ns in nums))

bananas = Counter()
for ns in nums:
    seen = set()
    for i in range(len(ns)):
        ns[i] %= 10
        if i >= 4:
            key = (ns[i-3] - ns[i-4], ns[i-2] - ns[i-3], ns[i-1] - ns[i-2], ns[i-0] - ns[i-1])
            if key not in seen:
                seen.add(key)
                bananas[key] += ns[i]

print(max(bananas.values()))
