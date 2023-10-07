# 백트래킹(dfs + 가지치기)
def backtracking(idx, now): # 행, 현재 합
    global result # 글로벌 변수로 선언해 result 변경하기

    # 모든 경우의 수를 따져볼 때, 값이 안 되는 경우는 바로 종료(유망성 검사)
    # 최소 비용을 구할 것이므로 현재 합이 result보다 커지면 종료
    if now >= result:
        return

    # 현재 보고 있는 행 번호가 제품 수와 같아진다면 모든 행을 다 본 것이므로
    # 최소 비용을 넣고 함수 종료
    if idx == n:
        result = min(result, now)
        return

    # n만큼 순회하면서 공장 방문 여부 체크
    for i in range(n):
        if not visited[i]:
            # 아직 방문하지 않은 공장이라면 방문 체크 후에
            visited[i] = 1
            # 재귀호출하여 다음 상품을 찾아가 누적 비용 합을 구한다
            backtracking(idx+1, now+cost[idx][i])
            # 재귀호출이 종료되면 다시 방문 여부를 초기화해 다른 경우의 수에서 확인할 수 있도록 함
            visited[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 제품 수
    # 제품 별 생산 비용 -> n줄에 걸쳐 입력
    cost = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n # 방문 여부 체크, 따로 번호 맞출 것 없이 개수에 맞추므로 그냥 n개
    result = int(1e9) # 최종 결과값 - 값들을 비교해 최소 비용을 넣을 것이므로 임의의 큰 수 지정
    backtracking(0, 0)
    print(f'#{tc} {result}')