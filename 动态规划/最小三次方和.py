n = int(input())

dp = [0] * (n+1)
limit = int(pow(n,1/3))

for t in range(1, n+1):
    tmp = float('inf')
    for i in range(1, limit+1):
        min_ = min(tmp, dp[t-i*i*i])
    dp[t] = min_ + 1
print(dp[n])
