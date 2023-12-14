n = int(input())
arr = list(map(int, input().split()))
sorted_list = sorted(arr)
result = []

for i in range(n):
    # 수열 적용 -> 오름차순 정렬했을 때 각 숫자의 인덱스
    idx = sorted_list.index(arr[i])
    result.append(idx)
    sorted_list[idx] = -1
print(*result)