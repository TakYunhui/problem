# 스택에 원소를 넣었다 빼는 것은 무시 (결과가 똑같)
from collections import deque
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
q = deque()

for i in range(n):
    if a[i] == 0:
        q.appendleft(b[i])
for i in range(m):
    q.append(c[i])
    print(q.popleft(), end=' ')

