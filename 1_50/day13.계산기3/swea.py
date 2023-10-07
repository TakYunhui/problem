# 후위표기식으로 변환
for tc in range(1, 11):
    n = int(input())
    case = input()
    stack = []
    # 입력 토큰, 스택 우선순위
    # 스택의 '(' 값을 0으로 주어 우선순위 고려 안 하게 함
    icp = {'(': 3, '*': 2, '+': 1}
    isp = {'(': 0, '*': 2, '+': 1}
    susik = ''
    # 주어진 문자열 식을 하나씩 살피면서
    for x in case:
        if x not in '(+*)': # 피연산자면 수식에 넣기
            susik += x
        else:               # 연산자면
            if x == ')':    # 닫는 소괄호일 때
                # 여는 소괄호를 만날 때까지 스택 최상단 값을 수식으로 pop
                # 여는 소괄호를 만나면 해당 동작을 멈추고 여는 소괄호 제거
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        susik += stack.pop()
                # 스택에 값이 있고, 현재 연산자의 우선순위가 스택 최상단의 것 이하라면
                # 스택 peek를 pop하여 수식에 넣고, 우선순위가 현재 연산자보다 작은 것이 나올때까지 반복
                # 작은 것을 만나면 본인을 스택에 넣는다
            elif stack and (icp[x] <= isp[stack[-1]]):
                while stack and icp[x] <= isp[stack[-1]]:
                    susik += stack.pop()
                stack.append(x)
                # 현재 연산자의 우선순위가 스택 peek보다 크다면 바로 스택에 push
            else:
                stack.append(x)
    # 스택에 연산자가 남아있다면
    # 수식에 넣어주기
    # 이 작업을 하지 않으면 스택에만 남아있고 표기식에 적히지 않게 된다!
    while stack:
        susik += stack.pop()
    # print(susik, stack)

    # 얻어낸 후위표기식을 스택으로 계산
    # 수식의 문자열 하나씩 확인
    for x in susik:
        # x가 피연산자면 정수로 스택에 push
        if x not in '+*':
            stack.append(int(x))
        else: # 연산자면
            right = stack.pop()
            left = stack.pop()
            if x == '+':
                stack.append(left + right)
            elif x == '*':
                stack.append(left * right)


    print(f'#{tc}', *stack)