"""
This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
"""

cnt = 0

with open("4.txt") as f:
    matrix = f.readlines()
    L = len(matrix)
    END = L - 1


def addd(seq):
    return seq.count("XMAS") + seq.count("SAMX")


for i in range(L):
    row = matrix[i]
    cnt += addd(row)

    clm = "".join([row[i] for row in matrix])
    cnt += addd(clm)

    d1 = ""
    d1b = ""
    d2 = ""
    d2b = ""
    for a in range(i + 1):
        d1 += matrix[a][i - a]  # tr to bl diagonal tl corner
        d1b += matrix[a][END - i + a]  # tl to br diagonal tr corner
        if i < END:  # central diagonals are calculated already
            d2 += matrix[END - a][END - i + a]  # tr to bl diagonal br corner
            d2b += matrix[END - a][i - a]  # tl to br diagonal bl corner

    cnt += addd(d1)
    cnt += addd(d1b)
    cnt += addd(d2)
    cnt += addd(d2b)

print(cnt)
