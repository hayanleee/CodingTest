# 위장 (0.06ms, 10.8MB)
clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
clothes_list = list(tmp[1] for tmp in clothes)
clothes_set = set(clothes_list)
answer = 1
for kind in clothes_set:
    answer *= (clothes_list.count(kind) + 1)

print(answer-1)


# 베스트 풀이
# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer
