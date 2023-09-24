def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
# 자연수 n, m
# 길이 m인 수열 -> 1. 1부터 n까지 자연수 중 중복 x 2. 오름차순
n, m = map(int, input().split())
# 수열이 들어갈 리스트
s = []
dfs(1)