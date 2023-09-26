# 크기가 n * n인 2차원 배열
# 비의 양에 따라 물에 잠기지 않는 영역 구하기
# dfs/bfs
from collections import deque
import sys
input = sys.stdin.readline
# bfs 로 잠기지 않는 영역 탐색 후, 한 덩어리 탐색마다 1 반환
def bfs(x, y, rain):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for d in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] > rain:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 비의 최댓값 구하기
max_rain = 0
for x in range(n):
    for y in range(n):
        max_rain = max(max_rain, arr[x][y])
# 1부터 최댓값 -1 만큼의 영역 확인 : 최댓값은 다 잠기므로 안전영역이 안 생김
max_rain -= 1
results = []
while max_rain:
    result = 0
    visited = [[0] * n for _ in range(n)]
    rain = max_rain
    for x in range(n):
        for y in range(n):
            # 물에 잠기지 않는 영역이므로 빗물보다 높이가 큰 값만 bfs 탐색
            if not visited[x][y] and arr[x][y] > max_rain:
                result += bfs(x, y, rain)
    results.append(result) # 나온 결과들을 리스트에 저장
    max_rain -= 1
# 저장된 리스트에서 최댓값 출력
# 아무 지역도 물에 잠기지 않을 수 있다
if results:
    print(max(results))
else:
    print(1)