import heapq
import random

def find_median(arr): 
    L = [] #최대 힙 / 파이썬 heapq에는 최대 힙이 없기 때문에 음수를 곱해서 최대 힙 꼴을 만듬
    R = [] #최소 힙 
    for i in range(len(arr)):
        heapq.heappush(L, -arr[i])
        if(len(R) > 0 and -L[0] > R[0]):
            heapq.heappush(R, -heapq.heappop(L))
        if(len(L) - len(R) > 1):
            heapq.heappush(R, -heapq.heappop(L))
        if(len(L) < len(R)):
            heapq.heappush(L, -heapq.heappop(R))
    return -L[0]
    
    
    # ////
    # five.sort()
    # return five[len(five)//2]
                                                            
def mom(arr, k): #
    if(len(arr) == 1): return arr[0]
    
    s = []
    l = []
    m = []
    medians = []
    
    # 5묶음 & 중간값
    i=0
    while(i+4 < len(arr)):
        medians.append(find_median(arr[i:i+5]))
        i+=5
    # 마지막 그룹 처리
    if i < len(arr) and i+4 >= len(arr): 
        medians.append(find_median(arr[i:len(arr)]))

    #중간값을 다시 중간값
    MoM = mom(medians, len(medians)//2)
    
    for v in arr:
        if v < MoM: s.append(v)
        elif v > MoM: l.append(v)
        else: m.append(v)
    
    if(len(s) >= k):
        return mom(s, k)
    elif(len(s) + len(m) < k):
        return mom(l, k-len(s)-len(m))
    else:
        return MoM 

# 입력
# A = [int(x) for x in input().split()]
M = []
A = random.sample(range(-5000,5000), 10000)


sum = 0
for i in range(len(A)):
    M.append(A[i])
    sum += mom(M, i//3+1)
print(sum)