s = input()
# 변화할 때 0 또는 1 둘 중 하나로만 바꾸면 되기에 변화횟수 // 2
cnt = 0
prev = '?'
for i in s:
    # 이전 문자열과 다른 게 나온다면 변화 횟수 +1
    if i != prev:
        prev = i
        cnt += 1
print(cnt // 2)