import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 동전 가치(타입)이 들어갈 list
coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True) # 큰 수부터 정렬(내림차순)

# 최종 횟수가 들어갈 total
total = 0
# 큰 값의 동전부터 살펴보면서
for coin in coins: 
    if coin <= k:   # 만약 k와 같거나 작은 수라면 
        result = k // coin # 해당 동전이 k에 들어갈 수 있는 개수(횟수) 구하기
        k -= coin * result # k - 해당 동전 * 개수 값 빼주기 
        total += result    # total 동전이 들어갈 횟수 누적 count 해주기 
        result = 0  # result 반복 실행시마다 초기화 
print(total)
