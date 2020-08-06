def merge(arr, L, M, R):

    LEFT_SIZE = M - L
    RIGHT_SIZE = R - M + 1
    left = [0] * LEFT_SIZE
    right = [0] * RIGHT_SIZE
    for i in range(L, M):
        left[i-L] = arr[i]
    for i in range(M, R+1):
        right[i-M] = arr[i]

    i, j, k = 0, 0, L
    while i < LEFT_SIZE and j < RIGHT_SIZE:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < LEFT_SIZE:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < RIGHT_SIZE:
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(arr, L, R):

    if L == R:
        return
    else:
        M = (L + R) // 2
        mergeSort(arr, L, M)
        mergeSort(arr, M + 1, R)
        merge(arr, L, M+1, R)

arr = [6, 8, 10, 9, 4, 5, 2, 7]
L = 0
R = 7
mergeSort(arr, L, R)
print(arr)