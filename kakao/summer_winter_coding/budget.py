
# d	budget	result
# [1,3,2,5,4]	9	3
# [2,2,3,3]	10	4

d = [2,2,3,3]
budget = 10
d.sort(reverse=True)
cnt = 0
while d:
    p = d.pop()
    if p <= budget:
        budget -= p
        cnt += 1
    else:
        break

print(cnt)