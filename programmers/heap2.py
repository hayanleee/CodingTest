stock = 4       # 현재 공장에 남아있는 수량
dates = [4, 10, 15]     # 밀가루 공급 일정
supplies = [20, 5, 10]      # 해당 시점에 공금 가능한 밀가루 수량
k = 30          # 원래 공장으로부터 공급받는 시점

# 밀가루 떨어지지않고 공장운영하려면 최소 몇번 해외에서 공급?
from collections import deque

A = deque(zip(dates,supplies))

cnt = 0
while k > 0:
    if stock < k:
        date, sup = A.popleft()
        k -= stock-date+sup
        cnt += 1

print(cnt)
