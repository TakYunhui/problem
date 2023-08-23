# 거스름돈 최소 개수
# 높은 금액의 돈을 우선적으로 지급
# 이때, 계산 금액보다는 지급할 잔돈이 작거나 같아야 함
t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 계산 금액
    S_changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 잔돈 종류

    # 금액이 0원이 될 때까지 계산 반복 실행
    total_cnt = []  # 각 동전 사용 개수가 들어갈 빈 리스트
    for change in S_changes: # 높은 금액의 동전부터 보면서
        cnt = 0 # 동전 개수는 반복할 때마다 0개로 초기화
        if n >= change: # 계산금액이 잔돈과 같거나 크다면
            cnt = n // change   # 사용될 동전 개수 = 금액 // 잔돈
            n -= cnt * change   # 금액 - (잔돈 동전 * 사용 개수)
            # print(n, cnt, cnt*change, total_cnt)
        total_cnt.append(cnt)
    print(f'#{tc}')
    print(*total_cnt)
