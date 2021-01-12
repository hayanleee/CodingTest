# 내부적으로 이진 트리에 원소를 추가하는 heappush() 함수의 시간 복잡도 : O(logN)
# 주의사항은 인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것
# 두번째로 작은 원소를 얻으려면 바로 heap[1]으로 접근하면 안되고,
# 반드시 heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]를 통해 새로운 최소값에 접근해야 함.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq
heapq.heapify(scoville)
ans = 0
while scoville:
    if len(scoville) == 1:
        if K <= scoville[0]:
            print(ans)
        else:
            print(-1)
    first = heapq.heappop(scoville)
    second = heapq.heappop(scoville)
    heapq.heappush(scoville, first + 2*second)
    ans += 1
    if K <= scoville[0]:
        print(ans)
        break
print(-1)

