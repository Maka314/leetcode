#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        bag = [0 for _ in range(target + 1)]
        for n in nums:
            for expSum in range(target + 1):
                bag
# @lc code=end

