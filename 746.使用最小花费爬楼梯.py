#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalCost = cost[:2]
        for i in range(2, len(cost)):
            totalCost.append(cost[i] + min(totalCost[i-2:i]))
        return min(totalCost[-2:])
# @lc code=end

