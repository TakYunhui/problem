def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
# 중복없이 M개 고르기
n, m = map(int, input().split())
s = []
dfs()