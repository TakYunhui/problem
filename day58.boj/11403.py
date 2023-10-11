from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
# 인접행렬
'''
1 -> 2 / 2 -> 3 / 3 -> 1
1,1 -> 1 2 3 1 
1,2 -> 1 2
1,3 -> 1 2 3
2,1 -> 2 3 1
2,2 -> 2 3 1 2
2,3 -> 2 3
3,1 -> 3 1
3,2 -> 3 1 2
3,3 -> 3 1 2 3
'''
graph = [[] for _ in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j]:
            graph[i].append(j)
def bfs(start, goal):
    q = deque([(start)])
    visited = [0] * n
    visited[start] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
            if next == goal:
                return 1
    return 0

for i in range(n):
    for j in range(n):
        if bfs(i, j):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()