# DP로 팩토리얼 구현
def fac(n):
    dp = [0] * (n+1)
    dp[0] = 1
    # dp[] 각 숫자에 맞는 숫자 넣기
    for i in range(1, n+1):
       dp[i] = i
    # 팩토리얼 계산 반복문
    for i in range(1, n+1):
        dp[i] = dp[i] * dp[i-1]
    return dp[-1] # 가장 마지막 숫자가 결과값
n = int(input())
# N!에서 뒤에서 처음 0이 아닌 숫자가 나올 때까지의 0의 개수
# 주어진 숫자(int)를 str로 변환, 뒤부터 살피며 0이 아니면 break
target = str(fac(n))[::-1]
cnt = 0
for i in target:
    if int(i) == 0:
        cnt += 1
    else:
        break
print(cnt)
