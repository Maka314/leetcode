#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.zeroCount = sum([line.count(0) for line in grid])+1
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == 1:
                    res = self.backTracking(grid, x, y, 0)
                    return res
    
    def backTracking(self, grid, x, y, stepCount):
        if x < 0 or x>=len(grid[0]) or y < 0 or y >= len(grid):
            return 0
        if grid[y][x] == 2 and stepCount >= self.zeroCount:
            print(stepCount,grid)
            return 1

        res = 0
        if grid[y][x] == 0 or grid[y][x] == 1:
            grid[y][x] = -1
            res += self.backTracking(grid, x+1, y, stepCount + 1)
            res += self.backTracking(grid, x-1, y, stepCount + 1)
            res += self.backTracking(grid, x, y+1, stepCount + 1)
            res += self.backTracking(grid, x, y-1, stepCount + 1)
            grid[y][x] = 0
        
        return res
# @lc code=end

