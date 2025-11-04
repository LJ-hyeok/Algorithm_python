#heapq 를 이용한 방법 
#minheap만 썻음

import heapq
import random

A = [int(x) for x in input().split()]
# A = random.sample(range(-50000,50000), 50000)
M = []
min_heap = []
tmp_queue = []

for i in range(len(A)):
    heapq.heappush(min_heap, A[i])
    k = i//3
    for j in range(0, k): 
        tmp_queue.append(heapq.heappop(min_heap))
    M.append(min_heap[0])
    for j in range(0, k):
        heapq.heappush(min_heap,tmp_queue.pop())
        

ans = 0
for i in range(len(M)):
    ans += M[i]
print(ans)

