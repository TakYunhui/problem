# 상의 n, 하의 n벌 1, 2, ..., i번째의 색깔
# 서로 다른 색상인 조합
# 조합: n! // (n-r)!r!
def fac(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = i * dp[i-1]
    return dp[n]
n = int(input())
if n == 1:
    print(0)
else:
    print(fac(n)//(fac(n-2)))