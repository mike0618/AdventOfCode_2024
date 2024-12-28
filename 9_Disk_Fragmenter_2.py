"""
layout of files and free space on the disk
each file on disk also has an ID number
move files one at a time from the end of the disk to the leftmost free space blocks, if they fit.
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
        blocks.append(int(n))  # empties
    else:
        blocks.append((id, int(n)))  # id and number of blocks
        id += 1

index = -1  # the end of blocks list
min_id = 10000
while True:
    if isinstance(blocks[index], int):
        index -= 1  # if ends with an empty, the target is a file
        continue
    file_id, file_b = blocks[index]
    if file_id > min_id:  # already processed
        index -= 1
        continue
    min_id = file_id
    if not file_id:
        break  # come to 0 id
    for i, b in enumerate(blocks[:index]):
        if isinstance(b, int) and b >= file_b:
            blocks[index] = file_b  # replace source file with empties
            blocks.remove(b)  # remove empties at destination
            blocks.insert(i, (file_id, file_b))  # insert a file
            if b > file_b:
                blocks.insert(i + 1, b - file_b)  # if a file smaller than empties
            break
    else:
        index -= 1


disk = []  # restore disk from the blocks table
for i, b in enumerate(blocks):
    if isinstance(b, int):
        for _ in range(b):
            disk.append(0)
        continue
    file_id, file_b = b
    for _ in range(file_b):
        disk.append(file_id)

checksum = 0

for i, n in enumerate(disk):
    checksum += i * n

print("Checksum:", checksum)
print(f"Time: {time() - start:.2f}s")
