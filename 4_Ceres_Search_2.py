"""
it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X
"""

cnt = 0

with open("4.txt") as f:
    matrix = f.readlines()
    L = len(matrix)
    END = L - 1


def check(r, c):
    test1 = matrix[r + 1][c + 1] + matrix[r - 1][c - 1]
    test2 = matrix[r + 1][c - 1] + matrix[r - 1][c + 1]
    if "M" in test1 and "S" in test1 and "M" in test2 and "S" in test2:
        return True
    return False


for r in range(1, END):
    for c in range(1, END):
        if matrix[r][c] == "A" and check(r, c):
            cnt += 1

print(cnt)
