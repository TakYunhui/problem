# def readln(n):
#     cnt = 0
#     for i in range(n-1, 0, -1):
#         cnt += 1
#         if n % i == 0:
#             break
#     print(cnt)
#
# n = int(input())
# readln(n)

# 해석 필요
n = int(input())
i = 2
cnt = 1
while i*i <= n:
    if n % i == 0:
        cnt = n // i
        break
    i += 1
print(n-cnt)