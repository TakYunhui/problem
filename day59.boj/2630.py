# 색종이 안에 서로 다른 색이 있다면 계속 4분할하여 단색의 색종이 만들기
# 쿼드 트리 : 하나의 부모 노드에 4개의 자식 노드 생성
import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
zero, one = 0, 0 # 0/1로만 이루어진 색종이 개수
# x, y 좌표
def sol(x, y, size):
    first = data[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            # 다른 색이 존재한다면 멈추기
            if data[i][j] != first:
                break
        # 모든 부분이 동일한 색일 경우에만 쿼드 트리 분할을 멈춤
        # 이 부분 없이 바로 첫번째 반복문 다음 else문을 실행하면 단일 색 구성이 아니더라도 값 증가시킴
        else:
            continue
        break
    # 단일 색 구성이라면 종이 개수 리턴(함수 종료)
    else:
        global zero, one
        if first == 0:
            zero += 1
        else:
            one += 1
        return

    # 단일 색 구성이 아니라면 쿼드트리 실행
    mid = size // 2
    # 좌측 하단
    sol(x+mid, y, mid)
    # 우측 상단
    sol(x, y+mid, mid)
    # 시작 위치
    sol(x, y, mid)
    # 우측 하단
    sol(x+mid, y+mid, mid)

sol(0, 0, n)
print(zero)
print(one)