with open("input.txt", "r") as f:
    inp = f.read()

def run(res, operands, part):
    if res <= 0:
        return False
    
    if len(operands) == 1:
        return res == operands[0]

    m = False
    c = False
    p = False
    
    if res % operands[-1] == 0:
        m = run(res // operands[-1], operands[:-1], part)
    
    if part == 2 and not m and str(res).endswith(str(operands[-1])) and len(str(res)) > len(str(operands[-1])):
        c = run(int(str(res)[:-len(str(operands[-1]))]), operands[:-1], part)
        
    if not m and not c:
        p = run(res - operands[-1], operands[:-1], part)
        
    return m or c or p

part1 = 0
part2 = 0
for line in inp.splitlines():
    res, operands = line.split(":")
    res = int(res)
    operands = [int(x) for x in operands.split()]
    part1 += res if run(res, operands, 1) else 0  
    part2 += res if run(res, operands, 2) else 0

print(part1)
print(part2)
