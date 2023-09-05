s = input()
# 집합 -> 중복 제거
subset = set()
# 전체 문자열 순회
for i in range(len(s)):
    # 그다음 문자열 부터 끝까지
    for j in range(i, len(s)):
        # 인덱스로 문자 가져옴 [0:1]부터...
        tmp = s[i:j+1]
        subset.add(tmp)
print(len(subset))