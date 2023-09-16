# 최소 횟수 -> BFS
from collections import deque
import sys
input = sys.stdin.readline
# a -> b 로 문자를 바꾼다(이동)
# 모든 문자는 n 이하의 자연수로 주어진다
a, b = map(int, input().split())
# n: 전체 문자(노드) 수, m: 치환 가능 문자쌍(간선) 수
n, m = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    c, d = map(int, input().split())
    matrix[c][d] = 1
    matrix[d][c] = 1
visited = [0] * (n+1)
q = deque([a])
visited[a] = 1
while q:
    focus = q.popleft()
    for i in range(1, n+1):
        if matrix[focus][i] == 1 and not visited[i]:
            visited[i] = visited[focus] + 1
            q.append(i)
# 처음 수는 카운트 이동 횟수에 포함 안 시키므로 1 뺀다
if visited[b]:
    print(visited[b]-1)
else:
    print(-1)

