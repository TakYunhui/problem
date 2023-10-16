def fibo(n):
    dp = [0] * (n+3)
    dp[1], dp[2] = 1, 1
    if n > 2:
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]
n = int(input())
print(fibo(n))
