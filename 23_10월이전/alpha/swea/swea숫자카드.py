# 0 - 9까지 숫자가 적힌 N장의 카드
# 가장 많이 적혀있는 숫자 + 카드 장수
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = input()
    numbers = [i for i in range(10)] # 0 1 2 3 4 5 6 7 8 9

    cnt = [0] * (10) # 0부터 9까지의 숫자 각 개수 카운팅
    for card in cards:
        cnt[int(card)] += 1

    # 숫자 번호와 개수를 한 리스트 안에 튜플로 묶어줌
    result = []
    for i in range(10):
        result.append((numbers[i], cnt[i]))

    # 가장 많이 나온 카드 번호와 장 수가 들어갈 max_card 변수
    max_card = (0, 0)
    for i in result:
        if i[1] > max_card[1]:  # 만약 카드 장 수가 더 많으면
            max_card = i
        if i[1] == max_card[1]: # 카드 장 수가 같을 때는
            if i[0] > max_card[0]:  # 카드 번호가 더 큰 값을 넣어줌
                max_card = i
    print(f'#{tc} {max_card[0]} {max_card[1]}')

