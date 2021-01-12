# # 5052
# import sys
# n = int(input())
# for _ in range(n):
#     idx = int(input())
#     numbers = [sys.stdin.readline().strip() for i in range(idx)]
#     num2 = sorted(numbers)
#     for i in range(0, len(num2)-1):
#         if num2[i] == num2[i+1][:len(num2[i])]:
#             print("NO")
#             break
#     else:
#         print("YES")


# # 2751
# import sys
# n = int(sys.stdin.readline())
# num = [sys.stdin.readline() for i in range(n)]
# for i in sorted(map(int,num)):
#     print(i)

# # 11650
# import sys
# n = int(sys.stdin.readline())
# matrix = [sys.stdin.readline().split() for i in range(n)]
# for x, y in sorted(matrix, key=lambda k : (k[0], k[1])):
#     print(x, y)

# 8
# -2 -10
# -1 -1
# -2 -5
# 0 0
# 3 2
# 3 4
# 3 10
# 5 1