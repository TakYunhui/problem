import sys
sys.stdin = open('in1.txt')
t = int(input())
for tc in range(1, t+1):
    # n: 배열의 크기, m: 스프레이 칸 수
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0 # 한 번에 잡을 수 있는 최대 파리 수
    # 스프레이 +
    d = [(1,0), (-1,0), (0,1), (0,-1)]
    x = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for i in range(n):
        for j in range(n): # 스프레이 뿌릴 위치
            # + 방향
            s = arr[i][j] # 스프레이 뿌린 칸에서 죽인 파리 수
            for k in range(4):
                for l in range(1, m): # 각 방향으로 뿌릴 위치
                    ni = i + d[k][0] * l
                    nj = j + d[k][1] * l
                    if 0 <= ni < n and 0 <= nj < n:
                        s += arr[ni][nj]
            result = max(result, s)
            # x 방향
            s = arr[i][j] # 스프레이 뿌린 칸에서 죽인 파리 수
            for k in range(4):
                for l in range(1, m): # 각 방향으로 뿌릴 위치
                    ni = i + x[k][0] * l
                    nj = j + x[k][1] * l
                    if 0 <= ni < n and 0 <= nj < n:
                        s += arr[ni][nj]
            result = max(result, s)

    print(f'#{tc} {result}')