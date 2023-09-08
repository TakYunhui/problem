def fibo(n):
    dp = [0] * (n+2)
    if n == 0:
        return 0
    else:
        dp[1], dp[2] = 1, 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
n = int(input())
print(fibo(n))
