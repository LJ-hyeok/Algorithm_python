n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = 0

stack.append((0,0)) # (index, height)
for i in range(1,n+1):
    while(stack[-1][1] > arr[i-1]):
        cur = stack[-1]
        stack.pop()
        ans = max(ans, cur[1] * (i-1-stack[-1][0]))
    stack.append((i, arr[i-1]))

while(stack[-1][0]):
    cur = stack[-1]
    stack.pop()
    ans = max(ans, cur[1] * (n-stack[-1][0]))
print(ans)

'''
스텍 자료구조와 그리디 알고리즘을 이용해서 해결한다.

1. 현재 빌딩이 이전의 빌딩 보다 크거나 같다 -> 스텍에 추가한다.
2. 현재 빌딩이 이전의 빌딩 보다 작다 -> 이전의 빌딩의 높이에서 구할수 있는 최대 직사각형의 면적을 구한다.
+ 스텍에 있는 빌딩은 전부 오름차순이 되므로 직사각형의 면적을 구할수 있다.


모든 막대에 대해 한 번씩 스텍에 들어왔다 나가는 과정을 거친다. 따라서 O(n)
시간복잡도 : O(n)
'''