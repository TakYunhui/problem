import heapq, sys
input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 0, 0)) # 방 바꾼 횟수, 초기 x, y 위치
    dist[0][0] = 0
    while pq:
        cnt, x, y = heapq.heappop(pq)
        # 끝방 도착
        if x == n-1 and y == n-1:
            print(cnt)
            return

        for i in d:
            nx, ny = x + i[0], y + i[1]
            # 다음 위치 거리 저장 값이 cnt +1 보다 크다면 이동 (to 최솟값 구하기)
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > cnt+1:

                # 다음 위치가 검은 방이면
                if arr[nx][ny] == '0':
                    # 방 하나 부시고 다음 위치 넣기
                    dist[nx][ny] = cnt + 1
                    heapq.heappush(pq, (cnt+1, nx, ny))
                else:
                    # 안 부수고 전의 값 넣기
                    dist[nx][ny] = dist[x][y]
                    heapq.heappush(pq, (cnt, nx, ny))

dijkstra()