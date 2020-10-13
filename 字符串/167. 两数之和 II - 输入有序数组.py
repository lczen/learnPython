def twoSum(A, target):

    i, j = 0, len(A)-1
    while i < j:
        if A[i] + A[j] == target:
            break
        if A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return [i+1, j+1]
A = [2, 7, 11, 15]
target = 9
print(twoSum(A, target))