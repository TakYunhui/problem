T = int(input())

for tc in range(T):
    data = input()
    stack = []
    for i in range(len(data)):
        if stack:
            if data[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(data[i])

        else:
            stack.append(data[i])
    if stack:
        print('NO')
    else:
        print('YES')