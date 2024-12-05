"""
The notation X|Y means that page number X must be printed at some point before page number Y.
The first section specifies the page ordering rules
The second section specifies the page numbers of each update
Get sum of the correct updates middle numbers.
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
        for m in upd[:i]:
            if m in afters:
                return 0
        for m in upd[i + 1 :]:
            if m in befores:
                return 0
    return int(upd[len(upd) // 2])


updates = sections[1].strip().split("\n")
for update in updates:
    update = update.split(",")
    summ += check(update)

print(summ)
