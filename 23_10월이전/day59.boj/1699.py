n = int(input())
squares = [i ** 2 for i in range(1, 317)]
dp = [0] * (n+1) # n번까지 dp 생성
 # 최소값 비교할 변수, 양의 무한대
for i in range(1, n+1): # 1번부터 n번까지
    # 현재 숫자가 제곱수면 1로 표현
    if i in squares:
        dp[i] = 1
    # 제곱수가 아니라면 제곱수인 수들을 빼주며 합이 i를 이루는 최소 개수 구함
    else:
        # value 완전히 밖에 빼면 적은 수로 갱신된 값이 고정되어서 올바른 비교 x
        # 계속 해서 value와 케이스 별 최소값 비교해야하므로 반복 돌리기 전 초기값 지정
        value = float('inf')
        for j in squares:
            if j > i:
                break
            # i - j 가 양수일 때만. . .
            if i - j > 0:
                # 현재 value보다 작은 값 있는지 확인
                value = min(value, dp[i-j])
            # 1 더해주는 이유? 제곱수들의 합 = 제곱수 하나 + 나머지 제곱수들의 합
            dp[i] = value + 1
print(dp[n])