def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    # nums에 있는 수들로 중복 없이 수열 만들기
    # nums 리스트 개수 == n
    for i in range(n):
        # 이미 수열에 있다면 pass
        if nums[i] in s:
            continue
        # 수열에 없다면 넣어주고 다음 숫자로 재귀호출
        s.append(nums[i])
        dfs(start+1)
        s.pop()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
# 오름차순 정렬
nums.sort()
s = []
dfs(1)