class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        ls = []
        if nums_len < 3:
            return ls
        nums.sort()

        for i in range(nums_len - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                l = i + 1
                r = nums_len - 1
                sum = 0 - nums[i]
                while l < r:
                    if nums[l] + nums[r] == sum:
                        ls.append((nums[i], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < sum:
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                    else:
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
        return ls

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
sorted()