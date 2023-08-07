# 8개의 문제에 대한 점수 지정 딕셔너리
scores = {}
for i in range(1, 9):
    scores[i] = int(input())

# 딕셔너리를 밸류(점수 값) 기준으로 내림차순 정렬 
sorted_scores = list(sorted(scores.items(), key=lambda x:x[1], reverse=True))

total = 0     # 점수 총합
questions = [] # 점수 번호가 들어갈 리스트

# 가장 점수가 높은 5문제
for i in range(5):
    rank5 = sorted_scores[i]  # 가장 점수가 높은 문제 번호, 점수 값 튜플 5개를 받아옴 
    total += rank5[1]         # 총합에는 점수 부분을 합해줌
    questions.append(rank5[0])# 문제 번호 리스트에 문제 번호 넣기
print(total) 

# 문제 번호를 오름차순으로 정렬 후 출력
questions.sort()
for question in questions:
    print(question, end=' ')