def fac(n):
    if n == 0:
        return 1
    return  fac(n-1) * n

n = int(input()) # 0보다 크거나 같은 정수
print(fac(n))