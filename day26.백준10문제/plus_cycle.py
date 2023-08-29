# 주어진 정수
n = input()
# 10보다 작으면 0붙이기
if int(n) < 10:
    n = '0'+n
# 왼쪽, 오른쪽 자리 수 나누기
left = n[0]
right = n[1]
# 사이클 횟수
cnt = 0
while True:
    # 두 자리 수의 각 자리 숫자 더하기
    plus = int(left) + int(right)
    # 만약 10보다 작다면 앞에 0붙여서 두 자리수로 만드는 작업
    if plus < 10:
        plus = '0'+str(plus)
        result = right + plus[1]
    else:
        plus = str(plus)
        result = right + plus[1]
    left = result[0]
    right = result[1]
    cnt += 1
    # 결과가 처음 주어진 n과 같아진다면 종료
    if result == n:
        print(cnt)
        break

