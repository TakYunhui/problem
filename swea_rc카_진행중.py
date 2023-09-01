# rc 카의 이동거리 계산
# 0: 현재 속도 유지
# 1: + 가속 속도 * 시간
# 2: - 감속 속도 * 시간
# 1, 2 -> 가속도의 값 추가
# 현재 속도보다 감속 속도가 더 크면 속도 -> 0
# 거리 계산 : 속도 * 시간
import sys
sys.stdin = open('input.txt')
t = int(input())
for tc in range(1, t+1):
    now = 0
    distance = 0
    n = int(input()) # 받을 명령어 수
    # n개 의 command 받아오기
    cmd = [list(input().split()) for _ in range(n)]
    # 1초부터 n초까지 시간 동안 거리 구할 것
    # i : 시간(초), cmd[i-1] : 해당 초의 명령어 리스트
    for i in range(1, n+1):
        if len(cmd[i-1]) == 2: # 가속 또는 감속 명령
            # 가속, 속도 더해주기
            if cmd[i-1][1] == 1:
                pass
            # 감속, 속도 빼주기
            else:
                pass
        # 현상 유지, 속도 변화 x
        else:
            pass
        # 구한 현재 속도 기준 거리 구하기








    print(f'#{tc}')