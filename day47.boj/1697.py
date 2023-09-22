# 1차원 리스트에서 이동
# 0번부터 k번까지 이동
from collections import deque
n, k = map(int, input().split())

q = deque([n])
# 최대 숫자가 십만이므로 인덱스 맞춰서 100001
visited = [0] * (100001)
visited[n] = 0

while q:
    now = q.popleft()
    # 목적지 k에 도달했으면 해당 시간 출력
    if now == k:
        print(visited[k])
        break

    for nx in (now-1, now+1, now*2):
        if 0 <= nx < 100001 and not visited[nx]: # 제한 범위 안이고 방문하지 않았다면
            visited[nx] = visited[now] + 1
            q.append(nx)

