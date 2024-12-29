"""
count stones, which change every blink
0 -> 1
even digits -> split in two
the rest -> multiply by 2024
"""

from time import time

start = time()

with open("11.txt") as f:
    stones = f.read().strip().split()
    counts = {s: 1 for s in stones}  # types of stones and their amounts

for bl in range(75):  # 25 for part 1, 75 for part 2
    new_counts = {}
    for s in counts:
        ls = len(s)
        if not s or s == "0":
            new_s = "1"
        elif not len(s) % 2:
            half = ls // 2
            new_s0 = s[:half]
            new_counts.setdefault(new_s0, 0)
            new_counts[new_s0] += counts[s]
            new_s = s[half:].lstrip("0")
        else:
            new_s = str(int(s) * 2024)
        new_counts.setdefault(new_s, 0)
        new_counts[new_s] += counts[s]
    counts = dict(new_counts)

total = 0
for v in counts.values():
    total += v

print(total)
print(f"Time: {time() - start:.2f}")
