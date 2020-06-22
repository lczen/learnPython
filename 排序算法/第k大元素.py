class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        self._k = len(nums) - k  # 0,1,2,3,4，  第2大数是3，3的位置是5-2=3
        return self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, left, right):
        if left == right:
            return nums[left]
        pivot = self.partition(nums, left, right)
        if pivot == self._k:
            return nums[pivot]
        elif pivot < self._k:
            return self.quicksort(nums, pivot + 1, right)
        else:
            return self.quicksort(nums, left, pivot - 1)

    def partition(self, nums, left, right):  # 挖坑法
        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot:  # 找到第一个比pivot小的数
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = pivot
        return i

print(Solution().findKthLargest([0,1,2,3,4],1))