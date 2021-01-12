X = 10
Y = 85
D = 30

gap = Y - X
if gap == 0:
    # return 0
    print(0)
q, r = divmod(gap, D)
if r == 0:
    # return q
    print(q)
else:
    # return q + 1
    print(q + 1)