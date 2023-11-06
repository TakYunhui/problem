# bfs로 한 묶음 저장, 같은 번호로 저장
# 이때, 칸 수도 세어서 저장한다
from collections import deque
import sys
input = sys.stdin.readline
num = 1
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = []
def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    visited[x][y] = num
    while q:
        x, y = q.popleft()
        for k in d:
            nx = x + k[0]
            ny = y + k[1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == '1':
                visited[nx][ny] = num
                cnt += 1
                q.append((nx, ny))

    result.append(cnt)

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if arr[x][y] == '1' and  not visited[x][y]:
            bfs(x, y)
            num += 1
result.sort()
print(len(result))
for i in result:
    print(i)
