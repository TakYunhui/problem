from collections import deque
import sys
input = sys.stdin.readline
# 가로, 세로, 상자 수(높이)
m, n, h = map(int, input().split())
# h 개의 쌓인 상자 별 n 개의 줄에 하나의 상자에 담긴 토마토의 정보
# 3차원 리스트
'''
0 : 익지 않은 토마토
1 : 익은 토마토
-1 : 토마토가 들어있지 않은 칸 
'''
boxes = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
visited = [list([0] * m for _ in range(n)) for _ in range(h)]
# print(boxes)
# print(visited)

# 처음부터 다 익은 상자들이라면 0 출력하고 전체 코드 종료
check = True
for i in boxes:
    for j in i:
        # print(j)
        if 0 in j:
            check = False
if check:
    print(0)
    exit(0)
# 상하좌우
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs():
    while q:
        z, x, y = q.popleft()
        # 한 상자내 4방향 델타탐색 bfs
        for i in d:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[z][nx][ny]:
                continue
            if boxes[z][nx][ny] == 0:
                visited[z][nx][ny] = visited[z][x][y] + 1
                q.append((z, nx, ny))
        # z축 앞, 뒤 생각하기
        for k in [1, -1]:
            nz = z + k
            # 높이 범위 내이고, 방문하지 않았다면 visited 처리 후 q에 추가
            if 0 <= nz < h and not visited[nz][x][y] and boxes[nz][x][y] == 0:
                visited[nz][x][y] = visited[z][x][y] + 1
                q.append((nz, x, y))

q = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if boxes[z][x][y] == 1 and not visited[z][x][y]:
                # print(z, x, y)
                q.append((z, x, y))
                visited[z][x][y] = 1
            # 토마토가 들어갈 수 없는 곳이면 1로 방문 처리해서 탐색 더 안하도록 한다
            # bfs 함수에서 이 작업을 하면 1 넣어준 걸 다시 탐색하게 되어서 로직이 틀리게 됨...
            elif boxes[z][x][y] == -1:
                visited[z][x][y] = 1
bfs()
# print(visited)
value = 0
for z in range(h):
    for i in range(n):
        for j in range(m):
            if visited[z][i][j] == 0:
                print(-1)
                exit(0)
            elif visited[z][i][j] > value:
                value = visited[z][i][j]
else:
    print(value-1)