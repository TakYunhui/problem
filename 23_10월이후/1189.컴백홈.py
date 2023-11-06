import sys
input = sys.stdin.readline
r, c, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = 0
# 백트래킹 dfs
def dfs(x, y, dist):
    global result
    # result + 조건 : 목적지인 0, c-1 도착 + 거리가 k
    if x == 0 and y == c-1 and dist == k:
        result += 1
    else:
        # 아니면 이동할 수 있는 범위 내에서 이동시키고 거리 누적시킨다
        # 현재 지점 방문 처리 필요
        arr[x][y] = 'T'
        for i in d:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != 'T':
                # 이동할 수 없게 했다가 다시 넣어서 이동하게 함
                arr[nx][ny] = 'T'
                dfs(nx, ny, dist+1)
                arr[nx][ny] = '.'


dfs(r-1, 0, 1)
print(result)
