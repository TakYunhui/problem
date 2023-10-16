t = int(input()) # 테스트 케이스 수
for _ in range(t):
    s = list(input())
    stack = []
    for x in s:
        if stack:
            if stack[-1] == '(' and x == ')':
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)

    if stack:
        print('NO')
    else:
        print('YES')