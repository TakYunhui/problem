'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    # 오름차순
    ascending = sorted(nums)
    # descending = sorted(nums, reverse=True)
    # 특별한 정렬
    special = []
    for i in range(n):
        if len(special) == 10:
            break
        special.append(ascending.pop())
        special.append(ascending.pop(0))

    print(f'#{tc}', *special)