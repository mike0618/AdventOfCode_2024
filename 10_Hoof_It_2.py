"""
hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1 at each step
score is the number of 9-height positions reachable from that trailhead via a hiking trail
What is the sum of the scores of all trailheads on your topographic map?
"""

with open("10.txt") as f:
    topomap = f.readlines()

total_score = 0
L = len(topomap)
R = range(L)
STEPS = (0, 1), (1, 0), (0, -1), (-1, 0)  # orthogonal directions


def hiking(pos):
    count = 0
    n = topomap[pos[0]][pos[1]]
    if n == "9":
        count += 1
        return count
    for step_y, step_x in STEPS:
        y, x = pos[0] + step_y, pos[1] + step_x
        if y not in R or x not in R:
            continue
        next = topomap[y][x]
        if int(next) - int(n) == 1:
            count += hiking((y, x))  # recursively create "branches"
    return count


for y, row in enumerate(topomap):
    for x, n in enumerate(row[:-1]):  # the last symbol is \n
        if n != "0":
            continue
        total_score += hiking((y, x))

print(total_score)
