N = 6
W = 21
B = [[0 for _ in range(0,W)] for _ in range(0,N)]
weight = [0, 2, 3, 4, 5, 9]
value = [0, 3, 4, 5, 8, 10]
def knapsack():
    for k in range(1,N):
        for C in range(1,W):
            if C < weight[k]:
                B[k][C] = B[k-1][C]
            else:
                value1 = B[k-1][C - weight[k]] + value[k]
                value2 = B[k-1][C]
                B[k][C] = max(value1,value2)

if __name__ == "__main__":
    knapsack()
    print(B[5][20])