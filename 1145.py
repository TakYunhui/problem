# 서로 다른 5개의 자연수 중 적어도 세 개로 나누어지는 가장 작은 수 찾기
nums = list(map(int, input().split()))
n = min(nums)
cnt = 0 # 나눠진 횟수 카운트
while True:
    cnt = 0
    # 주어진 5개의 숫자를 다 순회하면서 나눠진 횟수가 3이상이면 스탑
    for i in range(5):
        if n % nums[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1