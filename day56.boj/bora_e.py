n = int(input())
data = list(map(int, input().split()))
nums = [i for i in range(1, n+1)]
res = []
for i in range(n):
    res.append((data[i], nums[i]))
res.sort()

q = int(input())
for _ in range(q):
    d, x = map(int, input().split()) # 일수, 본인 군번