# 1부터 N까지의 숫자 중 홀수는 더하고 짝수는 뺀 최종 결괏값
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if i % 2:
            result += i
        else:
            result -= i
    print(f'#{tc} {result}')