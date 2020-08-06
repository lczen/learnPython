'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
'''
class Node:
    def __init__(self, value, passed=0):
        self.val = value
        self.passed = passed

class Solution:
    def numSquares(self, n: int) -> int:
        queue = [Node(n)]
        visited = [0] * n + [1] #为啥是1
        while queue:
            x = queue.pop(0)

            i = 1
            while True:
                temp = x.val - i * i
                if temp < 0:
                    break
                if temp == 0:
                    return x.passed + 1
                if not visited[temp]:
                    queue.append(Node(temp, x.passed + 1))
                    visited[temp] = 1
                i += 1