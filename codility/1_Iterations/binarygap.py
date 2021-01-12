N = 9
b = format(N, 'b')

index = list(filter(lambda x: b[x] == '1', range(len(b))))
if len(index) == 1:
    # return 0
    print(0)
gap = [index[i] - index[i+1] for i in range(len(index)-1)]
# return abs(min(gap) + 1)
print(abs(min(gap) + 1))


# 문제 잘못이해함.. N 이 정수 리스트인줄
# N = [9, 529, 32]
#
# binary = [list(format(i, 'b')) for i in N]
# ret = []
# for b in binary:
#     index = list(filter(lambda x: b[x] == '1', range(len(b))))        # fileter 사용
#     # index = [i for i, value in enumerate(b) if value == '1']      # enumerate 사용
#     if len(index) == 1:
#         ret.append(0)
#         continue
#     gap = [index[i] - index[i+1] for i in range(len(index)-1)]
#     ret.append(abs(min(gap) + 1))
# print(ret)