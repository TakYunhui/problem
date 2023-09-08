# 카드 놓기
# 1 - 99 이하의 정수가 적힌 n 장의 카드
# 이 중 k장을 선택하고 가로로 나란히 정수로 만든다
# 만들어지는 정수의 경우의 수?
# 순열로 카드 경우의 수 다 만들기
from itertools import permutations
n = int(input())
k = int(input())
cards = list(input() for _ in range(n))
p = list(permutations(cards, k))
# set -> 중복된 수 제거
result = set()
# k 장 수에 따라 만들어지는 문자 조합 조건 분기로 넣기
if k == 4:
    for x in p:
        result.add(x[0]+x[1]+x[2]+x[3])
elif k == 3:
    for x in p:
        result.add(x[0]+x[1]+x[2])
elif k == 2:
    for x in p:
        result.add(x[0]+x[1])
print(len(result))

