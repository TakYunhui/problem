def dfs(start):
    if len(s) == m:
        print(*s)
        return
    # nums 리스트 인덱스 번호에 맞춰 범위 지정되어야 함
    for i in range(start, n):
        s.append(nums[i])
        dfs(i)
        s.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
dfs(0)