"""
the price of fence required for a region is found by multiplying that region's area by its perimeter
"""

garden = []
types = {}
regions = {}
with open("12.txt") as f:
    for line in f:
        lst = list(line.strip())
        garden.append(lst)
L = len(garden)
R = range(L)
arounds = (1, 0), (0, 1), (-1, 0), (0, -1)


def mark_regions(pos):
    y, x = pos
    plant = garden[y][x]
    garden[y][x] += regions[plant]
    for p in arounds:
        y1, x1 = y + p[0], x + p[1]
        if y1 in R and x1 in R and garden[y1][x1] == plant:
            mark_regions((y1, x1))


for y, row in enumerate(garden):
    for x, plant in enumerate(row):
        if len(plant) > 1:  # already marked
            continue
        regions.setdefault(plant, 0)
        regions[plant] = str(int(regions[plant]) + 1)
        mark_regions((y, x))


def plants_around(pos):
    cnt = 0
    y, x = pos
    plant = garden[y][x][0]
    for p in arounds:
        y1, x1 = y + p[0], x + p[1]
        if y1 not in R or x1 not in R:
            continue
        if garden[y1][x1][0] == plant:
            cnt += 1
    return cnt


for y, row in enumerate(garden):  # calc area
    for x, plant in enumerate(row):
        plant = garden[y][x]
        types.setdefault(plant, {"area": 0, "perimeter": 0})
        types[plant]["area"] += 1


for y, row in enumerate(garden):  # calc perimeter
    for x, plant in enumerate(row):
        types[plant]["perimeter"] += 4 - plants_around((y, x))

price = 0
for k, v in types.items():
    price += v["area"] * v["perimeter"]

print(price)
