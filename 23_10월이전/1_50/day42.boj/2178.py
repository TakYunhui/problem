# (1,1) -> (n, m)
# bfs
from collections import deque
import sys
input = sys.stdin.readline
# BFS -> 최단 거리 or 최단 횟수, 탐색의 횟수 => 가장 처음 발견되는 해답이 최단 거리
# 왜냐? 동일한 레벨은 다 넣고 진행하기에 ...

# 문제풀이
# 나의 시도 -> cnt 를 주고, 조건에 맞으면 cnt +1을 하였다
# 그랬더니 최단거리가 아니라 다른 거리 들린 것도 세어버리거나 덜 셈
# => arr의 value 자체를 읻오 횟수로 저장하면서 탐색 진행
# 이러면 현재 위치에서 갈 수 있는 다음 레벨의 위치 모두 +1 해주어 이동 횟수가 구해짐
d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북
def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    arr[nx][ny] = arr[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return arr[n-1][m-1]

# 행: n, 열: m
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs(0, 0))
