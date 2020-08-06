class Solution:
    def canPartition(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        c = nums_sum // 2
        dp = [[0] * (c + 1) for _ in range(len(nums))]
        # 对第一列数据进行处理
        for i in range(len(nums)):
            dp[i][0] = 1
        # 对放进来的第一个数进行处理,这个地方是最难的
        if nums[0] <= c:
            dp[0][nums[0]] = 1
        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(1, c + 1):
                if num > j:
                    dp[i][j] = dp[i-1][j]
                    continue
                dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        return dp[-1][-1]

# 版本二
class Solution2:
    def canPartition(self, nums) -> bool:
        import numpy as np
        def dp_subset(arr, S):
            subset = np.zeros((len(arr), S+1), dtype=bool)
            subset[:, 0] = True
            subset[0, :] = False
            if arr[0] <= S:
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
        c = sum(nums)
        if c % 2 == 1:
            return 0
        c = c // 2
        return dp_subset(nums, c)

# 版本三

class Solution2:
    def canPartition(self, nums) -> bool:

        c = sum(nums)
        if c % 2 == 1:
            return False
        c = c // 2
        dp = [0] * (c + 1)
        dp[0] = 1
        for num in nums:
            for i in range(c, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1]