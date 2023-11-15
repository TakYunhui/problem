# 최소 스패닝 트리 가중치 출력
import sys

input = sys.stdin.readline
v, e = map(int, input().split()) # 정점, 간선
edge = []

for _ in range(e):
    a, b, c = map(int, input().split()) # 간선 정보 a-b가 c 가중치로 연결
    edge.append([a, b, c])
edge.sort(key=lambda x:x[2])

parents = [i for i in range(v+1)]
# 부모 찾기
def find_set(x):
    if parents[x] == x:
        return x
    return  find_set(parents[x])


# 합치기 -> 더 작은 수에 넣어 준다
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

cnt = 0 # 현재 방문 정점 수
sum_weight = 0 # 가중치
for a, b, c in edge:
    # 두 집합의 대표자가 서로 다르면 대표자를 합쳐 주는 작업
    if find_set(a) != find_set(b):
        cnt += 1
        sum_weight += c
        union(a, b) # 같은 집합으로 연결
        if cnt == v: # cnt가 정점의 개수만큼 가면 mst 구성 끝
            break
print(sum_weight)