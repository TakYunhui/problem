# 성 지키기
# 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다
n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]

row = 0

for i in range(n):
    cnt = 0
    for j in range(m):
        if castle[i][j] != 'X':
            cnt += 1
    if cnt == m:
        row += 1

col = 0
for i in range(m):
    cnt = 0
    for j in range(n):
        if castle[j][i] != 'X':
            cnt += 1
    if cnt == n:
        col += 1

print(max(row, col))