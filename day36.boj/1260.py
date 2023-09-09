from collections import deque
# dfs 재귀 구현
def dfs(v):
    dfs_v[v] = True # 현재 위치 방문 처리
    print(v, end=' ') # 방문한 위치 출력
    for node in range(1, n+1): # 1번부터 n+1번까지
        # 만약 해당 위치에 연결 정보가 존재하고 방문 기록이 없다면 . . .
        if matrix[v][node] == 1 and dfs_v[node] == 0:
            dfs(node)

# bfs 재귀 구현 불가, 반복을 통해 구현
def bfs(v):
    q = deque()
    q.append(v)
    bfs_v[v] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1, n+1):
            if matrix[x][i] == 1 and not bfs_v[i]:
                q.append(i)
                bfs_v[i] = True


# DFS 출력 후 BFS 출력
# node 개수, edge 개수, 탐색 시작할 start 번호
n, m, v = map(int, input().split())
# 연결 정보 자료 만들기 - 연결은 양방향!
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
dfs_v = [False] * (n+1)
bfs_v = [False] * (n+1)

dfs(v)
print()
bfs(v)
