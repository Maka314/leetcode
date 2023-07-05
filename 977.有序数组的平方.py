#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
# @lc code=end

