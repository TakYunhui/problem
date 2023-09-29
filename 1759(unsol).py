# c개의 문자로 l개의 문자를 가지는 암호 만들기
# 최소 한 개의 모음 + 최소 두 개의 자음
# 암호에서 증가하는 순서로 배열
l, c = map(int, input().split())
char = input().split()
char.sort()
vowel = 'aeiou'

