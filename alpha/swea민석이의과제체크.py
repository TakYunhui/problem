# 수강생 N명, 1번부터 N번까지 번호 매김
t = int(input())

for tc in range(1, t+1):
    # n: 수강생 수, k: 과제 제출 수
    n, k = map(int, input().split())
    # 과제 제출한 사람의 번호 k 개
    good_students = list(map(int, input().split()))
    # n번까지의 총 수강생 번호
    total_students = [i for i in range(1, n+1)]

    bad_students = []
    for student in total_students:
        if student not in good_students:
            bad_students.append(student)
    # print(bad_students)


    print(f'#{tc}', *bad_students)