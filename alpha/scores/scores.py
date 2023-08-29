import sys
sys.stdin = open('input.txt')
t = int(input())
# 평점 10가지
# 상대 평가로 총점 높은 순으로 점수 부여
# 각각의 평점은 같은 비율로 부여
for tc in range(1, t+1):
    n, k = map(int, input().split()) # 학생 수 n, 학점을 알고 싶은 학생 번호 k
    # 학생 데이터 만들기
    data = []
    for i in range(1, n+1):
        m, f, hw = map(int, input().split())
        score = m * 35 + f * 45 + hw * 20
        data.append([i, score])
    # 점수 기준 내림차순 정렬
    data.sort(key = lambda x:x[1], reverse=True)
    result = ''
    # 모든 점수 보기
    for i in range(len(data)):
        # 구하고자 하는 k번째 학생이라면
        if data[i][0] == k:
            # print(i) # i : 등수
            # 등수 / 총 인원수 = 백분율
            # 소수점까지 구해서 백분위 범위로 판별
            # i는 인덱스 번호이므로 +1 해줘서 실제 등수 숫자와 맞춰줌
            if (i+1) / n <= 0.1:
                result = 'A+'
            elif (i+1) / n <= 0.2:
                result = 'A0'
            elif (i+1) / n <= 0.3:
                result = 'A-'
            elif (i+1) / n<= 0.4:
                result = 'B+'
            elif (i+1) / n <= 0.5:
                result = 'B0'
            elif (i+1) / n <= 0.6:
                result = 'B-'
            elif (i+1) / n <= 0.7:
                result = 'C+'
            elif (i+1) / n <= 0.8:
                result = 'C0'
            elif (i+1) / n <= 0.9:
                result = 'C-'
            elif (i+1) / n <= 1:
                result = 'D0'
    print(f'#{tc} {result}')
