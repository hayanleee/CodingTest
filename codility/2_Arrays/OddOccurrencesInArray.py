from collections import Counter
A = [9,3,9,3,9,7,9]
for k, v in Counter(A).items():
    if v % 2 == 1:
        # return k
        print(k)
