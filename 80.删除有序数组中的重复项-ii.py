#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if left > 1 and nums[left - 1] == nums[left - 2] and nums[right] == nums[left - 2]:
                continue
            nums[left] = nums[right]
            left += 1 
        return left
# @lc code=end

