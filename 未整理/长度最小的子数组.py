class Solution:
    def minSubArrayLen(self, s: int, array) -> int:
        #j和i一起从0可是跑，j先跑找到大于则i+1，小于则j+1
        #复杂度是O(n):Accepted
        #这里计算复杂度的方法就是计算i和j两个指针最多的移动次数，都是n次
        #ans记录最小长度
        left, right, ans = 0, 0, len(array) + 1
        sums = []#通过创建一个和数组来将求和的速度从O(N)降到O(1)
        for num in array:
            if not sums:
                sums.append(num)
            else:
                sums.append(sums[-1] + num)
        while left < len(array) and right < len(array):
            if sums[right] - sums[left] + array[left] < s:
                right += 1
            else:
                if right - left + 1< ans:#计算长度
                    ans = right - left + 1
                left += 1
        if ans != len(array) + 1:
            return ans
        else:
            return 0
array = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(7, array))
