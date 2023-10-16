def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a , b)


s = input()
t = input()
# 문자열길이
ss = len(s)
tt = len(t)
# 1번째 시도: 길이 비교 후 긴 쪽에서 짧은쪽 패턴이 반복되는지 확인
# 무한번 반복하는 수열이기에 이 접근은 잘못됐다
# 최소공배수 이용
tmp = lcm(ss, tt)
# 최소공배수에서 길이만큼 나누어 몇배 할 지 찾음
ss = tmp//ss
tt = tmp//tt
# 각각을 곱해서 같은 형태가 되는지 확인
if s * ss == t * tt:
    print(1)
else:
    print(0)