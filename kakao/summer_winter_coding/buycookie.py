# # [1,2,4,5]
# from collections import deque
#
# cookie = [1,1,2,9,11,23,100]
#
# stack = []
# answer = 0
# for idx, val in enumerate(cookie):
#     stack.append(val)
#     if sum(stack) < cookie[idx+1]:
#         pass
#     elif sum(stack) > cookie[idx+1]:
#         tmp = deque(stack)
#         for k in tmp:
#             tmp.popleft()
#             if sum(tmp) == cookie[idx+1]:
#                 answer = cookie[idx+1]
#                 break
#             elif sum(tmp) < cookie[idx+1]:
#                 break
#     elif sum(stack) == cookie[idx+1]:
#         answer = cookie[idx+1]
