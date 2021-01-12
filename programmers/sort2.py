# (0 제외숫자, 0 갯수)

# numbers = [6, 27, 310, 200, 2000]        # 6210
numbers = [3, 30, 34, 5, 9]

# 베스트 풀이
numbers = sorted(list(map(str, numbers)))
print(numbers)
numbers.sort(key=lambda x : x*3, reverse=True)
print(numbers)
ans = str(int(''.join(numbers)))
print(ans)

# numbers = sorted(list(map(str, numbers)), reverse=True)
# print(numbers)

## 내풀이 : 실행 시간 초과,,,
# cnt = 0
# num = []
# for i in numbers:
#     flag = True
#     q, r = divmod(int(i), 10)
#     while r == 0:
#         flag = False
#         cnt += 1
#         q, r = divmod(q, 10)
#         if r != 0:
#             num.append((str(int(i) // 10**cnt), cnt))
#             break
#     if flag:
#         num.append((str(i), cnt))
#     cnt = 0
# sortnum = sorted(num, key=lambda x : (x[0], -x[1]))
#
# answer = ''
# while sortnum:
#     n, zero = sortnum.pop()
#     answer += n + '0'*zero
#
# print(answer)


