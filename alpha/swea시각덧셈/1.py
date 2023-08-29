# 시각 2개를 입력 받아 더한 값을 시 분으로 출력
# 1시부터 12시제
# 시: 1~12, 분: 0~59
t = int(input()) # 테스트 케이스 개수
for tc in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2
    # 분합이 60분 넘는다면
    if m >= 60:
        # 시간 + 1, 60분 빼기
        h += 1
        m -= 60

    # 시간 합이 12가 넘는다면
    if h > 12:
        # 12로 나누어 나온 몫
         h -= 12
    result = str(h) + ' ' + str(m)
    print(f'#{tc} {result}')