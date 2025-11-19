#
# 문단을 맞추기 위한 최소 비용을 구하는 문제 
# dp[i] = i 부터 마지막까지의 단어들을 사용해 만든 최소 Penalty (바텀-업)
#


w = int(input())
strings = input().split()

INF = 987654321 # 무한대라 가정
n = len(strings)
dp = [INF for _ in range(len(strings) + 1)]
dp[n] = 0
strings.append('')

for i in range(n-1, -1, -1):
    width = -1
    for j in range(i, n):
        width += len(strings[j]) + 1
        if(width > w): break
        penalty = (w - width) ** 3
        dp[i] = min(penalty+dp[j+1], dp[i])
        
print(dp[0])

#
# {i번째 단어의 penalty + i-1부터 마지막까지의 최소 penalty} VS {i번째 단어부터 (i+j)번째 단어의 penalty + j부터 마지막까지의 최소 penalty}
# 점화식: dp[i] = min(penalty + dp[j+1], dp[i])
#
# 결과적으로 이중 반복문을 사용하게 되므로 시간복잡도는 
# O(n^2)
#