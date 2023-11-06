import sys
sys.stdin = open('input.txt')

def check():
    n = 100
    while n > 1:
        for i in range(100): # 0 ... 99
            for j in range(100-n+1): # 1 -> 0, 2 -> 0 1
                # [0][0:100] [0][0:99] [1:100]
                # 가로 세로 슬라이싱으로 한 줄의 모든 길이의 단어 가져와봄
                # 최대 길이인 100부터, 즉 큰 수부터 내림차순으로 살핌
                check_row = row_target[i][j:j+n]
                check_col = col_target[i][j:j+n]
                for k in range(n//2): # row 조사
                    # 범위를 절반으로 나누고
                    # 가장 앞부분 - 뒷부분 순서대로 매칭, 대칭 비교
                    if check_row[k] != check_row[n-k-1]:
                        break
                else: # 대칭이면 현재 단어의 길이 반환
                    return n
                for k in range(n//2):
                    if check_col[k] != check_col[n-k-1]:
                        break
                else:
                    return n
        n -= 1 # n 1씩 감소하며 경우의 수 계산
    return 1 # 1 이상의 길이 회문이 없으면 1

for t in range(1, 11):
    tc = int(input())
    # 가로, 세로 탐색할 이차원 배열
    row_target = [list(input()) for _ in range(100)]
    col_target = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            col_target[i][j] = row_target[j][i]

    print(f'#{tc} {check()}')