from collections import deque
import sys
input = sys.stdin.readline
q = deque()
n = int(input())
for _ in range(n):
    cmd = list(input().split())
    c = cmd[0]
    if c == 'push':
        q.append(cmd[1])
    elif c == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)