t = int(input())
for _ in range(t):
    message = list(input())
    r, c = int(message.pop(0)), int(message.pop(1))

    message.pop(0)
    message.pop(0)
    # 공백 살리기
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
    # print(trans)
    # 구한 이진수 값들을 r, c 행열에 넣을 것
    # snail로 행열에 값 넣기
    trans = list(trans) # trans.pop(0)
    result = [[0]*c for _ in range(r)] # 열(가로 개수) x 행(세로 개수)
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num = r * c
    x, y = 0, 0
    i = 0
    # print(trans)
    # result[0][0] = trans.pop(0)
    while trans:
        if not result[x][y]:
            result[x][y] = trans.pop(0)
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < r and 0 <= ny < c and not result[nx][ny]:
            result[nx][ny] = trans.pop(0)
            x, y = nx, ny
        else:
            i = (i+1)%4
    # print(result)
    for i in result:
        print(''.join(i),end='')
    print()

