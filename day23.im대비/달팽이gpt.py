t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    x, y = 0, 0  # 시작 좌표 (0, 0)
    num = 1  # 순번
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
    di = 0  # 방향 인덱스

    while num <= n * n:
        arr[x][y] = num
        num += 1
        nx = x + d[di][0]
        ny = y + d[di][1]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
            di = (di + 1) % 4
            nx = x + d[di][0]
            ny = y + d[di][1]

        x, y = nx, ny

    print(f'#{tc}')
    for row in arr:
        print(*row)  # *를 사용하여 리스트를 언패킹하여 출력
