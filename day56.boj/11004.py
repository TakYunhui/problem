import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
print(nums[k-1])
