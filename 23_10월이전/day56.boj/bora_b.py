import sys
input = sys.stdin.readline
n, m, p = map(int, input().split()) # 적군 수, 각 기지 층수, 현재 전투력
cnt = 0  # -1 아이템 개수 카운트
check = True  # 모든 적 처치 여부 (기본: True)
for _ in range(n):
    data = list(map(int, input().split()))
    data.sort()

    for i in data:
        if i == -1:
            cnt += 1
    else:
        if p >= i:
            p += 1
        else:
            while cnt:
                cnt -= 1
                p *= 2
                if p >= i:
                    break
            if p >= i:
                p += i
            else:
                check = False
        while cnt:
            cnt -= 1
            p *= 2

if check:
    print(1)
else:
    print(0)


