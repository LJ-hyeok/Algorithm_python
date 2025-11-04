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
