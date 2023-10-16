# 9 x 9 격자판
# 81개의 자연수 또는 0
# 최댓값을 찾고 최댓값의 행 열 위치 구하기 

# 1. 데이터 입력 - 한 줄에 아홉 개씩 
# 100보다 작은 자연수 또는 0
import sys
input = sys.stdin.readline
# 받아오는 정수 값이 들어갈 2차원 리스트 arr
arr = list([0 for _ in range(9)] for _ in range(9))
for i in range(9):
    arr[i] = list(map(int, input().split()))  # 한 줄씩 arr에 넣어줌

# 2. 최댓값 찾기
max_v = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_v:  # 최댓값 비교
            max_v = arr[i][j]
        if arr[i][j] == max_v: # 최댓값이면 해당 행 열 인덱스 구함
            max_row = i + 1    # 1행, 1열부터 시작하는데 인덱스를 구했으니
            max_col = j + 1    # +1 해준다
print(max_v) 
print(max_row, max_col)

