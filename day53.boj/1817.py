import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # 책, 박스 최대 중량
tmp = 0
box = 0
if n:
    books = list(map(int, input().split()))
    for i in books:
        # 책의 무게 확인
        tmp += i
        # 박스 최대 중량과 같다면 누적 무게 초기화, 상자 + 1개
        if tmp == m:
            tmp = 0
            box += 1
        # 박스 최대 중량보다 현재 누적 무게가 무겁다면, 상자 + 1개 추가 후
        # 현재 책의 무게로 갱신
        elif tmp > m:
            tmp = i
            box += 1

    if tmp: # tmp 값이 존재 == 아직 무게가 있음
        box += 1
    print(box)
else: # n == 0
    print(0)