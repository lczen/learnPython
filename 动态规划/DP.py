#动态规划，本题求出arr中不相邻节点之和最大值
#解题思路：
arr = [1,2,4,1,7,8,3]
def rec_opt(arr,i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0],arr[1])
    else:
        A = rec_opt(arr,i-2) + arr[i]
        B = rec_opt(arr,i-1)
        return max(A,B)
print(rec_opt(arr,6))

import numpy as np
def dp_opt(arr):
    opt = np.zeros(len(arr))
    #下标0最优解就是arr[0]
    #下标1最优解是max(arr[0], arr[1])
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2,len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)
    return opt[len(arr)-1]
print(dp_opt([4,1,1,9,1]))


#题二：判断一个数，能否由列表中的数组成
#递归出口
# if s == 0: return True
# if i == 0: return arr[0] == s
# if arr[i] > s:
#    return subset(arr,i-1,s)
arr = [3, 34, 4, 12, 5, 2]
def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr,i-1,s)
    else:
        #选
        A = rec_subset(arr, i-1, s-arr[i])
        #不选
        B = rec_subset(arr, i - 1, s)
        return A or B
print(rec_subset(arr, len(arr)-1, 9))

import numpy as np
def dp_subset(arr, S):
    subset = np.zeros((len(arr), S+1), dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, S+1):
            if arr[i]>s:
                subset[i, s] = subset[i-1, s]
            else:
                A = subset[i-1, s-arr[i]]
                B = subset[i-1, s]
                subset[i, s] = A or B
    r, c = subset.shape
    return subset[r-1, c-1]
print(dp_subset(arr, 9))
