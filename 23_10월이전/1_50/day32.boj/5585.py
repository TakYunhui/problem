money = int(input())
change = [500, 100, 50, 10, 5, 1]
money = 1000 - money
while money:
    result = 0
    for i in change:
        if money >= i:
            result += money // i
            money %= i
print(result)