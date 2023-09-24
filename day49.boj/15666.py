def dfs(start):
    if len(s) == m:
        print(*s)
        return
    # 중복 수열 출력만 방지
    prev = 0
    for i in range(start, n):
        if prev != nums[i]:
            s.append(nums[i])
            prev = nums[i]
            dfs(i)
            s.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
dfs(0)