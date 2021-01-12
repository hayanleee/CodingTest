# N	stations	W	answer
# 11	[4, 11]	1	3               # 1, 7, 9
# 16	[9]	2	3                   # 3, 6, 14

N = 11
stations = [4, 11]
W = 1

fiveG = [0] * N
for i in stations:
    for k in range(i-W, i+W+1):
        if k <= N:
            fiveG[k-1] = 1
fiveG.append(1)
tmp = []
answer = []
print(fiveG)
for i, v in enumerate(fiveG):
    if v == 0:
        tmp.append(i+1)
    else:
        if len(tmp) > 0:
            answer.append(tmp)
            tmp = []
print(answer)
cnt = 0
for seq in answer:
    a, b = divmod(seq[-1]-seq[0]+1, W*2+1)
    print(a, b)
    if b != 0:
        a += 1
    cnt += a
print(cnt)
