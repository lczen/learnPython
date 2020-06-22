class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 1 or n == 0:
            return 0
        k = 2
        dp = [[[0, 0] for j in range(k+1)] for i in range(n)]
        # n,k,2(0 sell,1 buy)
        for i in range(0, n):
            for j in range(k, -1, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                elif j == 0:
                    dp[i][j][1] = -float('inf')
                    dp[i][j][0] = 0
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-1][k][0]
k = 2
dp = [[[0,0] for j in range(k+1)] for i in range(3)]
print(dp)