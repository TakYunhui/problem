name = input() # 연두의 영어이름
n = int(input()) # 팀 이름 개수
team = [input() for _ in range(n)]
# 우승 확률은 0 이상
max_val = -1
result = ''
# 같은 확률은 사전순으로 높다
team.sort()
for tn in team:
    teamname = name+tn
    L = teamname.count('L')
    O = teamname.count('O')
    V = teamname.count('V')
    E = teamname.count('E')
    victory = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E))  % 100
    if victory > max_val:
        max_val = victory
        result = tn
print(result)