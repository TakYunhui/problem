# swea 고대 유적
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    '''
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
1 0 0 0 0 0 1 0
1 0 1 1 1 0 1 0
1 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1
    '''

    # 가장 긴 길이 넣을 변수
    result = 0
    # 가로 유적
    cnt = 0
    for i in range(n):
        row = 0
        for j in range(m):
            if data[i][j] == 1:
                row += 1
            else:
                row = 0
            cnt = max(cnt, row)
    # 세로 유적
    for j in range(m):
        col = 0
        for i in range(n):
            if data[i][j] == 1:
                col += 1
            else:
                col = 0
            cnt = max(cnt, col)
    print(f'#{tc} {cnt}')


