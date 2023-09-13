n = int(input()) # 숫자 개수
cards = list(map(int, input().split()))
# 숫자 카드와 개수 딕셔너리에 담기
dict1 = {}
for card in cards:
    # 해당 숫자 카드가 존재하면
    # 존재하는 값을 키로 지정하고 그 값에 +1
    dict1[card] = dict1.get(card, 0) + 1
print(dict1)
m = int(input())
find = list(map(int, input().split()))
# 찾아야 할 숫자들을 순회하면서
for i in find:
    # 해당하는 값이 있으면 연결된 value(개수) 가져오고
    # 없으면 0 을 가져온다
    print(dict1.get(i, 0), end=' ')