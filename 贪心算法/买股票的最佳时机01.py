class Solution:
    #暴力法
    def maxProfitAll(self, prices):

        maxprofit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > maxprofit:
                    maxprofit = prices[j] - prices[i]
        return maxprofit
    #一次遍历
    def maxProfit(self, prices):
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:#先求最小值
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:#当前值减去最小值是否是当前最大利润（直线if，就不会直线elif）
                maxprofit = prices[i] - minprice
        return maxprofit
print(Solution().maxProfitAll([7,1,5,3,6,4]))