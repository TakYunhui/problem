import sys
input = sys.stdin.readline
# 최대공약수 구하는 함수
def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b
# 테스트 케이스의 수
t = int(input())
for _ in range(t):
    # 정수 개수 n개, n개의 정수로 이루어진 배열
    n, *nums = map(int,input().split())
    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            result += gcd(nums[i], nums[j])

    print(result)
