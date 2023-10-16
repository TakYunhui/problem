n = int(input())
people = [input() for _ in range(n)]
people.sort()
# 성이 들어갈 리스트
fn = []
# 사람들의 성 넣기
for i in people:
    fn.append(i[0])
# 세트로 중복 제거
result = set()
for i in fn
    # 만약 해당 성을 가진 사람이 5명 이상이면 result에 추가
    if fn.count(i) >= 5:
        result.add(i)
# 리스트로 만들어 정렬
result = sorted(list(result))
# 결과 공백 없이 출력
if result:
    for i in result:
        print(i, end='')
else:
    print('PREDAJA')