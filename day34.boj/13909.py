# 규칙성 : 111 22222 3333333 444444444
# 변화 지점: 1, 4, 9, 16, 25 -> 1, 2, 3, 4, 5의 제곱수
import sys
input = sys.stdin.readline
n = int(input())
result = 0
x = 1
while x*x <= n:
    x += 1
    result += 1
print(result)