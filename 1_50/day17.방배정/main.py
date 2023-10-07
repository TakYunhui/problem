# n: 총 학생 수, k: 한 방 배정 인원
n, k = map(int, input().split())
# n 줄 동안 학생 데이터 입력
# s: 성별 0 - 여, 1 - 남, y: 학년
# 두 개의 정보를 하나의 리스트로 묶어서 받기
data = [list(map(int, input().split())) for _ in range(n)]
# print(data) [[1, 1], [0, 1], [1, 1], [0, 2], [1, 2], [0, 2], [0, 3], [1, 3], [1, 4], [1, 3], [1, 3], [0, 6], [1, 5], [0, 5], [1, 5], [1, 6]]

# 전체 data를 순회하면서
# 1. 성별 확인
# 같은 성별끼리 묶음
male = []
female = []
for person in data:
    if person[0] == 0:
        female.append(person)
    else:
        male.append(person)
# print(male, female)

# 2. 같은 성별 안에서 학년 확인
# 총 6학년이 있으니 학년별 정보 카운트 (카운트 배열)
# 학년 별 인원 // 방 하나당 수용 인원 -> 방 개수
# 이때, 학년 별 인원이 방 수용 인원으로 나누어 떨어지는지 확인
xy = [0] * 7
xx = [0] * 7
# 남학생 학년 별 인원
for boy in male:
    xy[boy[1]] += 1
# 여학생 학년 별 인원
for girl in female:
    xx[girl[1]] += 1
# print(xy, xx)

# 방 개수 구하기
result = 0
for i in range(7):
    if xx[i] % k == 0: # 나누어 떨어지면
        result += xx[i] // k
    elif xx[i] % k: # 나누어 떨어지지 않으면
        result += (xx[i] // k) + 1

    if xy[i] % k == 0:
        result += xy[i] // k
    elif xy[i] % k:
        result += (xy[i] // k) + 1
print(result)