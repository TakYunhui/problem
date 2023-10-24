n = int(input())
one = '1'
two = '2'
result = 0
def three(acc, r):
    global result
    if r == n:
        if int(acc) % 3 == 0:
            result += 1
        return
    three(acc+'1', r+1)
    three(acc+'2', r+1)
    three(acc+'0', r+1)

three(one, 1)
three(two, 1)
print(result)
