def fib(n):
    global cnt
    if n == 0:
        cnt += 1
        return 0
    elif n == 1:
        cnt += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

t = int(input())
for _ in range(t):
    cnt = 0
    n = int(input())
    fib(n)
    print(cnt - fib(n), fib(n))