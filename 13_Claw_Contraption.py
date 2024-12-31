"""
press a = 3 tokens
press b = 1 token
find the fewest tokens to win all possible prizes
"""

with open("13.txt") as f:
    row = f.read().split("\n\n")

MAX = 100
counts = [0, 0]


def get_prize(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    limit_b = MAX
    max_bx = px // bx
    if max_bx < limit_b:
        limit_b = max_bx
    max_by = py // by
    if max_by < limit_b:
        limit_b = max_by
    for cb in range(limit_b, -1, -1):
        remain_bx = px - bx * cb
        remain_by = py - by * cb
        for ca in range(MAX):
            remain_x = remain_bx - ax * ca
            if remain_x < 0:
                break
            remain_y = remain_by - ay * ca
            if remain_y < 0:
                break
            if not remain_x and not remain_y:
                counts[0] += ca
                counts[1] += cb
                return True


for m in row:
    m = m.split("\n")
    a, b, p = m[0].split("+"), m[1].split("+"), m[2].split("=")
    a = int(a[1].split(",")[0]), int(a[2])
    b = int(b[1].split(",")[0]), int(b[2])
    p = int(p[1].split(",")[0]), int(p[2])
    get_prize(a, b, p)

print(counts[0] * 3 + counts[1])
