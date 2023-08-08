#
# @lc app=leetcode.cn id=1749 lang=python3
#
# [1749] 任意子数组和的绝对值的最大值
#

# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxPositive = 0
        currentPositive = 0
        maxNegative = 0
        currentNegative = 0
        for i,j in enumerate(nums):
            currentPositive += j
            currentNegative += j
            if currentNegative >= 0:
                currentNegative = 0
            if currentPositive <= 0:
                currentPositive = 0
            maxNegative = min(maxNegative, currentNegative)
            maxPositive = max(maxPositive, currentPositive)
        return max(maxPositive,-maxNegative)
# @lc code=end

