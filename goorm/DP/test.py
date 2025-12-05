n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(1, n):
    for j in range(1, n):
        if(dp[i][j] == 0): continue
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1   
        ans = max(ans, dp[i][j])
print(ans)