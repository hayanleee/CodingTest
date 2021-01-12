from collections import deque

progresses = [93,30,55]
speeds = [1,30,5]
dist = deque()
for p, s in zip(progresses, speeds):
    quot, remain = divmod(100-p, s)
    dist.append((quot + 1) if remain != 0 else quot)

answer = []
std = dist.popleft()
idx = 1
while dist:
    comp = dist.popleft()
    if std >= comp:
        idx += 1
    else:
        answer.append(idx)
        std = comp
        idx = 1
answer.append(idx)

print(answer)


### 베스트풀이
# Q = []
# for p, s in zip(progresses, speeds):
#     if len(Q)==0 or Q[-1][0] < -((p-100//s)):
#         Q.append([-((p-100)//s),1])
#     else:
#         Q[-1][1]+=1
# print([q[1] for q in Q])