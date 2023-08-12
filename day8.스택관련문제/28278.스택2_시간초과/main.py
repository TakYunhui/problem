N = int(input())
stack = []


for i in range(N):
    cmd = input()
    # print(len(cmd))
    if len(cmd) > 2:
        stack.append(int(cmd[-1]))
    elif cmd == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == '3':
        print(len(stack))
    elif cmd == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
