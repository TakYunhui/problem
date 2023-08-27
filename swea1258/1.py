import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 행렬 조사
    for x in range(n):
        for y in range(n):
            pass



    print(f'#{tc}')