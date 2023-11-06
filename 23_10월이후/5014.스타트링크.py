from collections import deque
# 총 층수, 시작 위치, 목표 위치, 위로 u칸(오른쪽), 아래로 d칸
F, S, G, U, D = map(int, input().split())
# visited 배열로 bfs
d = [U, -D]
q = deque([S])
visited = [0] * (F+1)
visited[S] = 1

while q:
    now = q.popleft()
    if now == G:
        print(visited[now]-1)
        exit(0)
    for i in d:
        next = now + i
        # 제한 범위: 1층 ~ 목표 층 까지
        # 방문한 적 없다면
        if 0 < next <= F and not visited[next]:
            # 방문 체크 + 누적 이동 횟수 더하기
            visited[next] = visited[now] + 1
            q.append(next)
print("use the stairs")