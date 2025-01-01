"""
press a = 3 tokens
press b = 1 token
find the fewest tokens to win all possible prizes
"""

with open("13.txt") as f:
    row = f.read().split("\n\n")

counts = [0, 0]
adjust = 10**13

for m in row:
    m = m.split("\n")
    a, b, p = m[0].split("+"), m[1].split("+"), m[2].split("=")
    ax, ay = int(a[1].split(",")[0]), int(a[2])
    bx, by = int(b[1].split(",")[0]), int(b[2])
    px, py = int(p[1].split(",")[0]), int(p[2])
    px += adjust
    py += adjust
    # px = ca * ax + cb * bx; py = ca * ay + cb * by
    # need formulas for ca and cb, and they must be whole numbers
    # ca = (px - cb * bx) / ax; cb = (py - ca * ay) / by
    # ca = px / ax - (py * bx - ca * ay * bx) / (by * ax)
    # ca * by * ax = px * by - (py * bx - ca * ay * bx)
    # ca = (px * by - py * bx) / (by * ax - ay * bx) must be divisible
    # cb = (px * ay - py * ax) / (ay * bx - by * ax) must be divisible
    ca, ra = divmod((px * by - py * bx), (by * ax - ay * bx))
    cb, rb = divmod((px * ay - py * ax), (ay * bx - by * ax))
    if not ra and not rb:
        counts[0] += ca
        counts[1] += cb

print(counts[0] * 3 + counts[1])
