n = int(input()) # 손님
p = list(map(int, input().split()))
pc = [i for i in range(1, 101)]

# 거절당한 손님 세기
cnt = 0
for i in p:
    # 현재 피시방 자리에 있다면
    if i in pc:
        # 자리 내줌(제거)
        pc.remove(i)
    # 없으면 거절당한 손님 세기
    elif not i in pc:
        cnt += 1
print(cnt)

