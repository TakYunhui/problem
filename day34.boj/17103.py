import sys
input = sys.stdin.readline
t = int(input())
nums = [int(input()) for _ in range(t)]
m = max(nums)
# 소수 리스트 만들기
prime = [False, False] + [True] * (m-1)
k = int(m ** 0.5) + 1
for i in range(2, k):
    if prime[i]:
        for j in range(i+i, m+1, i):
            prime[j] = False
# 만약 범위 안에서 현재 보는 수 & 주어진 숫자 - 현재 보는 수가 소수라면
# 두 소수의 합으로 짝수를 구성하는 것!
# 순서 다른 거 세지 않도록 . . .
for num in nums:
    result = 0
    for i in range(2, num //2 + 1):
        if prime[i] and prime[num - i]:
            result += 1
    print(result)