def recursion(S, l, r):
    # 전역 변수로 cnt 활용 
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif S[l] != S[r]:
        return 0
    else:
        return recursion(S, l+1, r-1)

def isPalindrome(S):
    return recursion(S, 0, len(S)-1)

t = int(input())
for _ in range(t):
    cnt = 0
    S = input()
    print(isPalindrome(S), cnt)