'''
1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
'''
md = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
t = int(input())
for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    if m1 == m2:
        result = d2 - d1 + 1
    else:
        # 월이 다르면 그 차이 구해서 더하기
        gap = 0
        for i in range(m1, m2):
            gap += md[i]
        result = gap + (d2 - d1 + 1)
    print(f'#{tc} {result}')