# 2칸 이상 아무것도 없는 자리에 누울 수 있다
import sys
input = sys.stdin.readline
n = int(input()) # n * n 의 방
arr = [list(input()) for _ in range(n)]

# 가로 누울 자리
garo_cnt = 0
for x in range(n):
    garo = 0
    for y in range(n):
        if arr[x][y] == '.':
            garo += 1
        elif arr[x][y] == 'X':
            if garo >= 2:
                garo_cnt += 1
            garo = 0
    if garo >= 2:
        garo_cnt += 1

# 세로 누울 자리
sero_cnt = 0
for y in range(n):
    sero = 0
    for x in range(n):
        if arr[x][y] == '.':
            sero += 1
        elif arr[x][y] == 'X':
            if sero >= 2:
                sero_cnt += 1
            sero = 0
    if sero >= 2:
        sero_cnt += 1

print(garo_cnt, sero_cnt)
