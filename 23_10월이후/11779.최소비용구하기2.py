import heapq, sys
input = sys.stdin.readline

# 도시의 개수 (정점) : 1번부터 시작
n = int(input())
# 버스의 개수 (간선)
m = int(input())
# 연결 정보
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
# 출발점과 도착점 정보
start, goal = map(int, input().split())

# 누적 비용 저장할 배열 만들기
INF = int(1e9)
data = [INF] * (n+1)
# 이전 노드 저장
prev_node = [0] * (n+1)

# 다익스트라
# 우선순위 큐 + 누적 비용 이용하여 최소 비용 구하기
def dijkstra(start, goal):
    pq = []
    # 시작 비용와 출발점 힙에 넣기
    # 비용부터 넣는 이유 -> 비용 기준으로 우선순위 잡기 위해서
    heapq.heappush(pq, (0, start))
    data[start] = 0  # 출발점의 시작비용은 0

    while pq:
        cost, now = heapq.heappop(pq)
        # 우리는 최소 비용을 구할 것이기에
        # 빼낸 값이 data에 저장된 누적 값보다 크다면 보지 않는다
        if now == goal:
            print(data[goal])
            return
        if cost > data[now]:
            continue

        # 아니라면 아래 코드 진행
        for next in graph[now]:
            # graph 에 연결된 도시 번호, 소요 비용 순으로 넣었으므로
            next_node = next[0] # 다음 정점 번호
            weight = next[1]    # 가중치

            next_cost = cost + weight
            # 다음 정점에 누적된 비용이 계산한 누적 비용보다 작다면
            # 계산 값이 최소 비용이 아니므로 pass
            if next_cost >= data[next_node]:
                continue

            # 아니라면 계산값을 최소 비용으로 갱신
            data[next_node] = next_cost
            heapq.heappush(pq, (next_cost, next_node))
            prev_node[next_node] = now



dijkstra(start, goal)

result = [goal]
previous = prev_node[goal]
while previous != start:
    result.append(previous)
    previous = prev_node[previous]

result.append(start)
result.reverse()
print(len(result))
print(*result)
