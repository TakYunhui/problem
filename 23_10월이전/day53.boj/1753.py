import heapq
import sys
input = sys.stdin.readline
V, e = map(int, input().split()) # 정점, 간선
start = int(input()) # 시작점
# 인접리스트
graph = [[] for _ in range(V+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
pq = []
INF = int(1e9)
distance = [INF] * (V+1)
heapq.heappush(pq, (0, start)) # 시작 거리와 시작점 넣기
distance[start] = 0
while pq:
    now = heapq.heappop(pq)
    cost, node = now[0], now[1]

    if cost > distance[node]:
        continue

    for next in graph[node]:
        next_node = next[0]
        next_dist = cost + next[1]
        if next_dist > distance[next_node]:
            continue
        distance[next_node] = next_dist
        heapq.heappush(pq, (next_dist, next_node))

for i in range(1, V+1):
    if distance[i] != INF:
        print( distance[i])
    else:
        print('INF')

