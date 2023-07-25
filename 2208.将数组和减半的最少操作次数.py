#
# @lc app=leetcode.cn id=2208 lang=python3
#
# [2208] 将数组和减半的最少操作次数
#

# @lc code=start
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        res, target = 0, sum(nums)/2
        s = 0
        while s < target:
            nums.sort()
            res += 1
            s += nums[-1]/2
            nums[-1] = nums[-1]/2
        return res
# @lc code=end

