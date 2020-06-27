def f3(n):
    memo = [-1] * (n + 1)
    for i in range(0, n + 1):
        if i == 0:
            memo[i] = 0
        elif i == 1:
            memo[i] = 1
        else:
            memo[i] = memo[n-1] + memo[n-2]
    return memo[n]