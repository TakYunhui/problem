# n * m 크기의 집터
# b : 인벤토리 안 블록 개수
n, m, b = map(int, input().split())
# n * m 땅의 높이 데이터
data = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
