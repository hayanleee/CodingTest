answers = [1,3,2,4,2]

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,

import operator
formula = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
ret = [0] * 3
for i, tmp in enumerate(formula):
    tmp *= ((len(answers) // len(tmp)) + 1)
    for x, y in zip(answers, tmp):
        if operator.eq(x, y):
            ret[i] += 1
# print(ret.index(max(ret)))
m = max(ret)
print([i+1 for i, j in enumerate(ret) if j == m])


# 배운점 : from itertools import cycle   -> 사용법 : cycle([list])