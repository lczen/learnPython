def test():
    nums = list(map(int, input().split(",")))

    nums.sort()
    count = 0
    nums2 = []
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            nums2.append(nums[i])
    if count > 2:
        print("Oh My God!")
    max_ = max(nums2)
    min_ = min(nums2)
    if (max_ - min_ + 1) != len(set(nums2)):
        print("Oh My God!")
    else:
        print("So Lucky!")
test()
