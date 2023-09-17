# 2644
from collections import deque
import sys
input = sys.stdin.readline

# 나(자식) - 부모 : 1촌
# 나 - 할배 : 2촌
# 나 - 아빠 형제 : 3촌
# 촌수 : 시작점부터 도착점까지 이어진 간선 개수??
# 데이터 입력
n = int(input()) # 전체 사람 수 n
s, g = map(int, input().split()) # 촌수 계산 start, goal
m = int(input()) # 관계(간선)의 수 m
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    p, c = map(int, input().split())
    matrix[p][c] = 1
    matrix[c][p] = 1
visited = [0] * (n+1)
q = deque([s])
while q:
    now = q.popleft()
    for node in range(1, n+1):
        if matrix[now][node] and not visited[node]:
            visited[node] = visited[now] + 1
            q.append(node)
if visited[g] == 0:
    print(-1)
else:
    print(visited[g])

