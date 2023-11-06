# 조합 9C7 -> 9명 중 중복, 순서 없이 7명 조합
from itertools import combinations
heights = [int(input()) for _ in range(9)]

for i in combinations(heights, 7):
    if sum(i) == 100:
        result = list(i)
        result.sort()

for i in result:
    print(i)


