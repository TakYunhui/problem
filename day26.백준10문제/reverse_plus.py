def REV(str):
    rev = list(str)
    rev = rev[::-1]
    rev = ''.join(rev)
    return rev

x, y = input().split()
print(int(REV(str(int(REV(x))+int(REV(y))))))
