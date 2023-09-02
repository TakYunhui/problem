t = int(input()) # 테스트케이스 수
for i in range(t):
    k = int(input()) # k층
    n = int(input()) # n호
    # k-1층의 1 - b 호까지 사람들의 수 합하기
    f0 = [x for x in range(1, n+1)]  # 0층 리스트
    for k in range(k):  # 층 수 만큼 반복
        for i in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력