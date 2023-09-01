# 스택: 선입선출
# 1부터 n까지의 수를 스택에 넣었따 뽑아 늘어놓으며 수열 생성
# 스택에 push하는 순서는 오름차순
# 임의의 수열이 주어졌을 때, 스택으로 만들 수 있는 여부
# 어떤 순서로 push / pop 연산 수행하는지 여부 알아내기
# n = int(input())
stack = []
new = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
new.append(stack.pop())
new.append(stack.pop())
stack.append(5)
stack.append(6)
new.append(stack.pop())
stack.append(7)
stack.append(8)
new.append(stack.pop())
new.append(stack.pop())
new.append(stack.pop())
new.append(stack.pop())
new.append(stack.pop())
print(new)