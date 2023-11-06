# 5000개의 버스 정류장
# 버스 노선 N 개, i번째 버스노선은 A 이상 B이하 모든 정류장을 다닌다
# 1 <= A <= B <= 5000
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001 # 1-5000번 각 정류장을 지나는 노선 수

    for _ in range(N): # N개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1 # 현재 노선이 i번 정류장을 지나면 + 1
    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]

    print(f'#{tc}', end=' ')
    for x in bus_stop:
        print(cnt[x], end=' ')
    print()