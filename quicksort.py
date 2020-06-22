def partition(list, s, t):
    temp = list[s]
    while s < t:
        while s<t and temp<=list[t]:
            t -= 1
        list[s] = list[t]
        while s<t and temp>=list[s]:
            s += 1
        list[t] = list[s]
    list[s] = temp
    return s

def quicksort(list, s, t):
    if s >= t:
        return list
    else:
        i = partition(list, s, t)
        quicksort(list, s, i-1)
        quicksort(list, i+1, t)
    return list
#print(quicksort([3,2,1,4],0,3))
nums = [1,2,3,4,5]
print(nums[0:len(nums)-1])
print(nums[1:len(nums)])