# 1 2 2 3 3 3 4 4 4 4 ... 수열 만들고
# 수열 구간 합 구하기 
a, b = map(int, input().split()) # 구간 시작 숫자, 끝 숫자

nums = []
for i in range(1, b+1): # 총 숫자 범위 1부터 b+1까지 
    for j in range(i):  
        # print(i)    i   | 1 2 2 3 3 3 4 4 4 4
        nums.append(i)

total = 0
for i in range(a-1, b): # 3번째 -> 인덱스 위치 2부터 
    total += nums[i]
print(total)

