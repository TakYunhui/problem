n = int(input())
dp = [0] * 51
dp[0], dp[1] = 1, 1
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % (int(1e9) + 7)
print(dp[n])
