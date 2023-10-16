from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    cnt = 0
    q = deque([start])
    visited[start] = 1
    while q:
        start = q.popleft()
        for next in graph[start]:
            if not visited[next]:
                visited[next] = visited[start] + 1
                q.append(next)
                cnt += 1
    return cnt

n, m = map(int, input().split()) # 정점, 간선 수
# 연결 리스트
graph = [[] for _ in range(n+1)] # 1번부터 시작하므로 인덱스 맞추기
for _ in range(m):
    # a가 b를 신뢰하면 b를 해킹하면 a도 해킹할 수 있다
    a, b = map(int, input().split())
    # 따라서 graph[b]에 a 연결 정보 넣는다
    graph[b].append(a)

node = n
result = []
while node:
    visited = [0] * (n+1)
    # 각 시작점의 최댓값과 정점 번호
    result.append((bfs(node), node))
    node -= 1

result.sort(reverse=True) # 최댓값 기준, 내림차순 정렬
# print(result)
max_value = result[0][0] # 최댓값 구했음
answer = []
# 최댓값을 가진 정점 번호들을 answer에 넣기
for i in result:
    if i[0] == max_value:
        answer.append(i[1])
# 오름차순 정렬 후 출력
answer.sort()
print(*answer)