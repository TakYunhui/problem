import sys
input = sys.stdin.readline

n = int(input())
energies = list(map(int, input().split()))
# 구슬 2개 남을 때까지 계속 에너지 모음
result = 0 # 최대 에너지 저장
def back(x):
    global result

    if len(energies) == 2:
        result = max(result, x)
        return
    for i in range(1, len(energies)-1):
        tmp = energies[i-1] * energies[i+1]
        energy = energies.pop(i)
        back(x+tmp)
        energies.insert(i, energy)

back(0)
print(result)
