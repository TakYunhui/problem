import sys
sys.stdin = open('input (1).txt')

# 붉은 자성체 N(1) -> S극:하 이동
# 푸른 자성체 S(2) -> N극:상 이동
# 세로 열 모양으로 한 줄씩 본다
# 이동하는 길에 다른 자성체 없으면 사라짐
# 이동하는 길에 하나라도 있으면 교착 상태
# 교착 상태의 예시
# 1. 1 2 1 2 -> 2개
# 2. 1 2     1 2 -> 2개
# 3. 221    -> 1개
for tc in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if table[i][j] == 1:
                pass

            elif table[i][j] == 2:
                pass

    print(f'#{tc}')