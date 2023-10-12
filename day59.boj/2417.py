import math
n = int(input())
tmp = math.isqrt(n) # isqrt : 정수 제곱근 반환
if tmp ** 2 != n:
    tmp += 1
print(tmp)