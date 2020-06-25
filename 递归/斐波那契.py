#递归
def f1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f1(n-1) + f1(n-2)
print(f1(10))

memo = [-1] * (n + 1)
def f2(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    if memo[n] == -1:
        memo[n] = f2(n-1) + f2(n-2)
    return memo[n]

#非递归
def fib(n):
    a,b = 1,1
    for i in range(n):
        print(a, end=" ")
        a,b = b,a+b
    print()
fib(10)
