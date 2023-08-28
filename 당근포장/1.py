# n개의 당근 -> 대/중/소
# 같은 크기의 당근은 같은 상자
# 빈 상자 x
# 한 상자에 n/2개를 초과하는 당근 x
# 각 상자에 든 당근 개수 차이 최소화 포장
# 포장 불가: -1, 포장 가능: 상자에 든 당근 개수차이가 최소일 때 차이값
import sys
sys.stdin = open('sample_in.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 당근 개수
    C = list(map(int, input().split())) # 당근 크기
    # 1차원 배열 3 개의 영역으로 나누기
    C.sort() # 당근 크기 오름차순 정렬
    min_v = 1000 # 포장별 최소 개수 차이
    # i -> n-3
    # j -> i+1, n-2
    # k -> j+1, n
    for i in range(n-2):
        for j in range(i+1, n-1):
            # 같은 크기 사이에 경계 두지 않는 조건
            if C[i] != C[i+1] and C[j] != C[j+1]:
                s = i+1 # 소 상자에 들어간 당근 개수
                m = j-i # 중 상자에 들어간 당근 개수
                l = n-1-j # 대 상자에 들어간 당근 개수
                # 한 상자에 절반을 초과해서 넣으면 안 됨
                if s <= n//2 and m <= n//2 and l <= n//2:
                    if min_v > (max(s, m, l) - min(s, m, l)):
                        min_v = (max(s, m, l) - min(s, m, l))
    # 포장할 수 없는 경우
    if min_v == 1000:
        min_v = -1
    print(F'#{tc} {min_v}')