
"""我们可以简单地继续在斜坡上爬升并持续增加从连续交易中获得的利润，
而不是在谷之后寻找每个峰值。最后，我们将有效地使用峰值和谷值，
但我们不需要跟踪峰值和谷值对应的成本以及最大利润，
但我们可以直接继续增加加数组的连续数字之间的差值，
如果第二个数字大于第一个数字，我们获得的总和将是最大利润。
"""
# class Solution:
#     def maxProfit(self, prices):
#         maxprofit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 maxprofit += prices[i] - prices[i - 1]
#         return maxprofit

class Solution:
    def maxProfit(self, prices):
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < prices.length - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit