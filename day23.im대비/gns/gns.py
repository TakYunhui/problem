import sys
sys.stdin = open('GNS_test_input.txt')
# 단어 - 숫자 매칭
nums = {'ZRO': 0, 'ONE': 1, 'TWO':2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
# 숫자 - 단어 매칭
word = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
t = int(input())
for tc in range(1, t+1):
    # 테스트 케이스 번호와 개수
    case_num, case_cnt = input().split()
    case_cnt = int(case_cnt)
    # 테스트 케이스
    case = input().split()
    word_to_num = []
    for i in case:
        word_to_num.append(nums[i])
    word_to_num.sort()

    num_to_word = []
    for i in word_to_num:
        num_to_word.append(word[i])
    print(case_num, *num_to_word)