from collections import deque
import sys
input = sys.stdin.readline
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for k in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + k[0]
            ny = y + k[1]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1
    return cnt
n, m = map(int, input().split()) # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
painting_cnt = 0
max_v = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 1 and not visited[x][y]:
            max_v = max(max_v, bfs(x,y))
            painting_cnt += 1
print(painting_cnt)
print(max_v)