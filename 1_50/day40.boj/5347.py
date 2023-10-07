n = int(input())
def gcd(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b



for _ in range(n):
    a, b = map(int, input().split())
    print((a * b) // gcd(a, b))