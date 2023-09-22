def backtracking(product, idx):




t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 제품 수
    # 제품 별 생산 비용 -> n줄에 걸쳐 입력
    cost = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n # 방문 여부 체크, 따로 번호 맞출 것 없이 개수에 맞추므로 그냥 n개
    result = int(1e9) # 최종 결과값 - 값들을 비교해 최소 비용을 넣을 것이므로 임의의 큰 수 지정

    print(f'#{tc} {result}')