#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res,s = max(nums),0
        for i in range(len(nums)):
            s+=nums[i]
            if s<=0:
                s=0
            else:
                res = max(res,s)
        return res
# @lc code=end

