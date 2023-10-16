# 결국 총 영역 칸 수만 구하면 되는 거 아닌가?

arr = [[0] * 101 for _ in range(101)]
for _ in range(4):
    # 네 개의 직사각형 면적 입력(왼쪽 아래, 오른쪽 위 좌표 값)
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            # print(x, y)
            arr[x][y] = 1
area = 0
for x in range(101):
    for y in range(101):
        if arr[x][y] == 1:
            area += 1

print(area)