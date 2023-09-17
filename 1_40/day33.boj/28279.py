from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    # 정수로 안 받고 그냥 문자열로 받았을 때 두 자리 수 이상도 분해된듯...
    cmd = list(map(int, input().split()))
    c = cmd[0]
    if c == 1:
        q.appendleft(cmd[1])
    elif c == 2:
        q.append(cmd[1])
    elif c == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif c == 5:
        print(len(q))
    elif c == 6:
        if q:
            print(0)
        else:
            print(1)
    elif c == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)