# 문자의 길이 n , 반복횟수 k
n, k = map(int, input().split())
word = input()
# 문자열에서 각 문자가 최소 k번 반복되면서 연속되어야 올바른 문장이 된다
# 올바른 문자를 만드는 최소한의 횟수 구하기

# 각 문자별 개수를 구하자
kind = dict()
for i in word:
    kind[i] = kind.get(i, 0) + 1
print(kind)
