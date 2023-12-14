t = int(input())

for tc in range(1, t+1):
    result = ''
    n = int(input())
    for _ in range(n):
        char, num = input().split()
        result += (char * int(num))

    print(f'#{tc}')
    for i in range(0, len(result), 10):
        print(result[i:i+10])