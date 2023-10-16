# DP를 이용한 팩토리얼 구현
def fac(n):
    dp = [1] * (n+1)
    if n > 0:
        for i in range(1, n+1):
            dp[i] = i * dp[i-1]
    return dp[n]

n = fac(int(input()))
# 문자열로 변환하여 뒤집기
# why? 뒤에서부터 0이 아닌 숫자가 나올 때까지 0을 셀 거기 때문이다
n = str(n)[::-1]
cnt = 0
for i in n:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)