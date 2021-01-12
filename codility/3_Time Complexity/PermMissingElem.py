A = [1,3,2,5]

tmp = [0] * (len(A) + 2)    # +2 이유: 리스트 맨앞, missing number
for i in A:
    tmp[i] = 1
print(tmp.index(0, 1))      # index(value, start, end)