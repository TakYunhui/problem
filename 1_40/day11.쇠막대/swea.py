import sys
sys.stdin = open('sample_input.txt')
# () -> raser
# ((( () -> 3개의 막대기 1번 자름 += 3
# ((( () () ) -> 3개의 막대기 2번 자름 += 3 * 2 + 막대기 남은 조각 1개 += 1
T = int(input())
for tc in range(1, T+1):
    case = input()
    result = 0
    stack = []
    for i in range(len(case)):
        if case[i] == '(':
            stack.append(case[i])
        elif case[i] == ')' and case[i-1] == ')':
            stack.pop()
            result += 1
        else:
            stack.pop()
            result += len(stack)

    print(f'#{tc} {result}')