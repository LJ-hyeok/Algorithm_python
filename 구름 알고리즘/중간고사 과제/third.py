'''
문제의 조건 n 의 최대 값은 100,000
제한 시간 1초
따라서 알고리즘을 O(n) or O(nlogn) 안에 설계하여야 함

알고리즘
    1. 리스트 A 입력 >> O(n)
    2. 리스트 A의 최솟값과 그 값의 index 구하기 >> O(n)
    3-1. index 가 0 이면 
        rotation 하지 않았음을 의미, 0 출력 >> O(1)
    3-2. index 가 0이 아니라면
        가장 작은 수가 뒤에서 k 번째라면 rotation k번 함을 의미, n - k 출력 >> O(1)
        
알고리즘의 시간 복잡도 = O(n)
'''


# 입력
A = [int(x) for x in input().split()]

min = 987654321 # A[i] 의 범위 -200,000 ~ 200,000 / 초기값으로 200,000을 초과하는 값을 저장
min_index = -1  # 최소값의 index를 저장할 변수
for i in range(len(A)): # 최솟값의 index 찾기
    if min > A[i]:
        min = A[i]
        min_index = i

if(min_index == 0): # 3-1
    print(0)
else: # 3-2
    print(len(A)-min_index)
