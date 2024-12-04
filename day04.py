import re

with open("input.txt", "r") as f:
    inp = f.read()

def search(p):
    p = re.compile(p, re.DOTALL)
    count = 0
    at = inp
    while at != "":
        if p.match(at):
            count += 1
        at = at[1:]
    return count

linelen = inp.find("\n")

patterns = [
    r"XMAS",
    r"SAMX",
    r"X.{LEN}M.{LEN}A.{LEN}S".replace("LEN", str(linelen-1)),
    r"S.{LEN}A.{LEN}M.{LEN}X".replace("LEN", str(linelen-1)),
    r"X.{LEN}M.{LEN}A.{LEN}S".replace("LEN", str(linelen)),
    r"S.{LEN}A.{LEN}M.{LEN}X".replace("LEN", str(linelen)),
    r"X.{LEN}M.{LEN}A.{LEN}S".replace("LEN", str(linelen+1)),
    r"S.{LEN}A.{LEN}M.{LEN}X".replace("LEN", str(linelen+1)),
]
print(sum(search(p) for p in patterns))

patterns = [
    r"M.S.{LEN}.A..{LEN}M.S".replace("LEN", str(linelen-2)),
    r"M.M.{LEN}.A..{LEN}S.S".replace("LEN", str(linelen-2)),
    r"S.M.{LEN}.A..{LEN}S.M".replace("LEN", str(linelen-2)),
    r"S.S.{LEN}.A..{LEN}M.M".replace("LEN", str(linelen-2)),
]
print(sum(search(p) for p in patterns))
