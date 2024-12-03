"""
Compare 2 lists.
To find out, pair up the numbers and measure how far apart they are.
Pair up the smallest number in the left list with the smallest number in the right list,
then the second-smallest left number with the second-smallest right number, and so on.
Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
"""

lst1 = []
lst2 = []

with open("1.txt") as f:
    for line in f:
        lst = line.split()
        lst1.append(lst[0])
        lst2.append(lst[1])

diff_total = 0
while lst1:
    n1 = min(lst1)
    n2 = min(lst2)
    lst1.remove(n1)
    lst2.remove(n2)
    diff_total += abs(int(n1) - int(n2))

print(diff_total)
