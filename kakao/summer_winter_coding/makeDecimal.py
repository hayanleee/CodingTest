# 소수 : 에라토스테네스의 체
from itertools import combinations

nums = [1, 2, 3, 4, 5, 7 , 8]

# max = 2997, 루트2997 = 54
n = 2997
allnum = [True] * n
m = int(n ** 0.5)
for i in range(2, m+1):
    if allnum[i] == True:
        for k in range(i+i, n, i):
            allnum[k] = False

decimals = [i for i in range(2, n) if allnum[i] == True]
# print(decimals)
# print(list(combinations(nums, 3)))
# print(list(map(sum, combinations(nums, 3))))
nd = list(map(sum, combinations(nums, 3)))
# print(len(list(set(nd).intersection(decimals))))

print(len(list(i for i in nd if i in decimals)))





















