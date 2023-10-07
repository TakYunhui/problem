# 총 라운드 수 n
n = int(input())
for tc in range(n):
  # a, b 입력 데이터 
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  # a, b 그림 개수 따로 빼기 
  a_cnt, b_cnt = a.pop(0), b.pop(0)
  
  # a, b 그림 1, 2, 3, 4 각각의 개수 셀 배열 
  cnt_a = [0] * (5)
  cnt_b = [0] * (5)
  
  
  
  # a, b그림 종류 별 개수 세기 
  for i in range(len(a)):
    cnt_a[a[i]] += 1
  for i in range(len(b)):
    cnt_b[b[i]] += 1
  
  # print(cnt_a, cnt_b)
  result = ''
  # 그림 별 개수 비교 
  # 역순 순회(4, 3, 2, 1)
  # 만약 값이 더 크다면 result 에 값 할당 후 반복문 종료
  # 값이 같다면 일단 무승부 'D'를 넣고, 반복을 계속 한다 
  for i in range(4, 0, -1):
    # print(i, cnt_a[i], cnt_b[i])
    if cnt_a[i] > cnt_b[i]:
      result = 'A'
      # print(cnt_a[i], cnt_b[i], result)
      break
    elif cnt_a[i] < cnt_b[i]:
      result = 'B'
      # print(cnt_a[i], cnt_b[i], result)
      break
    elif cnt_a[i] == cnt_b[i]: 
      result = 'D'
      # print(cnt_a[i], cnt_b[i], result)
  print(result)