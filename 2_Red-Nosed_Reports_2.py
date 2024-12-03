"""
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
"""

safe_reports = 0


def is_decreasing(r):
    cnt = 0
    for i in range(1, len(r)):
        if int(r[i - 1]) > int(r[i]):
            cnt += 1
            if cnt > 1:
                return True
    return False


def is_safe(r, mult):
    dampener = True
    i = 1
    ln = len(r)
    while i < ln:
        diff = int(r[i]) - int(r[i - 1])
        if diff * mult not in range(1, 4):
            if not dampener:
                return False
            dampener = False
            if i == 1:
                diff2 = int(r[i + 1]) - int(r[i])
                diff3 = int(r[i + 1]) - int(r[i - 1])
                if diff2 * mult in range(1, 4) or diff3 * mult in range(1, 4):
                    i += 2
                    continue
            elif i == ln - 1:
                break
            else:
                diff2 = int(r[i + 1]) - int(r[i - 1])
                diff3 = int(r[i]) - int(r[i - 2])
                diff4 = int(r[i + 1]) - int(r[i])
                if diff2 * mult in range(1, 4) or (
                    diff3 * mult in range(1, 4) and diff4 * mult in range(1, 4)
                ):
                    i += 2
                    continue
            return False

        i += 1
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
