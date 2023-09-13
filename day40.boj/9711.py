import sys
input = sys.stdin.readline
# 피보나치 수열, 제한 범위 내 만들기 
dp = [0] * 10001
dp[1], dp[2] = 1, 1
for i in range(3, 10001):
    dp[i] = dp[i-2] + dp[i-1]

# 테스트케이스 별 
t = int(input())
for tc in range(1, t+1):
    p, q = map(int, input().split())
    # p번째 피보나치 수를 q로 나눈 값 출력
    result = dp[p] % q
    print(f'Case #{tc}: {result}')