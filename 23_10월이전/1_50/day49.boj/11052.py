import sys
input = sys.stdin.readline
n = int(input()) # 구매하려는 카드 개수
pack = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
# for 문 2개로 1~i 까지의 경우의 수 다 더해서 비교
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + pack[j])
print(dp[n])