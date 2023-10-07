t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cnt2, cnt3, cnt5, cnt7, cnt11 = 0, 0, 0, 0, 0
    while n > 0:
        if n < 2:
            break
        if n % 2 == 0:
            cnt2 += 1
            n /= 2
        elif n % 3 == 0:
            cnt3 += 1
            n /= 3
        elif n % 5 == 0:
            cnt5 += 1
            n /= 5
        elif n % 7 == 0:
            cnt7 += 1
            n /= 7
        elif n % 11 == 0:
            cnt11 += 1
            n /= 11
    print(f'#{tc} {cnt2} {cnt3} {cnt5} {cnt7} {cnt11}')


