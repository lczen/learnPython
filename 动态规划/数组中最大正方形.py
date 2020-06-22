"""
构建2维dp数组：dp[i][j]表示i行j列为右下角顶点的正方形的边长！！
根据木桶效应，以i，j为右下的正方形的边长，取决于i-1，j-1和i，j-1和i-1，j(相同的dp物理意义，分别在i,j的左上，正左，正上方向)所代表的正方形的最短边长，
即dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
注意dp数组维度、遍历区间、符合条件判断等细节。
"""
class Solution:
    def maximalSquare(self, matrix):
        if(not matrix):
            return 0
        m=len(matrix)
        n=len(matrix[0])
        res=0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(matrix[i-1][j-1]==1):
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    res=max(dp[i][j],res)
        return res*res
#print(Solution().maximalSquare([[0,1,1,1 ,0],[1 ,1, 1 ,1 ,1],[0 ,1 ,1, 1 ,1],[0 ,1, 1 ,1 ,1],[0 ,0 ,1, 1 ,1]]))

"""
0 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 1 1 1 1
0 0 1 1 1
"""
def max_square(matrix):
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    print(dp)
    ans = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if matrix[i-1][j-1]=="1":
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                ans = max(ans,dp[i][j])
    return ans*ans
print(max_square([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
#时间复杂度：O(m*n)O(m∗n)
#空间复杂度：O(m*n)O(m∗n)