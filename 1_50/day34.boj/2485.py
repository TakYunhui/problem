def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a

import sys
input = sys.stdin.readline
N = int(input())
a = int(input())
arr = []

for i in range(N-1):
    num = int(input())
    arr.append(num - a)
    a = num

g = arr[0]
for j in range(1, len(arr)):
    g = Euclidean(g, arr[j])

result = 0
for each in arr:
    result += each // g - 1
print(result)