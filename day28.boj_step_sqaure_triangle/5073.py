while True:
    three = list(map(int, input().split()))
    if three[0] == 0 and three[1] == 0 and three[2] == 0:
        break
    copy = three[:]
    max_v = max(three)
    three.remove(max_v)
    # 삼각형 조건 만족 못할 시
    if sum(three) <= max_v:
        print('Invalid')
    else:
        # 세 변의 길이가 모두 같음
        if copy[0] == copy[1] and copy[1] == copy[2] and copy[2] == copy[0]:
            print('Equilateral')
        # 세 변의 길이가 모두 다름
        elif copy[0] != copy[1] and copy[1] != copy[2] and copy[2] != copy[0]:
            print('Scalene')
        # 나머지
        else:
            print('Isosceles')

