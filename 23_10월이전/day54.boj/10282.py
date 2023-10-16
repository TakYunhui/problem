# 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start)) # 우선순위 기준 (초)
    time[start] = 0

    while pq:
        now = heapq.heappop(pq)
        node = now[1]
        second = now[0]

        if time[node] < second:
            continue

        for next in graph[node]:
            next_node = next[0]
            next_second = next[1] + second
            if next_second < time[next_node]:
                time[next_node] = next_second
                heapq.heappush(pq, (next_second, next_node))


t = int(input()) # 테스트 케이스
for _ in range(t):
    # 컴퓨터(정점), 의존성(간선), 해킹당한 컴퓨터 번호(시작점)
    n, d, c = map(int, input().split())
    # d개의 줄에 의존성(관계)
    # a가 b에 의존 -> b가 감염되면 s초 후 a도 감염
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s)) # 의존하는 컴퓨터 번호와 초
    time = [INF] * (n + 1)
    dijkstra(c)
    # 감염된 컴퓨터 개수 세기
    # 최단 시간 구하는 과정에서 세면 중복으로 들어가기에
    # time에서 INF가 아닌 요소의 개수를 센다
    cnt = 0
    ans = 0
    for i in time:
        if i != INF:
            cnt += 1
            # 왜 max 로 해줘야하는지 모르겠음
            ans = max(ans, i)
    print(cnt, ans)