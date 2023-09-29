import sys
input = sys.stdin.readline
while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    arr = [list(input()) for _ in range(r)]

    for x in range(r):
        for y in range(c):
            cnt = 0
            if arr[x][y] == '.':
                for k in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                    nx = x + k[0]
                    ny = y + k[1]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '*':
                        cnt += 1
                arr[x][y] = str(cnt)
    for i in arr:
        print(''.join(i), end='')
