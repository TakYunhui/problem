import sys
input = sys.stdin.readline
n = int(input())
meetings = []
for _ in range(n):
    # 시작 시간, 종료 시간
    s, e = map(int, input().split())
    meetings.append((e, s))
# 종료 시간 기준으로 오름차순 정렬
# 왜? 제일 짧은 종료시간에 연달아서 이용되는 회의실 보는 게 가장 많은 회의 사용 개수가 될 거니까
meetings.sort()
cnt = 1
idx = 0

for i in range(1, n):
    # 현재 보고 있는 회의 시간의 종료가 이전 회의 종료시간 이상이다면 연달아 이용 가능
    if meetings[i][1] >= meetings[idx][0]:
        cnt += 1
        idx = i
print(cnt)