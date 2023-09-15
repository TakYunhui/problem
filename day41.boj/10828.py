# 10828
import sys
input = sys.stdin.readline
stack = []
n = int(input())
for _ in range(n):
    cmd = input().split()
    direct = cmd[0]
    if direct == 'push':
        stack.append(int(cmd[1]))
    elif direct == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif direct == 'size':
        print(len(stack))
    elif direct == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif direct == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
