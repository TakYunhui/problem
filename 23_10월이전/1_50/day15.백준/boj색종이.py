
# 색종이 개수
n = int(input())
# 색종이 붙여질 초기 영역 (이 시작점부터 10칸씩 자리 차지)
sections = [list(map(int, input().split())) for _ in range(n)] # [[3, 7] , [15, 7]]
# 100 x 100의 흰색 도화지
white = [[0] * 100 for _ in range(100)]

for sec in sections:
    for x in range(sec[0], sec[0]+10): # 10칸 완료
        for y in range(sec[1], sec[1]+10):
            white[x][y] = 1 # 색종이 붙이기

# 검은 색 영역 구하기( 1을 갖는 위치 개수 카운트)
result = 0
for x in range(100):
    for y in range(100):
        if white[x][y] == 1:
            result += 1
print(result)
