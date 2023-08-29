chess = [list(input()) for _ in range(8)]
n = len(chess)
cnt = 0
# 짝수 - 짝수 칸, 홀수 - 홀수 칸
for i in range(n):
    if i % 2 == 0:
        for j in range(0, n, 2):
            if chess[i][j] == 'F':
                cnt += 1
    else:
        for j in range(1, n, 2):
            if chess[i][j] == 'F':
                cnt += 1
print(cnt)