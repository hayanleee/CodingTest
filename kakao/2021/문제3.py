info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

info2 = [i.split() for i in info]
for i in info2:
    i[4] = int(i[4])

query2 = [i.replace('and','').split() for i in query]
# for i in query2:
#     i[4] = int(i[4])

print(info2)
print(query2)
info2 = sorted(info2, key = lambda x : -x[4])
print(info2)

answer = [0] * len(query2)
for idx, q in enumerate(query2):
    for i in info2:
        if i[4] >= int(q[4]):
            t = i.pop()
            flag = True
            for a, b in zip(q, i):
                if a == '-':
                    continue
                if a != b:
                    flag = False
                    break
            if flag:
                answer[idx] += 1
            i.append(t)
        else:
            break
print(answer)


# answer = [0] * len(query2)
# for idx, q in enumerate(query2):
#     for i in info2:
#         if i[4] >= q[4]:
#             tmp1 = i[:4]
#             tmp2 = q[:4]
#             flag = True
#             for t1, t2 in zip(tmp1, tmp2):
#                 if t2 == '-':
#                     continue
#                 if t1 != t2:
#                     flag = False
#                     break
#             if flag:
#                 answer[idx] += 1
# print(answer)


# answer = [0] * len(query2)
# for idx, q in enumerate(query2):
#     for i in info2:
#         if int(i[4]) >= int(q[4]):
#             t = i.pop()
#             flag = True
#             for a, b in zip(q, i):
#                 if a != '-' and a != b:
#                     flag = False
#                     break
#             if flag:
#                 answer[idx] += 1
#             i.append(t)
#
# print(answer)
