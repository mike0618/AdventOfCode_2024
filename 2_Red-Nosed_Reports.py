"""
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
"""

safe_reports = 0


def is_decreasing(r):
    cnt = 0
    for i in range(1, len(r)):
        if r[i - 1] > r[i]:
            cnt += 1
            if cnt > 1:
                return True
    return False


def is_safe(r, mult):
    for i in range(1, len(r)):
        diff = int(r[i]) - int(r[i - 1])
        if diff * mult not in range(1, 4):
            return False
    return True


with open("2.txt") as f:
    for r in f:
        r = r.split()
        mult = 1  # if increasing
        if is_decreasing(r):
            mult = -1  # if decreasing
        if is_safe(r, mult):
            safe_reports += 1

print(safe_reports)
