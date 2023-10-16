N = int(input())
students = list(map(int, input().split()))
order = []
for i in range(1, N+1):
    order.append(i)

print(order)
stack = []

for i in range(len(students)):
    for j in order:
        if j == students[i]:
            stack.pop()