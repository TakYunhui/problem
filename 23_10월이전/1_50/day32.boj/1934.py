# 최소공배수
def gcd(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def lcm(a, b):
    return (a*b) // gcd(a, b)



a, b = map(int, input().split())
print(lcm(a, b))