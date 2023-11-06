import sys
input = sys.stdin.readline
'''
그냥 세명 구하는 줄 알았는데 사람의 수가 n명 중 심리적 거리가 가장 가까운 수 구하는 거였음
종류 차이가 가장 적게 나는 세 명 고르기 -> 어떻게? 
심리적 거리 = (a-b) + (b-c) + (c-b)
'''
t = int(input())
for _ in range(t):
    n = int(input()) # 사람 수
    mbti = input().split()
    print(mbti)

