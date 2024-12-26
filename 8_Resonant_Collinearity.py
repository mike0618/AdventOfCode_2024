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
    for c in combinations(coord, 2):
        c0 = c[0]
        c1 = c[1]
        dy, dx = c1[0] - c0[0], c1[1] - c0[1]
        ay, ax = c0[0] - dy, c0[1] - dx
        if -1 < ay < L and -1 < ax < L:
            antinodes.add((ay, ax))
        ay, ax = c1[0] + dy, c1[1] + dx
        if -1 < ay < L and -1 < ax < L:
            antinodes.add((ay, ax))

print(len(antinodes))
