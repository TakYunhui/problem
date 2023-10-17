import heapq, sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input()) # q에 적용할 연산의 개수
    pq = []
    for _ in range(k):
        # 연산을 나타내는 문자 명령어, 정수 n
        cmd, n = input().split()
        n = int(n) # 정수 형 변환
        if cmd == 'I':
            heapq.heappush(pq, n)
        elif cmd == 'D' and pq:
            # 최솟값 삭제
            if n == -1:
                heapq.heappop(pq)
            # 최댓값 삭제
            elif n == 1:
                for i in range(len(pq)):
                    pq[i] = -pq[i]
                print(pq)
                a = heapq.heappop(pq)
                for i in range(len(pq)):
                    pq[i] = -pq[i]
        print(pq)
    # print(pq)

