dirs = 'LULLLLLLU'      # LULLLLLLU         ULURRDLLU          LR

x, y = 0, 0
visited = set()
answer = 0
for m in dirs:
    px, py = x, y
    if m == 'U' and y < 5:
        y += 1
    elif m == 'D' and y > -5:
        y -= 1
    elif m == 'L' and x > -5:
        x -= 1
    elif m == 'R' and x < 5:
        x += 1
    else:
        continue
    if (px, py, x, y) not in visited:
        visited.add((px, py, x, y))
        visited.add((x, y, px, py))
        answer += 1
print(answer)



# 처음푼거  이건 왜안될까....
# cur = [0, 0]
# answer = []
# for m in dirs:
#     tmp = []
#     prev = cur[:]
#     if m == 'U' and cur[1] < 5:
#         cur[1] += 1
#     elif m == 'D' and cur[1] > -5:
#         cur[1] -= 1
#     elif m == 'L' and cur[0] > -5:
#         cur[0] -= 1
#     elif m == 'R' and cur[0] < 5:
#         cur[0] += 1
#     else:
#         continue
#     tmp.append(tuple(prev))
#     tmp.append(tuple(cur))
#     answer.append(tmp)
#     print(answer)
#
# print(len(list(set([tuple(set(a)) for a in answer]))))