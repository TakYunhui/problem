n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
# 현재까지에서 자기 자신을 포함하여 만들 수 있는
# 증가하는 부분 수열 구하기
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))