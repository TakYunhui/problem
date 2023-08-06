import sys
input = sys.stdin.readline


# 흰 도화지 2차원 리스트 생성
white = [[0] * 100 for _ in range(100)]
# 색종이 수
n = int(input())
# 검은색 종이가 붙여질 위치 받는리스트
blacks = [list(map(int, input().split())) for _ in range(n)]
# print(blacks)

for black in blacks:
    # black x 축 범위
    # 이때 주어진 숫자는 좌표가 아니다!
    # 즉, 해당하는 칸만큼 색칠되는 거니까 인덱스로 세면 됨
    for x in range(black[0], black[0]+10):
        for y in range(black[1], black[1]+10):
            white[x][y] = 1

# 위에서 white 에 해당하는 영역만큼 검은색이 된다
# 이제 100 x 100 도화지 안에서 검은색이 된 영역의 넓이
# 즉, 1의 개수를 세면 된다
area = 0
for i in range(100):
    for y in range(100):
        if white[i][y] == 1:
            area += 1
print(area)
