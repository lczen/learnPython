class Solution:
    def numWays(self, n:int) -> int:
        memo = [-1] * (n+1)
        def dp(n):
            if n == 1 or n == 0:
                return 1
            if memo[n] == -1:
                tmp = 0
                for i in range(1,n+1):#转换成子问题 dp[n] = dp[n-1] + dp[n-2]+,...,+dp[0]
                    tmp += dp(n-i)
                memo[n] = (tmp)
            return memo[n]
        return dp(n) % 1000000007