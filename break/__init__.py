import math
class Solution:
    def numSquares(self, n: int) -> int:
        #动态规划
        opt = [0x7FFFFFFF] * (n+1)
        opt[0] = 0
        for i in range(1, n+1):
            for j in range(1, i+1):
                if i - j*j >= 0:
                    opt[i] = min(opt[i], opt[i-j*j] + 1)
        return opt[n]

print(Solution().numSquares(12))

class Solution2:
    def numSquares(self, n: int) -> int:
        #动态规划
        squart_nums = [i*i for i in range(0,int(math.sqrt(n))+1)]
        opt = [float('inf')] * (n+1)
        opt[0] = 0
        for i in range(1, n+1):
            for j in squart_nums:
                if i - j < 0:
                    break
                opt[i] = min(opt[i], opt[i-j] + 1)
        return opt[n]
