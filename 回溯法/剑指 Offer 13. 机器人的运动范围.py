'''地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0:
            return 0
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * n for _ in range(m)]

        def validate_boundary(x, y, xMax, yMax):
            if x < 0 or x >= xMax:
                return False
            if y < 0 or y >= yMax:
                return False
            return True

        def validate_k(x, y, k):
            res = 0
            while x > 0:
                res += x % 10
                x = x // 10
            while y > 0:
                res += y % 10
                y = y // 10
            return res > k

        def dfs(m, n, x, y, k):
            visited[x][y] = 1
            count = 1
            for i in range(len(moves)):
                newX = x + moves[i][0]
                newY = y + moves[i][1]
                # 判断新坐标有没有越界
                if not validate_boundary(newX, newY, m, n):
                    continue
                if visited[newX][newY] == 1:
                    continue
                if validate_k(newX, newY, k):
                    continue
                count += dfs(m, n, newX, newY, k)
            return count

        return dfs(m, n, 0, 0, k)
