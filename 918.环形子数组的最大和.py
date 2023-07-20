#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#


# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        innerMax, s = max(nums), 0
        for i in range(len(nums)):
            s += nums[i]
            if s <= 0:
                s = 0
            else:
                innerMax = max(innerMax, s)

        innerMin, s = min(nums), 0
        for i in range(len(nums)):
            s += nums[i]
            if s > 0:
                s = 0
            else:
                innerMin = min(innerMin, s)
        outerMax = sum(nums) - innerMin
        if not outerMax:
            #特殊情况处理
            outerMax = max(nums[0],nums[-1])
        return max(outerMax, innerMax)
# @lc code=end
