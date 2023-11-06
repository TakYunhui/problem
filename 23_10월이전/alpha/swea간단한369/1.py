# 3 6 9
# 해당 하는 숫자 개수만큼 박수 치기
n = int(input())
nums = [str(i) for i in range(1, n+1)]
result = []
cnt = 0
for num in nums:
    if '3' in num or '6' in num or '9' in num:
        cnt = num.count('3') + num.count('6') + num.count('9')
        result.append(cnt * '-')
    else:
        result.append(num)
print(*result)