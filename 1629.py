a, b, c = map(int, input().split())
''' 분할정복
- b 짝수 
2 ** 10 == (2 ** 5) * (2 ** 5) 
- b 홀수
2 ** 11 == (2 ** 5) * (2 ** 5) * 2
'''
# ( a ** b ) % c
def DaC(a, b):
    if b == 1:
        return a % c

    tmp = DaC(a, b // 2)
    if b % 2 == 0: # 짝수면 tmp * tmp
        return (tmp * tmp) % c
    else: # 홀수면(지수 짝수에 +1)이면 a까지 곱하고 나누기
        return (tmp * tmp * a) % c
print(DaC(a, b))