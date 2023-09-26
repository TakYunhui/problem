# 회원 수, 치킨 종류 - 이 중 3가지 종류만(not 개수) 시킨다
# 백트래킹?
# 치킨 선호도 저장, y값 선택 가짓수도 저장해야겠는데...
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]