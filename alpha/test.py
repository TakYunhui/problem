def back(count, now): # 현재 행과 합 넣기
    global result

    if count == n:
        result = min(result, now)
        return

    if now >= result:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            back(count+1, now + cost[count][i])
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 제품 수
    # 공장 별 생산 비용
    cost = [list(map(int, input().split())) for _ in range(n)]
    result = int(1e9)
    visited = [0] * n
    back(0, 0)
    print(f'#{tc} {result}')