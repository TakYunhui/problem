import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    name, korean, english, math = input().split()
    result.append([name, int(korean), int(english), int(math)])

result.sort()
result.sort(key=lambda x:x[3], reverse=True)
result.sort(key=lambda x:x[2])
result.sort(key=lambda x:x[1], reverse=True)
for i in result:
    print(i[0])