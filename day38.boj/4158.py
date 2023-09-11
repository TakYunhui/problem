import sys
input = sys.stdin.readline

# 여러 개의 테스트 케이스, 케이스 별로 출력
while True:
    n, m = map(int, input().split()) # 상근이, 선영이가 가진 cd의 수 n, m
    if n == 0 and m == 0:
        break
    sg = list(int(input()) for _ in range(n))
    sy = list(int(input()) for _ in range(m))

    cnt = 0
    for target in sg:
        start = 0
        end = m - 1
        while start <= end:
            mid = (start + end) // 2
            if sy[mid] == target:
                cnt += 1
                break
            elif sy[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
    print(cnt)