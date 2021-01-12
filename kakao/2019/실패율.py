N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# result = [3,4,2,1,5]

player = len(stages)
result = []
for i in range(N):
    if player == 0:
        result.append((i+1,0))
        continue
    a = stages.count(i+1)
    result.append((i+1, a / player))
    player -= a

print(result)
print(sorted(result, key = lambda x : (-x[1], x[0])))
print([r[0] for r in sorted(result, key = lambda x : (-x[1], x[0]))])       # return 이거
