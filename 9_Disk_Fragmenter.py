"""
layout of files and free space on the disk
each file on disk also has an ID number
move file blocks one at a time from the end of the disk to the leftmost free space blocks
calculate the checksum add up file ID * position
"""

from time import time

start = time()

with open("9.txt") as f:
    disk_map = f.readline().strip()

blocks = []
id = 0
for i, n in enumerate(disk_map):
    if i % 2:
        blocks += ["." for _ in range(int(n))]  # empties
    else:
        blocks += [id for _ in range(int(n))]  # id and number of blocks
        id += 1

while True:
    if "." not in blocks:
        break
    if blocks[-1] == ".":
        blocks.pop()
        continue
    blocks[blocks.index(".")] = blocks.pop()  # move blocks from the end to empties

checksum = 0

for i, n in enumerate(blocks):
    checksum += i * n

print("Checksum:", checksum)
print(f"Time: {time() - start:.2f}s")
