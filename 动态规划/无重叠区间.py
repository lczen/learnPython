class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        dp = [1] * n
        # ans = 1
        intervals.sort(key=lambda a: a[1])

        for i in range(len(intervals)):
            for j in range(i - 1, -1, -1):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    # 由于我事先进行了排序，因此倒着找的时候，找到的第一个一定是最大的数，因此不用往前继续找了。
                    # 这也是为什么我按照结束时间排序的原因。
                    break
            dp[i] = max(dp[i], dp[i - 1])
            #ans = max(ans, dp[i])
        ans = max(dp)
        return n - ans
# dp[0] 1个元素的时候，上升序列的数量为1。
# dp[1] 2个元素的时候，上升序列的数量要比较0，1位置[0][1],[1][0]大小。
# dp[2] 3个元素的时候，如果是上升时，第三个元素与上一个比是否有序。