# 
# 팰린드롬 = 가장 긴 앞과 뒤과 같은 단어
# -> 팰린드롬을 찾으려면 입력받은 문자열을 거꾸로 뒤집고 LCS한 것과 같다
# 시간복잡도 O(n^2) 
#
def paliindrome(x): # 문자열을 거꾸로 뒤집고 LCS 수행
    reverseX = ''.join(reversed(x)) # O(n)
    return LCS(x, reverseX) # O(n^2)

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
