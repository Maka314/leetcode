#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (s + target) % 2:
            # 无法平衡
            return 0
        
        targetSum = (s + target) // 2
        slutionDP = [0 for _ in range(targetSum + 1)]
        for item in range(len(nums)):
            for finalRes in range(targetSum, 0,-1):
                if finalRes > nums[item]: #可以从历史方案达成
                    slutionDP[finalRes] += slutionDP[finalRes - nums[item]]
            slutionDP[nums[item]] += 1
        return slutionDP[-1]
# @lc code=end
