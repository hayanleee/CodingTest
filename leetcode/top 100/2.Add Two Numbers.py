# 아.. 링크드리스트래 그냥리스트가아니라

def transList(tmplist):
    tmplist.reverse()
    ret = ''.join(map(str, tmplist))
    return int(ret)

def addTwoNumbers(l1, l2):
    t1 = transList(l1)
    t2 = transList(l2)
    ret = list(str(t1 + t2))
    ret.reverse()
    # return ret
    print(ret)

addTwoNumbers([2,4,3], [5,6,4])

