# 대소문자 바꾸기
w = input()
for i in w:
    if i.islower():
        print(i.upper(), end='')
    elif i.isupper():
        print(i.lower(), end='')