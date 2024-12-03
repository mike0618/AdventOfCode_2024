"""
Compare 2 lists.
This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
Calculate a total similarity score by adding up each number in the left list
after multiplying it by the number of times that number appears in the right list.
"""

lst1 = []
lst2 = []

with open("1.txt") as f:
    for line in f:
        lst = line.split()
        lst1.append(lst[0])
        lst2.append(lst[1])

diff_total = 0
for n in lst1:
    diff_total += int(n) * lst2.count(n)

print(diff_total)
