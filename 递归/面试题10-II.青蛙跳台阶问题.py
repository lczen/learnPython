# 青蛙有两种跳法：
# 1.青蛙先跳到n-1，再跳到n
# 2.青蛙先调到n-2

#所以还是知道了n == 0的时候 memo[0]=1的意思
class Solution:
    def numWays(self, n:int) -> int:
        memo = [-1] * (n+1)
        def dp(n):
            if n == 1 or n == 0:
                return 1
            if memo[n] == -1:
                memo[n] = (dp(n-1) + dp(n-2))
            return memo[n]
        return dp(n) % 1000000007

