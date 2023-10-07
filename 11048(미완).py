import sys

def candy(x, y):
    global tmp
    result = 0

    for k in [(1, 0), (0, 1), (1, 1)]:
        nx = x + k[0]
        ny = y + k[1]
        if nx == n and ny == m:
            result = max(tmp, result)
            print(result)
            return result

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            tmp += maze[nx][ny]
            result = max(result, tmp)
            candy(nx, ny)
            visited[nx][ny] = 0

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
tmp = maze[0][0]
res = candy(0, 0)
print(res)