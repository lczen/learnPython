maxn = 1005

f = [0] * maxn

def Find(x):
    if f[x] != x:
        f[x] = Find(f[x])
    return f[x]

T = int(input())
i, N, M, u, v = 0, 0, 0, 0, 0
N = int(input())
M = int(input())
while T:

    for i in range(1, N+1):
        f[i] = i
    while M:
        u = int(input())
        v = int(input())
        u = Find(u)
        v = Find(v)

        f[u] = v
        M -= 1

    ans = 0

    for i in range(1, N+1):
        if f[i] == i:
            ans += 1
    T -= 1
print(ans)