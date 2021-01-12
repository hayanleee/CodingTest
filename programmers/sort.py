array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# return = [5, 6, 3]
answer = [sorted(array[i-1:j])[k-1] for i, j, k in commands]
print(answer)


# 베스트 풀이
# answer = list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))