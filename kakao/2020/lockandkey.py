key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# for x, k in enumerate(key):
#     for y, v in enumerate(k):
#         print(x, y, v)

def Check(x, y):
    pass


out = len(key) - 1
n = out * 2 + len(lock)
ground = [[0]*n for _ in range(n)]

# ground 에 자물쇠 깔아주기
print(ground)
for i in range(len(lock)):
    pass


for y in range(n - out):
    for x in range(n - out):
        Check(x, y)



