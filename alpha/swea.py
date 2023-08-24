# n개의 과목 시험
# k개의 과목 선택해 넣어서 가장 큰 총점 구하기
from itertools import combinations
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    tmp = list(combinations(scores, k))
    print(tmp)
    total = []
    for i in tmp:
        total.append(sum(i))

    print(f'#{tc} {max(total)}')