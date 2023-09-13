import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # 배열의 크기
a = list(map(int, input().split()))
b = list(map(int, input().split()))
new = a + b
new.sort()
print(*new)