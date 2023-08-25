# 6.
# n = int(input())
# for i in range(n):
#     print(' '* i + '*' * (2* n - (i*2 + 1)))

# 7.
# n = int(input())
# for i in range(n-1):
#     print(' '*(n-i-1) + '*' * (i*2+1))
# for i in range(n):
#     print(' '*i + '*' * (2* n-(i*2+1)))

# 8.
# n = int(input())
# for i in range(n):
#     print('*'*(i+1)+' '*(2*(n-i-1)) + '*'*(i+1))
# for i in range(n-1, 0, -1): # 4 3 2 1
#     print('*' * i + ' '* (2*(n-i))  + '*'*i)

# 9.
n = int(input())
for i in range(n):
    print(' ' * i +'*'*(2*n - (2*i+1)))
for i in range(1, n):
    print(' '*(n-i-1)+'*'*(2*i+1))