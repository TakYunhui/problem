import sys
input = sys.stdin.readline
n = int(input())
dp = [-float('inf')] * n
nums = list(map(int, input().split()))

for i in range(n):
    dp[i] = nums[i]
    if i >= 1:
        dp[i] = max(dp[i], dp[i]+dp[i-1])
print(max(dp))


