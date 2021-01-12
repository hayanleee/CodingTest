# # 2557
# print("Hello World!")

# # 1000
# A, B = map(int, input().split())
# print(A+B)

# # 2558
# A = int(input())
# B = int(input())
# print(A+B)

# # 10950
# idx = int(input())
# for i in range(idx):
#     A, B = map(int, input().split())
#     print(A+B)

# # 10951
# import sys
# for line in sys.stdin:
#     A, B = map(int, line.split())
#     print(A+B)

# # 10952
# import sys
# for line in sys.stdin:
#     A, B = map(int, line.split())
#     if A == 0:
#         break
#     print(A+B)

# # 10953
# idx = int(input())
# for i in range(idx):
#     A, B = map(int, input().split(','))
#     print(A+B)

# # 11021
# import sys
# idx = int(sys.stdin.readline())
# for i in range(idx):
#     A, B = map(int, sys.stdin.readline().split())
#     print("Case #{0}: {1}".format(i+1, A+B))
#     # print('Case #%d: %d' % (i+1, A+B))

# # 11718
# import sys
# print(sys.stdin.read())

# # 11719
# import sys
# print(sys.stdin.read())

# # 11720
# import sys
# idx = sys.stdin.readline()
# print(sum(map(int, sys.stdin.readline().rstrip())))

# # 11721
# a = input()
# for i in range(0,len(a),10):
#     print(a[i:i+10])

# # 2741
# for i in range(int(input())):
#     print(i+1)

# # 2742
# for i in range(int(input()), 0, -1):
#     print(i)

# # 2739
# n = int(input())
# for i in range(1, 10):
#     print("%d * %d = %d"%(n, i, n*i))

# # 1924
# month = [31,28,31,30,31,30,31,31,30,31,30,31]
# day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
# x, y = map(int, input().split())
# print(day[(sum(month[:x-1])+y)%len(day)])

# # 8393
# n = int(input())
# print(sum(i+1 for i in range(n)))
# # 이것도가능 : sum(range(int(input())+1))

# # 10818
# input()
# n = list(map(int, input().split()))
# print(min(n), max(n))
# # * 쓴 방법
# import sys
# n, *m = map(int, sys.stdin.read().split())
# print(min(m), max(m))

# # 2438
# for i in range(1,int(input())+1):
#     print("*"*i)

# # 2439
# cnt = int(input())
# for i in range(1,cnt+1):
#     print(("*"*i).rjust(cnt))

# # 2440
# cnt = int(input())
# for i in range(cnt,0,-1):
#     print("*"*i)

# # 2441
# cnt = int(input())
# for i in range(cnt,0,-1):
#     print(("*"*i).rjust(cnt))

# # 2442
# n = int(input())
# for i in range(1,n+1):
#     star = 2*i-1
#     print(' '*(n-i)+'*'*star)

# # 2445
# n = int(input())
# for i in range(1,n+1):
#     k = 2*n - 2*i
#     print('*'*i+' '*k+'*'*i)
# for i in range(n-1,0,-1):
#     k = 2*n - 2*i
#     print('*'*i+' '*k+'*'*i)

# # 2522
# n = int(input())
# for i in range(1,n):
#     print(('*'*i).rjust(n))
# for i in range(n,0,-1):
#     print(('*'*i).rjust(n))

# # 2446
# n = int(input())
# for e, i in enumerate(range(n,1,-1)):
#     k = 2*i-1
#     print(' '*e+'*'*k)
# for i in range(1,n+1):
#     k = 2*i-1
#     print(' '*(n-i)+'*'* k)

# # 10991
# n = int(input())
# for i in range(n):
#     print(' '*(n-i-1)+'* '*i+'*')

# # 10992
# n = int(input())
# print(' '*(n-1)+'*')
# for i in range(n-2):
#     space = 2*i+1
#     print(' '*(n-i-2)+'*'+' '*space+'*')
# if n != 1:
#     print('*'*(2*n-1))











