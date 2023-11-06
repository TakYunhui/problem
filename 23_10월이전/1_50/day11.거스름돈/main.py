n = int(input())
count = 0

while n:
    if n < 2:
        break
    elif n >= 5:
        count += 1
        n -= 5
        print(n)
    elif n >= 2:
        count += 1
        n -= 2
        print(n)


print(count)
