import sys
import heapq
input = sys.stdin.readline

pq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if not pq and x == 0:
        print(0)
    elif pq and x == 0:
        print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, x)