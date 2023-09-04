import sys
input = sys.stdin.readline
n = int(input()) # 로그에 기록된 출입 기록 수
# 딕셔너리에 넣기
remain = dict()
for i in range(n):
    person, log = input().split()
    remain[person] = log
result = []
for k, v in remain.items():
    if v == 'enter':
        result.append(k)

result.sort(reverse=True)
for i in result:
    print(i)