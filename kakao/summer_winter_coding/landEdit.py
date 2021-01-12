land = [[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]
P = 5
Q = 3

from collections import Counter

land = sum(land,[])
setland = set(land)
cntland = Counter(land)
res = []
for floor in setland:
    val = 0
    for i in setland:
        if i > floor:
            val += cntland[i] * Q * (i-floor)
        else:
            val += cntland[i] * P * (floor-i)
    else:
        res.append(val)

print(min(res))

# 효율성 및.. 시간초과있음 머지?
#
# from collections import Counter
#
# land = sum(land,[])
# cntland = Counter(land)
# res = []
# for floor in set(land):
#     val = 0
#     for i in cntland:
#         if i > floor:
#             val += cntland[i] * Q * (i-floor)
#         elif i < floor:
#             val += cntland[i] * P * (floor-i)
#     else:
#         res.append(val)
#
# print(min(res))