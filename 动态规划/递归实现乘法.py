def multiply(A, B):
    # for i in range(B):
    sum = 0
    ss= 0

    def dp(sum, a, cur_b):
        if cur_b <= 0:
            ss = sum
            return
        sum = sum + a
        dp(sum, a, cur_b - 1)

    dp(sum, A, B)
    return ss

print(multiply(1, 10))
print((1, ) + (1, 1))