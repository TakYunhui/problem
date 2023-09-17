# 기약분수: 분모와 분자를 두 수의 최대 공약수로 나누었을 때 만들어짐
a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return  a+b

head = a * d + c * b
body = b * d
div = gcd(head, body)

print(head // div, body // div)