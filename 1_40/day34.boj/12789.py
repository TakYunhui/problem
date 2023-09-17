n = int(input()) # 학생들의 수
line = list(map(int, input().split())) # 학생들의 번호 표 (선입선출)
stack = [] # 대기자가 들어갈 스택 (후입선출)
i = 1

# 그냥 서있는 친구들과 대기열에 사람이 존재할 때, 그 둘을 동시에 확인하는 것이 관건!
while True:
    # 기존의 서있는 학생들이 존재하면
    if line:
        # 대기열에 있는 학생과 나가야 할 순번 비교 후
        if stack and stack[-1] == i:
            # 같다면 대기열 학생을 내보내고 순번 1 증가
            stack.pop()
            i += 1
        # 대기열에 학생이 없다면
        else:
            # 서있는 학생들 중 가장 앞에 있는 학생과 순번 비교
            val = line.pop(0)
            if val == i:
                i += 1
            else:
                # 순번이 맞지 않으면 대기열로 보냄
                stack.append(val)
    # 서있는 학생들 다 대기열 또는 내보냈거나 해서 없다면
    else:
        # 대기열이 존재한다면
        if stack:
            # 대기열 후입선출 하기
            if stack[-1] == i:
                stack.pop()
                i += 1
            # 만약 내보낼 수 없다면 오름차순으로 진행 불가! sad
            else:
                print('Sad')
                break
        # 만약 다 내보냈다면 성공!
        else:
            print('Nice')
            break

# while True:
#     if line:
#         val = line.pop(0)
#         if stack and i == stack[-1]:
#             stack.pop()
#             i += 1
#         if val == i:
#             i += 1
#         else:
#             stack.append(val)
#     elif stack:
#         if stack[-1] == i:
#             stack.pop()
#             i += 1
#         else:
#             print('Sad')
#             break
#     else:
#         print('Nice')
#         break






