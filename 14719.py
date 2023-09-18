h, w = map(int, input().split())
blocks = list(map(int, input().split()))
# 가장 큰 높이를 기준으로 반반 나누기
max_idx = blocks.index(max(blocks))
# 앞에서부터 본인보다 크거나 같은 수가 나오기 전까지는 일단 + 본인
# 근데 만약 다음 수가 존재하면 본인 - 다음 수 계산
# 큰 수가 나오면 그 수로 바꿔준다
# 더 뒷쪽에 채워주는 기둥이 없으면 0임

# 근데 max값을 가진 높이가 여러 개 주어지면 어캄?
print(max_idx)