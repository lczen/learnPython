"""
dp[i]为从头开始到当前i最大连续的和。
dp[i]=max(dp[i-1]+num[i],num[i])如果前面的数加当前的数不如当前的大，dp[i]就等于当前的数，等于自序和从当前开始计算
"""
def max_seq_sum(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]
    max_ = nums[0]#ans代表
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        if max_ < dp[i]:
            max_ = dp[i]
    return max_

print(max_seq_sum([-2, 3, -1, 1, -3]))



class Solution:
    def maxSubArray(self, nums):
        sum = 0
        ans = nums[0]#ans代表第一个数字
        for num in nums:
            if sum > 0:#每次判断sum值，如果是负数则舍弃
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
        return ans