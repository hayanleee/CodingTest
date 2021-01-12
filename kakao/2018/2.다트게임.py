dartResult = "1S2D*3T"

import re

arr = re.findall(r"\d{1,2}[SDT][*#]?", dartResult)
score = {'S':1, 'D':2, 'T':3}
total = [0, 0, 0]

for i in range(len(arr)):
    flag = 1
    cnt = 0
    if arr[i][-1] == "*":
        cnt = 1
        arr[i] = arr[i][:-1]
    elif arr[i][-1] == "#":
        flag = -1
        arr[i] = arr[i][:-1]

    temp = flag * int(arr[i][:-1]) ** (score[arr[i][-1]])
    total[i] += temp
    if cnt:
        if i == 0:
            total[i] *= 2
        else:
            total[i-1:i+1] *= 2
print (sum(total))