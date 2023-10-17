n = int(input()) # 학생 수
line = list(map(int, input().split())) # 뽑은 번호 숫자
students = [i for i in range(1, n+1)]  # 뽑은 학생 순서
# print(n, line, students)

# 첫번째 학생은 무조건 0번, 제일 앞 줄
# 두번째: 0 - 1 번 중 하나, 0번은 그대로, 1번은 바로 앞 학생 앞
# 세번째: 0: 그대로, 1-2: 뽑은 번호만큼 앞자리로 간다...
# 뽑은 번호와 학생 순서 엮기
data = []
for i in range(n):
    data.append((line[i], students[i]))
# data[row][0]: 뽑은 카드 번호, data[row][1]: 뽑은 순서
new_line = []
for i in range(n): # i | 0 1 2 3 4
    # i - 학생이 뽑은 숫자 | 0, 0, 1, 0, 2
    # 현재 앞에 있는 학생 수(i) - 뽑은 번호
    # -> n번 앞까지 서게 한다
    new_line.insert(i-data[i][0], data[i][1])
    # print(new_line)
    '''
    [1]
    [2, 1]
    [2, 3, 1]
    [4, 2, 3, 1]
    [4, 2, 5, 3, 1]
    '''

print(*new_line)


