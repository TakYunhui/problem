import sys
input = sys.stdin.readline
n = int(input())
s = int(input())
word = input().rstrip()
'''
Pn에는 IOI가 n개 들어있다 
'''
result = 0
pattern = 0
i = 1
while i < s-1:
    # 세 문자열 가져온 값이 IOI라면 IOI 패턴 찾았다는 표시
    if word[i-1]+word[i]+word[i+1] == 'IOI':
        pattern += 1
        # 만약 패턴이 우리가 찾는 목표 숫자와 같으면
        # 패턴 -1 해주고, 결과 +1
        if pattern == n:
            pattern -= 1
            result += 1
        i += 1
    else:
        pattern = 0
    i += 1
print(result)