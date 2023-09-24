def dfs():
    if len(s) == m:
        print(*s)
        return
    prev = 0 # 중복 방지 변수
    for i in range(n):
        if not visited[i] and prev != nums[i]:
            visited[i] = 1
            s.append(nums[i])
            prev = nums[i]
            dfs()
            visited[i] = 0
            s.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
visited = [0] * n
dfs()