import math
n = list(input())
# 6과 9는 count 횟수를 더한 뒤 2로 나누고 반올림 해준다 (홀수 처리)
tmp = max(n.count('0'), n.count('1'), n.count('2'), n.count('3'), n.count('4'), n.count('5'), n.count('7'), n.count('8'), math.ceil((n.count('6') + n.count('9')) / 2))
# 가장 많이 있는 수가 1개 이하 + 6이 하나 있고 9는 없을 때 -> 1 세트 필요
if tmp <= 1 and n.count('6') == 1 and n.count('9') == 0:
    print(1)
# 가장 많이 있는 수가 1개 이하 + 6이 없고 9는 하나 있을 때 -> 1 세트 필요
elif tmp <= 1 and n.count('6') == 0 and n.count('9') == 1:
    print(1)
# 많이 나온 수가 2개 이상이면 가장 많이 나온 수 출력
else:
    print(tmp)