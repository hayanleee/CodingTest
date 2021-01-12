N = 5
cnt = 1
while N != 1:
    if N % 2 == 0:
        N //= 2
    else:
        N -= 1
        cnt += 1

print(cnt)

# 베스트 풀이  한줄..
# print(bin(N).count('1'))