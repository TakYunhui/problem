import sys
input = sys.stdin.readline
n = int(input())
sell = dict()
# 책 제목 - 팔린 권수 연결한 딕셔너리
for _ in range(n):
    title = input()
    sell[title] = sell.get(title, 0) + 1
# value 중 최댓값 찾기(가장 많이 팔린 권수)
max_v = max(sell.values())
best = []
for k, v in sell.items():
    if v == max_v:
        best.append(k)
best = sorted(best) # 사전순 정렬
print(best[0]) # 가장 앞서는 하나만 출력

