import random, timeit        
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


    def __init__(self, L=[]): 
        self.A = L  
        self.make_heap() 

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)
	
    def heapify_down(self, k, n):
        while 2*k+1 < n: 
            L, R = 2*k + 1, 2*k + 2	 
            if L < n and self.A[L] > self.A[k]: 
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]: 
                m = R 
            if m != k:	
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else: break	

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1): 
            self.heapify_down(k, n)



# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
# 자유롭게 정의해 사용하면 됨
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0



n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))


print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))



# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))