def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()

# 길이 m의 수열 - 중복 o
n, m = map(int, input().split())
s = []
dfs(1)