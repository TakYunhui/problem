t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    x, y = 0, 0 # 좌표
    num = 1 # 순번
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
    i = 0  # 방향 인덱스
    while num <= n * n:
        arr[x][y] = num  # 숫자 넣기
        num += 1
        nx = x + d[i][0]
        ny = y + d[i][1]
        # 방향성 바꾸는 조건문
        # 1. 다음 위치 nx, ny 중 범위를 벗어나는 게 있다면 방향 바꾸기
        # 2. 다음 위치에 이미 값이 존재한다면 방향 바꾸기
        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny]:
            i = (i + 1) % 4  # 방향 전환
            nx = x + d[i][0]
            ny = y + d[i][1]

        x, y = nx, ny # 다음 위치로 바꾸기
    print(f'#{tc}')
    for i in arr:
        print(*i)
