m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def Find_4Block(m, n, myList, erase):
    for x in range(m - 1):
        for y in range(n - 1):
            if myList[x][y] == myList[x][y + 1] == myList[x + 1][y] == myList[x + 1][y + 1] != "2":
                erase.extend([x, y])


def Erase_Block(x, y, myList):
    for i in range(2):
        for j in range(2):
            myList[x + i][y + j] = "1"


def Fill_Block(m, n, myList):
    ret = 0
    for y in range(n):
        for x in range(m):
            if myList[x][y] == "1":
                ret += 1
                for k in range(x, 0, -1):
                    myList[k][y] = myList[k - 1][y]
                myList[0][y] = "2"
    return ret


def Make_StrToList(m, n, board):
    ret = []
    for i in range(m):
        tmplist = []
        for j in range(n):
            tmplist.append(board[i][j])
        ret.append(tmplist)
    return ret


ret = 0
mylist = Make_StrToList(m, n, board)
while 1:
    erase = []
    Find_4Block(m, n, mylist, erase)
    if not len(erase):
        break
    for i in range(int(len(erase) / 2)):
        Erase_Block(erase[i * 2], erase[i * 2 + 1], mylist)
    ret += Fill_Block(m, n, mylist)
print (ret)