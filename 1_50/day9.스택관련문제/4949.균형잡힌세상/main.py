while True:
    case = input()
    stack = []
    if case == '.':
        break
    for c in case:
        if c in ['(', '[', ')', ']']:
            if stack:
                if c == '(' or c == '[{]':
                    stack.append(c)
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
    if stack:
        print('no')
    else:
        print('yes')