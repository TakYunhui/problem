import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # print(sudoku)

    # default: 겹치는 숫자가 없으면 1
    result = 1
    # swea스도쿠 검사
    # 검사 후 겹치는 숫자가 있으면 result = 0 업데이트
    # 1. 가로줄 9개인지 검사(열순회)
    for i in range(9):
        width = set()
        for j in range(9):
            width.add(sudoku[i][j])
        # print(len(width))
        if len(width) != 9:
            result = 0
            break
    # 2. 세로줄 9개인지 조사(행순회)
    for i in range(9):
        height = set()
        for j in range(9):
            height.add(sudoku[j][i])
        # print(len(height))
        if len(height) != 9:
            result = 0
            break
    # 3. 9칸 조사
    for i in range(0, 9, 3): # 0 / 3 / 6
        for j in range(0, 9, 3):
            area = set()
            for x in range(3):
                for y in range(3):
                    area.add(sudoku[i+x][j+y])
            if len(area) != 9:
                result = 0
                break
    print(f'#{tc} {result}')