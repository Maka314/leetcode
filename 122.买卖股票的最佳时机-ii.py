#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        res = 0
        buyIn = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                res += prices[i - 1] - buyIn
                buyIn = prices[i]
        if prices[-1] >= prices[-2]:
            res += prices[-1] - buyIn
        return res


# @lc code=end
