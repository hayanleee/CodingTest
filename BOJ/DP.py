# 1463    10 9 3 1




# # 11726
# n = int(input())
# dp = [1, 2]
# for a in range(2, n+1):
#     dp.append(dp[a-1] + dp[a-2])
# print(dp[n-1] % 10007)

# # 11727
# n = int(input())
# dp = [1, 3]
# for a in range(2, n+1):
#     dp.append(dp[a-1] + dp[a-2]*2)
# print(dp[n-1] % 10007)

# # 9095
# T = int(input())
# for i in range(T):
#     dp = [1, 2, 4]
#     n = int(input())
#     for k in range(3, n+1):
#         dp.append(dp[k-1]+dp[k-2]+dp[k-3])
#     print(dp[n-1])

# # 10844





# # 11057






# # 2193
# n = int(input())
# cnt = [0]*91
# cnt[1] = 1
# cnt[2] = 1
# for i in range(3,n+1):
#     cnt[i] = cnt[i-1] + cnt[i-2]
# print(cnt[n])

# # 9465






# # 2156



# 10 20 10 30 20 50
# # 11053
n = int(input())
seq = list(map(int, input().split()))
print(seq)








