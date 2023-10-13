'''
문제:
배열이 주어지면 (0,0) -> (n,n) 까지의 거리를 최소비용으로 도달하는 값을 구하라.
조건:
    1. 한 점에서 다른점으로 갈때 현재 점보다 다음 점의 값이 낮다면 비용이 들지않는다.
    2. 값이 같다면 비용이 1이 든다
    3. 값이 기존보다 더 크다면, 두 수의 차에 2를 곱한 비용이 든다.

최소비용을 구하라.
2
4
9 3 7 5
8 5 6 3
7 5 4 3
9 9 9 4
5
1 1 1 1 1
9 9 9 1 9
9 9 9 1 9
9 9 9 1 1
9 9 9 9 1
'''
import heapq
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
t = int(input())
def dijkstra():
    pq = []
    # 우선순위 큐(pq)에 시작 소모 연료, 시작 위치(x, y) 값 push
    heapq.heappush(pq, (0, 0, 0))
    cost[0][0] = 0
    while pq:
        now_cost, x, y = heapq.heappop(pq)
        # 현재 저장된 소모 연료 값이 cost에 저장된 것보다 크다면 제외
        if now_cost > cost[x][y]:
            continue
        # 델타 탐색으로 4방향 이동
        for i in d:
            nx = x + i[0]
            ny = y + i[1]
            # 제한된 인덱스 값 벗어나면 제외
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue

            # 다음 연료 소모량 조건식
            if arr[x][y] > arr[nx][ny]:
                acc = 0
            elif arr[x][y] == arr[nx][ny]:
                acc = 1
            elif arr[x][y] < arr[nx][ny]:
                acc = (arr[nx][ny] - arr[x][y]) * 2

            # 현재 소모 연료 값 + 다음에 소모될 위치 값의 합이
            # cost의 다음 위치 부분에 이미 저장된 값보다 크다면 제외
            if cost[x][y] + acc > cost[nx][ny]:
                continue
            # 아니라면 cost 갱신하고 pq에 넣으셈
            cost[nx][ny] = cost[x][y] + acc
            heapq.heappush(pq, (cost[nx][ny], nx, ny))

    return cost[n-1][n-1]
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    INF = int(1e9)
    cost = [[INF] * n for _ in range(n)]
    print(f'#{tc} {dijkstra()}')