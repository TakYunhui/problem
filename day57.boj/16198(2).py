import sys
input = sys.stdin.readline
# 구슬 개수, 각 구슬 별 무게 리스트 데이터 입력
n = int(input())
weights = list(map(int, input().split()))
# 브루트포스 -> 완전 탐색, 모든 경우의 수 볼 것임
# 백트래킹 -> 재귀로 최댓값 구할 것임
# 첫 번째, 마지막 에너지 구슬은 고를 수 없으므로 . . .
# 구슬의 개수가 2개가 되면 선택 불가(종료)
result = 0
def back(x):
    global result # 전역 변수 선언
    if len(weights) == 2:
        result = max(x, result) # 누적된 에너지와 결과 비교
        return
    for i in range(1, len(weights)-1): # 첫 번째, 마지막 구슬 제외한 범위
        energy = weights[i-1] * weights[i+1] # i번째 구슬 기준 모은 에너지
        marble = weights.pop(i) # i번째 구슬 뺀 것을 변수에 저장해둠
        back(x+energy) # 재귀로 매개변수에 energy 누적합해준다
        weights.insert(i, marble) # 제거했던 구슬 다시 넣고 경우의 수 확인
back(0)
print(result)