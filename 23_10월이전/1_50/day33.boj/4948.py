import sys
input = sys.stdin.readline
def isprime(n):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input())
    # 0 입력시 종료
    if n == 0:
        break
    cnt = 0
    # n 보다 크고, 2n보다 작거나 같은 소수 찾기
    for x in range(n+1, 2*n+1):
        if isprime(x):
            cnt += 1
    print(cnt)

