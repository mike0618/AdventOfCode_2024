"""
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four sections are real mul instructions.
Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
Scan the corrupted memory for uncorrupted mul instructions.
The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
"""

result = 0

with open("3.txt") as f:
    data = f.read().split("do()")
for chunk in data:
    active = chunk.split("don't()")[0]
    instrs = active.split("mul")
    for inst in instrs:
        if inst.startswith("(") and ")" in inst:
            inst = inst[1 : inst.index(")")]
            if inst.count(",") != 1:
                continue
            nums = inst.split(",")
            if len(nums) != 2:
                continue
            n0, n1 = nums
            if n0.isdigit() and n1.isdigit():
                result += int(n0) * int(n1)
print(result)
