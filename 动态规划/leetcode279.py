import math
#完全平方数

class Solution:
    def numSquares(self, n: int) -> int:
        # 动态规划
        opt = [0x7FFFFFFF] * (n + 1)
        opt[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i - j * j >= 0:
                    opt[i] = min(opt[i], opt[i - j * j] + 1)
        return opt[n]




class Solution2:
    def numSquares(self, n: int) -> int:
        # 动态规划
        squart_nums = [i * i for i in range(0, int(math.sqrt(n)) + 1)]
        opt = [float('inf')] * (n + 1)
        opt[0] = 0
        for i in range(1, n + 1):
            for j in squart_nums:
                if i - j < 0:
                    break
                opt[i] = min(opt[i], opt[i - j] + 1)
        return opt[n]

class Node:
    def __init__(self, value, passed=0):
        self.val = value
        self.passed = passed

class Solution3:
    def numSquares(self, n:int) -> int:
        queue = [Node(n)]
        visited = [0]*n + [1]
        print(visited)
        while queue:
            x = queue.pop(0)
            i = 1
            while True:
                temp = x.val - i*i
                if temp < 0:
                    break
                if temp == 0:
                    return x.passed + 1
                if not visited[temp]:
                    queue.append(Node(temp, x.passed + 1))
                    visited[temp] = 1
                i += 1

print(Solution3().numSquares(12))