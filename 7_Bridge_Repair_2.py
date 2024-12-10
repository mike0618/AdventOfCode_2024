"""
Each line represents a single equation.
Operators are always evaluated left-to-right
types of operators: add (+) and multiply (*).
"""

from itertools import product

ops = "+*|"
summ = 0


def check(test, nums, p):
    res = nums[0]
    for i, op in enumerate(p):
        n = nums[i + 1]
        match op:
            case "+":
                res += n
            case "*":
                res *= n
            case "|":
                res = int(str(res) + str(n))
    return res == test


with open("7.txt") as f:
    for line in f:
        data = line.strip().split(":")
        test = int(data[0])
        nums = [int(n) for n in data[1].strip().split()]
        for p in product(ops, repeat=len(nums) - 1):
            if check(test, nums, p):
                summ += test
                break

print(summ)
