# 빠른 입출력
import sys
input = sys.stdin.readline
n = int(input())
sticks = [int(input()) for _ in range(n)]
stack = []
# 막대기를 오른쪽(뒤)부터 본다
for i in sticks[::-1]:
    if stack:
        # 만약 제일 오른쪽 막대기보다 작으면 제거
        if i <= stack[-1]:
            sticks.pop()
        # 오른쪽 막대기보다 크다면 꺼내서 스택에 넣기
        else:
            stack.append(sticks.pop())
    else:  # 스택이 비어있을 때는 초기값(가장 오른쪽 막대기) 넣기
        stack.append(sticks.pop())
print(len(stack))