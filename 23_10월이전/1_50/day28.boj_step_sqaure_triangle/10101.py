angle = [int(input()) for _ in range(3)]
# 세 각의 합이 180이 아니라면 에러
if sum(angle) != 180:
    print('Error')
else:
    # 3개, 2개, 같은 각도가 없는 경우 체크
    check = True
    I = 0
    S = 0
    for i in angle:
        # 60도가 아닌 게 나오면 정삼각형 x
        if i != 60:
            check = False
        # 같은 각이 2개인 게 있다면
        if angle.count(i) == 2:
            I = 1
        # 모든 각이 다르다면
        if angle[0] != angle[1] and angle[1] != angle[2] and angle[2] != angle[0]:
            S = 1
    if check == True:
        print('Equilateral')
    if I == 1:
        print('Isosceles')
    if S == 1:
        print('Scalene')



