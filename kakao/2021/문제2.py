# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

import itertools
import collections

answer = []
for index in course:
    new_menu = []
    for menu in orders:
        tmp = list(itertools.combinations(menu, index))
        for t in tmp:
            new_menu.append(''.join(sorted(t)))
    counter = collections.Counter(new_menu)
    max = 0
    flag = True
    for c, i in counter.most_common():
        if flag:
            max = i
            flag = False
        if max == i and i > 1:
            answer.append(''.join(c))

print(sorted(answer))

