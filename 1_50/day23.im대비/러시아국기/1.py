t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    # flag 한 줄씩 받아와 리스트에 하나의 문자열로 넣기
    flag = [input() for _ in range(n)]
    print(flag)
    # 각 색깔 별로 가장 많이 존재하는 수를 저장할 변수
    maximum = 0
    # 첫째 줄, 마지막 줄 -> w, r 고정
    for i in range(n-2):
        # 완전 탐색 횟수
        for j in range(i+1, n-1):
            cnt = 0
            for k in range(i+1): # 흰색은 1줄 넣고 시작
                cnt += flag[k].count('W')
            for k in range(i+1, j+1): # 파란색은 중간 범위
                cnt += flag[k].count('B')
            for k in range(j+1, n): # 빨간색은 끝까지
                cnt += flag[k].count('R')
            # k번째 깃발색에서 각 색깔들 개수 탐색하여 누적합
            # 누적합이 큰 쪽을 최댓값으로 넣는다
            maximum = max(maximum, cnt)
    # 결괏값: 칠하는 수가 가장 적은 경우
    # => 전체 - 각 색깔들 수가 가능한 범위에서 가장 큰 경우 
    print(f'#{tc} {n*m - maximum}')