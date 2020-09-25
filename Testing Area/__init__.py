chuan = ['b','c','a']

while chuan.pop(0) != 'a':
    continue
print('end')

print(int(pow(28,1/3)))

adjacency = [[] for _ in range(2)]
adjacency[0].append(3)
adjacency[0].append(4)
print(adjacency)


# 青蛙跳台阶
# dp[0] = 1 #特殊情况
# dp[1] = 1
# dp[2] = dp[0] + dp[1]
# dp[n] = dp[n-1] + dp[n-2]

n = 10
dp = [0]*(n+1)
dp[0] = 1 #特殊情况
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])