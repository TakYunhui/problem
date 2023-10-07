one = list(input())
two = list(input())
same = set(one) & set(two)
same = list(same)
cnt = 0
# 제거할 단어(다른 종류) 세기
for i in one:
    if i not in same:
        cnt += 1
for i in two:
    if i not in same:
        cnt += 1
# 같은 단어이나 개수가 다른 것 세기
for i in same:
    cnt += abs(one.count(i) - two.count(i))
print(cnt)

