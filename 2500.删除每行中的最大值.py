#
# @lc app=leetcode.cn id=2500 lang=python3
#
# [2500] 删除每行中的最大值
#

# @lc code=start
class Solution:
    def deleteGreatestValue(self, G: List[List[int]]) -> int:
        return sum(map(max, zip(*map(sorted, G))))
# @lc code=end

