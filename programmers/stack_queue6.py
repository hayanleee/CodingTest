prices = [1,2,3,2,3]

time = [0] * len(prices)
for loc, i in enumerate(prices):
    for k in range(loc+1, len(prices)):
        time[loc] += 1
        if prices[k] < i:
            break

print(time)


# 효율성 테스트 실패
# for loc, i in enumerate(prices):
#     sum = 1
#     flag = True
#     for k in prices[loc+1:]:      # 매번 리스트 슬라이싱은 소요 많이됨 : O(k) ... (k는 잘라낸 리스트의 크기) 가 소요
#         if k < i:
#             time[loc] = sum
#             flag = False
#             break
#         else:
#             sum += 1
#     if flag:
#         time[loc] = sum-1


