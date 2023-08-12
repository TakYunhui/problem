K = int(input())
stack = []
for i in range(K):
    number = int(input())
    if stack:
        if number == 0:
            stack.pop()
        else:
            stack.append(number)
    else:
        stack.append(number)


print(sum(stack))
