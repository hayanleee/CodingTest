arrangement = "()(((()())(())()))(())"

stack = []
answer = 0
continuity = False
for txt in arrangement:
    if txt == '(':
        stack.append(txt)
        continuity = False
    else:
        if continuity:
            stack.pop()
            answer += 1
            continue
        stack.pop()
        answer += len(stack)
        continuity = True

print(answer)


# # 베스트 풀이
# answer = 0
# sticks = 0
# rasor_to_zero = arrangement.replace('()','0')
#
# for i in rasor_to_zero:
#     if i == '(':
#         sticks += 1
#     elif i =='0' :
#         answer += sticks
#     else :
#         sticks -= 1
#         answer += 1
