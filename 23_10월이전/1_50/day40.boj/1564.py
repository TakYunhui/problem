n = int(input())
f = 1
# 팩토리얼 구하기
for i in range(2, n+1):
    f *= i
    while True:
        # 맨 뒤에 0이 있다면 0 제거
        if str(f)[-1] == "0":
            f //= 10
        else:
            break
    # 메모리 초과 방지를 위해 12자리로 나눈다
    f %= 10 ** 12
# 맨 뒤의 5자리 숫자만 출력
print(str(f)[-5:])