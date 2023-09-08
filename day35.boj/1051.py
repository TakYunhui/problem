import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# 주어진 직사각형
arr = [list(map(int, input().rstrip())) for _ in range(n)]
# 정사각형 한 변의 길이 -> 주어진 길이 중 최솟값 부터 가능
side = min(n, m) - 1
# 시작점 기준 꼭짓점 방향
d = [(0, 1), (1, 0), (1, 1)]
result = 1 # 가능한 가장 큰 변의 길이가 들어갈 변수
while side:
    for i in range(n - side + 1):
        for j in range(m - side + 1):
            dot = arr[i][j]
            count = 1 # 시작점 1개 를 초깃값으로 지정
            for k in range(3):
                ni = i + d[k][0] * side
                nj = j + d[k][1] * side
                # 구한 다음 위치가 범위 안이고, 그 위치의 수가 꼭짓점에 적힌 수가 같다면
                if ni < n and nj < m and arr[ni][nj] == dot:
                    count += 1
            # 꼭지점 4개가 다 같다면 정사각형의 크기(넓이) 넣어준다
            if count == 4:
                result = max(result, (side+1) ** 2)
    side -= 1
print(result)