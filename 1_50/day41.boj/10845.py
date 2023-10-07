from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()
    direct = cmd[0]

    if direct == 'push':
        q.append(int(cmd[1]))
    elif direct == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif direct == 'size':
        print(len(q))
    elif direct == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif direct == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif direct == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)