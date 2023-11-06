import sys
input = sys.stdin.readline
n, m = map(int, input().split())
girl_group = dict()
# dict 팀명 : 팀 멤버 리스트
for _ in range(n):
    team = input().rstrip()
    p = int(input())
    members = []
    for _ in range(p):
        member = input().rstrip()
        members.append(member)
    members.sort()
    girl_group[team] = members

# 퀴즈
for _ in range(m):
    quiz = input().rstrip()
    quiz_type = int(input())
    # 팀의 이름 -> 팀에 속한 멤버의 이름 사전순 출력
    if quiz_type == 0:
        for girl in girl_group[quiz]:
            print(girl)
    elif quiz_type == 1:
        for key, value in girl_group.items():
            if quiz in value:
                print(key)
                break
