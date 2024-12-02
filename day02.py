with open("input.txt", "r") as f:
    inp = f.read()

reports = [list(map(int, line.split())) for line in inp.splitlines()]

def is_safe(report):
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False

    for i in range(1, len(report)):
        if not (1 <= abs(report[i] - report[i-1]) <= 3):
            return False

    return True

unsafe_reports = []
safe = 0
for report in reports:
    if is_safe(report):
        safe += 1
    else:
        unsafe_reports.append(report)
print(safe)

for report in unsafe_reports:
    for i in range(len(report)):
        removed = report.copy()
        del removed[i]
        if is_safe(removed):
            safe += 1
            break
print(safe)

