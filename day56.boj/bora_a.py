import sys
input = sys.stdin.readline
n, x = map(int, input().split())
people = list(map(int, input().split()))
if sum(people) % x == 0:
    print(1)
else:
    print(0)