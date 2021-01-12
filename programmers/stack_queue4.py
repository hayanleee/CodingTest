from collections import deque

priorities = [2, 1, 3, 2]
location = 2
rotate = deque(list([i, p] for i, p in enumerate(priorities)))

# 재밌는거
# print(list(map(max, zip(*tmp))))
# print([max(ele) for ele in zip(*tmp)])
# print(list(map(list, zip(*tmp))))

stack = []
while True:
    if len(stack) > 0 and stack[-1][0] == location:
        break           # 아 여기에 return 해도 되겠다
    if list(map(max, zip(*rotate)))[1] > rotate[0][1]:
        rotate.rotate(-1)
    else:
        stack.append(rotate.popleft())

print(len(stack))

# 내 코드 풀이
# if [i][1] 에 큰게 있으면 deque.rotate(-1)
# else 큰게 없으면 popleft 하고 stack에 쌓아줘

