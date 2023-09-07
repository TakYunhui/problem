# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2346-%ED%92%8D%EC%84%A0-%ED%84%B0%EB%9C%A8%EB%A6%AC%EA%B8%B0-deque
# 1번부터 N개의 풍선
# i -> i + 1 .... n -> 1번 풍선
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
ballons = list(map(int, input().split()))
# 풍선 순서와 풍선 안 종이 갯수 연결
q = deque()
for i in range(n):
    q.append((i+1, ballons[i]))
result = []

while q:
    idx, paper = q.popleft()
    result.append(idx)
    if paper > 0:
        q.rotate(-(paper-1))
    elif paper < 0:
        q.rotate(-paper)

print(*result)



