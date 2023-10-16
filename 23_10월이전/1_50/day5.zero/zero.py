import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    count = 0
    for number in range(n, m+1):
        for j in str(number):
            if j == '0':
                count += 1
    print(count)