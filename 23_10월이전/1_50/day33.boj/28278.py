import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    cmd = list(map(int, input().split()))
    c = cmd[0]
    if c == 1:
        stack.append(cmd[1])
    elif c == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c == 3:
        print(len(stack))
    elif c == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)

