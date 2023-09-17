n = int(input())
result = 0
r_arr = []
for i in range(n+1): # n보다 작거나 같은 모든 양의 정수 조사
    arr = [n, i]  # 계산하여 집어 넣을 임시 배열
    tmp = n       # 원본 유지하는 변수
    idx = 1       # 계산 대상 인덱스
    while tmp >= 0: # tmp가 음수가 되면 종료
        # 직전 대상과 현재 대상의 차 계산
        tmp = arr[idx-1] - arr[idx]
        if tmp >= 0: # 양수만 다음 값으로 추가
            arr.append(tmp)
        idx += 1
    len_arr = len(arr)
    if len_arr > result: # 이전 조사 최대 길이보다 현재 조사 길이가 더 길면
        result = len_arr
        r_arr = arr
print(result)
print(*r_arr)