#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low, high = prices[0], 0
        for i in prices:
            res = max(res, i - low)
            if i < low:
                low = i
        return res
# @lc code=end

