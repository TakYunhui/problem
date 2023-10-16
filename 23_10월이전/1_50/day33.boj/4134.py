def prime(a):
    # 2부터 제곱근까지로 나누어서 나누어 떨어지면 소수 x
    for i in range(2, int((a**0.5)+1)):
        if a % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    # 같거나 큰 수 중 가장 작은 소수 구하기
    while True:
        # 0, 1의 경우 가능한 가장 작은 소수가 2!
        if n <= 1:
            print(2)
            break
        if prime(n):
            print(n)
            break
        n += 1




