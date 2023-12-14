import heapq, sys
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

pq = []
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e9)
dist = [[INF] * m for _ in range(n)]
def dijkstra():
    # 처음 부순 방의 개수, 초기 위치 (0, 0)
    heapq.heappush(pq, (0, 0, 0))
    dist[0][0] = 0

    while pq:
        cnt, x, y = heapq.heappop(pq)
        if x == n-1 and y == m-1:
            print(cnt)
            return
        for i in d:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] > cnt + 1:
                if arr[nx][ny]:
                    dist[nx][ny] = cnt+1
                    heapq.heappush(pq, (cnt+1, nx, ny))
                else:
                    dist[nx][ny] = cnt
                    heapq.heappush(pq, (cnt, nx, ny))

dijkstra()