'''
bfs
- 4와 7만을 이용한 금민수를 가능한 자릿수 별로 만든다
- 최종적으로 주어진 a~b 범위 안의 수들만 result에 들어간다
'''
from collections import deque
a, b = map(int, input().split())
q = deque([4, 7])
result = 0
while len(q) > 1:
    f = q.popleft()
    # f가 b보다 작고 a보다 클 때의 범위 if 조건
    if f <= b:
        if a <= f:
            result += 1 # 금민수이면서 범위에 맞으면 result에 추가
        # 범위 바깥(a보다 작을 때)이면 금민수를 만들어 q에 넣어준다
        # 이 금선수가 범위 안이면 result에 추가되고
        # 이렇게 추가된 금민수가 결국 b보다 커지면 첫번째 if문을 만족시키지 않으니 q에 넣지 않는다
        # -> 최종적으로 q의 길이가 0이 되면서 자동 종료
        q.append(f*10+4)
        q.append(f*10+7)
print(result)