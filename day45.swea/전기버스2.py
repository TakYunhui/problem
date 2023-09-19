# acc : 충전 횟수
def search(r, acc): # r : 사용한 원소의 개수
    global result
    # 종료 시점 : 내 버스가 종점에 도착한 상황
    if r == n-1:
        # 여기까지 오시는데 충전 몇 번 하셨습니까?
        if acc < result:
            result = acc
    else:
        search(r+1, acc+1)
        search(r+1, acc)

t = int(input())
for tc in range(1, t+1):
    n, *arr = list(map(int, input().split()))
    # 모든 정류소에서 다 충전한 게 worst
    result = n
    search(0, 0)
    print(result)