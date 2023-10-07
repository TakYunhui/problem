def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(n):
        s.append(nums[i])
        dfs(i+1)
        s.pop()
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
dfs(1)