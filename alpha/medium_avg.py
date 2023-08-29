t = int(input())
for tc in range(1, t+1):
    nums = list(map(int, input().split()))
    # 최댓값, 최솟값 제거
    nums.remove(max(nums))
    nums.remove(min(nums))
    # 나머지의 평균 값 구하기 (반올림)
    result = round(sum(nums) / len(nums))
    print(f'#{tc} {result}')