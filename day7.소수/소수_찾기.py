N = int(input())
numbers = list(map(int, input().split()))

def find_prime(number):
    if number == 1:
        return 0
    elif number == 2: # 2도 소수다
        return 1
    else:
        for i in range(2, number): # 2부터 number-1까지의 수 
            if number % i == 0:
                return 0
    return 1

cnt = 0 
for number in numbers:
    cnt += find_prime(number)
print(cnt)

