hashing = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
           'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
           'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
           'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
           'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
           'z': 26}
l = int(input()) # 문자열 길이
word = input() # 영문소문자문자열
result = 0
x = 1
for i in range(l):
    result += x * hashing[word[i]]
    x *= 31
# Large는 적당히 큰 수(소수 1234567891)로 나눈 나머지
# mod 출력
if result > 1234567891:
    print(result % 1234567891)
else:
    print(result)
