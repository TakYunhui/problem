n = int(input())
result = 0
for i in range(1, n+1):
    # 1부터 n까지의 숫자를 문자로 만들고 리스트 화 -> [9, 9]
    numbers = list(map(int, str(i)))
    # 100보다 작을 때는 모든 수가 한수
    if i < 100:
        result += 1
    # 100보다 클 때는 각 자리가 등차수열이어야 한수
    elif numbers[0] - numbers[1] == numbers[1] - numbers[2]:
        result += 1
print(result)