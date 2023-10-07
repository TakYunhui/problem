import heapq
import sys
input = sys.stdin.readline
pq = []

n = int(input())
for _ in range(n):
    x = int(input())
    if pq and x == 0:
        print(-heapq.heappop(pq))
    elif not pq and x == 0:
        print(0)
    else:
        heapq.heappush(pq, -x)