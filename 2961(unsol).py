import sys

n = int(input())
# 신맛, 쓴맛 리스트 저장
sour = []
bitter = []
for _ in range(n):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)
print(sour, bitter)
# 신맛 -> 재료 이용할 때, 곱하기
# 쓴맛 -> 재료 이용할 때, 더하기
# 신맛과 쓴맛의 차이가 가장 작은 요리 만들기
