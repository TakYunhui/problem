n = int(input())
length = 4 * n - 3
stars = [[' ' for _ in range(length)] for _ in range(length)]

def sol(n, x, y):
    if n == 1:
        stars[x][y] = '*'
        return
    # n이 재귀돌면서 변하기 때문에 length를 함수 안에서 다시 계산해줘야한다
    length = 4 * n -3
    for i in range(length):
        stars[x][y+i] = '*' # 첫번째 행 전부 '*' 처리
        stars[x+i][y] = '*' # 첫번째 열 '*' 처리
        stars[x+length-1][y+i] = '*' # 마지막 행 '*' 처리
        stars[x+i][y+length-1] = '*' # 마지막 열 전부 '*' 처리

    sol(n-1, x+2, y+2)


sol(n, 0, 0)
for s in stars:
    print(''.join(s))