skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

s = list(skill)
cnt = 0
print(list(map(list, skill_trees)))
for st in list(map(list, skill_trees)):
    print(st)
    tmp = ''.join(list(t for t in st if t in s))
    if tmp == skill[:len(tmp)]:
        cnt += 1
print(cnt)


