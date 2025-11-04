class Heap:
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
		
# 테스트
A = [1, 2, 3, 4, 5, 6, 7]
print(f"입력 리스트 {A}")
H = Heap(A)
print(f"make_heap 적용 후 {H}")