## 一次两个方向，上或者右边，且只能走1或2步
N = 6
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1
dp[1][0] = 1
dp[1][1] = 2
dp[0][2] = 2
dp[2][0] = 2
for i in range(2, len(dp)):
    dp[0][i] = dp[0][i - 1] + dp[0][i - 2]
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]

for i in range(2, len(dp)):
    for j in range(2, len(dp[0])):
        dp[i][j] = dp[i - 2][j] + dp[i - 1][j] + dp[i][j - 2] + dp[i][j - 1]
print(dp[-1][-1])