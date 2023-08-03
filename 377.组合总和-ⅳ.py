#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        bag = [0 for _ in range(target + 1)]
        bag[0] = 1
        for expSum in range(0, target):
            for num in nums:
                if (expSum+num) <= target:
                    bag[expSum+num] += bag[expSum]
        return bag[-1]
        
# @lc code=end

