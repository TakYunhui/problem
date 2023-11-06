# 가지치기 - 유망성 조사
# r : 현재 조사한 원소 개수
# 기본 순열문제 
def perm(r, acc):
    global result
    if acc <= result:
        return
    # 종료 시점
    if r == n:
        if acc > result:
            result = acc
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                perm(r+1, acc * arr[r][i])
                visited[i] = False

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 값의 개수
    visited = [0] * n # 방문 여부 체크
    # 비교 대상군 -> 0 (최댓값을 구할 것이기에 점점 커질 듯)
    result = 0
    # 각 정수 Pi = 확률
    # 70 => 0.7
    arr= [list(map(lambda x: int(x)/100, input().split())) for _ in range(n)]
    perm(0, 1)
    result *= 100
    print(f'#{tc} {result:7f}')