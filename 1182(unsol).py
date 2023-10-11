import sys
n, s = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * n
subset = []
cnt = 0
def back(x):
    global cnt
    if sum(subset) == s:
        cnt += 1
        return
    for i in range(x, n):
        if not visited[i]:
            s.append(nums[i])
            visited[i] = 1
            back(i+1)
            visited[i] = 0
back(0)
print(cnt)


