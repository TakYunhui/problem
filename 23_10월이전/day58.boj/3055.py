from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
forest = [list(input()) for _ in range(r)] # r * c 지도
'''
* : 물
. : 이동 가능한 공간
X : 돌, 이동 불가능
D : 비버 굴(도착지)
S : 고슴도치 처음 위치 
=> BFS 2번 돌려서 비교 
'''
hedgehog = [[0] * c for _ in range(r)]
water = [[0] * c for _ in range(r)]
hq = deque()
wq = deque()

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def wbfs():
    while wq:
        x, y = wq.popleft()

        for i in d:
            nx = x + i[0]
            ny = y + i[1]
            # 제한 범위 밖이면 이동 불가
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            # 방문 전적이 있거나, 돌로 막혀있거나, 비버의 굴이면 이동 불가
            if water[nx][ny] or forest[nx][ny] == 'X' or forest[nx][ny] == 'D':
                continue
            wq.append((nx, ny))
            water[nx][ny] = water[x][y] + 1



def hbfs():
    while hq:
        x, y = hq.popleft()

        for i in d:
            nx = x + i[0]
            ny = y + i[1]

            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if hedgehog[nx][ny] or forest[nx][ny] == 'X':
                continue
            # 같은 지역에 물이 존재하고 현재 고슴도치 + 1 의 값이 물의 값 이상이면 맞닥뜨린 것
            if water[nx][ny] and hedgehog[x][y] + 1 >= water[nx][ny]:
                continue
            hedgehog[nx][ny] = hedgehog[x][y] + 1
            hq.append((nx, ny))
            if forest[nx][ny] == 'D':
                # 처음에 1 주고 시작했으니 이동하기 전 값이 최단 거리
                print(hedgehog[x][y])
                return
    print('KAKTUS')
    return



for x in range(r):
    for y in range(c):
        if forest[x][y] == '*':
            wq.append((x, y))
            water[x][y] = 1
        elif forest[x][y] == 'S':
            hq.append((x, y))
            hedgehog[x][y] = 1

wbfs()
hbfs()


