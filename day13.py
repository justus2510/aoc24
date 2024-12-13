with open("input.txt", "r") as f:
    inp = f.read().strip()

parts = [0, 0]
for block in inp.split("\n\n"):
    parsed = []
    for line in block.splitlines():
        ns = []
        for c in "XY":
            i = line.index(c) + 2
            s = ""
            while i < len(line) and line[i].isdigit():
                s += line[i]
                i += 1
            ns.append(int(s))
        parsed.append(ns)

    for part in range(2):
        # quick and dirty manual gaussian elimination
        matrix = [
            [parsed[0][0], parsed[1][0], parsed[2][0] + 10000000000000*part],
            [parsed[0][1], parsed[1][1], parsed[2][1] + 10000000000000*part],
        ]
        for i in [2, 1, 0]:
            matrix[1][i] -= matrix[0][i] * (matrix[1][0] / matrix[0][0])
        for i in [0, 2, 1]:
            matrix[0][i] -= matrix[1][i] * (matrix[0][1] / matrix[1][1])
        for i in [2, 1, 0]:
            matrix[0][i] /= matrix[0][0]
        for i in [0, 2, 1]:
            matrix[1][i] /= matrix[1][1]
        a, b = round(matrix[0][-1]), round(matrix[1][-1])
        if abs(a - matrix[0][-1]) < 0.001 and abs(b - matrix[1][-1]) < 0.001:
            # check if there is an integer solution, seems to be good enough
            parts[part] += a*3 + b

[print(p) for p in parts]
