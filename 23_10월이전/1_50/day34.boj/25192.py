import sys
n = int(input()) # 채팅방의 기록 수
input = sys.stdin.readline
# ENTER 이후 아이디 개수 확인
# -> 딕셔너리에 넣어서 나오는 KEY 개수 COUNT를 결과에 저장
result = 0
# 문자열 입력 -> 개행문자 \n 제거를 위한 .rstrip()
data = list(input().rstrip() for _ in range(n))
chat = dict()
for i in data:
    if i == 'ENTER': # ENTER 입력 시, 기존 딕셔너리 결과 값에 넣어주고 딕셔너리 초기화
        result += len(chat)
        chat = dict()
    else:
        chat[i] = chat.get(i, 0) + 1
result += len(chat)
print(result)
