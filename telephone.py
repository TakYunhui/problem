N = int(input()) # 통화 개수
time = list(map(int, input().split()))
# Y 요금제
Y_money = 0
for i in time:
    if i < 30:
        Y_money += 10
    else:
        if i % 30 == 0:
            Y_money += (i//30) * 10
        else:
            Y_money += (i//30+1) * 10

# M 요금제
M_money = 0
for i in time:
    if i < 60:
        M_money += 15
    else:
        if i % 60 == 0:
            M_money += (i//60) * 15
        else:
            M_money += (i//60+1) * 15
print(Y_money, M_money)
if Y_money < M_money:
    print(f'Y {Y_money}')
elif M_money < Y_money:
    print(f'M {M_money}')
else:
    print(f'Y M {Y_money}')