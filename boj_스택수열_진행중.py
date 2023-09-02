# 스택: 선입선출
# 1부터 n까지의 수를 스택에 넣었따 뽑아 늘어놓으며 수열 생성
# 스택에 push하는 순서는 오름차순
# 임의의 수열이 주어졌을 때, 스택으로 만들 수 있는 여부
# 어떤 순서로 push / pop 연산 수행하는지 여부 알아내기
n = int(input())
# n개의 원하는 수열
target = [int(input()) for _ in range(n)]
nums = [i for i in range(1, n+1)]
idx = 0
stack = []
cmd = []
# while문 접근??