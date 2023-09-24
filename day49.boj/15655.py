def dfs(start):
    if start > n:
        return
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n):
        s.append(nums[i])
        dfs(i+1)
        s.pop()
# 오름차순 출력, 넣었던 수보다 작은 수는 안 넣기, 본인 중복 x
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
dfs(0)