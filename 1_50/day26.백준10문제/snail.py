m, n = map(int, input().split()) # m * n 표
arr = [[0] * n for _ in range(m)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
i = 0
x, y = 0, 0
arr[x][y] = 1
cnt = 0
while True:
    nx = x + d[i][0]
    ny = y + d[i][1]
    if 0<= nx < m and 0<= ny < n and not arr[nx][ny]:
        arr[nx][ny] = 1
        x, y = nx, ny
    else:
        # 방향 바꾸기
        i = (i+1) % 4
        cnt += 1
        nx = x + d[i][0]
        ny = y + d[i][1]
        # 만약 방향을 바꾼 좌표에 값이 있다면 모든 배열 값이 가득 찬 것이므로 반복문 종료
        if arr[nx][ny]:
            cnt -= 1
            break
print(cnt)