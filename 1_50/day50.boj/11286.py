import heapq
import sys
input = sys.stdin.readline
pq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if pq:
            # 실제 정수만 출력하기 위해 인덱스 [1]처리
            print(heapq.heappop(pq)[1])
        else:
            print(0)
    else:
        # 절댓값 x , 정수 x 튜플로 넣어서
        # 절댓값 기준으로 우선순위 큐에서 정렬되게 한다
        heapq.heappush(pq, (abs(x),x))
