# heapq 를 이용한 방법 
'''
문제의 조건 n의 최대 100,000
시간제한 10s
O(n^2)을 이용한다면 O(10,000,000,000)
=> worst case는 10초의 제한 시간에 절대 해결할 수 없음
O(nlogn)
=> 주어진 시간 제한에 해결 가능 

따라서 MoM 또는 selection algorithm을 이용한
M[i]값을 한번씩 k번째 수를 구하는 알고리즘은 O(n^2)이 되므로 만점을 받을 수 없다.
=> 새로운 알고리즘 구상 필요. (heap 자료구조를 이용하는 것이 핵심 힌트)

알고리즘
    1. 리스트 A 입력 >> O(n)
    작은수를 담아 놓는 리스트 left, 큰수를 담아 놓는 리스트 right를
    ** 각각 max_heap, min_heap으로 사용 **
    
    2. 리스트 A 만큼 반복하면서 M[i]를 구한다
        2-1. A[i]를 left에 삽입 => O(logn)
        2-2. left의 루트값이 right의 루트값 보다 커지면 작은수 큰수 나누기의 가정에 오류가 생기므로
            left의 루트값을 빼서 right의 루트값에 삽입한다. => O(2logn)
        2-3. left의 크기가 k 보다 크면 left의 루트가 k번째 수가 아니게 되므로
            left의 루트값을 빼서 right에 삽입 => O(2logn)
        2-4. left의 크기가 k 보다 작으면 left의 루트가 k - 1 번째 수가 되므로
            right의 루트갑을 빼서 left에 삽입 => O(2logn)
        2-5. 위 조건을 마친 리스트 left의 루트는 k번째 수가 되므로
            리스트 M[i]에 left의 루트를 추가 => O(1)
            
    3. 리스트 M에는 i//3+1 번째 수가 저장됐으므로
    각 수를 더해서 출력한다. => O(n)

알고리즘의 시간 복잡도 = O(nlogn)
'''
import heapq
#import random

A = [int(x) for x in input().split()]
# A = random.sample(range(-500000,500000), 100000)
M = []
left = [] # 작은 값 / max_heap
right = [] # 큰 값 / min_heap

for i in range(len(A)):
    k = i//3+1 # k 번째 수
    heapq.heappush(left , -A[i])
    if(len(right) > 0 and -left[0] > right[0]):
        heapq.heappush(right, -heapq.heappop(left))
    if(len(left) > k):
        heapq.heappush(right, -heapq.heappop(left))
    if(len(left) < k):
        heapq.heappush(left, -heapq.heappop(right))
    M.append(-left[0])

ans = 0 
for i in range(len(M)):
    ans += M[i]
print(ans)

