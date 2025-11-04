import random, time

def unique_n2(A):
    s = time.process_time()
    ans = False
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if(A[i] == A[j]): ans = True
    e = time.process_time()
    print("수행시간 =", e-s)
    return ans

def unique_nlogn(A):
    s = time.process_time()
    ans = False
    B = sorted(A)
    for i in range(n-1):
        if(B[i] == B[i+1]): ans = True
    e = time.process_time()
    print("수행시간 =", e-s)
    return ans 

def unique_n(A):
    ans = False
    C = [0 for _ in range(2*n+1)]# -n ~ +n 까지의 메모리 할당 / n이 최대 값일 때 크기: 100,000(양의 정수) + 100,000(음의 정수) + 1(0) +3(여유 메모리)
    s = time.process_time()
    for i in range(n):
        C[A[i] + n] += 1 
    for i in range(2*n+1):
        if (C[i] > 1): ans = True
    e = time.process_time()
    print("수행시간 =", e-s)
    return ans

n = int(input()) # input: 값의 개수 n
dataset = [random.randint(-n, n) for _ in range(n)] # 중복을 허용하는 데이터
# dataset = random.sample(range(-n, n+1), n) #중복을 허용하지 않는 데이터
# print(dataset)


# print("n^2")
# if(unique_n2(dataset)): print("YES")
# else: print("NO")

print("\nnLog(n)")
if(unique_nlogn(dataset)): print("YES")
else: print("NO")

print("\nn")
if(unique_n(dataset)): print("YES")
else: print("NO")



# 테스트 데이터를 생성한다
#   예1: 중복이 없는 랜덤 데이터 (아래 코드는 예제 코드임)
#      A = random.sample(range(-n, n+1), n)
#   예2: 중복이 상당히 많은 데이터
#   예3: 거의 정렬된 데이터
#   예4: 중복을 허락하는 랜덤 데이터

# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
# 같은 데이터를 세 함수에 전달해 실행 시간을 측정해본다
# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서, 다양한 특징의 데이터를 생성해 측정한다