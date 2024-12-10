"""
If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward
How many distinct positions will the guard visit before leaving the mapped area?
"""

matrix = []
positions = set()
origin = 0, 0
directions = {0: (True, -1), 1: (False, 1), 2: (True, 1), 3: (False, -1)}
with open("6.txt") as f:
    for line in f:
        matrix.append(list(line.strip()))
END = len(matrix) - 1


def add_positions(p, n, d):
    v, dir = directions[d]
    r, c = p
    for i in range(n):
        if v:
            p = r + (i + 1) * dir, c
        else:
            p = r, c + (i + 1) * dir
        if matrix[p[0]][p[1]] == ".":
            matrix[p[0]][p[1]] = "#"
            if check(0, origin, True):
                positions.add(p)
            matrix[p[0]][p[1]] = "."


def go(current, seq, d, loop):
    r, c = current
    v, dir = directions[d]
    if "#" not in seq:
        if not loop:
            add_positions(current, len(seq), d)
        return False
    if dir == -1:
        seq = seq[::-1]
    g = seq.index("#")
    if not loop:
        add_positions(current, g, d)
    if v:
        p = r + g * dir, c
    else:
        p = r, c + g * dir
    return p


def main():
    global origin
    for i, row in enumerate(matrix):
        if "^" in row:
            origin = i, row.index("^")
            break
    check(0, origin)


def check(start: int, current, loop=False):
    appeared = []
    dirs = (0, 1, 2, 3)
    rotation = dirs[start:] + dirs[:start]
    while True:
        for d in rotation:
            r, c = current
            match d:
                case 0:  # up
                    seq = [row[c] for row in matrix][:r]
                case 1:  # right
                    seq = matrix[r][c + 1 :]
                case 2:  # down
                    seq = [row[c] for row in matrix][r + 1 :]
                case 3:  # left
                    seq = matrix[r][:c]
            current = go(current, seq, d, loop)
            if not current:
                return False
        if not loop:
            continue
        if (current, start) in appeared:
            return True
        appeared.append((current, start))


main()
print(len(positions))
