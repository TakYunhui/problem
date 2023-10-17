import sys
# 재귀 깊이 제한 문제 해결
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(now):
    global cnt
    visited[now] = cnt # 방문하면 순서 나타내기
    for node in range(1, n+1):
        if matrix[now][node] == 1 and visited[node] == 0:
            cnt += 1
            dfs(node)


n, m, r = map(int, input().split())
cnt = 1
visited = [0] * (n+1)
# 간선 정보 데이터 만들기
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

dfs(r)
for i in range(1, n+1):
    print(visited[i])