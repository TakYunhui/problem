'''
1 -> 1
2 -> 2
3 -> 4
4 -> 7 (1 + 2 + 4)
5 -> 13 (2 + 4+ 7)
6 -> 24 (4 + 7 + 13)
'''

t = int(input())
# dp 점화식
dp = [0] * (11)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# 테스트 케이스 별 결과 출력
for _ in range(t):
    n = int(input())
    print(dp[n])
