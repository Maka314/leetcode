#
# @lc app=leetcode.cn id=2500 lang=python3
#
# [2500] 删除每行中的最大值
#

# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        res = 0
        for x in range(len(grid[0])):
            loopValue = grid[0][x]
            for y in range(1, len(grid)):
                loopValue = max(loopValue, grid[y][x])
            res += loopValue
        return res
# @lc code=end

