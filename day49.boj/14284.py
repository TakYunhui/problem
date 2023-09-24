import heapq
import sys
input = sys.stdin.readline
# 정점, 간선 수
n, m = map(int, input().split())
# 연결 인접 리스트
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split()) # a, b, 가중치 c
    # 무방향 그래프
    graph[a].append((b, c))
    graph[b].append((a, c))
# 시작점, 도착점
s, t = map(int, input().split())

# 구해야 할 것? s와 t가 연결되는 시점의 가중치 최소합
# 저장 배열 만들기
INF = int(1e9)
data = [INF] * (n+1) # 정점 번호 맞추기용 +1
# 힙큐 만들기
pq = []
heapq.heappush(pq, (0, s)) # 시작거리, 시작점
data[s] = 0

while pq:
    cost, now = heapq.heappop(pq)
    if cost > data[now]:
        continue

    for next in graph[now]:
        next_node = next[0]
        weight = next[1]
        next_cost = cost + weight

        if next_cost >= data[next_node]:
            continue

        data[next_node] = next_cost
        heapq.heappush(pq, (next_cost, next_node))
print(data[t])
