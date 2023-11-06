# 세로 n 가로 m
# 집터 내 땅의 높이 동일하게 만들기
# 1. 좌표 가장 위 블록을 제거해 인벤에 넣기 : 현재 높이 -1, 인벤 1 증가 (2초)
# 2. 인벤에서 블록 하나 꺼내 블록 위에 놓기 : 현재 높이 +1, 인벤 1 감소 (1초)
# 작업에 걸리는 최소 시간 + 땅의 높이 출력
import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
land = []
for _ in range(n):
    # extend를 이용해 1차원 배열로 만들어줌
    land.extend(list(map(int, input().split())))
land.sort(reverse=True) # 내림차순 정렬

count, height = -1, 0
# 모든 원소를 돌고나서 체크 h -> 목표 높이
for h in range(land[-1], land[0]+1): # 가장 작은 수 ~ 가장 큰 수 범위
    c, tmp = 0, b # 처음 시간 0초, 인벤 블록 개수
    for l in land:
        # 블록 제거 : 꺼낸 칸 * 2 초, 인벤 + 꺼낸 칸
        if l > h:
            c += (l-h) * 2
            tmp += l-h
        # 블록 쌓기 : 올린 칸 * 1 초, 인벤 - 올린 칸
        elif l < h:
            c += h-l
            tmp -= h-l

    if tmp < 0:
        break

    if count == -1 or c <= count:
        count = c
        height = h

print(count, height)
