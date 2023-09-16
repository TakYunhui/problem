from collections import deque
import sys
input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
# I 위치 구하기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            x, y = i, j
visited = [[0] * m for _ in range(n)]
q = deque()
q.append((x, y))
visited[x][y] = 1
cnt = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] != 'X' and not visited[nx][ny]:
                if arr[nx][ny] == 'P':
                    cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
if cnt == 0:
    print('TT')
else:
    print(cnt)