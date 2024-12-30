"""
the price of fence required for a region is found by multiplying that region's area by its number of walls
"""

garden = []
types = {}
regions = {}
with open("12.txt") as f:
    for line in f:
        lst = list(line.strip())
        garden.append(lst)
L = len(garden)
EDGE = L - 1
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


for y, row in enumerate(garden):  # calc area
    for x, plant in enumerate(row):
        plant = garden[y][x]
        types.setdefault(plant, {"area": 0, "walls": 0})
        types[plant]["area"] += 1

previous = ""
wall_up = False
wall_down = False
for y, row in enumerate(garden):  # calc horizontal walls
    for x, plant in enumerate(row):
        if previous != plant:
            wall_up = False
            wall_down = False
        previous = plant
        if not wall_up:
            if not y or garden[y - 1][x] != plant:
                types[plant]["walls"] += 1
                wall_up = True
        elif y and garden[y - 1][x] == plant:
            wall_up = False
        if not wall_down:
            if y == EDGE or garden[y + 1][x] != plant:
                types[plant]["walls"] += 1
                wall_down = True
        elif y < EDGE and garden[y + 1][x] == plant:
            wall_down = False

previous = ""
wall_left = False
wall_right = False
for x in R:  # calc vertical walls
    clm = [garden[y][x] for y in R]
    for y, plant in enumerate(clm):
        if previous != plant:
            wall_left = False
            wall_right = False
        previous = plant
        if not wall_left:
            if not x or garden[y][x - 1] != plant:
                types[plant]["walls"] += 1
                wall_left = True
        elif x and garden[y][x - 1] == plant:
            wall_left = False
        if not wall_right:
            if x == EDGE or garden[y][x + 1] != plant:
                types[plant]["walls"] += 1
                wall_right = True
        elif x < EDGE and garden[y][x + 1] == plant:
            wall_right = False

price = 0
for k, v in types.items():
    price += v["area"] * v["walls"]

print(price)
