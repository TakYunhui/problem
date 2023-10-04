n = int(input())
arr = [list(input()) for _ in range(n)]
result = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j].isdigit():
            result[i][j] = '*'
            for k in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                ni = i + k[0]
                nj = j + k[1]
                if 0 <= ni < n and 0 <= nj < n and arr[i][j] != '.':
                    result[ni][nj] += int(arr[i][j])


for i in range(n):
    for j in range(n):
        if type(result[i][j]) == int and result[i][j] > 9:
            print('M', end='')
        else:
            print(result[i][j], end='')
    print()