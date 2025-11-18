from matplotlib import pyplot as plt
import numpy as np
import math
import random, timeit        
import sys
sys.setrecursionlimit(1000000)

class Heap: 
    def __init__(self, L=[]): 
        self.A = L
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)
	
    def heapify_down(self, k, n):
        global Hc, Hs
        while 2*k+1 < n: 
            L, R = 2*k + 1, 2*k + 2	 
            if L < n and self.A[L] > self.A[k]: 
                Hc += 1
                m = L
            else:
                Hc += 1
                m = k
            if R < n and self.A[R] > self.A[m]: 
                Hc += 1
                m = R 
            if m != k:	
                self.A[k], self.A[m] = self.A[m], self.A[k]
                Hs += 1
                k = m
            else: break	

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1): 
            self.heapify_down(k, n)

def heap_sort(arr):
    global Hc, Hs
    self = Heap(arr)
    n = len(self.A)	
    for k in range(len(self.A)-1, -1, -1):
        self.A[0],self.A[k] = self.A[k],self.A[0]
        Hs += 1
        n = n - 1	# A[n-1]은 정렬되었으므로
        self.heapify_down(0, n)

def quick_sort(A, first, last):
    global Qc, Qs
    if first >= last: return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            Qc += 1
            left += 1
        while right > first and A[right] >= pivot:
            Qc += 1
            right -= 1
        if left <= right: # swap A[left] and A[right]
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
    # place pivot at the right place
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)

def merge_sort(A, first, last): # merge sort A[first] ~ A[last]
    global Mc, Ms
    if first >= last: return
    middle = (first+last)//2
    merge_sort(A, first, middle)
    merge_sort(A, middle+1, last)
    B = []
    i = first
    j = middle+1
    while i <= middle and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
        Mc += 1
        Ms += 1

    for i in range(i, middle+1):
        B.append(A[i])
        Ms += 1
    for j in range(j, last+1): 
        B.append(A[j])
        Ms += 1
    for k in range(first, last+1): 
        A[k] = B[k-first]
        Ms += 1

def merge_sort_3way(A, first, last):
    global M3c, M3s
    
    # 기본 사례: 리스트의 크기가 0이거나 1이면 이미 정렬된 상태
    if first >= last:
        return

    # 1. 분할 (Divide)
    # 리스트를 3등분하기 위한 두 개의 중간 지점(mid)을 계산합니다.
    mid1 = first + (last - first) // 3
    mid2 = first + 2 * (last - first) // 3
    
    # 2. 정복 (Conquer)
    # 3개의 부분 리스트에 대해 재귀적으로 정렬을 수행합니다.
    merge_sort_3way(A, first, mid1)
    merge_sort_3way(A, mid1 + 1, mid2)
    merge_sort_3way(A, mid2 + 1, last)

    # 3. 병합 (Merge)
    # 3개의 정렬된 부분 리스트를 하나의 임시 리스트 B로 병합합니다.
    B = []
    i = first       # 부분 1 포인터 [first ... mid1]
    j = mid1 + 1    # 부분 2 포인터 [mid1+1 ... mid2]
    k = mid2 + 1    # 부분 3 포인터 [mid2+1 ... last]

    # --- 3-way merge ---
    # 세 부분 모두에 요소가 남아있는 동안
    while i <= mid1 and j <= mid2 and k <= last:
        M3c += 1 # A[i] vs A[j]
        if A[i] <= A[j]:
            M3c += 1 # A[i] vs A[k]
            if A[i] <= A[k]:
                B.append(A[i]); M3s += 1; i += 1
            else:
                B.append(A[k]); M3s += 1; k += 1
        else: # A[j] < A[i]
            M3c += 1 # A[j] vs A[k]
            if A[j] <= A[k]:
                B.append(A[j]); M3s += 1; j += 1
            else:
                B.append(A[k]); M3s += 1; k += 1
    
    # --- 2-way merge (한 부분이 소진되었을 때) ---
    
    # Case 1: 부분 3이 소진됨 (i, j만 남음)
    while i <= mid1 and j <= mid2:
        M3c += 1
        if A[i] <= A[j]:
            B.append(A[i]); M3s += 1; i += 1
        else:
            B.append(A[j]); M3s += 1; j += 1

    # Case 2: 부분 2가 소진됨 (i, k만 남음)
    while i <= mid1 and k <= last:
        M3c += 1
        if A[i] <= A[k]:
            B.append(A[i]); M3s += 1; i += 1
        else:
            B.append(A[k]); M3s += 1; k += 1
            
    # Case 3: 부분 1이 소진됨 (j, k만 남음)
    while j <= mid2 and k <= last:
        M3c += 1
        if A[j] <= A[k]:
            B.append(A[j]); M3s += 1; j += 1
        else:
            B.append(A[k]); M3s += 1; k += 1

    # --- 1-way copy (두 부분이 소진되었을 때) ---
    # 남은 요소를 B에 마저 복사합니다.
    for i_ in range(i, mid1 + 1): B.append(A[i_]); M3s += 1
    for j_ in range(j, mid2 + 1): B.append(A[j_]); M3s += 1
    for k_ in range(k, last + 1): B.append(A[k_]); M3s += 1

    # --- 원본 리스트 A에 다시 복사 ---
    # 기존 merge_sort 로직과 동일
    for k_ in range(first, last + 1):
        A[k_] = B[k_ - first]
        M3s += 1

Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
M3c = M3s = 0
n = 300000
a_data = []
b_data = []
c_data = []
d_data = []

plt.ion()
for j in range(1, n, 1000):
    random.seed()
    A = []
    for i in range(j):
        A.append(random.randint(-1000,1000))
    B = A[:]
    # C = A[:]
    # D = A[:]
    
    # quick_sort(A, 0, j-1)
    # merge_sort(B, 0, j-1)
    # heap_sort(C)
    # a = timeit.timeit("merge_sort(A, 0, j-1)", globals=globals(), number=1)
    # b = timeit.timeit("merge_sort_3way(B, 0, j-1)", globals=globals(), number=1)
    merge_sort(A, 0, j-1)
    merge_sort_3way(B, 0, j-1)
    a = M3s
    b = M3c
    
    c = Ms
    d = Mc
    
    a_data.append(a)
    b_data.append(b)
    c_data.append(c)
    d_data.append(d)
    # c_data.append(Hs)
    print(j)

    plt.plot(a_data, 'b', b_data, 'indigo', c_data,'r', d_data, 'orange')
    plt.draw()
    plt.pause(0.00005)
    
plt.ioff()
plt.show()

# 15,000 부터 quick 역전