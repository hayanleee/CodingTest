board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1   # 세로    y
c = 0   # 가로    x
result = 14

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# for x, k in enumerate(key):
#     for y, v in enumerate(k):
#         print(x, y, v)

def findSame(idx):
    board[r][c] = 0
    for y, k in enumerate(board):
        for x, v in enumerate(k):
            if v == idx:
                return x, y

stack = []
cnt = 0
while sum(sum(board, [])):      # board 가 0 일때까지
    if board[r][c] != 0:
        cnt += 1
        x, y = findSame(board[r][c])
        print(x, y)

        break
    else:
        # 가까운거 찾아야함
        pass