'''
回溯法通常的模板
1.判断当前节点是否访问过
2.访问该节点，并将标记为1
3.访问玩该节点，并将标志即为0
'''
'''
1.n表示当前走到哪一步了
2.result表示单词结果
3.result_all 表示最终的结果
'''
class Solution:
    def permute(self, nums):
        result_all = []
        visited = [0] * len(nums)

        def dfs(n, nums, result):
            if n == len(nums):
                return result_all.append(result[:])
            for i in range(len(nums)):
                if visited[i] == 1:
                    continue
                result.append(nums[i])
                visited[i] = 1
                dfs(n+1, nums, result)
                result.pop()
                visited[i] = 0
        dfs(0, nums, [])
        return result_all
print(Solution().permute([0,1,2]))