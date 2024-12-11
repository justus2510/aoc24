with open("input.txt", "r") as f:
    inp = f.read().strip()

def run(gens):
    stones = {int(s): 1 for s in inp.split()}
    for gen in range(gens):
        new_stones = {}
        for s, n in stones.items():
            if s == 0:
                children = [1]
            elif len(sstr := str(s)) % 2 == 0:
                children = [int(sstr[:len(sstr)//2]), int(sstr[len(sstr)//2:])]
            else:
                children = [s * 2024]
            for c in children:
                new_stones[c] = new_stones.get(c, 0) + n
        stones = new_stones
    print(sum(stones.values()))

run(25)
run(75)
