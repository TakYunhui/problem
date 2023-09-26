t = int(input())
for _ in range(t):
    r, c, *message = input().split()
    r, c = int(r), int(c)

    # 공백 살리기
    message = ' '.join(message)
    # 문자 하나씩 이진수로 변환 (공백부터 Z까지)
    trans = ''
    for char in message:
        if char == ' ':
            char = 0
        else:
            char = ord(char) - 64
        char = format(char, 'b')
        if len(char) < 5:
            for i in range(5-len(char)):
                char = '0' + char
        trans += char

    if len(trans) < r * c:
        trans += '0' * (r * c - len(trans))
    # print(trans)
    # 구한 이진수 값들을 r, c 행열에 넣을 것
    # snail로 행열에 값 넣기
    trans = list(trans) # trans.pop(0)
    result = [[0]*r for _ in range(c)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num = r * c
    x, y = 0, 0
    i = 0
    result[0][0] = trans.pop(0)
    while trans:
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < c and 0 <= ny < r and not result[nx][ny]:
            result[nx][ny] = trans.pop(0)
            x, y = nx, ny
        else:
            i = (i+1)%4
    print(result)
    # for i in result:
    #     print(''.join(i),end='')
    # print()

