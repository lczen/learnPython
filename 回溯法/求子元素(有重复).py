#例一-b方法二：回溯法求有重复的子元素
def subsets(nums):
    result = []
    item = []
    res_set = []
    nums.sort()
    result.append(item[:])
    generate(0,nums,item,result,res_set)
    return result

def generate(i, nums, item, result,res_set):
    if i>=len(nums):
        return
    item.append(nums[i])
    if item not in res_set:
        result.append(item[0:])#只加入值
        res_set.append(item[0:])
    generate(i+1,nums,item,result,res_set)
    item.pop()
    generate(i+1,nums,item,result,res_set)


print(subsets([1,2,2]))
