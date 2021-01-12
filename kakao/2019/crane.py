board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

cnt = 0      # 사라진 인형의 갯수
new_board = list(map(list, zip(*board)))
moves = [e-1 for e in moves]
stack = []
for i in moves:
    for idx, doll in enumerate(new_board[i]):
        if doll != 0:
            get = new_board[i][idx]
            new_board[i][idx] = 0
            if len(stack) != 0 and stack[-1] == get:
                stack.pop()
                cnt += 2
            else:
                stack.append(get)
            break

print(cnt)
