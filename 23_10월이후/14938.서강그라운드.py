import heapq, sys
input = sys.stdin.readline
n, m, r = map(int, input().split()) # 노드 수, 수색 범위, 간선 수
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split()) # 길의 길이 - 양방향
    graph[a].append((b, l))
    graph[b].append((a, l))

INT = int(1e9)
result = 0
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start)) # 누적 거리, 현재 노드

    dist[start] = 0
    while pq:
        cost, node =heapq.heappop(pq)
        # 현재 노드로 가는 거리가 수색 범위보다 크다면 pass
        if cost > dist[node]:
            continue
        # 연결된 노드 확인 -> 다음 노드 + 다음 거리
        for next in graph[node]:
            next_node = next[0]
            next_cost = cost + next[1]

            if next_cost > dist[next_node]:
                continue
            dist[next_node] = next_cost
            heapq.heappush(pq, (next_cost, next_node))

    # print(dist, acc, result)

for i in range(1, n+1):
    dist = [INT] * (n + 1)
    dijkstra(i)
    tmp = 0
    for j in range(1, n+1):
        if dist[j] <= m:
            tmp += items[j]
    result = max(result, tmp)


print(result)