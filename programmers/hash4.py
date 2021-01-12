# 정답률 33.3% 왜냐,,

from collections import defaultdict
# 베스트앨범
# genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# plays = [500, 10, 150, 800, 2500]

genres = ['classic', 'pop', 'classic', 'pop', 'classic', 'classic']
plays = [400, 600, 150, 2500, 500, 500]

album = sorted(list([idx,g,p] for idx,(g,p) in enumerate(zip(genres,plays))), key=lambda x: (-x[2], x[0]))
print(album)

d = defaultdict(int)
for genre, play in zip(genres, plays):
    d[genre] += play
keys = sorted(d, key=lambda x : -d[x])
print(keys[:2])

answer = []
for key in keys[:2]:
    tmp = []
    for ele in album:
        if key in ele:
            tmp.append(ele[0])
        if len(tmp) == 2:
            break
    if len(tmp) != 0:
        answer.extend(tmp)

print(answer)




# 정답률 33.3%
# album = sorted(list([idx,g,p] for idx,(g,p) in enumerate(zip(genres,plays))), key=lambda x: (-x[2], x[0]))
#
# keys = []
# for ele in album:
#     if ele[1] not in keys:
#         keys.append(ele[1])
#     if len(keys) == 2:
#         break
#
# answer = []
# for key in keys:
#     tmp = []
#     for ele in album:
#         if key in ele:
#             tmp.append(ele[0])
#         if len(tmp) == 2:
#             break
#     answer.extend(tmp)

