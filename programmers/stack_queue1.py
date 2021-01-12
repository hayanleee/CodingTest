# reverse 하고 자기보다 큰숫자 나올때까지 인덱스찾아
heights = [1,5,3,6,7,6,5]

heights.reverse()
print(heights)
answer = []
for i in range(len(heights)):
    m = len(heights) - i
    flag = True
    for k in range(m-1):
        if heights[i] < heights[i+k+1]:
            flag = False
            answer.append(len(heights)-(i+k+1))
            break
    if flag:
        answer.append(0)
answer.reverse()

print(answer)


### 베스트풀이
# answer = [0] * len(heights)
# stack = []
# for i in reversed(range(len(heights))):
#     while stack and stack[-1][1] < heights[i]:
#         idx, height = stack.pop()
#         answer[idx] = i + 1
#     stack.append((i, heights[i]))
#
# print(answer)