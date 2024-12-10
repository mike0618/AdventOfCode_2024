"""
If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward
How many distinct positions will the guard visit before leaving the mapped area?
"""

positions = set()
directions = {0: (True, -1), 1: (False, 1), 2: (True, 1), 3: (False, -1)}
with open("6.txt") as f:
    matrix = f.readlines()


def add_positions(r, c, n, vertical=False, dir=1):
    for i in range(n):
        if vertical:
            p = r + (i + 1) * dir, c
        else:
            p = r, c + (i + 1) * dir
        positions.add(p)


def go(current, seq, direction):
    r, c = current
    v, dir = direction
    if "#" not in seq:
        add_positions(r, c, len(seq), v, dir)
        return False
    if dir == -1:
        seq = seq[::-1]
    g = seq.index("#")
    add_positions(r, c, g, v, dir)
    if v:
        p = r + g * dir, c
    else:
        p = r, c + g * dir
    return p


def main():
    current = 0, 0
    for i, row in enumerate(matrix):
        if "^" in row:
            current = i, row.index("^")
            positions.add(current)
            break
    check(0, current)


def check(start: int, current):
    dirs = (0, 1, 2, 3)
    rotation = dirs[start:] + dirs[:start]
    while True:
        for d in rotation:
            r, c = current
            match d:
                case 0:
                    seq = [row[c] for row in matrix][:r]
                case 1:
                    seq = matrix[r][c + 1 :]
                case 2:
                    seq = [row[c] for row in matrix][r + 1 :]
                case 3:
                    seq = matrix[r][:c]
            current = go(current, seq, directions[d])
            if not current:
                return False


main()
print(len(positions))
