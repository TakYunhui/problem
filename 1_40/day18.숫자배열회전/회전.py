import sys
sys.stdin = open('input.txt')
t = int(input()) # 테스트 개수
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = []
    # d90, d180, d270 = [],[], []
    for i in range(n): # 0 1 2
        val90, val180, val270 = '', '', ''
        for j in range(n): # 0 1 2
            # i = 0, n-j-1 | 2, 1, 0
            # i = 1, n-j-1 | 2, 1, 0
            # i = 2, n-j-1 | 2, 1, 0
            val90 += str(arr[n-j-1][i])
            #  n-i-1 | 2,  n-j-1 | 2, 1, 0
            #  n-i-1 | 1,  n-j-1 | 2, 1, 0
            #  n-i-1 | 0,  n-j-1 | 2, 1, 0
            val180 += str(arr[n-i-1][n-j-1])
            #  n-i-1 | 2,  2 -> j| 0, 1, 2
            #  n-i-1 | 1,  1 -> j| 0, 1, 2
            #  n-i-1 | 0,  0 -> j| 0, 1, 2
            val270 += str(arr[j][n-i-1])
        result.append(val90)
        result.append(val180)
        result.append(val270)

    # 요구대로 출력(gpt 도움 받음)
    print(f'#{tc}')
    for i in range(0, len(result), 3):
        for j in range(i, i+3):
            print(result[j], end=' ')
        print()



