a, b, c = map(int, input().split())
three = [a, b, c]
# 가장 긴 변 구하기
max_v = max(a, b, c)
three.remove(max_v)
# 가장 긴 변의 길이가 나머지 두 변의 합보다 크거나 같다면
while max_v >= sum(three):
    # 가장 긴 변 1 씩 빼주기
    max_v -= 1
    # 삼각형의 조건을 만족할 때, 둘레 출력
    if max_v < sum(three):
        print(max_v+sum(three))
        break
else:
    print(max_v+sum(three))