n = int(input())
while n:
    if n % 30 == 0:
        print(n)
        break
    n = str(n)
    if '0' not in n:
        print(-1)
        break
