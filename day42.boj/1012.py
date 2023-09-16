from collections import deque
import sys
input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1
# 테스트 케이스 개수
t = int(input())
for _ in range(t):
    # 배추 밭의 가로(행) m, 세로(열) n, 배추가 심어진 개수 k
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    # k 줄 동안 배추의 위치가 주어짐 -> 배추 심어진 정보 행렬로 만들기 
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1
    result = 0
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                result += bfs(i, j)
    print(result)



