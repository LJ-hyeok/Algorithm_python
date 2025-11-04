'''
문제 조건 n의 최대는 1,000
시간 제한은 1s
=> O(n^2)을 허용하는 문제

리스트 L 을 사용하지 않고 S 만 사용하여 복원할 수 있다.
복원을 위한 리스트 S[i]는 A[0] ~ A[i-1] 보다 작은 수의 개수가 저장 되어 있음
=> A[i]는 (S를 역순으로 진행하면서) 아직 사용하지 않은 수의 오름차순을 담은 리스트 중에서 S]i] 번째 수


알고리즘
    1. 리스트 S, L 을 입력 => O(2n)
    2. 
        아직 사용하지 않은 오름차순 순열을 담은 리스트 P 초기화 => O(n)
        복원을 위한 리스트 rec_A 초기화 => O(n)
    3. S[i]를 역순으로 순회
        3-1. 리스트 rec_A[i]는 P[S[i]], 사용하지 않은 순열의 S[i]번째 값이 i번째 복원값이 됨 => O(1)
        3-2. P는 사용하지 않은 순열의 리스트이므로 사용한 S[i]는 pop => O(n)
    => O(n^2)
    
알고리즘의 시간 복잡도 O(n)
'''


def reconstruct(S, L):
    # S, L로부터 A를 재구성해 리턴
    P = [i for i in range(len(S))]
    rec_A = [0 for i in range(len(S))]
    
    for i in range(len(S)-1, -1, -1):
        rec_A[i] = P[S[i]]
        P.pop(S[i])
    return rec_A
	
# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()] # 조건에 따라 입력을 받지만 사용하지 않음 
A = reconstruct(S, L)
print(A)

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# T(n) = (2 x n) + {n x (C + n)} + C

# 2. 수행시간 T(n)을 Big-O료 표기해보자
# O(n^2)