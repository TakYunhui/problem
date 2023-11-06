import sys
sys.stdin = open('input.txt')
t = int(input())
for tc in range(1, t+1):
    # 퍼즐 가로 세로 길이 n, 찾을 단어의 길이
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 범위 안 가능한 빈칸 세기 -> 모두 list에 저장
    # 만약 0을 만나면 칸 수를 reset하여 다시 탐색
    cnt = 0
    result = []
    # 가로 탐색
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt:
                    result.append(cnt)
                cnt = 0
        if cnt:
            result.append(cnt)
        cnt = 0

    # 세로 탐색
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            elif arr[j][i] == 0:
                if cnt:
                    result.append(cnt)
                cnt = 0
        if cnt:
            result.append(cnt)
        cnt = 0
    number = 0
    for i in result:
        if i == k:
            number += 1
    print(f'#{tc} {number}')