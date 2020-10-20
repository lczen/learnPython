ans = []

def kSumII(A, k, target):
    path = []
    dfs(A, k, target, 0, path)
    return ans

def dfs(A, k, target, m, path):
    if k == 0 and target == 0:
        ans.append(path)
    if k < 0 or target < 0:
        return
    for i in range(m, len(A)):
        temp = path[:]
        temp.append(A[i])
        dfs(A, k-1, target-A[i],i+1,temp)

A = [1,2,3,4]
k = 2
target = 5
kSumII(A, k, target)

# 下面是动态规划解法，尚未明白
def kSum(A, k, target):
    n = len(A)
    dp = [[0]*(target+1) for _ in range(k+1)]
    dp[0][0] = 1
    for a in A:
        for i in range(k,0,-1):
            for j in range(target,a-1,-1):
                dp[i][j] += dp[i-1][j-a]
    return dp[k][target]

A = [1,2,3,4]
k = 2
target = 5
print(kSum(A, k, target))