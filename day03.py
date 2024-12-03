from operator import mul
import re

with open("input.txt", "r") as f:
    inp = f.read()

def run(part):
    result = 0
    state = "do()"
    other = {"do()": "don't()", "don't()": "do()"}
    at = inp
    while at != "":
        if at.startswith("do()") and state == "don't()":
            state = "do()"
        elif at.startswith("don't()") and state == "do()":
            state = "don't()" if part == 2 else state
        elif m := re.match(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", at):
            result += mul(*map(int, m.groups())) if state == "do()" else 0
        at = at[1:]
    return result

print(run(1))
print(run(2))
