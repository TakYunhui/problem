n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]
# max, min 최소 최대 범위로 지정
max_X, min_X = -10001, 10001
max_Y, min_Y = -10001, 10001
# x, y 최대값 최소값 구한 뒤, 그 차를 곱하면 직사각형 넓이

for i in range(n):
    if dots[i][0] > max_X:
        max_X = dots[i][0]
    if dots[i][1] > max_Y:
        max_Y = dots[i][1]
    if dots[i][0] < min_X:
        min_X = dots[i][0]
    if dots[i][1] < min_Y:
        min_Y = dots[i][1]

print((max_X-min_X) * (max_Y-min_Y))