#方法一：回溯法求子元素
def generate(i, nums, item, result):
    if i>=len(nums):
        return
    item.append(nums[i])
    result.append(item[0:])#只加入值
    generate(i+1,nums,item,result)
    item.pop()
    generate(i+1,nums,item,result)


def subsets(nums):
    result = []
    item = []
    result.append(item[:])
    generate(0,nums,item,result)
    return result
print(subsets([1,2,3]))

#方法二：位运算求子元素
def subsets2(nums):
    result = []
    all_set = 1<<len(nums)
    for i in range(all_set):
        item = []
        for j in range(len(nums)):
            if i&(1<<j):
                item.append(nums[j])
        result.append(item[:])
    return result
print(subsets2([1,2,3]))
