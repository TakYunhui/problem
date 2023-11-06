# 임의의 괄호를 만들어 계산되는 최소값 출력
# - 부호가 나오면 다음 -부호가 나오기 전까지 모두 괄호로 묶기
# 10 + 20 - 30 + 40 + 50 - 60 + 70 + 80 - 90
# 10 + 20 - (30 + 40 + 50) - (60 + 70 + 80) - 90
susik = input().split('-')
# print(susik)
# ['10 + 20 ', ' 30 + 40 + 50 ', ' 60 + 70 + 80 ', ' 90']
result = 0

for i in range(len(susik)):
    susik[i] = susik[i].split('+')
# print(susik)
# [['10 ', ' 20 '], [' 30 ', ' 40 ', ' 50 '], [' 60 ', ' 70 ', ' 80 '], [' 90']]
# -가 없는 경우, 0번째 인덱스 값들을 다 더하면 끝
for i in range(len(susik[0])):
    result += int(susik[0][i])
for i in range(1, len(susik)):
    # -가 있어서 리스트가 분리된 경우, 존재하는 다음 리스트의 요소들을 더한 계산값을
    # result에서 빼준다
    tmp = 0
    for j in range(len(susik[i])):
        tmp += int(susik[i][j])
    result -= tmp
print(result)