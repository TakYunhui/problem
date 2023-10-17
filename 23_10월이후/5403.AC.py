from collections import deque
import sys
input = sys.stdin.readline
def sol(cmds, lst):
    r_cnt = 0
    lst = deque(lst)
    for cmd in cmds:
        if cmd == 'R':
            r_cnt += 1
        elif cmd == 'D':
            if not lst:
                print('error')
                return
            else:
                if r_cnt % 2: # 홀수면
                    lst.pop()
                else:
                    lst.popleft()
    if r_cnt % 2:
        lst.reverse()
        print('['+','.join(lst)+']')
    else:
        print('['+','.join(lst)+']')


t = int(input())
for _ in range(t):
    cmds = input()
    n = int(input())
    nums = input()
    q = deque()
    data = []
    for x in nums:
        if x.isdigit():
            q.append(x)
        elif x == ',':
            b = ''
            while q:
                a = q.popleft()
                b += a
            data.append(b)
    b = ''
    if q:
        while q:
            a = q.popleft()
            b += a
        data.append(b)
    sol(cmds, data)
