while True:
    case = list(map(int, input().split()))
    if case == [0, 0, 0]:
        break
    # 마지막 인덱스의 변이 항상 크다는 보장 x
    # 가장 큰 값을 따로 추출
    max_num = max(case)
    case.remove(max_num)
    if max_num ** 2 == (case[0] ** 2) + (case[1] ** 2):
        print('right')
    else:
        print('wrong')

