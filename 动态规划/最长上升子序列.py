class Solution:
    def lengthOfLIS(self, nums) -> int:

        if not nums:
            return 0
        dp = [1] * (len(nums)+1)
        for i in range(1,len(nums)+1):
            for j in range(1,i):
                if nums[j-1] < nums[i-1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
        #       0 1 2 3 4 5  6  7
        # 思路：10,9,2,5,3,7,101,18
        #       1 1 1 1 1 1 1   1   初始状态每个数字都是一个上升序列
        # dp[i] 1 1 1 2 2 3 4   4
        #5之前没有上升子序列
        #到5后25是一个上升子序列。dp[2]+1
        #到3后，23是一个上升子序列：dp[4] = dp[2]+1
        #到7后，257,237 dp[5]=3
        #到101后，257 101，237 101 dp[6] = 4
        #到18后， 257 18，237 18 dp[7] = 4