import sys
input = sys.stdin.readline
n = int(input())
card = dict()
for i in range(n):
    num = int(input())
    card[num] = card.get(num, 0) + 1
# 카드 수(value) 기준 내림차순 정렬한 뒤 같은 값이 있으면 더 작은 key값 기준 정렬
max_v = sorted(card.items(), key=lambda x:(-x[1], x[0]))
print(max_v[0][0])