from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)
def bfs():
    q = deque([1]) # 시작지점 1
    visited[1] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)
bfs()
# visited에 1번부터 n번까지의 거리 레벨 저장
visited.pop(0)
result = 0
for i in range(1, len(visited)+1):
    result += (len(set(combinations(visited, i)))) % 1000000007
print(result)

