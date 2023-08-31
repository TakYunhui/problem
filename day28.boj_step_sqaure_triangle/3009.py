# 네번째 점
# 3개 중 하나만 나온 값들로 x, y 좌표 설정
dots = [list(map(int, input().split())) for _ in range(3)]
# x 값
x = []
for i in dots:
    x.append(i[0])
# y 값
y = []
for i in dots:
    y.append(i[1])

a, b = 0, 0
for i in range(3):
    if x.count(x[i]) == 1:
        a = x[i]
    if y.count(y[i]) == 1:
        b = y[i]
print(a, b)
