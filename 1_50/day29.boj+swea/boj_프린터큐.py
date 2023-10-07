# 중요도(숫자 값) 확인, 높을 수록 중요
# 맨 앞의 문서 중요도 확인
# -> 중요도가 더 높은 값이 존재 한다면 뒤에 재배치 : append(popleft())
# 그렇지 않다면 바로 pop한 것을 인쇄
# 어떤 한 문서가 몇 번째로 인쇄되는 가?
from collections import deque
t = int(input()) # 테스트 케이스 수
for tc in range(t):
    # 문서의 총 개수, 몇 번째로 인쇄되었는지 궁금한 문서의 초기 위치(제로베이스 접근)
    n, m = map(int, input().split())
    # n개 문서의 중요도
    docs = list(map(int, input().split()))
    q = deque(docs)
    # 문서 별 위치
    idx = [i for i in range(n)]
    i = deque(idx)
    cnt = 0 # 인쇄 차례 : 타겟 위치의 값이 pop 될 때의 횟수

    # q : 문서 중요도, i : 문서 위치
    while q:
        if q[0] == max(q):
            q.popleft()
            # 현재 프린트하는 문서의 초기 위치 확인
            a = i.popleft()
            cnt += 1
            # 찾고자 했던 문서의 초기 위치와 같다면 종료
            if a == m:
                break
        else:
            q.append(q.popleft())
            i.append(i.popleft())
    print(cnt)





