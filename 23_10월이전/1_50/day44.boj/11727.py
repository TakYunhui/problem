'''
1 : 1
2 : 3
3 : 5
4 : 11
'''
n = int(input())
dp = [0] * (n)
dp[0] = 1
if n > 1:
    dp[1] = 3
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007
print(dp[n-1])