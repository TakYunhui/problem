n = int(input()) # 홀수 자연수
target = int(input()) # 위치를 찾고자 하는 n^2 이하의 수
# n * n 표에 순번대로 채우기
arr = [[0] * n for _ in range(n)]
# 하 우 상 좌
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 시작점
x, y = 0, 0
# 방향 시작 인덱스, 표를 채울 숫자(1부터 시작)
i = 0
num = n * n
while num != 1:
    arr[x][y] = num
    nx = x + d[i][0]
    ny = y + d[i][1]

    # 제한 범위 안이며 다음 위치에 값이 없으면
    if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
        num -= 1
        # 값을 넣고, x,y 위치 바꾸기
        arr[nx][ny] = num
        x, y = nx, ny
    else:
        # 갈 수 없는 경우 반환 전환
        i = (i+1) % 4

# 달팽이 이차원 리스트 한 줄씩 출력
for i in arr:
    print(*i)
n_arr = len(arr)
# target 좌표 구하기기
for i in range(n_arr):
    for j in range(n_arr):
        if arr[i][j] == target:
            print(i+1, j+1)

