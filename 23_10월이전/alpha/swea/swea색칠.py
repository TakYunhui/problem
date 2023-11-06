t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 색칠할 영역의 개수
    arr = [[0] * 10 for _ in range(10)]  # 10 * 10 격자
    # 왼쪽 위 모서리 인덱스(r1,c1), 오른쪽 아래 인덱스(r2,c2), 색깔
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if arr[x][y]:
                    arr[x][y] = 'p'
                else:
                    arr[x][y] = color
    result = 0
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 'p':
                result += 1
    print(f'#{tc} {result}')