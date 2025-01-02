"""
Given the original position and velocity of each robot.
Predict their positions in 100 seconds and count their amount in each of 4 quadrants, but not in the middle.
The result is the product of 4 amounts.
"""

T = 100
L = 101
H = 103
HALF_L = (L - 1) // 2
HALF_H = (H - 1) // 2
counts = [0, 0, 0, 0]


def next(p, v):
    x = p[0] + v[0]
    y = p[1] + v[1]
    if x < 0:
        x += L
    elif x >= L:
        x -= L
    if y < 0:
        y += H
    elif y >= H:
        y -= H
    return x, y


with open("14.txt") as f:
    for line in f:
        r = line.strip().split()
        p = r[0][2:].split(",")
        v = r[1][2:].split(",")
        p = int(p[0]), int(p[1])
        v = int(v[0]), int(v[1])
        for _ in range(T):
            p = next(p, v)
        x, y = p
        if x < HALF_L and y < HALF_H:
            counts[0] += 1
        elif x > HALF_L and y < HALF_H:
            counts[1] += 1
        elif x < HALF_L and y > HALF_H:
            counts[2] += 1
        elif x > HALF_L and y > HALF_H:
            counts[3] += 1

q1, q2, q3, q4 = counts
print(q1 * q2 * q3 * q4)
