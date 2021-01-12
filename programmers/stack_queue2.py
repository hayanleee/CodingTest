from collections import deque       # deque : double ended queue

bridge_len = 2
bridge_wight = 10
truck_wight = [7,4,5,6]
deq = deque(truck_wight)

answer = 0
go = deque(maxlen=bridge_len)
while deq:
    go.append(deq.popleft())
    print(go)