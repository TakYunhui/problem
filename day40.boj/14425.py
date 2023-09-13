import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set(input() for _ in range(n))
check = [input() for _ in range(m)]

cnt = 0
for i in check:
    if i in s:
        cnt += 1
print(cnt)