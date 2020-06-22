'''
已知一组数(其中有重复元素)，求这组数可以组成的所有子集中，子 集中的各个元素和为整数target的子集，结果中无重复的子集。
例如: nums[] = [10, 1, 2, 7, 6, 1, 5]， target = 8
结果为: [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
'''
class Solution:
    def combinationSum2(self, candidates, target):
        def generate(i, nums, item, result,res_set,sum,target):
            if i>=len(nums) or sum>target:
                return #当元素已选完或item中的元素和sum已超过target
            sum += nums[i]
            item.append(nums[i])
            #当item中的元素和即为target且该结果未添加时
            if target == sum and item not in res_set:
                result.append(item[0:])#只加入值
                res_set.append(item[0:])
            generate(i+1,nums,item,result,res_set,sum,target)
            sum -= nums[i]#回溯后，sum将nums[i]减去并从item中删去
            item.pop()
            generate(i+1,nums,item,result,res_set,sum,target)

        result = []
        item = []
        res_set = []
        candidates.sort()
        #result.append(item[:])
        generate(0,candidates,item,result,res_set,0,target)
        return result

