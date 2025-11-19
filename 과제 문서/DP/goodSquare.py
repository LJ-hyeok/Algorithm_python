#
# dp[i][j] = i, j가 정사각형의 오른쪽 꼭짓점일 때 만들수 있는 한변의 길이
# 점화식: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# 시간복잡도: 2차원 배열을 순회하면서 해결 = O(n^2)  
#

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(1, n):
    for j in range(1, n):
        if(dp[i][j] == 0): continue
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1   
        ans = max(ans, dp[i][j])
print(ans)


'''
import sys
input = sys.stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(1, n):
    for j in range(1, n):
        if(dp[i][j] == 0): continue
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        ans = max(ans, dp[i][j])
print(ans)
'''