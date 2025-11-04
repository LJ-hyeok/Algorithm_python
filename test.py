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


A = [4,132,5,34,21,-2]
M3c = M3s = 0
merge_sort_3way(A,0,len(A)-1)
print(A)