# 빙고 - 선이 3개 이상 그어지는 순간 승리!
# 몇 번째 수를 부른 후 빙고를 외치는 가?
# 데이터 입력
# 5 x 5 빙고판
arr = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 수
nums = [list(map(int, input().split())) for _ in range(5)]

# 1. 빙고 체크하기
# 2. 체크한 개수가 빙고가 되는지 확인하기
# - 가로, 세로, 대각선 좌편향 우편향 총 4가지 체크
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if nums[i][j] == arr[k][l]:
                    # print(nums[i][j])
                    arr[k][l] = 'v'
            # print(k, col_idx)
    # print(arr)
    # 한 줄 영역마다 카운트하는 지정 조건이 필요
    # 델타탐색? -> 굳이? 대각선은 어차피 사용하기 어려움
    # 그냥 range 범위를 5개씩 들어가게 보기
    # 행/열 이중 for문
    # 행 탐색: [0][0~4], [1][0~4] ...
    # 열 탐색: [0~4][0], [0~4][1] ...
    bingo = 0
    for x in range(5):
        row_cnt = 0
        for y in range(5):
            if arr[x][y] == 'v':
                row_cnt += 1
            else:
                break
        if row_cnt == 5:
            bingo += 1
    for x in range(5):
        col_cnt = 0
        for y in range(5):
            if arr[x][y] == 'v':
                col_cnt += 1
            else:
                break
        if col_cnt == 5:
            bingo += 1
    # 대각선(좌시작): 00 11 22 33 44
    # 대각선(우시작): 04 13 22 31 40
    d1, d2 = 0, 0
    for i in range(5):
        if arr[i][i]=='v':
            d1 += 1
        if arr[i][4-i]=='v':
            d2 += 1
    if d1 == 5:
        bingo += 1
    if d2 == 5:
        bingo += 1
    print(bingo)
















    # 아래 방식대로 세면 한 줄의 빙고 세는 게 아니라 전체 리스트의 v 개수를 세버림
    # v_cnt = 0
    # for x in range(5):
    #     for y in range(5):
    #         if arr[x][y] == 'v':
    #             v_cnt += 1
    #     print(arr, v_cnt)
    # print()










