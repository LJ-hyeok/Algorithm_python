#  inplace qucik sort
#  리스트를 너무 많이 사용해서 공간 복잡도 O(N^2)
def quick_sort(A, start, end):
    if start >= end:
        return 
    S, M, L = [], [], []
    p = A[start]
    for i in range(start, end+1):
        a = A[i]
        if a < p: S.append(a)
        elif a > p: L.append(a)
        else: M.append(a)
    
    A[start:end+1] = S+M+L
    quick_sort(A, start, start + len(S)-1)
    quick_sort(A, start + len(S) + len(M), end)

