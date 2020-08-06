class Solution:
    def maxAreaOfIsland(self, grid):
        if len(grid) == 0:
            return 0
        row, column = len(grid[0]), len(grid)
        visited = [[0] * row for _ in range(column)]
        r = 0
        for i in range(column):
            for j in range(row):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    # 向下向左右
                    area = [0]
                    self.dfs(i, j, grid, visited, area)
                    if r < area[0]:
                        r = area[0]
        return r

    def dfs(self, i, j, grid, visited, area):
        # 1.判断范围
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        # 2.是否访问
        if grid[i][j] == 0 or visited[i][j] == 1:
            return
        # 3.没访问的设置为访问
        visited[i][j] = 1
        area[0] += 1
        # 4.继续递归
        self.dfs(i - 1, j, grid, visited, area)
        self.dfs(i + 1, j, grid, visited, area)
        self.dfs(i, j - 1, grid, visited, area)
        self.dfs(i, j + 1, grid, visited, area)


########方法二
    def maxAreaOfIsland2(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        def dfs(i, j):
            if 0<=i<m and 0<=j<n and grid[i][j]:
                grid[i][j] = 0 # 因为grid[i][j]是1，所以面积至少是1
                return 1 + dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
            return 0
        for i in range(0,m):
            for j in range(0,n):
                ans = max(ans, dfs(i,j))
        return ans