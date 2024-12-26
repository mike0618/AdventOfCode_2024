"""
an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other.
This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them
"""

from itertools import combinations

with open("8.txt") as f:
    matrix = f.readlines()

L = len(matrix)

antinodes = set()
antennas = {}

for y, row in enumerate(matrix):
    for x, a in enumerate(row[:-1]):
        if a == ".":
            continue
        antennas.setdefault(a, [])
        antennas[a].append((y, x))

for coord in antennas.values():
    if len(coord) < 2:
        continue
    for c in coord:
        antinodes.add(c)
    for c in combinations(coord, 2):
        c0y, c0x = c[0]
        c1y, c1x = c[1]
        dy, dx = c1y - c0y, c1x - c0x
        while True:
            c0y -= dy
            c0x -= dx
            if c0y not in range(L) or c0x not in range(L):
                break
            antinodes.add((c0y, c0x))
        while True:
            c1y += dy
            c1x += dx
            if c1y not in range(L) or c1x not in range(L):
                break
            antinodes.add((c1y, c1x))

print(len(antinodes))
