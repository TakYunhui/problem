n = int(input())
numbers = list(map(int, input().split()))
# 중복 제거
num_to_set = set(numbers)
# 리스트로 만들어 정렬
tmp = list(num_to_set)
tmp.sort()

dict = {}
# set으로 중복 원소는 지워졌을 수도 있기에 범위는 len(tmp)에 맞춤
for i in range(len(tmp)):
    # 해당하는 숫자에 i 번째 수 넣음
    dict[tmp[i]] = i
# 수에 해당하는 value 출력
for i in numbers:
    print(dict[i], end=' ')
