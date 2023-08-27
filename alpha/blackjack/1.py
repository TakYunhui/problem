# n: 카드 개수, 찾을 값: m
# 카드 세 장의 합이 m을 넘지 않는 최댓값
n, m = map(int, input().split())
cards = list(map(int, input().split()))
maximum = 0
# 3장 씩 합하는 경우의 수 모두 구하는 범위 지정
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            # k 반복 한 번에 3장의 합을 바로 구하므로
            # k 실행할 때마다 초기화 선언
            black_jack = 0
            black_jack += cards[i] + cards[j] + cards[k]
            # blackjack 을 현재 for문에서 바로 구하니
            # 여기서 if문으로 m보다 작거나 같은지 확인
            if black_jack <= m:
                # 조건에 맞다면 최댓값 비교
                maximum = max(maximum, black_jack)
print(maximum)
