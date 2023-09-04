# set 이용
# n = int(input())
# card = set(map(int, input().split()))
# m = int(input())
# target = list(map(int, input().split()))
# target2 = set(target)
# intersection = card & target2
# for i in target:
#     if i in intersection:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

n = int(input())
card = list(map(int, input().split()))
m = int(input())
target =list(map(int, input().split()))
card.sort()
def binary(list, key):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == key:
            return 1
        elif list[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in target:
    print(binary(card, i), end=' ')