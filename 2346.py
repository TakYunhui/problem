# 1번부터 N개의 풍선
# i -> i + 1 .... n -> 1번 풍선
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
ballons = list(map(int, input().split()))
# 풍선 순서와 풍선 안 종이 갯수 연결
q = deque()
for i in range(n):
    q.append((i+1, ballons[i]))

result = []
val = q.popleft() # 가장 앞에 있는 풍선 터뜨려서 나온 종이
result.append(val[0])
while q:
    if 0< val[1] < n: # 풍선 안 종이가 양수면
        for i in range(val[1] -1):
             q.append(q.popleft())
        val = q.popleft()# val -1 만큼 이동시키고 가장 앞 풍선 터뜨리기
        result.append(val[0])
    elif val[1] >= n:
        val[1] -= n
        for i in range(val[1]-1):
            q.append(q.popleft())
        val = q.popleft()
        result.append(val[0])
    else:
        if abs(val[1]) < n:
            for i in range(abs(val[1])-1):
                q.appendleft(q.pop())
            val = q.pop()
            result.append(val[0])
        else:
            tmp = abs(val) - n
            for i in range(tmp):
                q.appendleft(q.pop())
            val = q.pop()
            result.append(val[0])
    print(q, result)
print(*result)



