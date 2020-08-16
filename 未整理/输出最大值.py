nums = input('请输入一些整数，以空格分隔：')
list_nums = nums.split(' ')
list_int_nums = [int(item) for item in list_nums]
list_int_nums.sort()
print(list_int_nums[len(list_int_nums)-1])