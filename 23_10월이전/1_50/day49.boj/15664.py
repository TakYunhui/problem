def dfs(start):
    if len(s) == m:
        print(*s)
        return
    prev = 0
    for i in range(start, n):
        if not visited[i] and prev != nums[i]:
            visited[i] = 1
            s.append(nums[i])
            prev = nums[i]
            dfs(i+1)
            s.pop()
            visited[i] = 0

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
visited = [0] * n
dfs(0)