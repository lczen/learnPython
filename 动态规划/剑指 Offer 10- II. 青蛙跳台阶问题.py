#本题垃圾的地方，dp[0] = 1,根本就没走怎么会是一。只不过是为了满足，当n=2的时候，可以从0走到2，也可以从1走到2
class Solution:
    def numWays(self, n: int) -> int:
        # a, b = 1, 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a % 1000000007
        dp = [0] * (n+3)
        if n == 0:
            return 1
        if n < 3:
            return n
        dp [0] = 1
        dp [1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 1000000007
