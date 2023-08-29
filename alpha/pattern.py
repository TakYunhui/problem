t = int(input())
for tc in range(1, t+1):
    # 문자 받기
    word = input()
    result = 0
    # 각 문자열 길이는 30, 마디의 최대 길이는 10이므로
    for i in range(1, 11): # 인덱싱 범위를 최대 10으로 잡아준다
        # 똑같은 개수만큼 슬라이싱 해서 비교
        if word[:i] != word[i:i+i]:
            continue
        else:
            result = i
            break
    print(f'#{tc} {result}')