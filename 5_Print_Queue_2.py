"""
The notation X|Y means that page number X must be printed at some point before page number Y.
The first section specifies the page ordering rules
The second section specifies the page numbers of each update
put the page numbers in the right order, get sum of their middle numbers
"""

summ = 0

with open("5.txt") as f:
    sections = f.read().split("\n\n")

rules = sections[0].strip().split("\n")
after_befores = {}
before_afters = {}
for rule in rules:
    b, a = rule.split("|")
    after_befores.setdefault(a, []).append(b)
    before_afters.setdefault(b, []).append(a)


def check(upd):
    for i, man in enumerate(upd):
        befores = after_befores.setdefault(man, [])
        afters = before_afters.setdefault(man, [])
        for j, m in enumerate(upd[:i]):
            if m in afters:
                return i, j
        for j, m in enumerate(upd[i + 1 :]):
            if m in befores:
                return i, j + i + 1
    return 0, 0


updates = sections[1].strip().split("\n")
for update in updates:
    update = update.split(",")
    i, j = check(update)
    if not i + j:
        continue
    update[i], update[j] = update[j], update[i]
    while True:
        i, j = check(update)
        if not i + j:
            summ += int(update[len(update) // 2])
            break
        update[i], update[j] = update[j], update[i]

print(summ)
