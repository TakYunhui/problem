import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    pigs = list(map(int, input().split()))
    cnt = 1
    while n >= sum(pigs):
        cnt += 1
        today = [0] * 6
        for i in range(6):
            # 인덱스 초과가 나올 수 있는 더하기 연산은 나머지 연산자로 인덱스 값 구하기
            today[i] += pigs[i] + pigs[i-1] + pigs[(i+1)%6] + pigs[(i+3)%6]
        # 추가된 돼지 사료양으로 갱신
        pigs = today
    print(cnt)

