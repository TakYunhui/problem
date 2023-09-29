from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx = x + i[0]
            ny = y + i[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                cnt += 1
                q.append([nx, ny])
    return cnt


n, m, k = map(int, input().split()) # 세로(행), 가로(열), 위치 개수
# 2차원 좌표로 주어짐 -> 이차원배열 만들어주기
# 0 : 기본 , 1: 쓰레기
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
# 쓰레기가 뭉칠수록 커진다 -> 그래프 탐색해 연결된 쓰레기 뭉치 크기 cnt
result = []
visited = [[0] * m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if arr[x][y] == 1 and not visited[x][y]:
            result.append(bfs(x, y))
print(max(result))