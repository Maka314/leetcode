#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        nums.sort()
        k = k % 2
        if k:
            nums[0] = -nums[0]
        return sum(nums)
# @lc code=end

