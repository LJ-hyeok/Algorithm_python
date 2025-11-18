def paliindrome(x):
    reverseX = ''.join(reversed(x))
    return LCS(x, reverseX)

def LCS(x, y):
    n = len(x)
    m = len(y)
    dp = [[0 for i in range(n+1) ] for j in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j-1])
            else: 
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
    return dp[n][m]

x = input()
print(paliindrome(x))
