t = int(input())
'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''
for tc in range(1, t+1):
    word = [input() for _ in range(5)]
    max_len = 0
    for i in word:
        max_len = max(max_len, len(i))
    result = ''
    for i in range(max_len):
        for j in range(5):
            try:
                result += word[j][i]
            except:
                pass

    print(f'#{tc} {result}')