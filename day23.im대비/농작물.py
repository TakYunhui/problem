t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(input()) for _ in range(n)]
    # print(farm)

    '''
    n = 5 
    i 0 | 2
      1 | 1 2 3   
      
      2 | 0 1 2 3 4    
      
      3 | 3 2 1 
      4 | 2
    '''
    result = 0
    # 윗 줄
    for i in range(n//2):
        for j in range(n//2-i, n//2+i+1):
            result += int(farm[i][j])
    # 아랫 줄
    for i in range(n//2):
        for j in range(n//2-i, n//2+i+1):
            result += int(farm[n-i-1][j])
            print(n-i-1, j)
    for i in farm[n//2]:
        result += int(i)


    print(f'#{tc} {result}')