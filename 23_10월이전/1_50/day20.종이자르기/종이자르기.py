w, h = map(int, input().split()) # 가로, 세로
n = int(input())                 # 점선 개수

# 가로/세로 처음 점, 끝 점 + 잘린 점들 들어갈 것
ls_width = [0, w]
ls_height = [0, h]

for _ in range(n):
    d, p = map(int, input().split()) # d: 방향, direction, p: point, 점
    # 세로 점선이 가로 방향을 자르므로 가로 리스트에 넣는다
    if d == 1:
        ls_width.append(p)
    # 반대로 가로 점선은 세로 방향을 자른다
    else:
        ls_height.append(p)
# print(ls_width, ls_height)

# 점들 오름차순 정렬 후 . . .
ls_width.sort()
ls_height.sort()

# 간격 간의 차 구하기
widths, heights = [], []
# 가로 길이
for i in range(1, len(ls_width)):
    widths.append(ls_width[i]-ls_width[i-1])
# 세로 길이
for i in range(1, len(ls_height)):
    heights.append(ls_height[i]-ls_height[i-1])


# 가장 큰 넓이 == 가장 큰 가로 x 가장 큰 세로
print(max(widths) * max(heights))